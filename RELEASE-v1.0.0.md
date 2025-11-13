# Release Notes: v1.0.0

## 🤖 AI Agent Ownership & Review Process

This repository is fully managed and owned by Claude AI (Sonnet 4.5), which has complete ownership of the codebase,
development process, and all outcomes. All changes to the main branch are made exclusively through Pull Request reviews,
which are automatically evaluated by GitHub Copilot. Claude critically assesses all Copilot suggestions and
recommendations with full context-awareness, as Copilot can also produce errors or suboptimal suggestions. Claude
actively monitors all created PRs (both self-created and Copilot-generated) to ensure code quality and architectural
consistency. The human user delegates all technical decisions, implementations, and repository management to the AI
agent. **Work resumes only after all pending Pull Requests have been merged; no new commits or PRs are created while any
PR remains unmerged.**

## Status: Initial Release

First public release of the text-only content repository.

## Release Type: MAJOR (Initial)

**v0.0.0 → v1.0.0**: Initial repository structure and contracts established

## Release Contents

### Added

- Initial directory structure for online-resources/raw-text/
- Content categories:
  - plaintext/ - Flowing text for content boxes
  - callouts/ - Highlighted messages
  - docks/ - Editorial side notes
  - tradeoffs/ - Pros/cons lists (+/-)
  - tables/ - TSV data tables (\*.tsv.txt)
  - data/ - TSV data for charts (\*.tsv.txt)
  - faqs/ - Q&A pairs (q.txt + a.txt)
  - diagrams/ - Graphviz DOT files (\*.dot.txt)
  - disclaimers/ - Legal/risk warnings
  - others/ - Generic textual content
- Metadata directory: meta/
  - glossario.json.txt - Glossary of technical terms
  - abbr.json.txt - Abbreviations dictionary
  - integrity.txt - SHA256 checksums for all files
  - TREE.txt - Directory tree structure
- Root documentation files:
  - server-contract.md - Server-side content contract
  - server-contract.spec - Formal specification
  - contract.schema - Schema definitions
  - brandguide.md - Content style guide
  - brandguide-bundle.md - Bundled brandguide reference
  - DEPRECATIONS.txt - Path deprecation tracking
  - CHANGELOG.txt - Version history log
  - README.md - Repository overview

### Core Contracts Established

- **Text-Only Policy**: Only .txt files allowed under raw-text/
- **UTF-8 + LF**: No BOM, no CRLF line endings
- **Path Stability**: Paths are stable identifiers within MAJOR version
- **Semantic Versioning**: MAJOR.MINOR.PATCH version scheme
- **Integrity Tracking**: SHA256 checksums for all content
- **Component Distribution**: 70-80% plaintext baseline enforcement

### File Format Rules

- `.txt` - Standard text files
- `.tsv.txt` - Tab-separated values (tables/data)
- `.dot.txt` - Graphviz diagrams
- `.json.txt` - JSON metadata dictionaries

### Validation Rules

- Lowercase-slug-with-hyphens naming convention
- No HTML/JS/CSS/binaries allowed
- No spaces, accents, or special characters in filenames
- TSV files must have header row with consistent column counts
- DOT files must define valid graphs

## Architecture Decisions

### Text-Only Repository

- **Server-side contract** governing pure text delivery
- **CDN-ready** content with immutable versioning
- **Client-agnostic** - no UI/rendering logic
- **Format enforcement** via CI validation gates

### Version Strategy

- **MAJOR**: Breaking changes (path moves, category additions, semantic changes)
- **MINOR**: Compatible additions (new content, new files)
- **PATCH**: Bug fixes (typos, corrections without semantic changes)

### Component Categories

11 content categories established:

- 10 content types (plaintext through others)
- 1 metadata directory (meta/)

## Validation Status

✓ Directory structure created ✓ Contract files established ✓ Brandguide documentation complete ✓ Metadata infrastructure
ready ✓ No content files yet (empty categories)

## Commits Included

```
[Initial commit hash] - feat: establish v1.0.0 repository structure
- Create raw-text/ directory hierarchy
- Add server-contract.md and specifications
- Add brandguide documentation
- Create empty component category directories
- Initialize CHANGELOG.txt and DEPRECATIONS.txt
```

## Migration Notes

**From**: N/A (initial release) **To**: v1.0.0

No migration needed - this is the first release.

## Repository URL

```
https://github.com/focofacofoco/ceocont-etica-public-resources
```

## Tag Information

**Tag**: `v1.0.0` **Target**: `main` branch **Date**: 2025-11-12

## Next Release

See RELEASE-v1.1.0.md for pre-commit hooks and first content ingestion.

______________________________________________________________________

**Release prepared by**: Manual setup **Date**: 2025-11-12 **Note**: This release documentation created retroactively on
2025-11-13
