# Utility Scripts

This directory contains helper scripts for working with the ontology.

## Available Scripts

### [validate.sh](validate.sh)

Validates the syntax of Turtle (.ttl) ontology files.

**Usage:**

```bash
bash scripts/validate.sh
```

**What it does:**
- Checks that all `.ttl` files in the `ontology/` directory are valid Turtle
- Reports errors or success
- Requires a Turtle validator (e.g., `riot`, `raptor2`, or online validators)

## Requirements

To run local validation, you'll need one of:

- **Apache Jena** — `riot` command for Turtle validation
- **Raptor 2** — `raptor2` command
- Online validators like [EarlGrey](http://www.earlgrey.io/)

### Install Apache Jena (macOS via Homebrew)

```bash
brew install jena
```

### Install Raptor 2 (macOS via Homebrew)

```bash
brew install raptor2
```

## Adding New Scripts

To add utility scripts:

1. Create a new shell script (`.sh`) or Python script (`.py`)
2. Add documentation to this README
3. Include usage examples

---

## Tips

- Always test scripts locally before committing
- Include error checking and helpful output messages
- Document any external dependencies
