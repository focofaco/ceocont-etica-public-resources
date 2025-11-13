#!/usr/bin/env bash
# Validate that files under online-resources/raw-text/ are .txt only
# Exceptions: README.md and .json metadata twins

set -e

EXIT_CODE=0

for file in "$@"; do
    # Only check files under raw-text/
    if [[ ! "$file" =~ ^online-resources/raw-text/ ]]; then
        continue
    fi

    # Exception 1: Allow README.md (case-sensitive)
    if [[ "$file" =~ /README\.md$ ]]; then
        continue
    fi

    # Exception 2: Allow .json metadata twins (same basename as .txt)
    if [[ "$file" =~ \.json$ ]]; then
        # Extract basename without .json
        json_basename="${file%.json}"
        # Check if corresponding .txt exists
        txt_file="${json_basename}.txt"
        if [[ -f "$txt_file" ]]; then
            continue  # Valid metadata twin
        else
            echo "ERROR: File '$file' is a .json but has no corresponding .txt twin"
            echo "       JSON metadata files MUST have matching .txt file: ${txt_file}"
            EXIT_CODE=1
            continue
        fi
    fi

    # Check if file ends with .txt
    if [[ ! "$file" =~ \.txt$ ]]; then
        echo "ERROR: File '$file' does not end with .txt extension"
        echo "       All files under online-resources/raw-text/ MUST be .txt files"
        echo "       Exceptions: README.md and .json metadata twins"
        EXIT_CODE=1
    fi

    # Check for forbidden extensions (excluding .json which is handled above)
    if [[ "$file" =~ \.(html|htm|js|css|xml|pdf|png|jpg|jpeg|gif|svg|webp)$ ]]; then
        echo "ERROR: File '$file' has forbidden extension"
        echo "       Only .txt files allowed (including .tsv.txt, .dot.txt, .json.txt)"
        EXIT_CODE=1
    fi
done

exit $EXIT_CODE
