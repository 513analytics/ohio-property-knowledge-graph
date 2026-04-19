# Example SPARQL Queries

This directory contains example SPARQL queries demonstrating how to query the cincinnati Housing Knowledge Graph ontology.

## Query Files

### 1. [list-parcels.rq](list-parcels.rq)
Lists all parcels in the knowledge graph with their identifiers and labels.

**Use case:** Discovering what parcels are available, basic exploration.

---

### 2. [find-residential-property.rq](find-residential-property.rq)
Finds all parcels with Residential land use codes for a given tax year.

**Use case:** Filtering properties by land use classification.

---

### 3. [owner-lookup.rq](owner-lookup.rq)
Finds all parcels owned by a specific person, along with their ownership details.

**Use case:** Finding all properties owned by an individual or organization.

---

### 4. [property-valuation.rq](property-valuation.rq)
Retrieves property assessments, including land value, improvements value, and total assessed value.

**Use case:** Analyzing property valuations, finding high-value properties.

---

### 5. [homestead-exempt-properties.rq](homestead-exempt-properties.rq)
Finds all owner-occupied properties with homestead exemptions for a given tax year.

**Use case:** Identifying owner-occupied residential properties.

---

### 6. [transfer-history.rq](transfer-history.rq)
Returns all recorded transfers for a given parcel, including sale price, deed type, transfer classification, parties, and conveyance fee details.

**Use case:** Investigating the ownership chain and transaction history of a property, identifying arm's length sales vs. non-market transfers.

---

### 7. [mortgage-lookup.rq](mortgage-lookup.rq)
Returns all mortgages recorded against a parcel, including lender, amount, interest rate, term, type, payment structure, and satisfaction status.

**Use case:** Understanding the financing history and current liens on a property. Identifying active vs. satisfied mortgages.

---

### 8. [ownership-interests.rq](ownership-interests.rq)
Returns how title is held for parcels, including ownership type (survivorship tenancy, tenancy in common, life estate, etc.), fractional interests, and remainder holders.

**Use case:** Analyzing co-ownership patterns, identifying survivorship tenancies, finding life estate arrangements.

---

### 9. [foreclosure-transfers.rq](foreclosure-transfers.rq)
Finds all transfers classified as foreclosures (judicial, tax, expedited), sheriff's sales, and auditor's sales within a date range.

**Use case:** Analyzing foreclosure activity by neighborhood, identifying distressed properties, tracking land bank acquisitions.

---

## Running These Queries

1. Copy the `.rq` file content
2. Paste into your SPARQL endpoint or client
3. Execute the query against your data
4. Modify the FILTER clauses (dates, names, values) as needed

## Query Template

All queries follow this structure:

```sparql
PREFIX cincy: <http://kg.513analytics.com/ont/cincy#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?variable1 ?variable2
WHERE {
  # Graph pattern matching
  ?variable1 a cincy:SomeClass ;
             cincy:someProperty ?variable2 .

  # Optional filters
  FILTER (?variable2 = "some value")
}
LIMIT 100
```

## Data Availability

**Note:** These are ontology schemas with example vocabulary. When actual RDF data is loaded into a SPARQL endpoint, these queries can be executed against real property records.

## Customization

To adapt these queries:

1. **Change the tax year:**
   ```sparql
   cincy:taxYear "2025"^^xsd:gYear
   # Change 2025 to your desired year
   ```

2. **Change the owner name:**
   ```sparql
   FILTER (regex(?ownerName, "^Smith", "i"))
   # Change "Smith" to search for different names
   ```

3. **Change the land use code:**
   ```sparql
   skos:notation "5xx"
   # Change "5xx" (Residential) to other codes:
   # "1xx" = Agricultural
   # "2xx" = Mineral Lands & Rights
   # "3xx" = Industrial
   # "4xx" = Commercial
   # "5xx" = Residential
   # "6xx" = Publicly Owned
   # "7xx" = Abated
   # "8xx" = Public Utilities
   ```

4. **Change the value range:**
   ```sparql
   FILTER (?value > "100000"^^xsd:decimal && ?value < "500000"^^xsd:decimal)
   # Adjust the numbers to your desired range
   ```

---

## Tips

- Use `LIMIT` during development to avoid overwhelming results
- Test with simpler queries first, then add complexity
- See [SPARQL Query Guide](../../docs/sparql-guide.md) for more patterns and functions
- Check [Glossary](../../docs/glossary.md) for term definitions

---

## Need Help?

- [SPARQL Query Guide](../../docs/sparql-guide.md) — Common query patterns
- [Ontology Overview](../../docs/ontology-overview.md) — Class and property definitions
- [Glossary](../../docs/glossary.md) — Term definitions
