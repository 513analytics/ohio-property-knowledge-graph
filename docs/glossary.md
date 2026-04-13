# Glossary

## Property & Land Administration

**Abatement**
Tax relief or forgiveness, typically granted through incentive programs like TIF (Tax Increment Financing). Abatements reduce the assessed value or taxable value, decreasing the tax bill. Abatements typically expire after a fixed number of years.

**Appraisal Area**
A geographic sub-area within a neighborhood used by the Hamilton County Auditor for mass appraisal comparisons. Assessors group comparable parcels within an appraisal area to establish market values during the Ohio 6-year reappraisal cycle. Identified by a 5-digit code. Within the City of Cincinnati, appraisal areas align with recognized neighborhood boundaries.

**Assessment / Assessed Value**
The appraised value of property for tax purposes. Ohio uses a 6-year reappraisal cycle with triennial (3-year) updates. Assessed value consists of three components: land value, improvements value, and agricultural use value (CAUV).

**Arm's Length Transaction**
A voluntary sale between unrelated parties, each acting in their own self-interest, at fair market value with adequate time and information. Arm's length sales are the primary metric for comparable sales in appraisals and sales ratio studies. Non-arm's-length transactions (gifts, family transfers, corporate restructurings) are excluded from these analyses.

**Auditor Parcel Number (APN) / Parcel ID**
A composite identifier for a parcel: book + page + parcel-ID-on-page + mltown. Assigned by the County Auditor.

**Book & Page**
Reference to the Auditor's record books where parcel information is recorded. Used as part of the Parcel identifier.

**Balloon Payment**
A mortgage payment structure where regular payments (often interest-only or partially amortizing) are made during the loan term, with a large lump-sum payment of the remaining principal balance due at maturity. Common terms are 5 or 7 years. The borrower must refinance or pay the balloon at the end of the term.

**CAUV (Current Agricultural Use Value)**
The assessed value of agricultural land based on its capacity to produce income, not its market value. Lower than fair market value for farmland.

**Cadastral**
Relating to a cadastre — an official register or map of properties, their ownership, and boundaries. The Parcel is the basic cadastral unit.

**Census Block**
The smallest U.S. Census Bureau geographic unit, bounded by streets, waterways, or other visible features. Identified by a 15-digit GEOID. Every parcel in Hamilton County maps to exactly one census block.

**Census Tract**
A U.S. Census Bureau statistical subdivision of a county designed to contain roughly 1,200–8,000 people with relatively homogeneous population characteristics. Identified by an 11-digit GEOID. Census tracts are the standard unit for neighborhood-level demographic and housing analysis.

**GEOID (Census)**
A standardized numeric identifier for Census geographic units. Built by concatenating FIPS codes: state (2 digits) + county (3 digits) + tract (6 digits) + block (4 digits, blocks only). Hamilton County's FIPS code is `39061` (Ohio = 39, Hamilton = 061).

**Conveyance Fee (Ohio Real Estate Transfer Tax)**
The Ohio transfer tax levied on real property conveyances. Consists of a mandatory state fee of $1.00 per $1,000 of consideration (ORC 319.54) plus an optional county permissive fee of up to $3.00 per $1,000 (ORC 322.02). Hamilton County levies the full permissive fee, for a combined rate of $4.00 per $1,000 (0.4%). Collected by the county auditor at the time of recording. Certain transfers are exempt, including transfers between spouses, parent-child transfers, court-ordered transfers, and transfers with consideration under $100.

