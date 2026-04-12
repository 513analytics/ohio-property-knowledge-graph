# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- `scripts/db_to_rdf/` — streaming Postgres → Turtle converter written in Python.
  - `db_to_rdf.py` — main script. Uses a Postgres server-side cursor to stream
    rows in configurable batches and writes triples directly to the output
    stream, keeping client-side memory flat regardless of result-set size.
  - `mapping.example.yaml` — example mapping showing how to convert parcels,
    owners, postal addresses, and the relationships between them into
    `cincy:` ontology triples using `SELECT DISTINCT` per entity class.
  - `pyproject.toml` — project metadata and dependencies. Install with
    `uv sync` (recommended) or `pip install -r requirements.txt`.
  - `requirements.txt` — pinned `psycopg[binary]` and `PyYAML` dependencies.
  - `README.md` — usage, mapping-file format reference, and tuning notes.

## [0.2.0] - 2026-04-05

### Added
- Hamilton County Sketch ID Codes vocabulary (`ontology/cincy-sketch-id-codes.ttl`)
  - SKOS ConceptScheme (`cincy:SketchIdScheme`) with 3 top-level categories
  - 46 detached addition codes (numeric 01–199): garages, carports, porches, sheds, pools, barns, pole barns, and miscellaneous structures
  - 28 attached addition / wall codes (alphanumeric, e.g. GR1, PR2): breezeways, balconies, garages, porches, decks, patios, pools
  - 9 story height codes (e.g. 1s, 2s, A1–A4): full/half/quarter stories and attic finish levels
- Hamilton County Deed Type Codes vocabulary (`ontology/cincy-deed-types.ttl`)
  - SKOS ConceptScheme (`cincy:DeedTypeScheme`) with 7 top-level categories
  - 44 deed type concepts covering warranty, quit claim, fiduciary, sheriff/court, survivorship, government, and special-purpose instruments
  - EX/Exempt variants documented with reference to ORC 319.54 conveyance fee exemptions
- `cincy:sketchIdCode` object property on `cincy:ParcelYearState` linking to `cincy:SketchIdCode`
- Updated `cincy:deedType` from DatatypeProperty (xsd:string) to ObjectProperty referencing `cincy:DeedType`

## [0.1.0] - 2026-04-05

### Added
- Initial Cincinnati Housing Knowledge Graph Ontology
  - Core classes: Parcel, ParcelYearState, Party (Person, Organization, LLC, Trust, GovernmentEntity, NonProfit, MortgageServicer)
  - Assessment and valuation classes: Assessment
  - Taxation classes: TaxDistrict, SchoolDistrict, Levy, TaxBill
  - Exemption classes: Exemption, HomesteadExemption, OtherExemption
  - Abatement classes: Abatement, TIFAbatement, OtherAbatement
  - TIF District classes: TIFDistrict
  - Rental registration classes: RentalRegistration
  - Property relationships: ownership, mortgages, tenure
  - Temporal support: tax year tracking via OWL-Time
- Hamilton County Land Use Codes vocabulary (SKOS ConceptScheme)
  - 8 top-level categories (1xx–8xx)
  - Detailed codes aligned with Ohio Department of Tax Equalization (DTE)
- Project documentation and query examples
- Standard repository structure following ontology project conventions
