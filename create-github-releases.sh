#!/bin/bash
# Script to create GitHub releases via API
# Usage: GITHUB_TOKEN=your_token ./create-github-releases.sh

set -euo pipefail

REPO="focofaco/ceocont-etica-public-resources"
API_BASE="https://api.github.com"

# Check for GitHub token
if [ -z "${GITHUB_TOKEN:-}" ]; then
    echo "ERROR: GITHUB_TOKEN environment variable not set"
    echo ""
    echo "Usage:"
    echo "  export GITHUB_TOKEN=ghp_your_token_here"
    echo "  ./create-github-releases.sh"
    echo ""
    echo "Or in one line:"
    echo "  GITHUB_TOKEN=ghp_your_token_here ./create-github-releases.sh"
    echo ""
    echo "Create token at: https://github.com/settings/tokens/new"
    echo "Required scopes: repo (full control)"
    exit 1
fi

echo "====================================================================="
echo "GitHub Releases Creation Script"
echo "====================================================================="
echo "Repository: $REPO"
echo ""

# Function to create a release
create_release() {
    local tag_name="$1"
    local target_branch="$2"
    local release_name="$3"
    local body="$4"
    local is_prerelease="${5:-false}"

    echo "Creating release: $release_name ($tag_name)"

    # Create release JSON payload
    local payload=$(cat <<EOF
{
  "tag_name": "$tag_name",
  "target_commitish": "$target_branch",
  "name": "$release_name",
  "body": $(echo "$body" | jq -Rs .),
  "draft": false,
  "prerelease": $is_prerelease
}
EOF
)

    # Create release via API
    response=$(curl -s -w "\n%{http_code}" \
        -X POST \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer $GITHUB_TOKEN" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        "$API_BASE/repos/$REPO/releases" \
        -d "$payload")

    # Extract HTTP status code
    http_code=$(echo "$response" | tail -n1)
    response_body=$(echo "$response" | head -n-1)

    if [ "$http_code" = "201" ]; then
        echo "✓ Release created successfully"
        release_url=$(echo "$response_body" | jq -r '.html_url')
        echo "  URL: $release_url"
        return 0
    else
        echo "✗ Failed to create release (HTTP $http_code)"
        echo "  Response: $response_body" | jq -r '.message // .'
        return 1
    fi
}

# Release v1.0.0
echo ""
echo "---------------------------------------------------------------------"
echo "Release v1.0.0 - Initial Release"
echo "---------------------------------------------------------------------"
RELEASE_BODY_1_0_0="## Initial Release

First public release of the text-only content repository.

### Added:
- Initial directory structure for online-resources/raw-text/
- 11 content categories (plaintext → others + meta)
- Server-side contract and brandguide documentation
- Text-only policy enforcement
- UTF-8 + LF line ending requirements
- Path stability within MAJOR version
- Semantic versioning strategy
- 70-80% plaintext baseline enforcement

### Core Features:
- Text-only repository (no HTML/JS/CSS/binaries)
- CDN-ready with immutable versioning
- Client-agnostic content delivery
- Cryptographic integrity (SHA256)

### Validation Rules:
- Lowercase-slug-with-hyphens naming
- TSV tables with headers
- Graphviz DOT diagrams
- JSON metadata dictionaries

**Note**: This is the foundation release with empty content directories."

create_release "v1.0.0" "main" "v1.0.0 - Initial Release" "$RELEASE_BODY_1_0_0" false

# Release v1.1.0
echo ""
echo "---------------------------------------------------------------------"
echo "Release v1.1.0 - Pre-commit Hooks"
echo "---------------------------------------------------------------------"
RELEASE_BODY_1_1_0="## Pre-commit Hooks Release

MINOR version bump - Added automated validation infrastructure.

### Added:
- Pre-commit hooks configuration (.pre-commit-config.yaml)
- Standard hooks from pre-commit v4.4.0 and v6.0.0
- 5 custom validation hooks:
  - \`validate_raw_text_only.sh\` - Raw-text file verification
  - \`validate_audit_json.py\` - JSON schema validation
  - \`forbid_html_js_css.sh\` - Content purity checks
  - \`check_crlf.sh\` - Line ending enforcement
  - \`validate_filename_pattern.sh\` - Naming convention checks
- First content fragment: 001-politica-controle-qualidade-contabil-41f5.txt
- Ingestion audit trail system (.claude/ingestion-audit.json)
- Ingestion audit schema (.claude/ingestion-audit-schema.json)

### Removed:
- shadow-original/ folder (replaced by JSON audit trail)
- shadow-fragments-original/ folder (replaced by JSON audit trail)
- shadow-fragments-transformed/ folder (replaced by JSON audit trail)

### Changed:
- Updated brandguide bundle integration
- Fixed trailing whitespace in contract files
- Fixed end-of-file newlines in schema files

### Validation Status:
✓ All pre-commit hooks passing
✓ JSON schema validation active
✓ Raw-text file verification enabled
✓ HTML/JS/CSS blocking enforced
✓ LF line endings enforced
✓ Filename patterns validated"

create_release "v1.1.0" "main" "v1.1.0 - Pre-commit Hooks" "$RELEASE_BODY_1_1_0" false

# Release v2.0.0
echo ""
echo "---------------------------------------------------------------------"
echo "Release v2.0.0 - Header Components (BREAKING)"
echo "---------------------------------------------------------------------"
RELEASE_BODY_2_0_0="## Header Components Release (BREAKING CHANGES)

MAJOR version bump - New component categories added.

### BREAKING CHANGES:
- Added new component categories: header_h1/, header_h2/, header_h3/
- Headers are structural elements and do NOT count towards 70-80% plaintext baseline
- Component enum in all schemas updated to include new header types
- ComponentDistribution and ComponentDistributionPercentage models extended

### Added:
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

### Changed:
- Updated all Pydantic models to include header_h1, header_h2, header_h3 components
- Migrated validate_audit_json.py from jsonschema to Pydantic v2
- Updated server-contract.md §3 with new header component categories
- Updated .pre-commit-config.yaml to use Pydantic validators
- Updated validate_raw_text_only.sh to allow README.md and .json metadata twins
- chunks.json component_distribution extended with header fields

### SSoT Architecture:
- JSON metadata twins = Single Source of Truth (full content + metadata, no CDN, no size limits)
- TXT files = Derived content (CDN delivery, text only)

### Validation Status:
✓ All pre-commit hooks passing
✓ Pydantic v2 validation passing
✓ Metadata twin validation passing
✓ chunks.json validation passing
✓ Component README files created
✓ Contract documentation updated"

create_release "v2.0.0" "main" "v2.0.0 - Header Components" "$RELEASE_BODY_2_0_0" false

echo ""
echo "====================================================================="
echo "Release creation complete!"
echo "====================================================================="
echo ""
echo "Next steps:"
echo "1. Verify releases at: https://github.com/$REPO/releases"
echo "2. Tags created: v1.0.0, v1.1.0, v2.0.0"
echo "3. Update CHANGELOG.txt links if needed"
echo ""
