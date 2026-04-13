# Ontology Overview

## File Information

- **Ontology:** `cincy-housing.ttl`
- **Version:** 0.3.0
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

### 4. Geographic Reference Areas

#### **Neighborhood**
A named geographic area within Hamilton County used as a high-level grouping for appraisal areas. Within Cincinnati, neighborhoods align with community council areas.

**Superclasses:** `geo:Feature`

**Properties:**
- `rdfs:label` — neighborhood name
- `cincy:neighborhoodOf` — links to child AppraisalArea entities

---

#### **AppraisalArea**
A sub-area within a neighborhood used by the County Auditor for mass appraisal comparisons during the Ohio 6-year reappraisal cycle. Identified by a 5-digit code.

**Superclasses:** `geo:Feature`

**Properties:**
- `cincy:appraisalAreaCode` (xsd:string) — 5-digit code
- `cincy:inNeighborhood` — links to parent Neighborhood
- `rdfs:label` — area description

---

### 5. Taxation

#### **TaxDistrict**
A geographic area determining which levies apply. Composites of overlapping jurisdictions (city, county, school, library, park, etc.). Identified by a 3-digit code.

**Properties:**
- `cincy:districtCode` (xsd:string) — 3-digit district code
- `cincy:municipalityName` (xsd:string) — municipality, if any
- `cincy:townshipName` (xsd:string) — township, if any
- `cincy:fireDivisionName` (xsd:string) — fire district, if any
- `cincy:servesSchoolDistrict` — links to SchoolDistrict
- `cincy:hasLevy` — links to Levy entities
- `geo:hasGeometry` — spatial boundary

---

#### **SchoolDistrict**
School districts (tracked separately as largest tax recipients). Identified by a 5-digit IRN code.

**Properties:**
- `cincy:schoolDistrictCode` (xsd:string) — 5-digit IRN
- `rdfs:label` — district name

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

### 6. Exemptions & Abatements

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

### 7. TIF Districts

#### **TIFDistrict**
Tax Increment Financing districts — geographic areas where property tax increases from new development are captured for reinvestment.

**Properties:**
- `cincy:tifName` (xsd:string)
- `cincy:establishedYear` (xsd:gYear)
- `cincy:incrementStart` (xsd:decimal) — baseline value
- `geo:hasGeometry` — spatial boundary

---

### 8. Rental Registration

#### **RentalRegistration**
Tracking of rental properties and contact information.

**Properties:**
- `cincy:registrationYear` (xsd:gYear)
- `cincy:rentingAgent` (Party)
- `cincy:contactPhone`, `cincy:contactEmail`
- `cincy:unitCount` (xsd:integer) — number of rental units

---

### 8. Tax Delinquency

#### **DelinquencyRecord**
A formal designation that a parcel has been placed on the Hamilton County delinquent land list. A parcel becomes delinquent when an unpaid tax balance survives the Treasurer's end-of-year reconciliation — this is distinct from simply having an unpaid installment. Delinquent parcels are subject to county or third-party collector foreclosure if the balance remains unpaid the following year.

**Linked from:**
- `cincy:Parcel` via `cincy:hasDelinquencyRecord`

**Key Properties:**
- `cincy:delinquentAmount` (xsd:integer) — total delinquent balance flagged by the Auditor, in USD
- `cincy:delinquentYear` (xsd:gYear) — the tax year the parcel was placed on the delinquent land list
- `cincy:isUnderRepaymentContract` (xsd:boolean) — whether the owner has entered a formal delinquent tax repayment contract; protects from active foreclosure while payments are current

---

### 9. Census Geography

#### **CensusTract**
A U.S. Census Bureau statistical subdivision of a county (~1,200–8,000 people). The standard unit for neighborhood-level analysis.

**Linked from:**
- `cincy:Parcel` via `cincy:inCensusTract`

**Key Properties:**
- `cincy:tractGEOID` (xsd:string, functional) — 11-digit GEOID: state (2) + county (3) + tract (6). E.g., `39061002700`
- `cincy:tractNumber` (xsd:string) — 6-digit tract code alone (e.g., `002700`)

