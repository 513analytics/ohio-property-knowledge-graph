# Ohio Property Knowledge Graph

A semantic ontology for modeling Ohio real estate data, specifically Cincinnati and Hamilton County property records including parcels, ownership, valuation, taxation, and land use classification.

## What's Included

- **Ontology schemas** (RDF/OWL in Turtle format) — not actual property records
- **Reference vocabularies** — standardized land use codes aligned with Ohio Department of Tax Equalization
- **Documentation** — ontology overview, glossary, and SPARQL query guide
- **Example queries** — template SPARQL queries for common questions

## Quick Start

1. **View the ontology:**
   - [`ontology/cincy-housing.ttl`](ontology/cincy-housing.ttl) — Main ontology covering parcels, ownership, valuation, taxation, abatements, TIF districts
   - [`ontology/cincy-land-use-codes.ttl`](ontology/cincy-land-use-codes.ttl) — SKOS vocabulary for land use codes (1xx–8xx)

2. **Explore the documentation:**
   - [Ontology Overview](docs/ontology-overview.md) — Core classes and relationships
   - [Glossary](docs/glossary.md) — Key terms and definitions
   - [SPARQL Query Guide](docs/sparql-guide.md) — How to query the ontology

3. **See example queries:**
   - [Example Queries](examples/queries/) — Template SPARQL queries

## Scope

This ontology covers:
- **Cadastral data:** Parcels (composite keys: book, page, parcel ID, mltown)
- **Ownership:** Persons, organizations, LLCs, trusts, government entities, nonprofits, mortgage servicers
- **Valuation & Assessment:** Land, improvements, agricultural use values; exempt and abated amounts
- **Taxation:** Tax districts, school districts, levies, tax bills
- **Temporal data:** Tax year snapshots, owner-occupied status, homestead exemptions, rental registration
- **Land use:** 8 top-level categories (Agricultural, Extraction, Industrial, Commercial, Residential, Publicly Owned, Abated, Public Utilities)

## Standards & Imports

This ontology aligns with and imports:
- **ISO 19152 LADM** — Land Administration Domain Model
- **OGC GeoSPARQL 1.1** — Geospatial data
- **W3C SKOS** — Knowledge organization
- **W3C OWL-Time** — Temporal reasoning
- **schema.org** — General semantic web vocabulary
- **QUDT** — Quantities, units, dimensions

## Files

```
.
├── README.md                    (this file)
├── LICENSE                      (CC0 1.0 Universal — public domain)
├── CHANGELOG.md                 (version history)
├── .gitignore                   (standard RDF tool artifacts)
├── ontology/                    (core ontology files)
│   ├── cincy-housing.ttl        (main ontology)
│   └── cincy-land-use-codes.ttl (SKOS vocabulary)
├── docs/                        (documentation)
│   ├── index.md                 (overview)
│   ├── ontology-overview.md     (classes & properties)
│   ├── glossary.md              (terms & definitions)
│   └── sparql-guide.md          (query guide)
├── examples/                    (example data & queries)
│   ├── queries/                 (SPARQL queries)
│   └── data/                    (notes on example data)
├── tests/                       (validation)
│   └── sparql-tests.rq          (validation queries)
└── scripts/                     (utilities)
    └── validate.sh              (TTL syntax validation)
```

## License

This work is dedicated to the public domain under [CC0 1.0 Universal](LICENSE).

## Contributing

This is an early-stage ontology (v0.1.0). Feedback on coverage, relationships, and alignment with standards is welcome.

## Contacts

Created by 513 Analytics.
