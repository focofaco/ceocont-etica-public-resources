# Keep a Changelog Template for AI Agents

**DIRECTIVE**: This template is FOR AI AGENTS ONLY. Follow this specification exactly when maintaining CHANGELOG.md.

## Core Principles

**AI AGENT: Memorize these rules**:

1. Changelogs are for HUMANS, not machines
2. Every version must have an entry
3. Same type of changes must be grouped
4. Latest version comes first
5. Release date of each version must be displayed
6. Semantic Versioning must be followed

## File Structure (EXACT FORMAT)

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New features that are not yet released

## [1.0.0] - 2024-01-15

### Added
- New features for 1.0.0

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Removed features

### Fixed
- Bug fixes

### Security
- Security fixes and improvements

[unreleased]: https://github.com/user/repo/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/user/repo/releases/tag/v1.0.0
```

## Change Type Categories (USE THESE EXACTLY)

**INSTRUCTION**: Classify every change into ONE of these categories. Order them in this sequence:

### 1. Added
**USE FOR**: New features, new functionality, new capabilities
**EXAMPLE**: `- User authentication via OAuth2`

### 2. Changed
**USE FOR**: Changes to existing functionality (not bug fixes)
**EXAMPLE**: `- Update API response format for better readability`

### 3. Deprecated
**USE FOR**: Features that will be removed in upcoming releases
**EXAMPLE**: `- `/api/v1/old-endpoint` - use `/api/v2/new-endpoint` instead`

### 4. Removed
**USE FOR**: Features that have been completely removed
**EXAMPLE**: `- Support for Node.js 12 and below`

### 5. Fixed
**USE FOR**: Bug fixes only
**EXAMPLE**: `- Null pointer exception in user profile loading`

### 6. Security
**USE FOR**: Security-related fixes and improvements
**EXAMPLE**: `- SQL injection vulnerability in search endpoint`

## Version Header Format

**SYNTAX**: `## [VERSION] - YYYY-MM-DD`

**EXAMPLES**:
- `## [1.2.3] - 2024-03-15` ✅
- `## [2.0.0] - 2024-03-15` ✅
- `## [Unreleased]` ✅ (no date for unreleased)

**NEVER**:
- `## 1.2.3 - 2024-03-15` ❌ (missing brackets)
- `## [1.2.3] - 03/15/2024` ❌ (wrong date format)
- `## [1.2.3]` ❌ (missing date for released version)

## Entry Format Rules

**DIRECTIVE**: Each entry must:

1. Start with `-` (dash with space)
2. Use present tense for descriptions
3. Be concise but descriptive
4. Focus on WHAT changed, not HOW
5. Group related changes under appropriate category
6. Include issue/PR references if available

**FORMAT**: `- Brief description of change [#123]`

**CORRECT EXAMPLES**:
```markdown
### Added
- User profile picture upload functionality [#456]
- Email notification system for important events
- Support for PostgreSQL database alongside MySQL

### Fixed
- Memory leak in WebSocket connection handler [#789]
- Incorrect date formatting in exported reports
```

**INCORRECT EXAMPLES** (DO NOT USE):
```markdown
### Added
- Added user profile picture upload. (wrong tense, period at end)
- users can now upload profile pictures (not capitalized)
```

## Semantic Versioning Decision Tree

**AI AGENT: Execute this logic to determine version number**:

### Given current version X.Y.Z:

1. **Does this release have breaking changes or remove features?**
   - YES → Increment X (major): `(X+1).0.0`
   - NO → Continue to 2

2. **Does this release add new features or functionality?**
   - YES → Increment Y (minor): `X.(Y+1).0`
   - NO → Continue to 3

3. **Does this release only fix bugs or make patches?**
   - YES → Increment Z (patch): `X.Y.(Z+1)`

**EXAMPLES**:
- Current: `1.2.3` → Added feature → New: `1.3.0`
- Current: `1.2.3` → Fixed bug → New: `1.2.4`
- Current: `1.2.3` → Breaking change → New: `2.0.0`

## Unreleased Section (MANDATORY)

**RULE**: ALWAYS maintain an `## [Unreleased]` section at the top.

**INSTRUCTION**: When working on changes:
1. Add changes to `[Unreleased]` section first
2. When creating a release, move changes from `[Unreleased]` to new version section
3. Keep `[Unreleased]` section empty (or with template) after release

**EXAMPLE**:
```markdown
## [Unreleased]

### Added
- New feature being worked on

### Fixed
- Bug fix in progress

## [1.0.0] - 2024-03-15
...
```

## Link References (BOTTOM OF FILE)

**DIRECTIVE**: Add comparison links at the bottom of the file.

**FORMAT**:
```markdown
[unreleased]: https://github.com/owner/repo/compare/vX.Y.Z...HEAD
[X.Y.Z]: https://github.com/owner/repo/compare/vX.Y.Z-1...vX.Y.Z
[X.Y.Z-1]: https://github.com/owner/repo/releases/tag/vX.Y.Z-1
```

**EXAMPLE**:
```markdown
[unreleased]: https://github.com/myorg/myrepo/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/myorg/myrepo/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/myorg/myrepo/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/myorg/myrepo/releases/tag/v1.0.0
```

## Complete Example (COPY THIS PATTERN)

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Dark mode support for user interface

## [2.0.0] - 2024-03-20

### Added
- GraphQL API endpoint for flexible data queries
- Real-time notifications via WebSocket
- User preference settings page

### Changed
- **BREAKING**: REST API response format now uses camelCase instead of snake_case
- Database migration to PostgreSQL 15

### Removed
- **BREAKING**: Support for API v1 endpoints

