# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Ohio Property Knowledge Graph** — A semantic ontology for Cincinnati and Hamilton County real estate data, structured as a standard RDF/OWL project with comprehensive documentation, examples, and validation tests.

This is a **schema repository**, not a data repository. It contains:
- Ontology definitions (RDF/Turtle format)
- Controlled vocabularies (SKOS)
- Documentation and glossaries
- Example SPARQL queries
- Validation tests

No actual property records or sensitive data are stored here.

## Repository Structure

```
.
├── ontology/                    # Core RDF/OWL ontologies (Turtle format)
│   ├── cincy-housing.ttl        # Main ontology (OWL): ~637 lines, classes for parcels, ownership, assessment, taxation
│   └── cincy-land-use-codes.ttl # Reference vocabulary (SKOS): ~628 lines, land use codes 1xx–8xx
├── docs/                        # Documentation
│   ├── index.md                 # Navigation hub
│   ├── ontology-overview.md     # Classes, properties, design principles (270+ lines)
│   ├── glossary.md              # 70+ term definitions
│   └── sparql-guide.md          # SPARQL syntax, patterns, functions (300+ lines)
├── examples/                    # Example queries and future data
│   ├── queries/                 # 5 SPARQL query templates (.rq files)
│   └── data/                    # Reserved for future example RDF data
├── tests/                       # Validation
│   ├── sparql-tests.rq          # 20+ SPARQL ASK validation queries
│   └── README.md                # How to run validation
└── scripts/                     # Utilities
    └── validate.sh              # TTL syntax validation (requires riot or raptor2)
```

### Key Files

- **README.md** — Project overview, quick start, scope
- **CHANGELOG.md** — Version history (currently v0.1.0, created 2026-04-05)
- **.gitignore** — Ignores RDF tool artifacts (*.nq, *.nt, *.rj), IDE files, cache files

## Ontology Design

### Core Concepts

**Parcel** — The fundamental cadastral unit (auditor parcel number = book + page + parcel ID + mltown)

**ParcelYearState** — Time-varying attributes per tax year (land use code, exemptions, owner-occupied status, etc.)

**Parties** — Owners, organizations, mortgage servicers (hierarchy: Party > Person/Organization > LLC/Trust/etc.)

**Assessment** — Valuation (land, improvements, agricultural use; Ohio 6-year cycle with triennial updates)

**Taxation** — Tax districts, levies, school districts, tax bills

**Exemptions & Abatements** — Homestead, government, nonprofit, TIF abatements

### Standards & Imports

- **ISO 19152 LADM** — Cadastral/land administration alignment
- **OGC GeoSPARQL 1.1** — Geospatial features
- **W3C SKOS** — Controlled vocabularies
- **W3C OWL-Time** — Temporal relationships
- **schema.org** & **Dublin Core** — General semantic metadata

### IRI Namespace

All project ontology entities use prefix `cincy:` → `http://kg.513analytics.com/ont/cincy#`

## Common Development Tasks

### Validating Ontology Files

```bash
# Validate TTL syntax (requires Apache Jena or Raptor2)
bash scripts/validate.sh

# Install validators:
# macOS: brew install jena    (or: brew install raptor2)
# Ubuntu: apt-get install raptor2-utils
```

### Running SPARQL Queries

Example queries are in `examples/queries/` (*.rq files):
- `list-parcels.rq` — Discover available parcels
- `find-residential-property.rq` — Filter by land use code
- `owner-lookup.rq` — Find properties by owner name
- `property-valuation.rq` — Analyze valuations
- `homestead-exempt-properties.rq` — Find owner-occupied properties

To run against a SPARQL endpoint or triple store:
1. Load `ontology/cincy-housing.ttl` and `ontology/cincy-land-use-codes.ttl`
2. Paste query content into your SPARQL client
3. Modify FILTER clauses and limits as needed

### Running Validation Tests

The `tests/sparql-tests.rq` file contains 20+ SPARQL ASK queries that validate ontology integrity:

```bash
# Load ontology files into SPARQL endpoint
# Run tests/sparql-tests.rq
# All queries should return TRUE
```

Tests verify:
- Core classes exist (Parcel, ParcelYearState, Party, Assessment, etc.)
- Class hierarchy is correct (Person ⊆ Party, LLC ⊆ Organization, etc.)
- SKOS vocabulary is complete (LandUseScheme, LandUseCode categories)
- Ontology metadata and imports are declared

## Understanding the Documentation

