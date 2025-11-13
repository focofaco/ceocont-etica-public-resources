# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `online-resources/raw-text/plaintext/002-introducao-manual-controle-qualidade-a1b8.txt` - Manual quality control introduction (190 words)
- `online-resources/raw-text/docks/003-estudo-caso-irregularidade-cliente-4800.txt` - Case study: irregularity identified in client (121 words) - **First dock component**
- `online-resources/raw-text/plaintext/004-sistema-controle-qualidade-documentacao-7eff.txt` - Quality control system documentation (360 words)

### Features

- Content ingestion: chunk_02 with 3 fragments (2 plaintext + 1 docks)
- Component distribution balanced: 75% plaintext / 25% docks (within 70-80% target)
- Total content: 4 fragments across 2 chunks, 836 words
- First dock component added to repository

### Notes

- 9 placeholders tracked: `${razao-social}`, `${tipo-servico}`, `${tipo-irregularidade}`, `${responsavel-tecnico}`, `${objetivo-correcao}`, `${responsavel-qualidade}`, `${diagrama-piramide}`
- All fragments approved with 0.95 brandguide compliance score
- Metadata twins validated via pre-commit hooks

## [2.3.0] - 2025-11-13

### Added

- `.github/workflows/commit-validator-agent.yml` for enforcing conventional commits
- `.github/workflows/auto-label-agent.yml` for auto-labeling issues by keywords
- `.github/workflows/pr-size-labeler-agent.yml` for labeling PRs by size (XS/S/M/L/XL)
- `.github/workflows/growth-tracker-agent.yml` for tracking repository growth metrics
- `.github/workflows/readme-updater-agent.yml` for auto-updating README.md statistics
- `.github/workflows/changelog-formatter-agent.yml` for validating CHANGELOG.txt format
- `.github/workflows/unused-deps-agent.yml` for detecting unused Python dependencies
- `.github/workflows/outdated-deps-agent.yml` for reporting outdated packages & security issues
- `.github/workflows/dep-graph-agent.yml` for generating visual dependency graphs
- `.github/workflows/breaking-change-agent.yml` for detecting breaking changes in dep updates

### Features

- Quality & Validation Agents (4): commit format, changelog format, PR size, auto-labels
- Maintenance & Tracking Agents (2): growth tracking, README auto-updates
- Dependency Management Agents (4): unused/outdated detection, graphs, breaking changes
- All agents run autonomously via cron schedules + workflow_dispatch for manual testing
- Comprehensive reporting with GitHub issues, PR comments, and workflow summaries
- Least-privilege permission model for security

### Notes

- Total workflow count: 20 autonomous agents (3 basic + 5 specialized + 2 advanced + 10 new)
- All 10 workflows are YAML-validated and production-ready
- Agents generate actionable reports with task checklists
- Breaking change detector labels PRs and fails on major version bumps
- Growth tracker commits weekly metrics to `.github/metrics/growth.csv`

## [2.2.0] - 2025-11-13

### Added

- `.github/workflows/stale-content-detector.yml` for identifying outdated content
- `.github/workflows/link-checker.yml` for validating internal file references
- `.github/workflows/changelog-auto.yml` for generating changelog from commits

### Changed

- Pre-commit CI: Auto-fix ENABLED (commits fixes to PRs automatically)
- Dependabot: Weekly → Daily updates (09:00/10:00 BRT)

### Features

- Stale Content Detector: Monthly cron to find files >180 days old
- Link Checker: Validates .txt references, metadata twins, and chunks.json
- Changelog Auto: Parses conventional commits and suggests version bumps

### Notes

- All 3 workflows are YAML-validated and production-ready
- Stale detector creates/updates GitHub issues automatically
- Link checker fails pipeline if broken links detected
- Changelog generator produces Keep a Changelog format

## [2.1.0] - 2025-11-13

### Added

- `.github/pull_request_template.md` with comprehensive validation checklist
- `.github/dependabot.yml` for automated dependency updates (Python + GitHub Actions)
- `.github/CODEOWNERS` for automatic review assignments
- `.github/workflows/pre-commit-ci.yml` for CI-based linting and auto-fix
- `.github/workflows/validate-content.yml` for specialized .txt file validation
- `.github/workflows/dependency-review.yml` for security scanning of dependencies
- `.github/workflows/release.yml` for semi-automated release process
- `.github/SECURITY.md` with vulnerability reporting policy

### Changed

- Enhanced GitHub infrastructure with 8 new automation files
- Improved developer experience with standardized PR templates
- Strengthened security posture with multiple scanning workflows