### Fixed
- Race condition in concurrent user updates [#234]
- Memory leak in background job processor [#245]

### Security
- Updated dependencies to patch CVE-2024-1234

## [1.5.2] - 2024-03-10

### Fixed
- Incorrect calculation in invoice total [#220]
- Email delivery failure for Gmail accounts [#225]

## [1.5.1] - 2024-03-05

### Fixed
- Login redirect loop for new users [#210]

### Security
- XSS vulnerability in comment rendering [#215]

## [1.5.0] - 2024-03-01

### Added
- Export data to CSV functionality [#180]
- Batch operations for user management [#185]

### Changed
- Improved search performance by 50% [#190]

### Deprecated
- `/api/old-search` endpoint - use `/api/search/v2` instead [#195]

## [1.0.0] - 2024-02-15

### Added
- Initial release with core functionality
- User authentication and authorization
- RESTful API endpoints
- Admin dashboard

[unreleased]: https://github.com/myorg/myrepo/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/myorg/myrepo/compare/v1.5.2...v2.0.0
[1.5.2]: https://github.com/myorg/myrepo/compare/v1.5.1...v1.5.2
[1.5.1]: https://github.com/myorg/myrepo/compare/v1.5.0...v1.5.1
[1.5.0]: https://github.com/myorg/myrepo/compare/v1.0.0...v1.5.0
[1.0.0]: https://github.com/myorg/myrepo/releases/tag/v1.0.0
```

## AI Agent Workflow: Adding a New Release

**EXECUTE THESE STEPS IN ORDER**:

### Step 1: Determine Version Number
- Analyze changes in `[Unreleased]` section
- Apply Semantic Versioning decision tree
- Calculate new version number

### Step 2: Create Version Header
- Add new version header below `[Unreleased]`
- Format: `## [X.Y.Z] - YYYY-MM-DD`
- Use today's date in ISO format

### Step 3: Move Changes
- Copy all entries from `[Unreleased]` section
- Paste under new version header
- Keep category order: Added, Changed, Deprecated, Removed, Fixed, Security
- Remove empty categories

### Step 4: Clean Unreleased Section
- Leave `## [Unreleased]` header
- Remove all entries (or add template comments)

### Step 5: Update Link References
- Update `[unreleased]` link to compare from new version
- Add new version comparison link
- Update previous version link if needed

### Step 6: Validate
- Run validation checklist (below)

## Validation Checklist (RUN BEFORE COMMIT)

**AI AGENT: Execute this checklist**:

- [ ] `# Changelog` header is present at top
- [ ] Introduction paragraph is present
- [ ] `## [Unreleased]` section exists (even if empty)
- [ ] Version headers use format `## [X.Y.Z] - YYYY-MM-DD`
- [ ] Versions are in reverse chronological order (newest first)
- [ ] Each entry starts with `- ` (dash + space)
- [ ] Categories are in correct order: Added, Changed, Deprecated, Removed, Fixed, Security
- [ ] No empty categories present (remove if empty)
- [ ] All entries are concise and human-readable
- [ ] Breaking changes are marked with **BREAKING**
- [ ] Link references exist at bottom
- [ ] All versions have corresponding links
- [ ] Links use correct format and are not broken

## Mapping Conventional Commits to Changelog

**DIRECTIVE**: When you see these commit types, map them:

| Commit Type | Changelog Category | Notes |
|-------------|-------------------|-------|
| `feat` | Added | New feature |
| `fix` | Fixed | Bug fix |
| `perf` | Changed | Performance improvement |
| `refactor` | Changed | If user-visible; otherwise skip |
| `docs` | Changed or skip | Only if affects user-facing docs |
| `style` | Skip | Internal code style |
| `test` | Skip | Testing changes |
| `build` | Changed | If affects users; otherwise skip |
| `ci` | Skip | Internal CI/CD |
| `chore` | Skip | Internal maintenance |
| `revert` | Depends | Analyze what was reverted |
| `feat!` or BREAKING | Added + note | Mark as **BREAKING** |
| `fix!` or BREAKING | Fixed + note | Mark as **BREAKING** |

## Anti-Patterns (NEVER DO THIS)

❌ Listing every commit as a changelog entry
❌ Using past tense ("Added feature" instead of "Feature added")
❌ Including internal/technical details users don't care about
❌ Forgetting to move changes from Unreleased when releasing
❌ Wrong date format (MM/DD/YYYY instead of YYYY-MM-DD)
❌ Missing link references at bottom
❌ Empty sections (remove them)
❌ Wrong category order

## Special Cases

### Breaking Changes
**FORMAT**: Prefix with `**BREAKING**:` in description

**EXAMPLE**:
```markdown
### Changed
- **BREAKING**: API authentication now requires Bearer token format instead of Basic auth
```

### Yanked Releases
**FORMAT**: `## [X.Y.Z] - YYYY-MM-DD [YANKED]`

**EXAMPLE**:
```markdown
## [1.2.3] - 2024-03-15 [YANKED]

### Fixed
- Critical security vulnerability (this release was yanked due to incomplete fix)
```

### Pre-releases
**FORMAT**: Include pre-release identifier in version

**EXAMPLE**:
```markdown
## [2.0.0-beta.1] - 2024-03-15

### Added
- Beta feature for testing
```

## Final Directive

**AI AGENT**: When maintaining changelog:

1. **ALWAYS** update `[Unreleased]` during development
2. **ALWAYS** use present tense for entries
3. **ALWAYS** think from user's perspective (not developer's)
4. **ALWAYS** remove empty categories
5. **ALWAYS** validate before committing
6. **PREFER** grouping related changes into single entry
7. **PREFER** clarity over brevity
8. **NEVER** include internal implementation details
9. **NEVER** forget link references at bottom

**WHEN IN DOUBT**: Ask yourself "Would a user care about this change?" If NO, don't include it.
