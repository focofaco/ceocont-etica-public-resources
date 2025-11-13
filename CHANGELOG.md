# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 🤖 AI Agent Ownership & Review Process

This repository is fully managed and owned by Claude AI (Sonnet 4.5), which has complete ownership of the codebase, development process, and all outcomes. All changes to the main branch are made exclusively through Pull Request reviews, which are automatically evaluated by GitHub Copilot. Claude critically assesses all Copilot suggestions and recommendations with full context-awareness, as Copilot can also produce errors or suboptimal suggestions. Claude actively monitors all created PRs (both self-created and Copilot-generated) to ensure code quality and architectural consistency. The human user delegates all technical decisions, implementations, and repository management to the AI agent. **Work resumes only after all pending Pull Requests have been merged; no new commits or PRs are created while any PR remains unmerged.**

## [Unreleased]

## [2.0.0] - 2025-11-13

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

## [1.1.0] - 2025-11-13

### Added

- Pre-commit hooks configuration (.pre-commit-config.yaml)
- Standard hooks from pre-commit v4.4.0 and v6.0.0
- Custom validation hook: validate_raw_text_only.sh
- Custom validation hook: validate_audit_json.py (JSON schema validation)
- Custom validation hook: forbid_html_js_css.sh
- Custom validation hook: check_crlf.sh
- Custom validation hook: validate_filename_pattern.sh
- First content fragment: 001-politica-controle-qualidade-contabil-41f5.txt
- Ingestion audit trail system (.claude/ingestion-audit.json)
- Ingestion audit schema (.claude/ingestion-audit-schema.json)

### Removed

- shadow-original/ folder (replaced by JSON audit trail)
- shadow-fragments-original/ folder (replaced by JSON audit trail)
- shadow-fragments-transformed/ folder (replaced by JSON audit trail)

### Changed

- Updated brandguide bundle integration
- Fixed trailing whitespace in contract files
- Fixed end-of-file newlines in schema files

## [1.0.0] - 2025-11-12

### Added

- Initial directory structure for online-resources/raw-text/
- Content categories: plaintext/, callouts/, docks/, tradeoffs/, tables/, data/, faqs/, diagrams/, disclaimers/, others/
- Metadata directory: meta/
- Metadata files: glossario.json.txt, abbr.json.txt, integrity.txt, TREE.txt
- Root files: DEPRECATIONS.txt, CHANGELOG.txt
- Initial server contract specification files
- Contract schema definition (contract.schema)
- Server contract documentation (server-contract.md)
- Server contract specification (server-contract.spec)
- Server brandguide documentation (server-brandguide.md)
- Server brandguide specification (server-brandguide.spec)
- Server brandguide schema (server-brandguide-schema.json)
- Conventional Commits template for AI agents
- Keep a Changelog template for AI agents

[Unreleased]: https://github.com/focofacofoco/ceocont-etica-public-resources/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/focofacofoco/ceocont-etica-public-resources/compare/v1.1.0...v2.0.0
[1.1.0]: https://github.com/focofacofoco/ceocont-etica-public-resources/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/focofacofoco/ceocont-etica-public-resources/releases/tag/v1.0.0
