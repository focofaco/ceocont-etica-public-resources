## Summary

<!-- Briefly describe what this PR does and why -->

## Type of Change

- [ ] **feat**: New content or functionality (MINOR version bump)
- [ ] **fix**: Bug fix or typo correction (PATCH version bump)
- [ ] **docs**: Documentation updates
- [ ] **refactor**: Code/content restructuring without semantic changes
- [ ] **chore**: Infrastructure, CI/CD, or tooling changes
- [ ] **BREAKING**: Path changes, removals, or semantic changes (MAJOR version bump)

## Changes Made

<!-- List the specific files/content added or modified -->

-
-
-

## Validation Checklist

### Content Rules (if applicable)
- [ ] All files under `raw-text/` end with `.txt`
- [ ] All `.txt` files have corresponding `.json` metadata twins
- [ ] File encoding is UTF-8, LF line endings, no BOM
- [ ] No HTML/JS/CSS content in `.txt` files
- [ ] Filenames follow `lowercase-slug-with-hyphens` pattern
- [ ] No new category directories created (or MAJOR version bump justified)
- [ ] No path changes/renames (or MAJOR + DEPRECATIONS.txt updated)

### TSV/Data Files (if applicable)
- [ ] TSV files use `.tsv.txt` extension
- [ ] Header row present and all rows have same column count
- [ ] Tab separators used (not spaces)
- [ ] Decimal separator is period (.), no thousand separators

### Structural Elements (if applicable)
- [ ] Headers (h1/h2/h3) excluded from 70-80% plaintext baseline calculation
- [ ] Component distribution documented in `chunks.json`

### Pre-commit Validation
- [ ] All pre-commit hooks passed locally
- [ ] No validation errors in CI/CD

### Documentation
- [ ] `CHANGELOG.txt` updated with changes
- [ ] Version bump type documented (MAJOR/MINOR/PATCH or NONE)
- [ ] If BREAKING: `DEPRECATIONS.txt` updated with old→new path mappings

## Semantic Versioning

**Proposed Version**: `vX.Y.Z`

**Justification**:
<!-- Explain why this version bump is appropriate -->
- MAJOR (X): Breaking changes? Path renames? Removals?
- MINOR (Y): New content/features? Backward compatible additions?
- PATCH (Z): Bug fixes? Typos? Clarifications?

## Testing

- [ ] Local testing completed
- [ ] Pre-commit hooks pass
- [ ] Content validation successful

## Post-Merge Actions

<!-- Any manual steps needed after merge? -->

- [ ] Create GitHub release with tag `vX.Y.Z`
- [ ] Update meta/integrity.txt checksums (if release)
- [ ] Update meta/TREE.txt structure (if release)
- [ ] Other: _____

---

**Related Issues**: Closes #XXX (if applicable)

**Breaking Changes**: <!-- Describe any breaking changes, or write "None" -->

**Migration Guide**: <!-- If breaking, describe how clients should adapt, or write "N/A" -->