**Deed**
A legal instrument that conveys real property from a grantor to a grantee. Ohio recognizes several deed types with varying levels of title warranty: general warranty deed (full protection), limited warranty deed (protection only during grantor's ownership), quitclaim deed (no warranty), fiduciary deed (executed by a representative), sheriff's deed (from foreclosure sale), and auditor's deed (from tax-forfeited land sale). See `cincy-deed-types.ttl` for the complete vocabulary.

**Delinquent / Delinquency**
A formal designation that a parcel carries an unpaid tax balance that survived the Treasurer's end-of-year reconciliation and was placed on the Hamilton County delinquent land list. A parcel is *unpaid* if it simply has an outstanding balance; it becomes *delinquent* only when that balance persists through year-end. Delinquent parcels are subject to foreclosure by the county or its third-party collector if the balance remains unpaid the following year. The Auditor flags each delinquent parcel with the current delinquent dollar amount.

**Delinquency Penalty**
An interest or penalty charge assessed on a past-due tax installment. Ohio law (ORC 323.121) prescribes penalty rates for late payment, which accrue until the balance is paid or a repayment contract is entered.

**DTE Form 100**
Ohio Department of Tax Equalization Form 100 (Real Property Conveyance Fee Statement of Value and Receipt) is required for all real property transfers. Filed with the county auditor before the deed is recorded. Declares the sale price and whether a conveyance fee exemption applies. Form 100EX is used for exempt transfers. These forms are public records and are the primary source for sale price data in county records.

**Exemption**
Tax relief based on property type or ownership status. Common exemptions include:
- **Homestead Exemption** — for owner-occupied residential properties
- **Government/Public Exemption** — for government-owned property
- **Nonprofit Exemption** — for qualified nonprofit organizations
- **Agricultural Exemption** — for active farmland

**Foreclosure (Ohio)**
The legal process by which a lender forces the sale of a property to satisfy an unpaid mortgage. Ohio is a judicial foreclosure state — all mortgage foreclosures must go through the courts of common pleas (ORC 2323.07). There is no power-of-sale or non-judicial foreclosure in Ohio. The owner may redeem by paying the full judgment amount up until the court confirms the sheriff's sale. Ohio has no statutory post-sale redemption period. Tax foreclosure follows a similar judicial process, with an expedited path available for abandoned or severely delinquent properties (ORC 323.25, 5721.18-19).

**Improvements**
Structures and man-made objects on a parcel (buildings, driveways, etc.). Assessed separately from the land value.

**Levy**
An individual tax rate or tax obligation within a tax district. A parcel's tax bill is the sum of levies from all applicable jurisdictions. Expressed in millage (tax per $1,000 of assessed value).

**Life Estate**
A present possessory interest in property lasting for the lifetime of the life tenant. Upon the life tenant's death, the property passes automatically to the remainderman without probate. The life tenant must avoid waste (ORC 5301.011 et seq.) and is responsible for property taxes and maintenance. In Ohio, Transfer on Death (TOD) affidavits have largely replaced life estates for simple estate planning because TOD is revocable and does not limit the owner's control during life.

**Lien Priority (Ohio)**
The order in which competing liens on a property are satisfied. Ohio follows a "first in time, first in right" rule based on recording date, with key exceptions: (1) real property tax liens have absolute priority over all other liens, including previously recorded mortgages (ORC 5721.10); (2) mechanic's liens relate back to the date of first visible improvement; (3) purchase money mortgages have automatic priority over liens attaching at acquisition.

**Lien Theory State**
A state where the mortgage creates a lien on the property but the borrower retains legal title. Ohio is a lien theory state — the lender has no right to possession unless foreclosure is completed. Compare with "title theory" states where the lender holds legal title until the mortgage is paid.

**Millage**
The property tax rate, expressed as dollars per $1,000 of assessed value. Example: 25 millage = $25 tax per $1,000 of assessed value.

**Mortgage**
A recorded lien on real property securing a debt obligation. In Ohio (a lien theory state), the borrower retains legal title while the lender holds a security interest. Mortgages must be recorded with the county recorder (ORC Chapter 5301) to establish constructive notice and priority. Types include conventional (conforming, jumbo), government-backed (FHA, VA, USDA), and Ohio state program (OHFA) loans. Ohio recognizes open-end mortgages (ORC 5301.232) that allow future advances without re-recording.

**Mortgage Servicer**
The organization that collects mortgage payments and pays taxes/insurance from escrow accounts on behalf of the owner.

**OHFA (Ohio Housing Finance Agency)**
A state agency that administers below-market-rate mortgage programs for Ohio homebuyers. Key programs include: First-Time Homebuyer (for borrowers who have not owned a primary residence in 3 years), Ohio Heroes (reduced rates for military, veterans, teachers, first responders), and Down Payment Assistance (2.5% or 5% grants or forgivable second mortgages). Income and purchase price limits apply by county.

**Open-End Mortgage**
A mortgage under ORC 5301.232 that allows additional advances up to a stated maximum without re-recording. Priority for all advances relates back to the original recording date. Commonly used for Home Equity Lines of Credit (HELOCs).

**Ownership Interest**
The manner in which one or more parties hold title to real property. Ohio recognizes sole ownership, survivorship tenancy (ORC 5302.20), tenancy in common (the default), life estate with remainder, trust ownership, and Transfer on Death designation. Ohio does NOT recognize tenancy by the entireties or community property.

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

**Purchase Money Mortgage**
A mortgage given by the buyer to the seller as part of the purchase price (seller financing). Under Ohio common law, a purchase money mortgage has automatic priority over other liens that attach at the time of acquisition, even if recorded simultaneously.

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

**Repayment Contract (Delinquent Tax)**
A formal agreement between a delinquent property owner and the Hamilton County Auditor to repay a delinquent tax balance over time. A parcel under an active repayment contract is still delinquent, but is protected from active foreclosure proceedings as long as scheduled payments remain current. The Auditor flags parcels under contract separately from those with unpaid delinquent balances and no contract.

**Survivorship Tenancy (Ohio)**
Ohio's statutory form of joint ownership with right of survivorship (ORC 5302.20). Created by deed that includes explicit survivorship language such as "for their joint lives, remainder to the survivor." Upon the death of one tenant, the surviving tenant(s) automatically receive full title without probate. This is Ohio's functional replacement for common-law joint tenancy. Without explicit survivorship language, Ohio presumes a tenancy in common. Very commonly used by married couples in Ohio.

**Tenancy in Common**
The default form of concurrent ownership in Ohio when a deed conveys to two or more persons without specifying survivorship. Each tenant holds an undivided fractional interest that is freely transferable and inheritable. Interests need not be equal. No right of survivorship — a deceased tenant's share passes through their estate.

**Tenure**
The legal relationship between a person/organization and property (ownership, mortgage, easement, etc.).

**Transfer on Death (TOD) Designation**
An Ohio-specific non-probate transfer mechanism (ORC 5302.22). The owner records a TOD designation affidavit naming beneficiaries who receive the property automatically upon the owner's death. The designation is revocable during the owner's lifetime and does not affect the owner's rights to sell, mortgage, or otherwise deal with the property. No interest passes to the beneficiary until the owner's death. Widely used in Ohio estate planning because it is simpler than a life estate or trust.

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
| FHA | Federal Housing Administration |
| GeoSPARQL | Geospatial SPARQL (OGC standard) |
| HCLRC | Hamilton County Land Reutilization Corporation |
| HECM | Home Equity Conversion Mortgage (reverse mortgage) |
| HELOC | Home Equity Line of Credit |
| IRI | Internationalized Resource Identifier (unique URI for ontology concepts) |
| IRN | Institution Revenue Number (school district identifier) |
| LADM | Land Administration Domain Model (ISO 19152) |
| LLC | Limited Liability Company |
| OAC | Ohio Administrative Code |
| OHFA | Ohio Housing Finance Agency |
| OGC | Open Geospatial Consortium |
| ORC | Ohio Revised Code |
| OWL | Web Ontology Language |
| OWL-Time | W3C OWL for temporal entities |
| RDF | Resource Description Framework |
| SKOS | Simple Knowledge Organization System |
| SPARQL | SPARQL Protocol and RDF Query Language |
| TIF | Tax Increment Financing |
| TOD | Transfer on Death |
| TTL | Turtle (RDF serialization format) |
| USDA | U.S. Department of Agriculture |
| VA | U.S. Department of Veterans Affairs |
| W3C | World Wide Web Consortium |
