#!/usr/bin/env python3
"""Validate chunks.json manifest using Pydantic v2."""

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
    from chunks import ChunksManifest
except ImportError as e:
    print(f"ERROR: Failed to import ChunksManifest model: {e}")
    print("Ensure .claude/models/chunks.py exists")
    sys.exit(1)


def validate_chunks_manifest() -> int:
    """Validate chunks.json against Pydantic schema.

    Returns:
        0 if valid, 1 if invalid
    """
    chunks_file = repo_root / "chunks.json"

    # Check if file exists
    if not chunks_file.exists():
        print(f"ERROR: {chunks_file} does not exist")
        return 1

    # Load JSON
    try:
        with open(chunks_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {chunks_file}")
        print(f"       {e}")
        return 1
    except Exception as e:
        print(f"ERROR: Failed to read {chunks_file}: {e}")
        return 1

    # Validate with Pydantic
    try:
        ChunksManifest(**data)
        print(f"✓ chunks.json is valid")
        return 0
    except ValidationError as e:
        print(f"ERROR: Pydantic validation failed for chunks.json")
        print(f"       {e}")
        return 1


if __name__ == "__main__":
    sys.exit(validate_chunks_manifest())
