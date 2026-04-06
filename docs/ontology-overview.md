# Ontology Overview

## File Information

- **Ontology:** `cincy-housing.ttl`
- **Version:** 0.1.0
- **Created:** 2026-04-05
- **IRI:** `http://kg.513analytics.com/ont/cincy`
- **License:** CC0 1.0 Universal (Public Domain)

## Namespace Prefixes

| Prefix  | Namespace | Description |
|---------|-----------|-------------|
| `cincy` | `http://kg.513analytics.com/ont/cincy#` | cincinnati Housing Ontology |
| `owl`   | `http://www.w3.org/2002/07/owl#` | OWL vocabulary |
| `rdf`   | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` | RDF vocabulary |
| `rdfs`  | `http://www.w3.org/2000/01/rdf-schema#` | RDF Schema |
| `xsd`   | `http://www.w3.org/2001/XMLSchema#` | XML Schema datatypes |
| `skos`  | `http://www.w3.org/2004/02/skos/core#` | SKOS vocabulary |
| `geo`   | `http://www.opengis.net/ont/geosparql#` | GeoSPARQL |
| `schema` | `https://schema.org/` | Schema.org vocabulary |
| `time`  | `http://www.w3.org/2006/time#` | OWL-Time |
| `qudt`  | `http://qudt.org/schema/qudt/` | QUDT Units & Quantities |
| `dcterms` | `http://purl.org/dc/terms/` | Dublin Core |
| `ladm`  | `http://www.iso.org/19152/ladm#` | ISO 19152 LADM |

## Core Classes

### 1. Cadastral Entities

#### **Parcel**
The fundamental unit of property. Identified by a composite key: book + page + parcel ID + mltown.

**Superclasses:**
- `geo:Feature` — from GeoSPARQL
- `ladm:LA_SpatialUnit` — from ISO 19152 LADM

**Properties:**
- `cincy:hasParcelYearState` — links to time-varying attributes
- `cincy:hasOwnership` — links to ownership records
- `geo:hasGeometry` — spatial boundary (from GeoSPARQL)

---

#### **ParcelYearState**
A snapshot of mutable parcel attributes for a single tax year. Land use code, owner-occupied status, homestead exemption, rental registration status, and other properties can change between tax years.

**Key Properties:**
- `cincy:taxYear` (xsd:gYear) — the tax year
- `cincy:landUseCode` — property use classification
- `cincy:ownerOccupied` (xsd:boolean)
- `cincy:homesteadExemption` (xsd:boolean)
- `cincy:rentalStatus` — status of rental registration
- `cincy:newConstructionFlag` (xsd:boolean)
- `cincy:recentlyDividedFlag` (xsd:boolean)
- `cincy:boardOfRevisionDispute` (xsd:boolean)

---

### 2. Parties (Ownership & Administration)

**Party** (abstract base class)
- `cincy:Person` — Individual owner or agent
- `cincy:Organization` — Corporate entities and institutions
  - `cincy:LLC` — Limited Liability Company
  - `cincy:Trust` — Trust entities
  - `cincy:GovernmentEntity` — Government agencies
  - `cincy:NonProfit` — Nonprofit organizations
  - `cincy:MortgageServicer` — Mortgage provider or servicer

**Key Properties:**
- `cincy:hasName` (xsd:string)
- `cincy:hasAddress` (xsd:string or Address object)
- `cincy:hasEmail`, `cincy:hasPhone`, `cincy:hasURL`

---

### 3. Valuation & Assessment

#### **Assessment**
A time-bound valuation record. Ohio reappraises on a 6-year cycle with triennial updates.

**Key Properties:**
- `cincy:assessmentYear` (xsd:gYear)
- `cincy:landValue` (xsd:decimal, in dollars)
- `cincy:improvementsValue` (xsd:decimal)
- `cincy:agriculturalUseValue` (CAUV, xsd:decimal)
- `cincy:totalAssessedValue` (sum of above)
- `cincy:taxableValue` (assessed value minus exemptions/abatements)
- `cincy:appraisedBy` — the assessor (Party)

---

### 4. Taxation

#### **TaxDistrict**
A geographic area determining which levies apply. Composites of overlapping jurisdictions (city, county, school, library, park, etc.).

**Properties:**
- `cincy:districtName` (xsd:string)
- `cincy:hasLevies` — links to Levy entities
- `geo:hasGeometry` — spatial boundary

---

#### **SchoolDistrict**
School districts (tracked separately as largest tax recipients).

---

#### **Levy**
An individual tax levy (voted or unvoted).

**Properties:**
- `cincy:millage` (xsd:decimal) — tax rate per $1000 of value
- `cincy:isVoted` (xsd:boolean)

---

#### **TaxBill**
The computed tax obligation for a parcel in a given tax year.

