# db_to_rdf

Stream rows from a Postgres database and write RDF triples to a Turtle
(`.ttl`) file using a declarative YAML mapping.

Built for bulk exports of **millions of triples** with constant memory:

- **Server-side cursor.** A Postgres named cursor streams rows in
  fixed-size batches (`batch_size` in the config). Client-side memory
  does not grow with the result size.
- **Streaming Turtle writer.** Triples are written to the output stream
  the moment they're produced. There is no in-memory RDF graph, so you
  never pay the O(triples) overhead of a library like `rdflib`.
- **Declarative mapping.** Columns map to predicates via YAML. You can
  iterate on the mapping without touching Python.

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/db_to_rdf/requirements.txt
```

Dependencies:

- `psycopg[binary] >= 3.1` — Postgres driver with server-side cursor support
- `PyYAML >= 6.0`

## Run

```bash
export DATABASE_URL='postgresql://user:pass@host:5432/auditor'

python scripts/db_to_rdf/db_to_rdf.py \
    --config scripts/db_to_rdf/mapping.example.yaml \
    --output output/cincy-triples.ttl
```

Standard `PGHOST`, `PGPORT`, `PGUSER`, `PGPASSWORD`, `PGDATABASE`
environment variables are honored by libpq if you leave `--dsn` and
`database.dsn` unset.

### Flags

| Flag                | Description                                                   |
|---------------------|---------------------------------------------------------------|
| `-c`, `--config`    | YAML mapping file (required)                                  |
| `-o`, `--output`    | Output `.ttl` path (overrides `output.path` in the config)    |
| `--dsn`             | Postgres libpq DSN (overrides the config and `$DATABASE_URL`) |
| `--gzip`            | Gzip the output; also implied if the path ends in `.gz`       |
| `-m`, `--mapping`   | Only run the named mapping(s); may be given multiple times    |
| `--batch-size`      | Server-side cursor batch size                                 |
| `--dry-run`         | Parse the config and print loaded mappings without connecting |
| `-v`, `--verbose`   | DEBUG-level logging                                            |

## Mapping file format

The mapping is a YAML file with these top-level keys:

```yaml
database:
  dsn: "${DATABASE_URL}"       # libpq conn string; ${VAR} is expanded

output:
  path: output/cincy-triples.ttl
  batch_size: 10000            # rows per server-side cursor fetch

prefixes:                      # written to the TTL header
  cincy:  http://kg.513analytics.com/ont/cincy#
  schema: https://schema.org/

mappings:
  - name: parcels              # free-form; appears in progress logs
    query: |
      SELECT parcel_number, book, page, parcel_id_on_page, mltown
      FROM auditor.parcel
    subject:
      template: "cincy:parcel/{parcel_number}"
      type: cincy:Parcel
      skip_if_null: [parcel_number]
    properties:
      - predicate: cincy:parcelNumber
        literal: { column: parcel_number, datatype: xsd:string }
      - predicate: cincy:ownedBy
        iri: { template: "cincy:party/{owner_hash}" }
```

### `subject`

- `template` — IRI template. `{column}` placeholders are substituted from
  the row. Use a CURIE prefix (e.g. `cincy:parcel/…`) so the output is
  compact. If any placeholder column is null the whole row is skipped.
- `type` — an optional `rdf:type` to assert for every subject.
- `type_column` + `type_map` — dynamic `rdf:type`: look up the class in
  `type_map` by the value of `type_column`. Falls back to `type` if the
  value is not in the map.
- `skip_if_null` — list of columns; if any are null the row is skipped
  entirely (no triples emitted).

### `properties`

Each entry emits one triple per row with the mapping's subject. There
are two property kinds.

**Literal** — bind a column value to a predicate:

```yaml
- predicate: cincy:parcelNumber
  literal: { column: parcel_number, datatype: xsd:string }
