# SPARQL Query Guide

This guide explains how to query the cincinnati Housing Knowledge Graph ontology using SPARQL.

## What is SPARQL?

SPARQL is a query language for RDF data—similar to SQL for relational databases. It allows you to:
- **SELECT** specific data from the knowledge graph
- **FILTER** results based on conditions
- **AGGREGATE** data (count, sum, avg, etc.)
- **JOIN** data from multiple entities

## SPARQL Query Structure

A basic SPARQL query has this structure:

```sparql
PREFIX prefix: <namespace>
PREFIX cincy: <http://kg.513analytics.com/ont/cincy#>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>

SELECT ?subject ?predicate ?object
WHERE {
  ?subject a cincy:Parcel .
  ?subject ?predicate ?object .
}
LIMIT 10
```

### Key Elements

- **PREFIX** — Define shorthand for namespaces (optional but recommended)
- **SELECT** — Specify what variables to return (using `?name` syntax)
- **WHERE** — Define the graph pattern(s) to match
- **FILTER** — Add conditions (optional)
- **LIMIT** — Restrict number of results (optional)

---

## Core Namespaces

Use these prefixes in your queries:

```sparql
PREFIX cincy: <http://kg.513analytics.com/ont/cincy#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX time: <http://www.w3.org/2006/time#>
```

---

## Common Query Patterns

### 1. Find All Instances of a Class

```sparql
PREFIX cincy: <http://kg.513analytics.com/ont/cincy#>

SELECT ?parcel
WHERE {
  ?parcel a cincy:Parcel .
}
LIMIT 100
```

Returns all parcels in the knowledge graph.

---

### 2. Get Properties of an Entity

```sparql
PREFIX cincy: <http://kg.513analytics.com/ont/cincy#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?parcel ?label ?comment
WHERE {
  ?parcel a cincy:Parcel ;
          rdfs:label ?label ;
          rdfs:comment ?comment .
}
```

Returns all parcels with their labels and comments.

---

### 3. Filter by Property Value

```sparql
PREFIX cincy: <http://kg.513analytics.com/ont/cincy#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?parcelYearState
WHERE {
  ?parcelYearState a cincy:ParcelYearState ;
                    cincy:taxYear "2025"^^xsd:gYear ;
                    cincy:ownerOccupied "true"^^xsd:boolean .
}
```

Returns all owner-occupied parcels in tax year 2025.

---

### 4. Filter by Land Use Code

```sparql
PREFIX cincy: <http://kg.513analytics.com/ont/cincy#>

SELECT ?parcelYearState ?landUseCode
WHERE {
  ?parcelYearState a cincy:ParcelYearState ;
                    cincy:landUseCode ?landUseCode .
  ?landUseCode skos:notation "5xx" .
}
```

Returns all parcels with Residential land use (5xx codes).

---

### 5. Find Properties in a Range

```sparql
PREFIX cincy: <http://kg.513analytics.com/ont/cincy#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?assessment ?value
WHERE {
  ?assessment a cincy:Assessment ;
              cincy:landValue ?value .
  FILTER (?value > "100000"^^xsd:decimal && ?value < "500000"^^xsd:decimal)
}
```

Returns assessments with land values between $100k and $500k.

---

### 6. Join Multiple Entities

```sparql
PREFIX cincy: <http://kg.513analytics.com/ont/cincy#>

SELECT ?parcel ?owner ?ownerName
WHERE {
  ?parcel a cincy:Parcel ;
          cincy:hasOwnership ?ownership .
  ?ownership cincy:owner ?owner .
  ?owner cincy:hasName ?ownerName .
}
```

Returns all parcels with their owners' names.

---

### 7. Count Results

```sparql
PREFIX cincy: <http://kg.513analytics.com/ont/cincy#>

SELECT (COUNT(?parcel) as ?totalParcels)
WHERE {
  ?parcel a cincy:Parcel .
}
```

Returns the total number of parcels.

---

### 8. Group and Count by Category

