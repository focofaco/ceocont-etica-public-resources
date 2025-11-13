#!/usr/bin/env python3
"""Validate ingestion-audit.json using Pydantic v2."""

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
    from ingestion_audit import IngestionAudit
except ImportError as e:
    print(f"ERROR: Failed to import IngestionAudit model: {e}")
    print("Ensure .claude/models/ingestion_audit.py exists")
    sys.exit(1)


def validate_audit_json():
    """Validate ingestion-audit.json using Pydantic schema."""
    audit_file = repo_root / ".claude" / "ingestion-audit.json"

    # Check if file exists
    if not audit_file.exists():
        print(f"ERROR: {audit_file} does not exist")
        return 1

    # Load JSON
    try:
        with open(audit_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {audit_file}")
        print(f"       {e}")
        return 1
    except Exception as e:
        print(f"ERROR: Failed to read {audit_file}: {e}")
        return 1

    # Validate with Pydantic
    try:
        IngestionAudit(**data)
        print(f"✓ {audit_file.name} is valid")
        return 0
    except ValidationError as e:
        print(f"ERROR: Pydantic validation failed for {audit_file.name}")
        print(f"       {e}")
        return 1


if __name__ == "__main__":
    sys.exit(validate_audit_json())