```

`datatype` is any CURIE the prefixes resolve. `xsd:integer`,
`xsd:decimal`, and `xsd:boolean` are written using Turtle's numeric
shorthand (`42`, `3.14`, `true`) when the column value matches.
`xsd:string` is written without a datatype tag since it is the default.
`lang` sets a language tag instead of a datatype.

**IRI** — emit a triple whose object is another templated IRI:

```yaml
- predicate: cincy:ownedBy
  iri: { template: "cincy:party/{owner_hash}" }
```

If a literal column is null, or any placeholder in an IRI template is
null, that individual triple is skipped (but the rest of the row is
still processed).

### `derived` (optional)

Computes synthetic columns from other columns before the templates are
rendered. Useful for hashing PII into stable IRI fragments without
exposing raw names or addresses in the graph.

```yaml
derived:
  owner_hash:
    type: sha1
    columns: [owner_name, mail_street, mail_city, mail_zip]
```

The `sha1` function hashes the concatenation of each column's value
(separated by null bytes) and exposes the hex digest as a new column
the templates can reference. For production use, prefer computing the
hash in SQL so the digest is consistent with other consumers:

```sql
SELECT encode(
         digest(
           lower(trim(owner_name))
           || '|' || coalesce(mail_street, '')
           || '|' || coalesce(mail_city, '')
           || '|' || coalesce(mail_zip, ''),
           'sha1'
         ),
         'hex'
       ) AS owner_hash
```

## Mapping pattern for 300 k parcels and 700 k addresses

With many joined rows the most efficient layout is:

1. One mapping per **entity class** (parcels, owners, addresses), each
   with a `SELECT DISTINCT` query so each subject IRI is written at
   most once.
2. One mapping per **relationship** (parcel → owner, owner → mailing
   address, parcel → site address). Relationship mappings produce
   single-predicate triples and don't re-emit entity metadata.

See `mapping.example.yaml` for a complete six-mapping example in this
style.

## Performance notes

- **Batch size.** The default `10000` balances round-trip overhead
  with per-batch memory. For very wide rows drop it; for narrow rows
  `50000` is fine.
- **I/O.** The script uses a 4 MB text buffer for plain output; `--gzip`
  adds a `gzip.open` wrapper. A 10 M-triple file is typically 1–2 GB
  uncompressed, ~150 MB gzipped.
- **Read-only transaction.** Each run opens a single read-only
  transaction that survives the whole export so the server-side
  cursors remain valid.
- **Parallelism.** The script is single-threaded. If CPU or DB latency
  becomes the bottleneck, run several invocations with `--mapping`
  targeting disjoint mappings to separate files, then concatenate.
- **Deduplication.** Triples are not deduplicated in memory. Identical
  triples are benign (RDF is a set; triplestores ignore duplicates on
  import). Deduplicate at the SQL level with `SELECT DISTINCT` when
  you want a smaller file.

## Loading the output

```bash
# Apache Jena — validate syntax
riot --validate output/cincy-triples.ttl

# Apache Jena Fuseki — bulk load
tdb2.tdbloader --loc=fuseki-data output/cincy-triples.ttl

# GraphDB — HTTP import
curl -X POST -H 'Content-Type: text/turtle' \
     --data-binary @output/cincy-triples.ttl \
     'http://localhost:7200/repositories/cincy/statements'
```

After loading, run `tests/sparql-tests.rq` against the triplestore to
verify the resulting graph matches the ontology's class/property
expectations.

## Limitations

- No schema validation against the ontology. The script will happily
  emit triples that use predicates or classes not declared in
  `ontology/cincy-housing.ttl`; add queries to `tests/sparql-tests.rq`
  if you want to catch that.
- No blank nodes. All subjects and objects are named IRIs. If you want
  blank nodes for, say, unnamed assessments, add a synthetic column in
  SQL (e.g. `gen_random_uuid()`) and template it into the IRI.
- No SPARQL Update target. The output format is always Turtle; if you
  need N-Triples or JSON-LD, post-process with `riot`.
