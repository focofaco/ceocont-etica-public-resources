# GitHub Actions Workflows

## 🤖 AI Agent Ownership & Review Process

This repository is fully managed and owned by Claude AI (Sonnet 4.5), which has complete ownership of the codebase,
development process, and all outcomes. All changes to the main branch are made exclusively through Pull Request reviews,
which are automatically evaluated by GitHub Copilot. Claude critically assesses all Copilot suggestions and
recommendations with full context-awareness, as Copilot can also produce errors or suboptimal suggestions. Claude
actively monitors all created PRs (both self-created and Copilot-generated) to ensure code quality and architectural
consistency. The human user delegates all technical decisions, implementations, and repository management to the AI
agent.

______________________________________________________________________

## Workflows Overview

### 1. Pre-commit Hooks (`pre-commit.yml`)

**Triggers**: Pull requests to main, pushes to main and claude/\* branches

**Purpose**: Runs all pre-commit hooks (50+ checks) including:

- File format validation (UTF-8, LF, no BOM)
- Markdown linting (markdownlint-cli2, mdformat)
- JSON/YAML formatting (prettier)
- Python code quality (ruff, bandit, tryceratops, vulture, xenon)
- Conventional commit validation (commitizen)
- Custom validation hooks

**Why**: Ensures code quality and consistency before merging

______________________________________________________________________

### 2. Content Validation (`content-validation.yml`)

**Triggers**: Pull requests and pushes affecting `online-resources/raw-text/**`

**Purpose**: Validates text content integrity:

- File extensions (.txt only)
- Forbidden content (no HTML/JS/CSS)
- Line endings (LF only)
- Filename patterns
- Metadata twins (every .txt has .json)
- Pydantic schema validation

**Why**: Enforces server-side contract for text-only content

______________________________________________________________________

### 3. Continuous Integration (`ci.yml`)

**Triggers**: All pull requests and pushes to main

**Purpose**: Repository-wide integrity checks:

- Directory structure validation
- Required files presence
- UTF-8 encoding verification
- BOM detection
- Overall repository health

**Why**: Ensures repository structure remains intact

______________________________________________________________________

### 4. Copilot Review (`copilot-review.yml`)

**Triggers**: Pull requests opened/synchronized/reopened

**Purpose**: Automated code review assistant:

- Analyzes changed files by type
- Detects critical file modifications
- Validates conventional commit messages
- Posts automated review comment
- Provides guidance for Claude AI review

**Why**: Assists Claude AI in evaluating PRs systematically

______________________________________________________________________

### 5. Release Automation (`release.yml`)

**Triggers**: Git tags matching `v*.*.*` pattern

**Purpose**: Automated release creation:

- Extracts version from tag
- Locates release notes (RELEASE-vX.Y.Z.md or CHANGELOG.md)
- Adds AI ownership notice
- Creates GitHub Release
- Generates release notes

**Why**: Streamlines version release process

______________________________________________________________________

### 6. Integrity Verification (`integrity.yml`)

**Triggers**: Changes to `online-resources/raw-text/**`, manual dispatch

**Purpose**: SHA256 checksum validation:

- Verifies all checksums in meta/integrity.txt
- Lists new files without checksums
- Generates current checksums for PRs
- Warns on mismatches (non-fatal for PRs)

**Why**: Ensures cryptographic integrity of content

______________________________________________________________________

### 7. Documentation Quality (`documentation.yml`)

**Triggers**: Changes to .md files or contract/brandguide files

**Purpose**: Documentation validation:

- Checks required documentation files exist
- Verifies AI ownership declaration presence
- Validates CHANGELOG format (Keep a Changelog)
- Detects broken internal links
- Checks version consistency

**Why**: Maintains documentation quality and completeness

______________________________________________________________________

### 8. CodeQL Security Analysis (`codeql.yml`)

**Triggers**: PRs to main, pushes to main/claude/\*, scheduled weekly, manual dispatch

**Purpose**: Advanced security code scanning:

- Multi-language analysis (Python, JavaScript)
- Security vulnerability detection
- Code quality analysis
- SAST (Static Application Security Testing)
- Results uploaded to GitHub Security tab

**Why**: Proactive security monitoring (non-blocking, informational)

**Note**: ⚠️ Results are **informational only** and do not block PR merges