### Notes

- All workflows are YAML-validated and follow GitHub Actions best practices
- Dependabot configured for weekly updates with grouped PRs to reduce noise
- Release workflow requires manual trigger (workflow_dispatch) for safety
- Security policy establishes responsible disclosure process

## [1.2.0] - 2025-11-13

### Added

- `header_h1/` directory with README.md (H1-level headers)
- `header_h2/` directory with README.md (H2-level headers)
- `header_h3/` directory with README.md (H3-level headers)
- Pydantic v2 validation framework (pydantic>=2.9.0, pydantic-settings>=2.5.0)
- Pydantic v2 models: `.claude/models/metadata_twin.py`
- Pydantic v2 models: `.claude/models/chunks.py`
- Pydantic v2 models: `.claude/models/ingestion_audit.py`
- Pydantic validator: `.claude/hooks/validate_metadata_twin_pydantic.py`
- Pydantic validator: `.claude/hooks/validate_chunks_pydantic.py`
- `requirements.txt` for Python dependencies
- `.gitignore` for Python artifacts
- Root-level `chunks.json` manifest
- Metadata twin validation hook (`validate_metadata_twins.sh`)
- Distribution note in chunks.json about header exclusion from baseline
- Component-specific README files for all 11 categories plus headers

### Changed

- Updated all Pydantic models to include header_h1, header_h2, header_h3 components
- Migrated `validate_audit_json.py` from jsonschema to Pydantic v2
- Updated `server-contract.md` §3 with new header component categories
- Updated `.pre-commit-config.yaml` to use Pydantic validators
- Updated `validate_raw_text_only.sh` to allow README.md and .json metadata twins
- `chunks.json` component_distribution extended with header fields

### Notes

- Headers (header_h1, header_h2, header_h3) are structural elements
- Headers do NOT count towards 70-80% plaintext and 20-30% others baseline
- This is backward compatible - existing clients continue to work
- New components are additive only, no breaking changes

## [1.1.0] - 2025-11-13

### Added

- Pre-commit hooks configuration (`.pre-commit-config.yaml`)
- Standard hooks from pre-commit v4.4.0 and v6.0.0
- Custom validation hook: `validate_raw_text_only.sh`
- Custom validation hook: `validate_audit_json.py` (JSON schema validation)
- Custom validation hook: `forbid_html_js_css.sh`
- Custom validation hook: `check_crlf.sh`
- Custom validation hook: `validate_filename_pattern.sh`
- First content fragment: `001-politica-controle-qualidade-contabil-41f5.txt`
- Ingestion audit trail system (`.claude/ingestion-audit.json`)
- Ingestion audit schema (`.claude/ingestion-audit-schema.json`)

### Removed

- `shadow-original/` folder (replaced by JSON audit trail)
- `shadow-fragments-original/` folder (replaced by JSON audit trail)
- `shadow-fragments-transformed/` folder (replaced by JSON audit trail)

### Changed

- Updated brandguide bundle integration
- Fixed trailing whitespace in contract files
- Fixed end-of-file newlines in schema files

## [1.0.0] - 2025-11-12

### Added

- Initial directory structure for `online-resources/raw-text/`
- Content categories: `plaintext/`, `callouts/`, `docks/`, `tradeoffs/`, `tables/`, `data/`, `faqs/`, `diagrams/`, `disclaimers/`, `others/`
- Metadata directory: `meta/`
- Metadata files: `glossario.json.txt`, `abbr.json.txt`, `integrity.txt`, `TREE.txt`
- Root files: `DEPRECATIONS.txt`, `CHANGELOG.txt`
- Initial server contract specification files
- Contract schema definition (`contract.schema`)
- Server contract documentation (`server-contract.md`)
- Server contract specification (`server-contract.spec`)
- Conventional Commits template for AI agents
- Keep a Changelog template for AI agents

[Unreleased]: https://github.com/focofacofoco/ceocont-etica-public-resources/compare/v2.3.0...HEAD
[2.3.0]: https://github.com/focofacofoco/ceocont-etica-public-resources/compare/v2.2.0...v2.3.0
[2.2.0]: https://github.com/focofacofoco/ceocont-etica-public-resources/compare/v2.1.0...v2.2.0
[2.1.0]: https://github.com/focofacofoco/ceocont-etica-public-resources/compare/v1.2.0...v2.1.0
[1.2.0]: https://github.com/focofacofoco/ceocont-etica-public-resources/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/focofacofoco/ceocont-etica-public-resources/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/focofacofoco/ceocont-etica-public-resources/releases/tag/v1.0.0
