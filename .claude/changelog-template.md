# CHANGELOG TEMPLATE - AI AGENT ONLY

## META-TEMPLATE INSTRUCTIONS

**TARGET**: Claude AI Sonnet 4.5 autonomous changelog generation
**PRIORITY**: Deterministic, structured, machine-parseable
**CONSTRAINTS**: Strict categorization, zero ambiguity, exact pattern

## MANDATORY STRUCTURE

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [X.Y.Z] - YYYY-MM-DD

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

[Unreleased]: https://github.com/USER/REPO/compare/vX.Y.Z...HEAD
[X.Y.Z]: https://github.com/USER/REPO/compare/vX.Y.Z-1...vX.Y.Z
```

## SECTION TAXONOMY (EXHAUSTIVE)

```yaml
Added: # New features, functionality, files
Changed: # Changes in existing functionality
Deprecated: # Soon-to-be removed features
Removed: # Removed features, breaking deletions
Fixed: # Bug fixes, corrections
Security: # Vulnerabilities, security updates
```

## SECTION RULES

### Added

- **Trigger**: `feat:` commits
- **Content**: New capabilities users can now use
- **Examples**:
  - New API endpoints
  - New configuration options
  - New command-line flags
  - New UI components

### Changed

- **Trigger**: `refactor:`, `perf:`, `style:` commits with user impact
- **Content**: Modifications to existing behavior
- **Examples**:
  - Updated dependencies
  - Modified API responses
  - Changed default values
  - Improved performance

### Deprecated

- **Trigger**: Explicit deprecation notices in code/docs
- **Content**: Features still working but will be removed
- **Format**: `X is deprecated, use Y instead`

### Removed

- **Trigger**: `feat!:`, `refactor!:` commits removing features
- **Content**: Features no longer available (breaking)
- **Examples**:
  - Deleted API endpoints
  - Removed configuration options
  - Dropped platform support

### Fixed

- **Trigger**: `fix:` commits
- **Content**: Bug corrections, error handling
- **Examples**:
  - Resolved crashes
  - Corrected calculations
  - Fixed memory leaks

### Security

- **Trigger**: Security-related fixes, updates
- **Content**: Vulnerability patches, security improvements
- **Format**: Include CVE if applicable
- **Priority**: Always list first if present

## VERSION HEADER FORMAT

```
## [X.Y.Z] - YYYY-MM-DD
```

- Version in square brackets
- Semver format: MAJOR.MINOR.PATCH
- ISO 8601 date: YYYY-MM-DD
- Space-dash-space separator

## UNRELEASED SECTION

- Always maintain `## [Unreleased]` at top
- Accumulate changes not yet released
- Move to versioned section on release
- Never delete, always keep empty after release

## ENTRY FORMAT RULES

- Use bullet points (-)
- Start with capital letter
- End with period
- One change per line
- Group related changes
- Most recent version first
- Blank line between sections

## LINK REFERENCES (BOTTOM)

```markdown
[Unreleased]: https://github.com/USER/REPO/compare/vX.Y.Z...HEAD
[X.Y.Z]: https://github.com/USER/REPO/compare/vX.Y.Z-1...vX.Y.Z
[X.Y.Z-1]: https://github.com/USER/REPO/compare/vX.Y.Z-2...vX.Y.Z-1
```

- Compare links for diffs
- Unreleased compares latest tag to HEAD
- Each version compares to previous

## COMMIT TYPE → CHANGELOG SECTION MAPPING

```python
COMMIT_TO_CHANGELOG = {
    "feat": "Added",
    "fix": "Fixed",
    "perf": "Changed",
    "refactor": "Changed",  # if user-facing, else skip
    "style": "Changed",     # if user-facing, else skip
    "docs": None,           # skip (not user-facing)
    "test": None,           # skip (not user-facing)
    "build": None,          # skip unless affects users
    "ci": None,             # skip (not user-facing)
    "chore": None,          # skip (not user-facing)
    "revert": "Fixed",      # if reverting a bug
}

BREAKING_CHANGE = {
    "Added": "Added",       # new breaking feature
    "Changed": "Changed",   # breaking modification
    "Removed": "Removed",   # breaking deletion
}
```

## DECISION TREE FOR ENTRY PLACEMENT

```
Is it a security fix? → Security
Is it a new feature? → Added
Is it a bug fix? → Fixed
Is it breaking removal? → Removed
Is it deprecation notice? → Deprecated
Is it user-facing change? → Changed
Is it internal only? → SKIP (no entry)
```

## EXAMPLE CHANGELOG

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.1.0] - 2024-03-15

### Added

- New PDF export functionality with customizable templates.
- Support for multi-language documentation generation.

### Changed

- Improved performance of data parsing by 40%.
- Updated dependency `axios` from 0.27.0 to 1.6.0.

### Fixed

- Resolved race condition in concurrent file uploads.
- Corrected timezone handling in date calculations.

## [2.0.0] - 2024-02-01

### Added

- New authentication system with OAuth2 support.
- Webhook support for real-time notifications.

### Changed

- API response format now uses JSON envelopes.

### Removed

- Legacy XML API endpoints (use JSON instead).
- Support for Node.js 12 and 14.

### Security

- Patched SQL injection vulnerability in search endpoint (CVE-2024-1234).