**Properties:**
- `cincy:billYear` (xsd:gYear)
- `cincy:amountDue` (xsd:decimal)
- `cincy:dueDate` (xsd:date)
- `cincy:isPaid` (xsd:boolean)

---

### 5. Exemptions & Abatements

#### **Exemption**
Tax relief based on property classification or ownership.

- `cincy:HomesteadExemption` — for owner-occupied residential properties
- `cincy:OtherExemption` — nonprofit, government, agricultural, etc.

**Properties:**
- `cincy:exemptionType` (xsd:string)
- `cincy:exemptionAmount` (xsd:decimal)
- `cincy:appliedYear` (xsd:gYear)

---

#### **Abatement**
Tax relief granted via incentive programs.

- `cincy:TIFAbatement` — Tax Increment Financing abatement
- `cincy:OtherAbatement` — other abatement programs

**Properties:**
- `cincy:abatementType` (xsd:string)
- `cincy:abatementAmount` (xsd:decimal)
- `cincy:abatementPercent` (xsd:decimal) — percentage (0–100)
- `cincy:appliedYear` (xsd:gYear)
- `cincy:expirationYear` (xsd:gYear)

---

### 6. TIF Districts

#### **TIFDistrict**
Tax Increment Financing districts — geographic areas where property tax increases from new development are captured for reinvestment.

**Properties:**
- `cincy:tifName` (xsd:string)
- `cincy:establishedYear` (xsd:gYear)
- `cincy:incrementStart` (xsd:decimal) — baseline value
- `geo:hasGeometry` — spatial boundary

---

### 7. Rental Registration

#### **RentalRegistration**
Tracking of rental properties and contact information.

**Properties:**
- `cincy:registrationYear` (xsd:gYear)
- `cincy:rentingAgent` (Party)
- `cincy:contactPhone`, `cincy:contactEmail`
- `cincy:unitCount` (xsd:integer) — number of rental units

---

## Land Use Vocabulary

See [`cincy-land-use-codes.ttl`](../ontology/cincy-land-use-codes.ttl) for the complete SKOS ConceptScheme.

**Top-level categories:**
- **1xx** — Agricultural
- **2xx** — Extraction
- **3xx** — Industrial
- **4xx** — Commercial
- **5xx** — Residential
- **6xx** — Publicly Owned
- **7xx** — Abated
- **8xx** — Public Utilities

---

## Imported Ontologies

This ontology imports:
1. **GeoSPARQL 1.1** — geospatial features, geometry, and spatial relationships
2. **W3C SKOS** — concept schemes and controlled vocabularies
3. **W3C OWL-Time** — temporal entities, intervals, and instants

---

## Example Triples (RDF)

```turtle
# A parcel and its 2025 tax year snapshot
ex:parcel_001
    a cincy:Parcel ;
    cincy:hasParcelYearState ex:pys_001_2025 ;
    cincy:hasOwnership ex:ownership_001 ;
    geo:hasGeometry ex:geometry_001 .

ex:pys_001_2025
    a cincy:ParcelYearState ;
    cincy:taxYear "2025"^^xsd:gYear ;
    cincy:landUseCode <http://kg.513analytics.com/ont/cincy#LU_510> ;  # Residential
    cincy:ownerOccupied "true"^^xsd:boolean ;
    cincy:homesteadExemption "true"^^xsd:boolean .

# An owner
ex:owner_john_doe
    a cincy:Person ;
    cincy:hasName "John Doe" ;
    cincy:hasAddress "123 Main St, cincinnati, OH 45202" .

# Ownership relationship
ex:ownership_001
    a cincy:Ownership ;
    cincy:owner ex:owner_john_doe ;
    cincy:parcel ex:parcel_001 ;
    cincy:ownershipStart "2020-01-15"^^xsd:date .

# Assessment
ex:assessment_001_2025
    a cincy:Assessment ;
    cincy:assessmentYear "2025"^^xsd:gYear ;
    cincy:landValue "50000.00"^^xsd:decimal ;
    cincy:improvementsValue "150000.00"^^xsd:decimal ;
    cincy:totalAssessedValue "200000.00"^^xsd:decimal .
```

---

## Design Principles

1. **Time-variability:** Properties that change between tax years (land use, exemptions) are captured in separate entities (ParcelYearState, Exemption) linked to the Parcel.

2. **Composite keys:** Parcels use a composite identifier (book+page+parcel+mltown) reflecting Auditor record-keeping.

3. **Standards alignment:** Classes and properties align with ISO 19152 LADM, GeoSPARQL, and Dublin Core where applicable.

4. **Extensibility:** The ontology is designed to incorporate future data (court records, evictions, foreclosures) while maintaining core parcel/ownership structures.

---

## Next Steps

- [Glossary](glossary.md) — Detailed term definitions
- [SPARQL Query Guide](sparql-guide.md) — How to query the ontology
- [Example Queries](../examples/queries/) — Real query examples
