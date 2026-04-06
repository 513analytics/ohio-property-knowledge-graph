#!/bin/bash

# Validate Turtle (.ttl) files in the ontology/ directory
# Requires Apache Jena (riot) or Raptor 2

set -e

ONTOLOGY_DIR="ontology"
VALID=true

# Color codes for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "Validating Turtle files in $ONTOLOGY_DIR/"
echo "============================================"

# Check if directory exists
if [ ! -d "$ONTOLOGY_DIR" ]; then
    echo -e "${RED}Error: Directory '$ONTOLOGY_DIR' not found${NC}"
    exit 1
fi

# Find all .ttl files
TTL_FILES=$(find "$ONTOLOGY_DIR" -name "*.ttl" -type f)

if [ -z "$TTL_FILES" ]; then
    echo -e "${YELLOW}No .ttl files found in $ONTOLOGY_DIR/${NC}"
    exit 0
fi

# Try to use riot (Apache Jena) or raptor2
if command -v riot &> /dev/null; then
    VALIDATOR="riot"
    echo "Using Apache Jena (riot) for validation"
elif command -v raptor2 &> /dev/null; then
    VALIDATOR="raptor2"
    echo "Using Raptor 2 for validation"
else
    echo -e "${YELLOW}Warning: No Turtle validator found (riot or raptor2)${NC}"
    echo "Install with:"
    echo "  - macOS: brew install jena"
    echo "  - Ubuntu: apt-get install raptor2-utils"
    echo "  - Or use an online validator: http://www.earlgrey.io/"
    exit 1
fi

echo ""

# Validate each file
for FILE in $TTL_FILES; do
    echo -n "Checking $FILE ... "

    if [ "$VALIDATOR" = "riot" ]; then
        if riot --validate "$FILE" > /dev/null 2>&1; then
            echo -e "${GREEN}✓ Valid${NC}"
        else
            echo -e "${RED}✗ Invalid${NC}"
            riot --validate "$FILE" 2>&1 | head -10
            VALID=false
        fi
    elif [ "$VALIDATOR" = "raptor2" ]; then
        if raptor2 -i turtle "$FILE" > /dev/null 2>&1; then
            echo -e "${GREEN}✓ Valid${NC}"
        else
            echo -e "${RED}✗ Invalid${NC}"
            raptor2 -i turtle "$FILE" 2>&1 | head -10
            VALID=false
        fi
    fi
done

echo ""
if [ "$VALID" = true ]; then
    echo -e "${GREEN}All files are valid!${NC}"
    exit 0
else
    echo -e "${RED}Some files have errors. Fix them and try again.${NC}"
    exit 1
fi
