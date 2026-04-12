#!/usr/bin/env python3
"""
db_to_rdf.py — Stream rows from a Postgres database and write RDF triples
to a Turtle (.ttl) file using a declarative YAML mapping.

Designed for bulk exports of millions of triples with constant memory:

  * A Postgres server-side (named) cursor streams rows in fixed-size batches
    instead of buffering the whole result set client-side.
  * A small hand-rolled Turtle writer emits each triple to the output stream
    immediately — there is no in-memory RDF graph, so memory use does not
    grow with the number of triples.
  * Only PyYAML and psycopg are required; no rdflib dependency.

See README.md in this directory for usage, mapping-file format, and tuning.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import logging
import os
import re
import sys
import time
from typing import Any, Iterable, Mapping, Sequence, TextIO, TYPE_CHECKING

import yaml

if TYPE_CHECKING:
    import psycopg

log = logging.getLogger("db_to_rdf")


# ---------------------------------------------------------------------------
# Turtle serialization helpers
# ---------------------------------------------------------------------------

# Escape backslash, double-quote, newline, carriage return, and tab for
# Turtle double-quoted short-form literals. str.translate is the fastest
# way to do this in CPython.
_LITERAL_TRANSLATE = str.maketrans(
    {
        "\\": "\\\\",
        '"': '\\"',
        "\n": "\\n",
        "\r": "\\r",
        "\t": "\\t",
    }
)


def escape_literal(value: str) -> str:
    return value.translate(_LITERAL_TRANSLATE)


# Matches {column_name} placeholders inside an IRI template.
_TEMPLATE_RE = re.compile(r"\{([A-Za-z_][A-Za-z0-9_]*)\}")


def _encode_pn_local(local: str) -> str | None:
    """Encode a local name as a valid Turtle PN_LOCAL.

    Returns the encoded local (possibly with ``/`` characters rewritten as
    ``\\/`` per the PN_LOCAL_ESC grammar production) or ``None`` if the
    local contains a character we can't safely encode, in which case the
    caller should fall back to writing a full IRI in angle brackets.

    Grammar enforced (a conservative subset of the Turtle 1.1 PN_LOCAL):
      * Non-empty.
      * First char: letter, digit, or underscore.
      * Other chars: letter, digit, ``_``, ``-``, ``.`` (not last), or ``/``
        (emitted as the escape form ``\\/``).
    """
    if not local:
        return None
    n = len(local)
    out: list[str] = []
    for i, ch in enumerate(local):
        if "A" <= ch <= "Z" or "a" <= ch <= "z" or "0" <= ch <= "9" or ch == "_":
            out.append(ch)
        elif ch == "-" and i > 0:
            out.append(ch)
        elif ch == "." and 0 < i < n - 1:
            out.append(ch)
        elif ch == "/":
            out.append("\\/")
        else:
            return None
    return "".join(out)

_INT_RE = re.compile(r"^-?\d+$")
_DEC_RE = re.compile(r"^-?\d+\.\d+$")

RDF_TYPE_CURIE = "a"  # Turtle shorthand for rdf:type.


def render_iri(
    template: str,
    row: Mapping[str, Any],
    prefixes: Mapping[str, str],
) -> str | None:
    """Render an IRI template against a row.

    Returns a Turtle-ready IRI string: either a compact CURIE (``cincy:foo``)
    when the resolved local part is safe, or an absolute IRI wrapped in
    angle brackets (``<http://...>``). Returns ``None`` if any column
    referenced by a ``{placeholder}`` is null — the caller should then
    skip the triple.
    """
    missing = [False]

    def repl(match: re.Match[str]) -> str:
        key = match.group(1)
        value = row.get(key)
        if value is None:
            missing[0] = True
            return ""
        return str(value)

    rendered = _TEMPLATE_RE.sub(repl, template)
    if missing[0]:
        return None

    # Already an absolute IRI in angle brackets.
    if rendered.startswith("<") and rendered.endswith(">"):
        return rendered

    # A CURIE of the form "prefix:local".
    if ":" in rendered and not rendered.startswith(("http://", "https://", "urn:")):
        prefix, _, local = rendered.partition(":")
        if prefix in prefixes:
            encoded = _encode_pn_local(local)
            if encoded is not None:
                return f"{prefix}:{encoded}"
            return f"<{prefixes[prefix]}{local}>"

    # Fall back to an absolute IRI.
    return f"<{rendered}>"


def format_literal(
    value: Any,
    datatype: str | None = None,
    lang: str | None = None,
) -> str:
    """Format a value as a Turtle literal.

    `datatype` is a CURIE (``xsd:integer``) or an absolute IRI in angle
    brackets. Numeric and boolean datatypes are written with Turtle's
    numeric shorthand when the value is a valid literal of that type.
    """
    if lang:
        return f'"{escape_literal(str(value))}"@{lang}'

    if datatype == "xsd:integer":
        if isinstance(value, bool):
            # Python's True/False are ints — don't emit "1"/"0" for bools.
            pass
        elif isinstance(value, int):
            return str(value)
        elif isinstance(value, str) and _INT_RE.match(value):
            return value

    if datatype == "xsd:decimal":
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            s = f"{value}"
            if "." not in s:
                s += ".0"
            return s
        if isinstance(value, str) and _DEC_RE.match(value):
            return value

    if datatype == "xsd:boolean":
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, str) and value.lower() in ("true", "false"):
            return value.lower()

    escaped = escape_literal(str(value))
    # xsd:string is the default Turtle datatype and can be omitted.
    if not datatype or datatype == "xsd:string":
        return f'"{escaped}"'
    return f'"{escaped}"^^{datatype}'


class TurtleWriter:
    """Streaming Turtle writer. Each method writes one triple and returns
    immediately; no buffering beyond the underlying file object."""

    def __init__(self, stream: TextIO, prefixes: Mapping[str, str]):
        self.stream = stream
        self.prefixes = dict(prefixes)
        self._write = stream.write  # Local ref for a small speed gain.

    def write_header(self) -> None:
        w = self._write
        w("# Generated by scripts/db_to_rdf/db_to_rdf.py\n")
        w(f"# Generated at {time.strftime('%Y-%m-%dT%H:%M:%S%z')}\n\n")
        for prefix, uri in self.prefixes.items():
            w(f"@prefix {prefix}: <{uri}> .\n")
        w("\n")

    def triple(self, s: str, p: str, o: str) -> None:
        """Write a triple whose object is an IRI (or a pre-formatted literal
        produced by :func:`format_literal`)."""
        self._write(f"{s} {p} {o} .\n")


# ---------------------------------------------------------------------------
# Derived column functions
# ---------------------------------------------------------------------------


def _sha1(parts: Iterable[Any]) -> str:
    """Stable hex SHA-1 of concatenated column values, separated by NUL.

    Use this to build deterministic IRI fragments for parties and addresses
    without exposing raw PII in the IRI. For best results, normalize the
    columns in SQL (lowercase, trim, collapse whitespace) before the hash.
    """
    h = hashlib.sha1()
    for part in parts:
        h.update(b"\x00")
        if part is not None:
            h.update(str(part).encode("utf-8"))
    return h.hexdigest()


DERIVERS = {
    "sha1": _sha1,
}


# ---------------------------------------------------------------------------
# Mapping compilation & execution
# ---------------------------------------------------------------------------


class CompiledProperty:
    __slots__ = ("kind", "predicate", "column", "datatype", "lang", "template")

    def __init__(
        self,
        kind: str,
        predicate: str,
        column: str | None = None,
        datatype: str | None = None,
        lang: str | None = None,
        template: str | None = None,
    ):
        self.kind = kind
        self.predicate = predicate
        self.column = column
        self.datatype = datatype
        self.lang = lang
        self.template = template


class CompiledMapping:
    __slots__ = (
        "name",
        "query",
        "subject_template",
        "subject_type",
        "type_column",
        "type_map",
        "skip_if_null",
        "properties",
        "derived",
    )

    def __init__(self, raw: Mapping[str, Any]):
        self.name = raw["name"]
        self.query = raw["query"]

        subject = raw["subject"]
        self.subject_template: str = subject["template"]
        self.subject_type: str | None = subject.get("type")
        self.type_column: str | None = subject.get("type_column")
        self.type_map: Mapping[str, str] = subject.get("type_map") or {}
        self.skip_if_null: tuple[str, ...] = tuple(subject.get("skip_if_null") or ())

        self.properties: list[CompiledProperty] = []
        for prop in raw.get("properties") or ():
            predicate = prop["predicate"]
            if "literal" in prop:
                lit = prop["literal"]
                self.properties.append(
                    CompiledProperty(
                        kind="literal",
                        predicate=predicate,
                        column=lit["column"],
                        datatype=lit.get("datatype"),
                        lang=lit.get("lang"),
                    )
                )
            elif "iri" in prop:
                iri = prop["iri"]
                self.properties.append(
                    CompiledProperty(
                        kind="iri",
                        predicate=predicate,
                        template=iri["template"],
                    )
                )
            else:
                raise ValueError(
                    f"Property on mapping {self.name!r} must have either "
                    f"'literal' or 'iri' (got {list(prop)})"
                )

        self.derived: Mapping[str, Mapping[str, Any]] = raw.get("derived") or {}


def process_mapping(
    writer: TurtleWriter,
    conn: "psycopg.Connection",
    mapping: CompiledMapping,
    prefixes: Mapping[str, str],
    batch_size: int,
) -> tuple[int, int]:
    """Stream rows for a single mapping and emit triples. Returns (rows, triples)."""

    log.info("Running mapping %r", mapping.name)
    t0 = time.monotonic()
    row_count = 0
    triple_count = 0

    # Server-side (named) cursor. Postgres streams rows in batches of
    # `itersize` over a single transaction — client-side memory stays flat.
    with conn.cursor(name=f"db_to_rdf_{mapping.name}") as cur:
        cur.itersize = batch_size
        cur.execute(mapping.query)

        if cur.description is None:
            log.warning("  %s: query returned no columns", mapping.name)
            return 0, 0
        columns = [c.name for c in cur.description]

        subject_template = mapping.subject_template
        subject_type = mapping.subject_type
        type_column = mapping.type_column
        type_map = mapping.type_map
        skip_if_null = mapping.skip_if_null
        properties = mapping.properties
        derived = mapping.derived

        for raw_row in cur:
            row: dict[str, Any] = dict(zip(columns, raw_row))

            # Compute derived columns.
            for derived_name, spec in derived.items():
                fn = DERIVERS[spec["type"]]
                row[derived_name] = fn(row.get(c) for c in spec["columns"])

            # Skip row if any required column is null.
            if any(row.get(c) is None for c in skip_if_null):
                continue

            subject_iri = render_iri(subject_template, row, prefixes)
            if subject_iri is None:
                continue

            # rdf:type — dynamic via type_column/type_map, else fixed.
            type_iri: str | None = None
            if type_column is not None:
                key = row.get(type_column)
                if key is not None:
                    type_iri = type_map.get(str(key))
            if type_iri is None and subject_type is not None:
                type_iri = subject_type
            if type_iri is not None:
                writer.triple(subject_iri, RDF_TYPE_CURIE, type_iri)
                triple_count += 1

            for prop in properties:
                if prop.kind == "literal":
                    value = row.get(prop.column)
                    if value is None:
                        continue
                    literal = format_literal(value, prop.datatype, prop.lang)
                    writer.triple(subject_iri, prop.predicate, literal)
                    triple_count += 1
                else:  # kind == "iri"
                    obj = render_iri(prop.template, row, prefixes)
                    if obj is None:
                        continue
                    writer.triple(subject_iri, prop.predicate, obj)
                    triple_count += 1

            row_count += 1
            if row_count % 50_000 == 0:
                elapsed = time.monotonic() - t0
                rate = row_count / elapsed if elapsed > 0 else 0
                log.info(
                    "  %s: %d rows, %d triples (%.0f rows/s)",
                    mapping.name,
                    row_count,
                    triple_count,
                    rate,
                )

    elapsed = time.monotonic() - t0
    log.info(
        "Finished %r: %d rows, %d triples in %.1fs",
        mapping.name,
        row_count,
        triple_count,
        elapsed,
    )
    return row_count, triple_count


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def load_config(path: str) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    if not isinstance(config, dict):
        raise ValueError(f"Config file {path} must be a YAML mapping at the top level")
    return config


def expand_env(value: Any) -> Any:
    """Expand ${ENV_VAR} references inside a string config value."""
    if isinstance(value, str):
        return os.path.expandvars(value)
    return value


def resolve_dsn(config: dict[str, Any], override: str | None) -> str | None:
    if override:
        return override
    db = config.get("database") or {}
    dsn = expand_env(db.get("dsn"))
    if dsn:
        return dsn
    # Fall back to environment (psycopg reads PGHOST, PGUSER, PGPASSWORD, ...).
    return os.environ.get("DATABASE_URL")


def open_output(path: str, force_gzip: bool) -> TextIO:
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    if force_gzip or path.endswith(".gz"):
        # 1 MB buffer in the gzip wrapper.
        return gzip.open(path, mode="wt", encoding="utf-8", compresslevel=6)
    # 4 MB text buffer — big writes amortize syscall cost on bulk exports.
    return open(path, mode="w", encoding="utf-8", buffering=4 * 1024 * 1024)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Stream Postgres rows into a Turtle (.ttl) file.",
    )
    parser.add_argument("-c", "--config", required=True, help="YAML mapping file")
    parser.add_argument("-o", "--output", help="Output .ttl file (overrides config)")
    parser.add_argument(
        "--dsn",
        help="Postgres libpq DSN (overrides config.database.dsn and $DATABASE_URL)",
    )
    parser.add_argument(
        "--gzip",
        action="store_true",
        help="Gzip the output. Implied if the output path ends in .gz.",
    )
    parser.add_argument(
        "-m",
        "--mapping",
        action="append",
        help="Only run the named mapping(s); may be given multiple times.",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        help="Server-side cursor batch size (overrides config.output.batch_size)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Load the config and print the mapping list without connecting.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable DEBUG-level logging.",
    )
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    config = load_config(args.config)

    output_cfg = config.get("output") or {}
    out_path: str = args.output or output_cfg.get("path")
    if not out_path:
        log.error("No output path set (provide --output or output.path in the config)")
        return 2
    batch_size: int = args.batch_size or int(output_cfg.get("batch_size", 10_000))

    prefixes: dict[str, str] = dict(config.get("prefixes") or {})
    # Required for the rdf:type shorthand and literal datatypes.
    prefixes.setdefault("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    prefixes.setdefault("xsd", "http://www.w3.org/2001/XMLSchema#")

    raw_mappings = config.get("mappings") or []
    if args.mapping:
        wanted = set(args.mapping)
        raw_mappings = [m for m in raw_mappings if m.get("name") in wanted]
        missing = wanted - {m.get("name") for m in raw_mappings}
        if missing:
            log.error("Unknown mapping(s): %s", ", ".join(sorted(missing)))
            return 2
    if not raw_mappings:
        log.error("No mappings to run")
        return 2

    compiled = [CompiledMapping(m) for m in raw_mappings]

    if args.dry_run:
        log.info(
            "Dry run — %d mapping(s) loaded: %s",
            len(compiled),
            ", ".join(m.name for m in compiled),
        )
        log.info("Output would be written to %s", out_path)
        return 0

    # Import psycopg lazily so --dry-run and mapping validation work
    # without the driver installed.
    try:
        import psycopg
    except ImportError:
        log.error(
            "psycopg is not installed. Run: "
            "pip install -r scripts/db_to_rdf/requirements.txt"
        )
        return 2

    dsn = resolve_dsn(config, args.dsn)

    with open_output(out_path, args.gzip) as stream:
        writer = TurtleWriter(stream, prefixes)
        writer.write_header()

        log.info("Connecting to Postgres")
        total_rows = 0
        total_triples = 0
        # `with` on the connection rolls back on exception — safe because
        # we're only reading.
        with psycopg.connect(dsn) as conn:
            conn.read_only = True
            conn.autocommit = False
            for mapping in compiled:
                r, t = process_mapping(writer, conn, mapping, prefixes, batch_size)
                total_rows += r
                total_triples += t

    log.info(
        "DONE: %d rows, %d triples → %s",
        total_rows,
        total_triples,
        out_path,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