Use these docs to onboard to the project:

1. **Start here:** `docs/index.md` — Overview and navigation
2. **Understand classes:** `docs/ontology-overview.md` — Full class definitions with properties and examples
3. **Learn terminology:** `docs/glossary.md` — 70+ terms: Parcel, Assessment, Exemption, Land Use Code, etc.
4. **Write queries:** `docs/sparql-guide.md` — SPARQL patterns, functions, and 10 query examples

All docs reference the ontology via property names like `cincy:landUseCode`, `cincy:taxYear`, etc.

## Namespace Prefixes (for SPARQL)

```sparql
PREFIX cincy: <http://kg.513analytics.com/ont/cincy#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
```

## File Format Notes

- **Turtle (.ttl)** — Human-readable RDF serialization; all ontology files use this format
- **SPARQL (.rq)** — Query files; includes comments documenting use cases
- **Markdown (.md)** — All documentation uses GitHub-flavored markdown

## Making Changes

### Adding or Modifying Classes/Properties

1. Edit `ontology/cincy-housing.ttl` (Turtle format)
2. Maintain namespace prefix consistency (all new entities use `cincy:` prefix)
3. Include `rdfs:label` and `rdfs:comment` for human readability
4. Update `docs/ontology-overview.md` with class/property documentation
5. Update `docs/glossary.md` with new term definitions if needed
6. Add validation tests to `tests/sparql-tests.rq` if adding core classes
7. Validate syntax: `bash scripts/validate.sh`

### Adding Example Queries

1. Create a new `.rq` file in `examples/queries/`
2. Include comment header with use case
3. Use consistent SPARQL formatting (prefixes, indentation)
4. Test the query syntax against the ontology
5. Update `examples/queries/README.md` with query description
6. Limit results with `LIMIT` clause during development

### Updating Documentation

1. **Glossary updates:** Add terms alphabetically in `docs/glossary.md`; include examples and abbreviations when relevant
2. **Query guide:** Add patterns to `docs/sparql-guide.md` under "Common Query Patterns"
3. **Overview changes:** Keep `docs/ontology-overview.md` synchronized with actual class definitions in TTL files

### Adding to CHANGELOG

Record significant changes in `CHANGELOG.md`:
- New ontology versions (update `owl:versionInfo` in TTL file)
- Major class/property additions
- Documentation improvements
- Follow semantic versioning

## Git Workflow

- **Branch naming:** Use descriptive branch names (e.g., `feature/add-court-data-classes`, `docs/improve-sparql-guide`)
- **Commits:** Provide clear commit messages; reference what changed and why
- **PR reviews:** Include link to relevant documentation (e.g., "See docs/ontology-overview.md for class definitions")
- **Testing:** Run `bash scripts/validate.sh` before committing TTL files

## Related Tools & Resources

- **SPARQL endpoints:** GraphDB, Virtuoso, Apache Jena Fuseki (for querying ontologies)
- **Ontology editors:** Protégé (visual OWL/Turtle editor), VocBench (SKOS editor)
- **Validation:** SPARQL ASK queries (see `tests/sparql-tests.rq`), ShaCL (future)
- **RDF tools:** Apache Jena (riot), Raptor2 (turtle validators)

## Development Notes

### No CI/CD Configuration

This repo currently has no automated tests or build pipeline. Validation is manual:
- Turtle syntax checking via `scripts/validate.sh`
- SPARQL test queries run manually against endpoints

### No Package Management

This is a schema repo, not code. No Python requirements.txt, package.json, or similar. To use the ontology:
1. Download the TTL files
2. Load into a SPARQL-capable triplestore (GraphDB, Virtuoso, etc.)
3. Query via SPARQL

### Future Scope

Current ontology covers parcel, ownership, assessment, and taxation. README notes intent to incorporate court data (evictions, foreclosures) in future versions. This would require new classes and relationships in the ontology.

## Quick Checklist for New Work

When working on ontology changes:

- [ ] Edit `.ttl` files in `ontology/` directory
- [ ] Maintain `cincy:` namespace prefix
- [ ] Run `bash scripts/validate.sh` to check Turtle syntax
- [ ] Update relevant documentation (`docs/ontology-overview.md`, `docs/glossary.md`)
- [ ] Add/update validation tests in `tests/sparql-tests.rq` if modifying core classes
- [ ] Update `CHANGELOG.md` with version and changes
- [ ] Write clear commit message explaining ontology changes
