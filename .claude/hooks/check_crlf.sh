#!/usr/bin/env bash
# Check for CRLF line endings in raw-text files

set -e

EXIT_CODE=0

for file in "$@"; do
    if [[ ! -f "$file" ]]; then
        continue
    fi

    # Check for CRLF (\r\n)
    if grep -q $'\r' "$file"; then
        echo "ERROR: File '$file' contains CRLF line endings"
        echo "       Raw-text files MUST use LF (\\n) line endings only"
        echo "       Fix with: dos2unix '$file' or sed -i 's/\\r$//' '$file'"
        EXIT_CODE=1
    fi

    # Check for standalone CR (\r)
    if file "$file" | grep -qi "CR line"; then
        echo "ERROR: File '$file' contains CR line endings"
        echo "       Raw-text files MUST use LF (\\n) line endings only"
        EXIT_CODE=1
    fi
done

exit $EXIT_CODE
