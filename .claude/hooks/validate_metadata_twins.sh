#!/usr/bin/env bash
# Validate that every .txt file has a corresponding .json metadata twin
# Exceptions: Special system files (TREE.txt, integrity.txt, etc)

set -e

EXIT_CODE=0
REPO_ROOT=$(git rev-parse --show-toplevel)

# Find all .txt files under raw-text/ (excluding special cases)
while IFS= read -r -d '' txt_file; do
    # Skip .json.txt files (these are special JSON-as-text in meta/)
    if [[ "$txt_file" =~ \.json\.txt$ ]]; then
        continue
    fi

    # Skip .tsv.txt files (TSV tables)
    if [[ "$txt_file" =~ \.tsv\.txt$ ]]; then
        continue
    fi

    # Skip .dot.txt files (Graphviz diagrams)
    if [[ "$txt_file" =~ \.dot\.txt$ ]]; then
        continue
    fi

    # Skip system files in meta/ (TREE.txt, integrity.txt)
    if [[ "$txt_file" =~ /meta/(TREE|integrity)\.txt$ ]]; then
        continue
    fi

    # Check if corresponding .json metadata file exists
    json_twin="${txt_file%.txt}.json"

    if [[ ! -f "$json_twin" ]]; then
        echo "ERROR: File '$txt_file' is missing its .json metadata twin"
        echo "       Expected: $json_twin"
        echo "       Every .txt content file MUST have a .json metadata file"
        EXIT_CODE=1
    fi
done < <(find "${REPO_ROOT}/online-resources/raw-text" -type f -name "*.txt" -print0 2>/dev/null || true)

if [[ $EXIT_CODE -eq 0 ]]; then
    echo "✓ All .txt files have corresponding .json metadata twins"
fi

exit $EXIT_CODE
