# Release Notes: v2.0.0

## Status: Ready for Merge

All code and validation complete. Release branches ready for PR creation.

## Breaking Changes (MAJOR version bump)

**v1.1.0 → v2.0.0**: New component categories added to content hierarchy

### What Changed

- Added three new component directories: `header_h1/`, `header_h2/`, `header_h3/`
- Headers are **structural elements** and do NOT count towards 70-80% plaintext baseline
- Component enum expanded in all Pydantic schemas
- ComponentDistribution models extended with header fields

### Migration Impact

- Client code must handle new component types
- Distribution calculations exclude headers from baseline metrics
- Schema validation updated across all validators

## Release Contents

### BREAKING CHANGES

- Added new component categories: header_h1/, header_h2/, header_h3/
- Headers are structural elements and do NOT count towards 70-80% plaintext baseline
- Component enum in all schemas updated to include new header types
- ComponentDistribution and ComponentDistributionPercentage models extended

### Added

- header_h1/ directory with README.md (H1-level headers)
- header_h2/ directory with README.md (H2-level headers)
- header_h3/ directory with README.md (H3-level headers)
- Pydantic v2 validation framework (pydantic>=2.9.0, pydantic-settings>=2.5.0)
- Pydantic v2 models: .claude/models/metadata_twin.py
- Pydantic v2 models: .claude/models/chunks.py
- Pydantic v2 models: .claude/models/ingestion_audit.py
- Pydantic validator: .claude/hooks/validate_metadata_twin_pydantic.py
- Pydantic validator: .claude/hooks/validate_chunks_pydantic.py
- requirements.txt for Python dependencies
- .gitignore for Python artifacts
- Root-level chunks.json manifest
- Metadata twin validation hook (validate_metadata_twins.sh)
- Distribution note in chunks.json about header exclusion from baseline

### Changed

- Updated all Pydantic models to include header_h1, header_h2, header_h3 components
- Migrated validate_audit_json.py from jsonschema to Pydantic v2
- Updated server-contract.md §3 with new header component categories
- Updated .pre-commit-config.yaml to use Pydantic validators
- Updated validate_raw_text_only.sh to allow README.md and .json metadata twins
- chunks.json component_distribution extended with header fields

### Validation Status

✓ All pre-commit hooks passing
✓ Pydantic v2 validation passing
✓ Metadata twin validation passing
✓ chunks.json validation passing
✓ Component README files created
✓ Contract documentation updated

## Commits Included

```
9cd7dbb - feat(components)!: add header_h1, header_h2, header_h3 component categories
2101590 - feat(validation): integrate Pydantic v2 for JSON validation
cb6589b - feat(manifest): add chunks.json root-level manifest
5e81fe4 - feat(metadata): update JSON metadata twin to SSoT schema
b17562d - feat(validation): add metadata twin validation and README support
```

## Available Branch for Merge

**claude/dev003-content-ingestion-011CV4kf1V2XbPxRYPEA6QKV**

- Development branch with all v2.0.0 changes
- Latest commit: 9cd7dbb
- PR URL: <https://github.com/focofacofoco/ceocont-etica-public-resources/pull/new/claude/dev003-content-ingestion-011CV4kf1V2XbPxRYPEA6QKV>

## Local Tags (Documentation)

Git tags created locally for version tracking:

- `v1.0.0` - Initial release
- `v1.1.0` - Pre-commit hooks release
- `v2.0.0` - Header components release (cannot push due to 403)

**Note**: Tags cannot be pushed due to proxy restrictions. Create official release tag via GitHub UI after merge.

## Next Steps for Official Release

1. **Create Pull Request** from `claude/dev003-content-ingestion-011CV4kf1V2XbPxRYPEA6QKV` to `main`
2. **Review PR** - Verify breaking changes documented
3. **Merge to main** via GitHub Pull Request UI
4. **Create GitHub Release** from `main` branch
   - Release title: `v2.0.0 - Header Components`
   - Tag: `v2.0.0`
   - Description: Copy from BREAKING CHANGES section above
5. GitHub will automatically create the `v2.0.0` tag on release

## Architecture Notes

### Header Components

Headers represent **document structure** (H1/H2/H3 hierarchy) separate from content distribution:

- **Not counted** in 70-80% plaintext baseline
- **Not counted** in 20-30% others baseline
- Tracked separately for structural organization
- Short text content (typically one line per header)

### SSoT Architecture

- **JSON metadata twins** = Single Source of Truth (full content + metadata)
- **TXT files** = Derived content (CDN delivery, text only)
- JSON files don't go to CDN, no size limits

### Validation Stack

- **Pydantic v2** for all JSON schema validation
- **Pre-commit hooks** enforce all rules before commit
- **Metadata twin pairing** enforced bidirectionally

---

**Release prepared by**: Claude Code Agent
**Session ID**: 011CV4kf1V2XbPxRYPEA6QKV
**Date**: 2025-11-13
