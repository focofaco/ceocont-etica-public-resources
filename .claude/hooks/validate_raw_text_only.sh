#!/usr/bin/env bash
# Validate that files under online-resources/raw-text/ are .txt only

set -e

EXIT_CODE=0

for file in "$@"; do
    # Only check files under raw-text/
    if [[ ! "$file" =~ ^online-resources/raw-text/ ]]; then
        continue
    fi

    # Check if file ends with .txt
    if [[ ! "$file" =~ \.txt$ ]]; then
        echo "ERROR: File '$file' does not end with .txt extension"
        echo "       All files under online-resources/raw-text/ MUST be .txt files"
        EXIT_CODE=1
    fi

    # Check for forbidden extensions
    if [[ "$file" =~ \.(html|htm|js|css|json|xml|pdf|png|jpg|jpeg|gif|svg|webp)$ ]]; then
        echo "ERROR: File '$file' has forbidden extension"
        echo "       Only .txt files allowed (including .tsv.txt, .dot.txt, .json.txt)"
        EXIT_CODE=1
    fi
done

exit $EXIT_CODE
