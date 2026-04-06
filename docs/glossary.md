# Glossary

## Property & Land Administration

**Abatement**
Tax relief or forgiveness, typically granted through incentive programs like TIF (Tax Increment Financing). Abatements reduce the assessed value or taxable value, decreasing the tax bill. Abatements typically expire after a fixed number of years.

**Appraisal Area**
A geographic sub-area within a neighborhood used by the Hamilton County Auditor for mass appraisal comparisons. Assessors group comparable parcels within an appraisal area to establish market values during the Ohio 6-year reappraisal cycle. Identified by a 5-digit code. Within the City of Cincinnati, appraisal areas align with recognized neighborhood boundaries.

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

**Platted / Unplatted**
A **platted** lot is one that has been formally surveyed and recorded on an official subdivision plat map with defined lot boundaries. **Unplatted** land has not been formally subdivided; it is described by metes-and-bounds or acreage rather than lot numbers. In the Ohio land use coding system, the third digit of residential codes (500s) distinguishes platted lots (0) from unplatted tracts by acreage band (1 through 5).

**Principal and Current Use**
For improved parcels (those with structures), Ohio law (OAC 5703-25-10) requires classification based on the property's principal and current use. When a parcel has multiple uses, the principal use is the use to which the greatest percentage of the parcel's value is devoted. Compare with **Highest and Best Use** for vacant parcels.

**Property Classification (Ohio Two-Tier System)**
Ohio Revised Code Section 5713.041 requires each parcel of taxable real property to be placed into one of two assessment classes: (1) **Residential and agricultural** land and improvements, or (2) **All other** taxable land and improvements, including commercial, industrial, mineral, and public utility. The classification determines the applicable assessment ratio (the percentage of true value subject to taxation).

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

**Highest and Best Use**
For vacant parcels (no structures), Ohio law (OAC 5703-25-10) requires classification based on the parcel's location and its "highest and best probable legal use," rather than its current (non-)use. Compare with **Principal and Current Use** for improved parcels.

**Land Use Code**
A 3-digit classification code for real property defined by Ohio Administrative Code Rule 5703-25-10 (per ORC Section 5713.041). The first digit identifies the major use category, and the last two digits identify the sub-use. Eight major categories: Agricultural (1xx), Mineral Lands & Rights (2xx), Industrial (3xx), Commercial (4xx), Residential (5xx), Exempt (6xx), Abatements (7xx), and Public Utilities (8xx). Hamilton County extends the state-defined codes with additional sub-codes for local classification needs. For residential codes, the third digit encodes tract size (0 = platted lot, 1–5 = unplatted acreage bands).

**Minor Township (MLtown)**
One of the geographic subdivisions within Hamilton County. Part of the Auditor Parcel Number.

**Neighborhood**
A named geographic area within Hamilton County used as a high-level grouping for appraisal areas. Within the City of Cincinnati, neighborhood boundaries align with recognized community council areas. Each neighborhood contains one or more appraisal areas.

**OAC 5703-25-10 (Classification of Real Property)**
Ohio Administrative Code rule that defines the land use coding system used by all county auditors. Establishes the 8 major code groups (100–899), the sub-use numbering convention, and the legal definitions for each property class. Effective for tax year 1985. Hamilton County extends this base system with additional local sub-codes.

**Ohio Department of Tax Equalization (DTE)**
The state agency responsible for ensuring uniform and fair property taxation across all 88 Ohio counties. DTE oversees local county auditors, manages the 6-year reappraisal cycle and triennial (3-year) valuation updates, processes real property tax exemptions, and sets statewide standards for land use codes and assessment practices.

**ORC 5713.041**
Ohio Revised Code section that requires each county auditor to classify every parcel into one of two assessment categories: (1) residential and agricultural, or (2) all other taxable property. This classification drives different assessment ratios and is the legal foundation for OAC 5703-25-10.

**School District**
A geographic jurisdiction responsible for public education. School district levies are the largest recipients of property tax revenue in Ohio. Identified by a 5-digit IRN (Institution Revenue Number) code.

---

## Common Abbreviations

| Abbreviation | Meaning |
|---|---|
| APN | Auditor Parcel Number |
| CAUV | Current Agricultural Use Value |
| CRA | Community Reinvestment Area (abatement type, code 710) |
| DTE | Ohio Department of Tax Equalization |
| GeoSPARQL | Geospatial SPARQL (OGC standard) |
| IRI | Internationalized Resource Identifier (unique URI for ontology concepts) |
| IRN | Institution Revenue Number (school district identifier) |
| LADM | Land Administration Domain Model (ISO 19152) |
| LLC | Limited Liability Company |
| OAC | Ohio Administrative Code |
| OGC | Open Geospatial Consortium |
| ORC | Ohio Revised Code |
| OWL | Web Ontology Language |
| OWL-Time | W3C OWL for temporal entities |
| RDF | Resource Description Framework |
| SKOS | Simple Knowledge Organization System |
| SPARQL | SPARQL Protocol and RDF Query Language |
| TIF | Tax Increment Financing |
| TTL | Turtle (RDF serialization format) |
| W3C | World Wide Web Consortium |
