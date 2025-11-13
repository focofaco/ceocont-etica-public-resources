#!/usr/bin/env bash
# Forbid HTML/JS/CSS content in raw-text files

set -e

EXIT_CODE=0

# Forbidden patterns
HTML_PATTERNS=(
    '<html'
    '<head>'
    '<body>'
    '<div'
    '<span'
    '<script'
    '<style'
    'document\.getElementById'
    'addEventListener'
    'querySelector'
)

CSS_PATTERNS=(
    'background-color:'
    'font-size:'
    'margin:'
    'padding:'
    '.className {'
    '#idName {'
)

for file in "$@"; do
    if [[ ! -f "$file" ]]; then
        continue
    fi

    # Check for HTML patterns
    for pattern in "${HTML_PATTERNS[@]}"; do
        if grep -qi "$pattern" "$file"; then
            echo "ERROR: File '$file' contains forbidden HTML pattern: $pattern"
            echo "       Raw-text files MUST NOT contain HTML tags"
            EXIT_CODE=1
        fi
    done

    # Check for CSS patterns
    for pattern in "${CSS_PATTERNS[@]}"; do
        if grep -qi "$pattern" "$file"; then
            echo "ERROR: File '$file' contains forbidden CSS pattern: $pattern"
            echo "       Raw-text files MUST NOT contain CSS styles"
            EXIT_CODE=1
        fi
    done
done

exit $EXIT_CODE
