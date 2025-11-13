#!/usr/bin/env bash
# Validate filename patterns for raw-text files

set -e

EXIT_CODE=0

for file in "$@"; do
    # Extract just the filename
    filename=$(basename "$file")

    # Skip meta/ directory files
    if [[ "$file" =~ /meta/ ]]; then
        continue
    fi

    # Check for uppercase letters
    if [[ "$filename" =~ [A-Z] ]]; then
        echo "ERROR: File '$file' contains uppercase letters"
        echo "       Filenames MUST be lowercase-slug-with-hyphens"
        EXIT_CODE=1
    fi

    # Check for spaces
    if [[ "$filename" =~ \  ]]; then
        echo "ERROR: File '$file' contains spaces"
        echo "       Filenames MUST use hyphens instead of spaces"
        EXIT_CODE=1
    fi

    # Check for underscores (except in special extensions)
    if [[ "$filename" =~ _ ]] && [[ ! "$filename" =~ \.(tsv|dot|json)\.txt$ ]]; then
        echo "ERROR: File '$file' contains underscores"
        echo "       Filenames MUST use hyphens instead of underscores"
        EXIT_CODE=1
    fi

    # Check for accents/diacritics
    if [[ "$filename" =~ [áàâãäéèêëíìîïóòôõöúùûüçñ] ]]; then
        echo "ERROR: File '$file' contains accented characters"
        echo "       Filenames MUST use only [a-z0-9-] characters"
        EXIT_CODE=1
    fi

    # Check for forbidden characters
    if [[ "$filename" =~ [\!\@\#\$\%\^\&\*\(\)\=\+\[\]\{\}\\\|\;\:\'\"\,\<\>\?\/\`\~] ]]; then
        echo "ERROR: File '$file' contains special characters"
        echo "       Filenames MUST use only [a-z0-9-] characters (plus .txt extension)"
        EXIT_CODE=1
    fi

    # Check pattern for non-meta files: NNN-slug-HHHH.txt
    if [[ ! "$filename" =~ ^[0-9]{3}-[a-z0-9-]+-[a-f0-9]{4}\.(txt|tsv\.txt|dot\.txt|json\.txt)$ ]]; then
        echo "WARNING: File '$file' doesn't match recommended pattern"
        echo "         Expected: NNN-descriptive-slug-HHHH.txt"
        echo "         Where NNN = 3-digit sequence, HHHH = 4-char hash"
        # Don't set EXIT_CODE for warnings, just inform
    fi
done

exit $EXIT_CODE
