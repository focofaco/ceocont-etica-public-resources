# ceocont-etica-public-resources

Text-only content repository for CEO Contabilidade ethics and professional standards materials.

## 📋 Overview

This repository serves as a **server-side contract** for delivering pure text content via CDN. It follows strict format enforcement and semantic versioning with cryptographic integrity guarantees.

### Key Characteristics

- **Text-only content**: UTF-8 encoded `.txt` files with LF line endings
- **Immutable versioning**: Semantic versioning with SHA256 integrity checks
- **Path stability**: File paths are stable within MAJOR versions
- **SSoT architecture**: JSON metadata twins as source of truth

## 📊 Repository Statistics

- **Content Files**: 4 text files (836 words total)
- **Metadata Files**: 4 JSON metadata twins
- **Content Distribution**: 75% plaintext (3), 25% docks (1)
- **Total Size**: 111K
- **Commits**: 52
- **Latest Release**: v1.1.0
- **In Development**: v2.3.0

*Stats auto-updated by README Updater Agent*

## 🗂️ Content Structure

```
online-resources/raw-text/
├── plaintext/          # Flowing text content
├── callouts/           # Highlighted messages
├── docks/              # Editorial side notes
├── tradeoffs/          # Pros/cons lists (+/-)
├── tables/             # *.tsv.txt (tabular data)
├── data/               # *.tsv.txt (for charts)
├── faqs/               # q.txt and a.txt pairs
├── diagrams/           # *.dot.txt (Graphviz)
├── disclaimers/        # Legal/risk warnings
├── others/             # Generic textual content
└── meta/               # Metadata files
    ├── glossario.json.txt
    ├── abbr.json.txt
    ├── integrity.txt
    └── TREE.txt
```

## 🤖 Autonomous Agents (20)

This repository is maintained by 20 autonomous GitHub Actions agents running on schedules:

### Basic Health & Maintenance (3)

- **Daily Health Check Agent** - Validates metadata twin sync, file counts
- **Branch Cleanup Agent** - Removes merged feature branches weekly
- **Morning Standup Agent** - Daily status updates (weekdays)

### Content Quality Agents (5)

- **Spell Checker Agent** - Detects typos in PT-BR content daily
- **Translation Memory Agent** - Builds PT-BR ↔ EN glossary weekly
- **Character Encoding Agent** - Validates UTF-8, detects BOM/control chars
- **Locale Validator Agent** - Checks Brazilian date/currency formats
- **SOC2 Audit Trail Agent** - Immutable compliance logs for all changes

### Advanced Quality Workflows (3)

- **Stale Content Detector** - Identifies content >180 days old monthly
- **Link Checker** - Validates internal file references weekly
- **Changelog Auto Generator** - Suggests version bumps from commits

### Repository Maintenance (4)

- **Commit Message Validator** - Enforces conventional commits
- **Auto-label Issues Agent** - Labels issues by keywords
- **PR Size Labeler** - Labels PRs as XS/S/M/L/XL
- **Changelog Formatter** - Validates Keep a Changelog format

### Growth & Documentation (2)

- **Content Growth Tracker** - Tracks file counts, size weekly
- **README Updater** - Auto-updates statistics in this file

### Dependency Management (4)

- **Unused Dependency Cleaner** - Detects unused Python packages monthly
- **Outdated Dependency Reporter** - Reports outdated deps & security issues weekly
- **Dependency Graph Generator** - Creates visual dep graphs monthly
- **Breaking Change Detector** - Alerts on major version bumps in PRs

## 🔄 Workflows & CI/CD

### Pre-commit Hooks (26 checks)

- Format validation (UTF-8, LF, no BOM)
- Security checks (no private keys, no binaries)
- Structural validation (paths, metadata twins)
- Code quality (YAML, JSON syntax)

### Dependabot

- **Daily** dependency updates at 09:00 BRT (Python) and 10:00 BRT (GitHub Actions)
- Grouped updates to reduce PR noise
- Automated security updates

### CodeQL Security Scanning

- Runs on all branches
- Python security analysis
- Automated vulnerability detection

## 📦 Versioning

Follows **Semantic Versioning** (MAJOR.MINOR.PATCH):

- **MAJOR**: Breaking changes (path renames, category changes)
- **MINOR**: New content, compatible enhancements
- **PATCH**: Bug fixes, typo corrections

### Recent Versions

- **v2.1.0** (2025-11-13): GitHub automation infrastructure (20 agents)
- **v1.2.0** (2025-11-13): Content quality workflows (v2.2.0)
- **v1.1.0** (2025-11-12): Enhanced validation and ingestion metadata
- **v1.0.0** (2025-11-11): Initial stable release

See [CHANGELOG.txt](CHANGELOG.txt) for full version history.

## 🛠️ Development

### Branch Naming Convention

Feature branches must follow: `claude/*-SESSION_ID`

Example: `claude/dev004-v1.2.0-release-011CV4kf1V2XbPxRYPEA6QKV`

### Commit Message Format

Follows **Conventional Commits**:

```
<type>(<scope>): <description>

[optional body]
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`, `ci`, `build`

### Creating Content

1. Determine content category (plaintext, callouts, etc.)
2. Create `.txt` file with lowercase-slug-with-hyphens naming
3. Ensure UTF-8 encoding with LF line endings
4. Commit with conventional commit message
5. Open PR for review

## 📜 Contracts & Specifications

- **server-contract.md** - Normative contract for content delivery
- **server-contract.spec** - Formal specification with validation rules
- **contract.schema** - Latin schema with examples
- **CLAUDE.md** - AI agent operational rules

## 🔒 Security

- All file changes logged in SOC2 audit trail
- Pre-commit security checks (no private keys, no binaries)
- Daily CodeQL security scanning
- Dependabot security updates

## 📄 License

[License information to be added]

## 🤝 Contributing

[Contribution guidelines to be added]

---

**Maintained by**: CEO Contabilidade
**Last Updated**: 2025-11-13
**Repository**: [ceocont-etica-public-resources](https://github.com/focofacofoco/ceocont-etica-public-resources)
