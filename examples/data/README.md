# Example Data

This directory is reserved for example RDF data files that demonstrate the cincinnati Housing Knowledge Graph ontology in use.

## Content

Currently this directory is empty. When actual property data is available, example RDF triples in Turtle format can be placed here to show:

- Sample parcels with their attributes
- Ownership relationships
- Assessments and valuations
- Tax bills and exemptions

## Format

Example data files would use Turtle (.ttl) format and reference the ontology classes:

```turtle
@prefix cincy: <http://kg.513analytics.com/ont/cincy#> .
@prefix ex: <http://example.com/cincinnati/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

# Example parcel
ex:parcel_001
    a cincy:Parcel ;
    cincy:hasParcelYearState ex:pys_001_2025 ;
    cincy:hasOwnership ex:ownership_001 .

# 2025 tax year state
ex:pys_001_2025
    a cincy:ParcelYearState ;
    cincy:taxYear "2025"^^xsd:gYear ;
    cincy:ownerOccupied "true"^^xsd:boolean ;
    cincy:homesteadExemption "true"^^xsd:boolean .
```

## Usage

When data files are available:

1. Load them into a SPARQL endpoint or RDF store
2. Run the example queries from `../queries/` against the data
3. Modify queries to explore the data

## See Also

- [Example Queries](../queries/) — Ready-to-run SPARQL queries
- [Ontology Overview](../../docs/ontology-overview.md) — Class and property definitions