______________________________________________________________________

### 9. Dependency Review (`dependency-review.yml`)

**Triggers**: Pull requests to main

**Purpose**: Dependency vulnerability scanning:

- Scans all dependency changes in PRs
- Detects known vulnerabilities (CVEs)
- License compliance checking (denies GPL-3.0, AGPL-3.0)
- Posts summary comments in PRs
- Severity-based alerting

**Why**: Early detection of vulnerable dependencies (non-blocking, informational)

**Note**: ⚠️ Reports vulnerabilities but does not block PR merges

______________________________________________________________________

### 10. Dependabot (Configuration)

**Configuration**: `.github/dependabot.yml`

**Purpose**: Automated dependency updates:

- Weekly dependency updates (Mondays)
- Python packages (requirements.txt)
- GitHub Actions versions
- Automated PR creation with version bumps
- Grouped updates by ecosystem

**Why**: Keeps dependencies up-to-date and secure

**Note**: Creates PRs automatically, reviewed by Claude AI before merge

______________________________________________________________________

## Workflow Dependencies

```mermaid
graph TD
    A[Push/PR] --> B[Pre-commit]
    A --> C[CI]
    A --> D[Documentation]
    A --> M[CodeQL Scan]

    E[PR to main] --> F[Copilot Review]
    E --> G[Content Validation]
    E --> H[Integrity Check]
    E --> N[Dependency Review]

    I[Tag Push] --> J[Release Automation]

    O[Schedule/Weekly] --> M
    O --> P[Dependabot Updates]

    B -.->|must pass| K[Merge]
    C -.->|must pass| K
    G -.->|must pass| K
    H -.->|warn only| K
    M -.->|informational| K
    N -.->|informational| K

    K --> L[Main Branch]
    L --> J

    P -.->|creates PRs| E
```

## Status Badges

Add these to your README.md:

```markdown
![Pre-commit](https://github.com/focofaco/ceocont-etica-public-resources/actions/workflows/pre-commit.yml/badge.svg)
![CI](https://github.com/focofaco/ceocont-etica-public-resources/actions/workflows/ci.yml/badge.svg)
![Content Validation](https://github.com/focofaco/ceocont-etica-public-resources/actions/workflows/content-validation.yml/badge.svg)
![Documentation](https://github.com/focofaco/ceocont-etica-public-resources/actions/workflows/documentation.yml/badge.svg)
![CodeQL](https://github.com/focofaco/ceocont-etica-public-resources/actions/workflows/codeql.yml/badge.svg)
![Dependency Review](https://github.com/focofaco/ceocont-etica-public-resources/actions/workflows/dependency-review.yml/badge.svg)
```

## Required Secrets

None currently required. All workflows use `GITHUB_TOKEN` which is automatically provided by GitHub Actions.

## Permissions

Workflows require these permissions (already configured):

- `contents: read` - Read repository content (all workflows)
- `contents: write` - Create releases (release.yml only)
- `pull-requests: write` - Post PR comments (copilot-review.yml, dependency-review.yml)
- `security-events: write` - Upload security results (codeql.yml only)
- `actions: read` - Read workflow status (codeql.yml only)

## Local Testing

Test workflows locally before pushing:

```bash
# Install act (GitHub Actions local runner)
# https://github.com/nektos/act

# Run specific workflow
act pull_request -W .github/workflows/pre-commit.yml

# Run all workflows
act
```

## Maintenance

- **Weekly**: Review workflow runs for failures and security scan results
- **Weekly**: Check Security tab for CodeQL alerts (non-blocking but important)
- **Weekly**: Review Dependabot PRs for dependency updates
- **Monthly**: Update action versions (@v4, @v5, etc.)
- **Per Release**: Ensure release.yml creates proper releases
- **As Needed**: Adjust validation rules in workflows

## Security Scanning

All security workflows are **non-blocking** (informational only):

- **CodeQL**: Results in Security → Code scanning alerts
- **Dependency Review**: Comments posted on PRs with vulnerability details
- **Dependabot**: Creates PRs automatically for dependency updates

These checks do not prevent PR merges but should be reviewed regularly.

______________________________________________________________________

**Last Updated**: 2025-11-13 | **Total Workflows**: 9 (+ 1 Dependabot config)