```sparql
PREFIX cincy: <http://kg.513analytics.com/ont/cincy#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?landUseLabel (COUNT(?parcelYearState) as ?count)
WHERE {
  ?parcelYearState a cincy:ParcelYearState ;
                    cincy:landUseCode ?landUseCode .
  ?landUseCode skos:prefLabel ?landUseLabel .
}
GROUP BY ?landUseLabel
ORDER BY DESC(?count)
```

Returns counts of parcels grouped by land use code.

---

### 9. Filter by String Pattern

```sparql
PREFIX cincy: <http://kg.513analytics.com/ont/cincy#>

SELECT ?owner ?ownerName
WHERE {
  ?owner a cincy:Person ;
         cincy:hasName ?ownerName .
  FILTER (regex(?ownerName, "^Smith", "i"))
}
```

Returns all persons whose names start with "Smith" (case-insensitive).

---

### 10. Optional Properties

```sparql
PREFIX cincy: <http://kg.513analytics.com/ont/cincy#>

SELECT ?parcel ?owner ?ownerAddress
WHERE {
  ?parcel a cincy:Parcel ;
          cincy:hasOwnership ?ownership .
  ?ownership cincy:owner ?owner .
  OPTIONAL { ?owner cincy:hasAddress ?ownerAddress . }
}
```

Returns parcels with owners, including missing addresses as nulls (rather than excluding those rows).

---

## Data Types

When filtering on values, specify the data type:

```sparql
"2025"^^xsd:gYear              # Year
"2026-04-05"^^xsd:date         # Date
"123.45"^^xsd:decimal          # Decimal number
"true"^^xsd:boolean            # Boolean
"text value"^^xsd:string       # String (default)
```

---

## Useful Functions

| Function | Example | Result |
|----------|---------|--------|
| `STRLEN()` | `STRLEN("hello")` | 5 |
| `UCASE()` | `UCASE("hello")` | "HELLO" |
| `LCASE()` | `LCASE("HELLO")` | "hello" |
| `SUBSTR()` | `SUBSTR("hello", 1, 2)` | "he" |
| `REGEX()` | `REGEX(?name, "^J")` | true/false |
| `YEAR()` | `YEAR(xsd:date)` | numeric year |
| `COUNT()` | `COUNT(?item)` | count of items |
| `SUM()` | `SUM(?value)` | sum of values |
| `AVG()` | `AVG(?value)` | average |
| `MAX()` | `MAX(?value)` | maximum |
| `MIN()` | `MIN(?value)` | minimum |

---

## Running Queries

### Using a SPARQL Endpoint

If you're querying against a SPARQL endpoint (e.g., a Virtuoso or GraphDB server):

1. Copy a query from the examples
2. Paste it into your endpoint's query editor
3. Execute the query
4. View results

### Validating Locally

To validate query syntax without running against data:
- Use an online SPARQL validator like [EarlGrey](http://www.earlgrey.io/) or the SPARQL Query Builder
- Most RDF tools (Protégé, Virtuoso, GraphDB) provide query validation

---

## Best Practices

1. **Use Prefixes** — Makes queries shorter and more readable
2. **Filter Early** — Apply FILTER clauses to reduce intermediate results
3. **Limit Results** — Use LIMIT during development to avoid overwhelming output
4. **Comment Your Queries** — Use `#` for single-line comments
5. **Test Incrementally** — Start simple, add complexity step-by-step

---

## Example Queries

See the [examples/queries/](../examples/queries/) directory for ready-to-run SPARQL queries.

---

## Learn More

- [SPARQL Tutorial](https://www.w3.org/TR/sparql11-query/) — W3C specification
- [SPARQL by Example](http://www.cambridgesemantics.com/semantic-university/sparql-by-example/) — Beginner-friendly guide
- [DBpedia SPARQL Endpoint](https://dbpedia.org/sparql) — Large, public RDF dataset for learning

---

## Next Steps

- [View Example Queries](../examples/queries/)
- [Return to Index](index.md)
