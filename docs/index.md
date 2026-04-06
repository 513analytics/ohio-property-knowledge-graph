# Documentation Index

Welcome to the Ohio Property Knowledge Graph documentation.

## Overview

This project provides a semantic ontology for Cincinnati and Hamilton County, Ohio real estate data. The ontology defines the structure and relationships for modeling:

- **Real property parcels** — the fundamental cadastral units
- **Ownership and tenure** — persons, organizations, and their relationships to property
- **Valuation and assessment** — land value, improvements, and tax assessment
- **Taxation** — tax districts, levies, and tax bills
- **Land use classification** — standardized codes for property use types
- **Exemptions and abatements** — tax relief mechanisms and their tracking

## Getting Started

1. **First time?** Start with the [Ontology Overview](ontology-overview.md) to understand the main classes and relationships.

2. **Looking for a specific term?** Check the [Glossary](glossary.md) for definitions of key concepts.

3. **Want to query the data?** Read the [SPARQL Query Guide](sparql-guide.md) and see [example queries](../examples/queries/).

## Key Concepts

### The Parcel
The **Parcel** is the central entity in this ontology. Every parcel is identified by a composite key:
- **Book** and **Page** — audit book and page references
- **Parcel ID** — position on that page
- **Mltown** — minor township
Together these form the Auditor's Parcel Number.

### Time-Varying Properties
Many properties change between tax years (owner, land use code, exemption status). These are captured via **ParcelYearState**, which snapshots mutable attributes for a single tax year.

### Standards Alignment
This ontology aligns with:
- **ISO 19152 LADM** — for cadastral and land administration concepts
- **OGC GeoSPARQL** — for geospatial features and spatial relationships
- **W3C SKOS** — for controlled vocabularies (land use codes)
- **W3C OWL-Time** — for temporal reasoning

## Files

- **[ontology-overview.md](ontology-overview.md)** — Classes, properties, and structure
- **[glossary.md](glossary.md)** — Definitions of key terms
- **[sparql-guide.md](sparql-guide.md)** — How to write SPARQL queries
- **[../ontology/](../ontology/)** — The actual ontology files (Turtle/RDF format)
- **[../examples/queries/](../examples/queries/)** — Example SPARQL queries
