# Glossary

## Property & Land Administration

**Abatement**
Tax relief or forgiveness, typically granted through incentive programs like TIF (Tax Increment Financing). Abatements reduce the assessed value or taxable value, decreasing the tax bill. Abatements typically expire after a fixed number of years.

**Assessment / Assessed Value**
The appraised value of property for tax purposes. Ohio uses a 6-year reappraisal cycle with triennial (3-year) updates. Assessed value consists of three components: land value, improvements value, and agricultural use value (CAUV).

**Auditor Parcel Number (APN) / Parcel ID**
A composite identifier for a parcel: book + page + parcel-ID-on-page + mltown. Assigned by the County Auditor.

**Book & Page**
Reference to the Auditor's record books where parcel information is recorded. Used as part of the Parcel identifier.

**CAUV (Current Agricultural Use Value)**
The assessed value of agricultural land based on its capacity to produce income, not its market value. Lower than fair market value for farmland.

**Cadastral**
Relating to a cadastre — an official register or map of properties, their ownership, and boundaries. The Parcel is the basic cadastral unit.

**Exemption**
Tax relief based on property type or ownership status. Common exemptions include:
- **Homestead Exemption** — for owner-occupied residential properties
- **Government/Public Exemption** — for government-owned property
- **Nonprofit Exemption** — for qualified nonprofit organizations
- **Agricultural Exemption** — for active farmland

**Improvements**
Structures and man-made objects on a parcel (buildings, driveways, etc.). Assessed separately from the land value.

**Levy**
An individual tax rate or tax obligation within a tax district. A parcel's tax bill is the sum of levies from all applicable jurisdictions. Expressed in millage (tax per $1,000 of assessed value).

**Millage**
The property tax rate, expressed as dollars per $1,000 of assessed value. Example: 25 millage = $25 tax per $1,000 of assessed value.

**Mortgage Servicer**
The organization that collects mortgage payments and pays taxes/insurance from escrow accounts on behalf of the owner.

**Parcel**
The fundamental unit of real property. A legally defined area of land identified by an Auditor Parcel Number. Parcels may be subdivided or consolidated over time.

**Parcel Year State**
A snapshot of a parcel's mutable attributes for a single tax year. Changes between years are captured in separate ParcelYearState entities (e.g., different owner, different land use code, different exemption status).

**Party**
A person or organization with a legal relationship to property (owner, mortgagee, agent, etc.).

**Rental Registration**
The status and details of a property registered as rental property. Includes contact information for the management agent.

**Taxable Value**
The value against which the tax rate is applied. Calculated as: Assessed Value − Exemptions − Abatements − TIF Reductions.

**Tax Bill**
The computed tax obligation for a parcel in a given tax year. Calculated as: Taxable Value × (Total Millage Rate).

**Tax District**
A geographic area that determines which levies apply to parcels within it. Each parcel is in exactly one tax district. A tax district is typically a composite of overlapping jurisdictions (city, county, school district, library district, park district, etc.).

**TIF District (Tax Increment Financing)**
A geographic area where increases in property tax revenue from new development are captured and reinvested in district improvements (infrastructure, schools, etc.). Properties in TIF districts may receive abatements.

**Tenure**
The legal relationship between a person/organization and property (ownership, mortgage, easement, etc.).

---

## Data Standards & Ontology

**Dublin Core**
A widely adopted vocabulary for describing resources with properties like title, creator, date, description, and license.

**GeoSPARQL**
An OGC (Open Geospatial Consortium) standard for representing and querying geospatial data in RDF. Includes classes like Feature, geometry representations, and spatial relationships.

**ISO 19152 LADM (Land Administration Domain Model)**
An international standard for modeling land administration data, including parties, rights, parcels, and surveying information. This ontology aligns with LADM concepts.

**OWL (Web Ontology Language)**
A semantic web standard for describing ontologies—the structure and relationships of entities in a domain.

**OWL-Time**
A W3C standard for temporal entities, intervals, and instants in RDF. Used to represent time-varying properties and temporal relationships.

**RDF (Resource Description Framework)**
The foundational semantic web standard for representing structured data as triples (subject–predicate–object).

**SKOS (Simple Knowledge Organization System)**
A W3C standard for representing controlled vocabularies, thesauri, and classification schemes. This project uses SKOS for the land use code vocabulary.

**SPARQL**
A query language for RDF data. Similar to SQL for relational databases. SPARQL can retrieve, filter, and aggregate RDF triples.

**Turtle (TTL)**
A text-based serialization format for RDF. Easier to read than XML or JSON-LD. This project uses Turtle for all ontology files.

---

## Hamilton County Tax & Governance

**County Auditor**
The official responsible for maintaining property records, assessing values, and administering tax collection in Hamilton County, Ohio.

**Land Use Code**
A standardized classification of how property is used (Residential, Commercial, Industrial, Agricultural, etc.). Codes range from 100–899 and are aligned with the Ohio Department of Tax Equalization (DTE) standards.

**Minor Township (MLtown)**
One of the geographic subdivisions within Hamilton County. Part of the Auditor Parcel Number.

**Ohio Department of Tax Equalization (DTE)**
The state agency responsible for ensuring equitable property assessment across Ohio. Sets standards for land use codes and assessment practices.

**School District**
A geographic jurisdiction responsible for public education. School district levies are the largest recipients of property tax revenue in Ohio.

---

## Common Abbreviations

| Abbreviation | Meaning |
|---|---|
| APN | Auditor Parcel Number |
| CAUV | Current Agricultural Use Value |
| DTE | Ohio Department of Tax Equalization |
| GeoSPARQL | Geospatial SPARQL (OGC standard) |
| IRI | Internationalized Resource Identifier (unique URI for ontology concepts) |
| LADM | Land Administration Domain Model (ISO 19152) |
| LLC | Limited Liability Company |
| OGC | Open Geospatial Consortium |
| OWL | Web Ontology Language |
| OWL-Time | W3C OWL for temporal entities |
| RDF | Resource Description Framework |
| SKOS | Simple Knowledge Organization System |
| SPARQL | SPARQL Protocol and RDF Query Language |
| TIF | Tax Increment Financing |
| TTL | Turtle (RDF serialization format) |
| W3C | World Wide Web Consortium |
