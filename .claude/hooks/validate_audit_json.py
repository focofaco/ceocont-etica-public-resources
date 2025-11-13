#!/usr/bin/env python3
"""Validate ingestion-audit.json against schema."""

import json
import sys
from pathlib import Path

try:
    import jsonschema
    from jsonschema import validate, ValidationError
except ImportError:
    print("ERROR: jsonschema library not installed")
    print("Install with: pip install jsonschema>=4.20.0")
    sys.exit(1)


def validate_audit_json():
    """Validate ingestion-audit.json against ingestion-audit-schema.json."""
    repo_root = Path(__file__).parent.parent.parent
    audit_file = repo_root / ".claude" / "ingestion-audit.json"
    schema_file = repo_root / ".claude" / "ingestion-audit-schema.json"

    # Check if files exist
    if not audit_file.exists():
        print(f"ERROR: {audit_file} does not exist")
        return 1

    if not schema_file.exists():
        print(f"ERROR: {schema_file} does not exist")
        return 1

    # Load files
    try:
        with open(audit_file, 'r', encoding='utf-8') as f:
            audit_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {audit_file}")
        print(f"       {e}")
        return 1

    try:
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {schema_file}")
        print(f"       {e}")
        return 1

    # Validate
    try:
        validate(instance=audit_data, schema=schema_data)
        print(f"✓ {audit_file.name} is valid against schema")
        return 0
    except ValidationError as e:
        print(f"ERROR: Schema validation failed for {audit_file}")
        print(f"       {e.message}")
        if e.path:
            print(f"       Path: {' -> '.join(str(p) for p in e.path)}")
        return 1


if __name__ == "__main__":
    sys.exit(validate_audit_json())
