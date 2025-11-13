#!/usr/bin/env python3
"""Validate metadata twin JSON files using Pydantic v2."""

import json
import sys
from pathlib import Path

try:
    from pydantic import ValidationError
except ImportError:
    print("ERROR: pydantic library not installed")
    print("Install with: pip install pydantic>=2.9.0")
    sys.exit(1)

# Add .claude/models to path
repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root / ".claude" / "models"))

try:
    from metadata_twin import MetadataTwin
except ImportError as e:
    print(f"ERROR: Failed to import MetadataTwin model: {e}")
    print("Ensure .claude/models/metadata_twin.py exists")
    sys.exit(1)


def validate_metadata_twin(file_path: str) -> int:
    """Validate a metadata twin JSON file against Pydantic schema.

    Args:
        file_path: Path to the JSON file to validate

    Returns:
        0 if valid, 1 if invalid
    """
    json_file = Path(file_path)

    # Skip if not a JSON file in raw-text/
    if not json_file.name.endswith('.json'):
        return 0

    if 'raw-text' not in str(json_file):
        return 0

    # Skip meta/ directory JSON files (glossario.json.txt, abbr.json.txt)
    if 'meta/' in str(json_file):
        return 0

    # Load JSON
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {json_file}")
        print(f"       {e}")
        return 1
    except Exception as e:
        print(f"ERROR: Failed to read {json_file}: {e}")
        return 1

    # Validate with Pydantic
    try:
        MetadataTwin(**data)
        print(f"✓ {json_file.name} is valid metadata twin")
        return 0
    except ValidationError as e:
        print(f"ERROR: Pydantic validation failed for {json_file}")
        print(f"       {e}")
        return 1


def main():
    """Main entry point for pre-commit hook."""
    if len(sys.argv) < 2:
        print("ERROR: No files provided for validation")
        return 1

    exit_code = 0
    for file_path in sys.argv[1:]:
        result = validate_metadata_twin(file_path)
        if result != 0:
            exit_code = result

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
