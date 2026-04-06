# Changelog

All notable changes to this project will be documented in this file.

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