---

#### **CensusBlock**
The smallest Census geographic unit, bounded by streets or visible features. Every parcel maps to exactly one block.

**Linked from:**
- `cincy:Parcel` via `cincy:inCensusBlock`
- `cincy:CensusTract` via `cincy:tractContainsBlock`

**Key Properties:**
- `cincy:blockGEOID` (xsd:string, functional) — 15-digit GEOID: state (2) + county (3) + tract (6) + block (4). E.g., `390610027001001`
- `cincy:blockNumber` (xsd:string) — 4-digit block number within its tract (e.g., `1001`)

---

### 10. Property Transfers

#### **TransferEvent**
Records an ownership change for a parcel. Enhanced in v0.3.0 with conveyance fee tracking, arm's-length classification, and transfer type categorization.

**Linked from:**
- `cincy:Parcel` via `cincy:hasTransfer`

**Key Properties:**
- `cincy:salePrice` (xsd:integer) — sale price in USD
- `cincy:transferDate` (xsd:date) — date of transfer
- `cincy:instrumentNumber` (xsd:string) — county recorder instrument number
- `cincy:deedType` — links to DeedType (see `cincy-deed-types.ttl`)
- `cincy:transferType` — links to TransferClassification (arm's length, foreclosure, gift, etc.)
- `cincy:fromParty` — the grantor/seller
- `cincy:toParty` — the grantee/buyer
- `cincy:financedBy` — links to the Mortgage used to finance the purchase, if any
- `cincy:conveyanceFee` (xsd:decimal) — Ohio conveyance fee paid ($4.00 per $1,000 in Hamilton County)
- `cincy:isConveyanceFeeExempt` (xsd:boolean) — exempt per ORC 319.54(G)
- `cincy:isArmsLength` (xsd:boolean) — true for market-rate transactions between unrelated parties
- `cincy:dteFormNumber` (xsd:string) — Ohio DTE Form 100 or 100EX number

---

#### **Mortgage**
A recorded lien on a parcel securing a debt obligation. Ohio is a lien theory state — the borrower retains legal title while the lender holds a security interest.

**Linked from:**
- `cincy:Parcel` via `cincy:hasMortgage`
- `cincy:TransferEvent` via `cincy:financedBy`

**Key Properties:**
- `cincy:mortgageAmount` (xsd:integer) — original principal in USD
- `cincy:mortgageDate` (xsd:date) — execution date
- `cincy:mortgageRecordingDate` (xsd:date) — date recorded with county recorder
- `cincy:mortgageInstrumentNumber` (xsd:string) — county recorder instrument number
- `cincy:interestRate` (xsd:decimal) — annual rate as percentage
- `cincy:termMonths` (xsd:integer) — loan term in months (e.g., 360 for 30-year)
- `cincy:mortgageType` — links to MortgageType (conventional, FHA, VA, OHFA, etc.)
- `cincy:paymentStructure` — links to PaymentStructure (amortizing, balloon, interest-only, etc.)
- `cincy:mortgagor` — the borrower (Party)
- `cincy:mortgagee` — the lender (Party)
- `cincy:isOpenEnd` (xsd:boolean) — open-end mortgage under ORC 5301.232
- `cincy:maxOpenEndAmount` (xsd:integer) — maximum secured amount for open-end mortgages
- `cincy:isSatisfied` (xsd:boolean) — true if paid off (ORC 5301.36)
- `cincy:satisfactionDate` (xsd:date) — date of payoff
- `cincy:lienPriority` (xsd:integer) — priority position (1 = first mortgage)

---

#### **OwnershipInterest**
Records how one or more parties hold title to a parcel. Ohio recognizes survivorship tenancy (ORC 5302.20), tenancy in common, life estate with remainder, trust ownership, and TOD designation. Ohio does NOT recognize tenancy by the entireties or community property.

**Linked from:**
- `cincy:Parcel` via `cincy:hasOwnershipInterest`

**Key Properties:**
- `cincy:interestHolder` — the party holding this interest
- `cincy:ownershipType` — links to OwnershipType (survivorship tenancy, tenancy in common, life estate, etc.)
- `cincy:interestFraction` (xsd:decimal) — fractional share (e.g., 0.5 for 50%)
- `cincy:interestStartDate` (xsd:date) — when this interest was established
- `cincy:interestEndDate` (xsd:date) — when this interest terminated
- `cincy:remainderHolder` — for life estates: the party receiving the property upon the life tenant's death

---

#### **HeirsPropertyDesignation**
A designation that a parcel is heirs' property (also called "tangled title"). This occurs when the owner of record is deceased and the surviving heirs continue to occupy or hold the property without clearing title through probate court. Under Ohio intestate succession (ORC 2105.06), heirs hold undivided fractional interests as tenants in common by operation of law, but without a recorded deed the title remains clouded and unmarketable. Ohio adopted the Uniform Partition of Heirs Property Act (ORC 5307.20 et seq., effective April 6, 2023) to protect heirs from forced partition sales.

**Linked from:**
- `cincy:Parcel` via `cincy:hasHeirsPropertyDesignation`

**Key Properties:**
- `cincy:decedentOwner` — the deceased party who remains the owner of record
- `cincy:decedentDeathDate` (xsd:date) — date of death, if known
- `cincy:estimatedHeirCount` (xsd:integer) — estimated number of potential heirs
- `cincy:isOccupiedByHeir` (xsd:boolean) — whether one or more heirs occupy the property
- `cincy:heirsPropertyIdentifiedDate` (xsd:date) — when the property was flagged
- `cincy:isTitleCleared` (xsd:boolean) — whether title has been resolved
- `cincy:titleClearedDate` (xsd:date) — date title was cleared, if resolved

---

### 11. Transfer and Mortgage Vocabularies

See [`cincy-transfer-vocab.ttl`](../ontology/cincy-transfer-vocab.ttl) for four SKOS ConceptSchemes:

**Transfer Classification Scheme** — Classifies the nature of transfers:
- **Market Sales** — arm's length sale, short sale, land contract sale
- **Court-Ordered and Involuntary** — judicial foreclosure, tax foreclosure (standard/expedited), sheriff's sale, auditor's sale, divorce, eminent domain
- **Family and Estate** — gift, inheritance, survivorship transfer, TOD, life estate termination
- **Entity and Organizational** — corporate/LLC transfer, trust transfer
- **Government** — land bank transfer, government acquisition/disposition

**Mortgage Type Scheme** — Classifies mortgage loans:
- **Conventional** — conforming, jumbo, purchase money, open-end
- **Government-Backed** — FHA, VA, USDA
- **Ohio State Programs** — OHFA first-time homebuyer, Ohio Heroes, down payment assistance
- **Special Purpose** — reverse mortgage, HELOC, construction loan, land installment contract

**Payment Structure Scheme** — How the mortgage is repaid:
- Fixed rate fully amortizing, adjustable rate (ARM), balloon, interest-only, graduated payment

**Ownership Type Scheme** — Ohio-specific forms of title holding:
- Sole ownership, survivorship tenancy (ORC 5302.20), tenancy in common, life estate, trust ownership, TOD designation (ORC 5302.22), heirs' property / tangled title

---

## Land Use Vocabulary

See [`cincy-land-use-codes.ttl`](../ontology/cincy-land-use-codes.ttl) for the complete SKOS ConceptScheme.

**Top-level categories** (per Ohio Administrative Code 5703-25-10):
- **1xx** — Agricultural
- **2xx** — Mineral Lands & Rights
- **3xx** — Industrial
- **4xx** — Commercial
- **5xx** — Residential
- **6xx** — Exempt
- **7xx** — Special Tax Abatements
- **8xx** — Public Utilities

**Reference data files:**
- `cincy-land-use-codes.ttl` — All use codes (state-defined + Hamilton County extensions)
- `cincy-appraisal-areas.ttl` — 1,771 appraisal areas across 100 neighborhoods
- `cincy-tax-districts.ttl` — 124 tax districts with jurisdiction breakdown
- `cincy-school-districts.ttl` — 23 school districts with IRN codes

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