## [1.0.0] - 2024-01-10

### Added

- Initial release with core functionality.
- User management system.
- RESTful API with authentication.

[Unreleased]: https://github.com/user/repo/compare/v2.1.0...HEAD
[2.1.0]: https://github.com/user/repo/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/user/repo/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/user/repo/releases/tag/v1.0.0
```

## ANTI-PATTERNS (FORBIDDEN)

```markdown
❌ ## 2.1.0 - 2024-03-15 # Missing brackets
❌ ## [2.1.0] 2024-03-15 # Missing dash separator
❌ ## [2.1.0] - 03/15/2024 # Wrong date format
❌ ### Features # Non-standard section name
❌ - added new feature # Lowercase start
❌ - Fixed bug # Inconsistent capitalization
❌ - New API endpoint # No period at end
❌ ## [2.0.0] (Breaking Changes) # Extra annotation
```

## CORRECT PATTERNS (REQUIRED)

```markdown
✓ ## [2.1.0] - 2024-03-15
✓ ### Added
✓ - New PDF export functionality.
✓ ### Fixed
✓ - Resolved race condition in file uploads.
```

## CHANGELOG UPDATE ALGORITHM

```python
def update_changelog(commits_since_last_release):
    changelog = parse_existing_changelog()
    unreleased_section = {
        "Added": [],
        "Changed": [],
        "Deprecated": [],
        "Removed": [],
        "Fixed": [],
        "Security": []
    }

    for commit in commits_since_last_release:
        # Parse conventional commit
        type, scope, breaking, description = parse_commit(commit)

        # Determine section
        if is_security_related(commit):
            section = "Security"
        elif breaking and type in ["feat", "refactor", "perf"]:
            if "remove" in description or "drop" in description:
                section = "Removed"
            elif type == "feat":
                section = "Added"
            else:
                section = "Changed"
        else:
            section = COMMIT_TO_CHANGELOG.get(type)

        # Skip if not user-facing
        if section is None:
            continue

        # Format entry
        entry = format_changelog_entry(description, scope)

        # Add to section
        unreleased_section[section].append(entry)

    # Update changelog with unreleased section
    update_unreleased(changelog, unreleased_section)

def release_version(version, date):
    changelog = parse_existing_changelog()

    # Move unreleased to new version
    version_section = changelog["Unreleased"]
    changelog[version] = {
        "date": date,
        "sections": version_section
    }

    # Clear unreleased
    changelog["Unreleased"] = empty_sections()

    # Update comparison links
    update_comparison_links(changelog, version)

    write_changelog(changelog)
```

## ENTRY FORMATTING RULES

```python
def format_changelog_entry(description, scope):
    # 1. Capitalize first letter
    entry = description[0].upper() + description[1:]

    # 2. Add scope if present
    if scope:
        entry = f"{scope.capitalize()}: {entry}"

    # 3. Remove redundant words
    entry = entry.replace("fixed bug in", "").strip()
    entry = entry.replace("added feature for", "").strip()

    # 4. Ensure period at end
    if not entry.endswith('.'):
        entry += '.'

    return f"- {entry}"
```

## SEMVER DETERMINATION

```python
def determine_next_version(current_version, commits):
    has_breaking = any(c.breaking for c in commits)
    has_feat = any(c.type == "feat" for c in commits)
    has_fix = any(c.type == "fix" for c in commits)

    major, minor, patch = parse_version(current_version)

    if has_breaking:
        return f"{major + 1}.0.0"
    elif has_feat:
        return f"{major}.{minor + 1}.0"
    elif has_fix:
        return f"{major}.{minor}.{patch + 1}"
    else:
        return current_version  # No version bump needed
```

## PRIORITY EXECUTION RULES

1. ALWAYS maintain `[Unreleased]` section at top
2. ALWAYS use exact section names (Added, Changed, etc.)
3. ALWAYS format versions as `[X.Y.Z] - YYYY-MM-DD`
4. ALWAYS include comparison links at bottom
5. NEVER include non-user-facing changes
6. ALWAYS capitalize entry first letter
7. ALWAYS end entries with period
8. ALWAYS list Security section first if present
9. ALWAYS order versions newest to oldest
10. NEVER use custom section names

## EXCLUSION RULES

**DO NOT include in CHANGELOG:**

- Internal refactoring (unless user-facing impact)
- Test additions/updates
- CI/CD configuration changes
- Documentation updates (unless user-facing docs)
- Code style/formatting changes
- Build configuration changes
- Dependency updates (unless security or breaking)

**DO include in CHANGELOG:**

- New features users can access
- Bug fixes users will notice
- Breaking changes requiring user action
- Security vulnerabilities patched
- Deprecated features (with migration path)
- Removed features
- Performance improvements users will notice

## VALIDATION CHECKLIST

- [ ] Header format: `## [X.Y.Z] - YYYY-MM-DD`
- [ ] Section names from approved list only
- [ ] Entries start with capital letter
- [ ] Entries end with period
- [ ] Entries use bullet points (-)
- [ ] Blank line between sections
- [ ] Comparison links at bottom
- [ ] Unreleased section exists
- [ ] Versions in descending order
- [ ] Only user-facing changes included

---

**END OF TEMPLATE - VERSION 1.0.0**
