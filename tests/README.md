# Ontology Validation & Testing

This directory contains SPARQL queries for validating the integrity and completeness of the ontology.

## Purpose

These queries help ensure that:
- All expected classes and properties are defined
- Class hierarchies are correct
- Required properties are present
- Data conforms to the ontology schema

## Validation Queries

### [sparql-tests.rq](sparql-tests.rq)

A collection of SPARQL ASK queries that validate:
- Core classes exist (Parcel, ParcelYearState, Party, etc.)
- Core properties are defined
- Subclass relationships are correct
- Namespace declarations are present

## Running Validation

1. Load the ontology files from `ontology/` into a SPARQL endpoint
2. Run the queries in `sparql-tests.rq` against your endpoint
3. Verify that all ASK queries return `true`

### Example

```bash
# Using curl with a SPARQL endpoint (e.g., Virtuoso)
curl -X POST http://localhost:8890/sparql \
  --data-urlencode "query@sparql-tests.rq"
```

## SPARQL ASK Queries

An ASK query returns `true` or `false`:

```sparql
ASK WHERE {
  cincy:Parcel a owl:Class .
}
```

Returns `true` if the Parcel class is defined; `false` otherwise.

## Adding New Tests

To add validation checks:

1. Identify the ontology rule or requirement
2. Write an ASK query that validates it
3. Add the query to `sparql-tests.rq`
4. Run the query against the ontology

Example: Validate that all land use codes have a notation:

```sparql
PREFIX cincy: <http://kg.513analytics.com/ont/cincy#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

ASK WHERE {
  ?code a cincy:LandUseCode .
  FILTER NOT EXISTS { ?code skos:notation ?notation . }
}
```

If this returns `false`, all land use codes have notations. If it returns `true`, some are missing.

## Best Practices

1. **Test class definitions** — Verify expected classes exist
2. **Test properties** — Verify expected properties are defined
3. **Test relationships** — Verify domain and range constraints
4. **Test controlled vocabularies** — Verify SKOS concept schemes are complete
5. **Test naming conventions** — Verify consistent use of prefixes and naming

## See Also

- [Ontology Overview](../docs/ontology-overview.md) — Class and property definitions
- [SPARQL Query Guide](../docs/sparql-guide.md) — SPARQL syntax and patterns
