# CLAUDE.md — AI Agent Operational Rules

## META-INSTRUCTIONS
**TARGET**: Claude AI Sonnet 4.5 autonomous operation on text-only content repository
**AUTHORITY**: This document is NORMATIVE for AI agent behavior
**PRIORITY**: Deterministic, zero-ambiguity, explicit boundaries
**LANGUAGE**: English (project contracts are multilingual: PT-BR, Latin)

---

## PROJECT IDENTITY

### What This Repository IS
- **Text-only content repository** for `online-resources/raw-text/`
- **Server-side contract** governing pure text delivery via CDN
- **Immutable versioned content** with cryptographic integrity (SHA256)
- **Strict format enforcement**: UTF-8, LF line endings, no BOM
- **Semantic versioning** with breaking change discipline

### What This Repository IS NOT
- NOT a client application
- NOT a UI/rendering system
- NOT a general-purpose code repository
- NOT a documentation wiki
- NOT a binary/media storage

---

## CORE CONSTRAINTS (ABSOLUTE)

### 1. FILE FORMAT RULES

```yaml
ALLOWED:
  - Extension: .txt (ONLY)
  - Encoding: UTF-8 (MUST)
  - Line endings: LF (\n) (MUST)
  - BOM: MUST NOT exist
  - Special formats:
    - *.tsv.txt (tab-separated values)
    - *.dot.txt (Graphviz DOT)
    - *.json.txt (JSON as text)

FORBIDDEN:
  - HTML files
  - JavaScript files
  - CSS files
  - Images (SVG, PNG, JPG, WebP)
  - PDFs
  - Binary files
  - Audio/video
  - Any extension other than .txt
```

### 2. DIRECTORY STRUCTURE (IMMUTABLE)

```
online-resources/raw-text/          # ROOT (mandatory)
├── plaintext/                      # flowing text per box
├── callouts/                       # highlighted messages
├── docks/                          # editorial side notes
├── tradeoffs/                      # pros/cons lists (+/-)
├── tables/                         # *.tsv.txt (1st line = header)
├── data/                           # *.tsv.txt for charts
├── faqs/                           # q.txt and a.txt pairs
├── diagrams/                       # *.dot.txt (Graphviz)
├── disclaimers/                    # legal/risk warnings
├── others/                         # generic textual content
└── meta/                           # metadata files
    ├── glossario.json.txt
    ├── abbr.json.txt
    ├── integrity.txt               # SHA256 checksums
    └── TREE.txt                    # directory tree
```

**RULE**: MUST NOT create new category directories without MAJOR version bump

### 3. PATH STABILITY

```python
STABLE_IDENTIFIER = full_path_under_raw_text

# Path cannot change within same MAJOR version
# Rename/move requires:
#   1. MAJOR version bump
#   2. Entry in DEPRECATIONS.txt
#   3. Mapping: old_path → new_path + removal_version
```

### 4. NAMING CONVENTIONS

```yaml
Format: lowercase-slug-with-hyphens
Allowed: [a-z0-9-]
Forbidden:
  - Spaces
  - Accents/diacritics
  - Uppercase letters
  - Special characters (except hyphen)
  - .. (parent directory)
  - Leading slash
  - URLs in path

Examples:
  ✓ intro-to-topic.txt
  ✓ risk-analysis-2024.tsv.txt
  ✓ process-flow.dot.txt
  ✗ Intro To Topic.txt
  ✗ análise_risco.txt
  ✗ ../other/file.txt
```

---

## AI AGENT BEHAVIOR RULES

### RULE 1: Text Purity Enforcement

```python
def validate_content(file_path, content):
    """AI agent MUST validate before writing ANY file."""

    # Check 1: Extension
    assert file_path.endswith('.txt'), "MUST end with .txt"

    # Check 2: UTF-8 validity
    assert content.encode('utf-8'), "MUST be valid UTF-8"

    # Check 3: Line endings
    assert '\r\n' not in content, "MUST NOT contain CRLF"
    assert '\r' not in content, "MUST NOT contain CR"

    # Check 4: BOM
    assert not content.startswith('\ufeff'), "MUST NOT have BOM"

    # Check 5: No HTML
    html_patterns = ['<html', '<script', '<style', '<div', '<span']
    assert not any(p in content.lower() for p in html_patterns), \
        "MUST NOT contain HTML tags"

    # Check 6: Control characters
    forbidden_chars = ['\x00', '\x01', '\x02', '\x03', '\x04']
    assert not any(c in content for c in forbidden_chars), \
        "MUST NOT contain control characters"

    return True
```

### RULE 2: Subtype-Specific Validation

```python
def validate_by_subtype(category, file_path, content):
    """AI agent MUST apply subtype rules."""

    if category == 'tradeoffs':
        # Each line MUST start with + or -
        lines = content.strip().split('\n')
        for line in lines:
            assert line.startswith(('+', '-')), \
                "tradeoffs MUST have +/- per line"

    elif category == 'faqs':
        # MUST have q.txt and a.txt pairs
        if file_path.endswith('q.txt'):
            answer_path = file_path.replace('q.txt', 'a.txt')
            assert answer_path_exists(), "FAQ MUST have both q.txt and a.txt"

    elif category in ['tables', 'data']:
        # MUST be TSV format
        assert file_path.endswith('.tsv.txt'), "MUST use .tsv.txt extension"
        lines = content.strip().split('\n')
        assert len(lines) >= 2, "TSV MUST have header + data"

        # Check tab separator
        header_cols = len(lines[0].split('\t'))
        for i, line in enumerate(lines[1:], 2):
            cols = len(line.split('\t'))
            assert cols == header_cols, \
                f"Line {i}: MUST have {header_cols} columns, got {cols}"

        # Check no formulas, no thousand separators
        assert '=' not in content, "TSV MUST NOT contain formulas"
        # Decimal separator must be period
        # No thousand separators (comma)

    elif category == 'diagrams':
        # MUST be DOT format
        assert file_path.endswith('.dot.txt'), "MUST use .dot.txt extension"
        assert 'digraph' in content or 'graph' in content, \
            "DOT MUST define digraph or graph"

    elif category == 'meta':
        if file_path.endswith('.json.txt'):
            import json
            try:
                json.loads(content)
            except:
                raise ValueError("JSON.txt MUST be valid JSON")
```

### RULE 3: Pre-Commit Checklist

```yaml
BEFORE_EVERY_COMMIT:
  - [ ] All files under raw-text/ end with .txt
  - [ ] All files are UTF-8, LF, no BOM
  - [ ] No HTML/JS/CSS/binaries added
  - [ ] Paths follow lowercase-slug-with-hyphens
  - [ ] No new categories created (unless MAJOR bump)
  - [ ] No path changes (unless MAJOR + DEPRECATIONS.txt)
  - [ ] Subtype-specific rules validated
  - [ ] meta/integrity.txt updated (if release)
  - [ ] meta/TREE.txt updated (if release)
  - [ ] CHANGELOG.txt updated (if release)
```

### RULE 4: Commit Message Generation

```python
def generate_commit_message(changes):
    """AI agent MUST follow conventional commits."""

    # Determine type
    if is_new_content(changes):
        type = "feat"
    elif is_fix(changes):
        type = "fix"
    elif is_docs(changes):
        type = "docs"
    elif is_refactor(changes):
        type = "refactor"
    else:
        type = "chore"

    # Check breaking changes
    breaking = ""
    if path_changed(changes) or category_added(changes):
        breaking = "!"

    # Determine scope
    scope = extract_category(changes)  # e.g., "plaintext", "faqs"

    # Format
    message = f"{type}"
    if scope:
        message += f"({scope})"
    message += f"{breaking}: {description}"

    return message

# Examples:
# feat(plaintext): add introduction text for ethics chapter
# fix(tables): correct column alignment in risk-matrix.tsv.txt
# feat(meta)!: restructure glossary format
```

### RULE 5: Version Bump Decision

```python
def determine_version_bump(changes):
    """AI agent MUST apply semver rules."""

    # MAJOR (X.0.0)
    if any([
        path_renamed_or_moved(changes),
        path_removed_without_substitute(changes),
        new_category_added(changes),
        semantic_change_incompatible(changes)
    ]):
        return "MAJOR"

    # MINOR (0.X.0)
    elif any([
        new_content_added(changes),
        compatible_enhancement(changes)
    ]):
        return "MINOR"

    # PATCH (0.0.X)
    elif any([
        bug_fix(changes),
        typo_correction(changes),
        clarification_without_semantic_change(changes)
    ]):
        return "PATCH"

    else:
        return "NONE"  # No version bump needed
```

---

## WORKFLOW PROCEDURES

### Procedure A: Adding New Content

```bash
# 1. Determine category
CATEGORY=plaintext  # or callouts, docks, etc.

# 2. Create file with proper naming
FILE_PATH="online-resources/raw-text/${CATEGORY}/topic-name.txt"

# 3. Write content
# AI agent writes pure text, UTF-8, LF

# 4. Validate
validate_content(FILE_PATH, content)
validate_by_subtype(CATEGORY, FILE_PATH, content)

# 5. Commit
git add "${FILE_PATH}"
git commit -m "feat(${CATEGORY}): add topic-name content"

# 6. Push
git push -u origin claude/devXXX-description-SESSION_ID
```

### Procedure B: Modifying Existing Content

```bash
# 1. Read current content
current_content = read_file(FILE_PATH)

# 2. Apply modifications
# NEVER change path/filename within same MAJOR

# 3. Validate
validate_content(FILE_PATH, new_content)

# 4. Commit
git add "${FILE_PATH}"
git commit -m "fix(category): correct description in topic-name"

# 5. Push
git push -u origin claude/devXXX-description-SESSION_ID
```

### Procedure C: Renaming/Moving Content (BREAKING)

```bash
# 1. Determine this requires MAJOR bump
OLD_PATH="online-resources/raw-text/plaintext/old-name.txt"
NEW_PATH="online-resources/raw-text/plaintext/new-name.txt"

# 2. Update DEPRECATIONS.txt
echo "${OLD_PATH} → ${NEW_PATH} (removed in vX.0.0)" >> DEPRECATIONS.txt

# 3. Move file
git mv "${OLD_PATH}" "${NEW_PATH}"

# 4. Commit with breaking change marker
git add DEPRECATIONS.txt
git commit -m "feat(plaintext)!: rename old-name to new-name

BREAKING CHANGE: Path changed from old-name.txt to new-name.txt.
Update references to use new path."

# 5. Note: This REQUIRES MAJOR version bump
```

### Procedure D: Preparing Release

```bash
# 1. Update meta/integrity.txt
# Generate SHA256 for ALL files under raw-text/
find online-resources/raw-text -type f -name "*.txt" | while read file; do
    sha256sum "$file" >> meta/integrity.txt.tmp
done
mv meta/integrity.txt.tmp online-resources/raw-text/meta/integrity.txt

# 2. Update meta/TREE.txt
tree online-resources/raw-text > online-resources/raw-text/meta/TREE.txt

# 3. Update CHANGELOG.txt (root level)
# Follow Keep a Changelog format
# Document all changes since last version

# 4. Commit metadata
git add online-resources/raw-text/meta/integrity.txt \
        online-resources/raw-text/meta/TREE.txt \
        CHANGELOG.txt
git commit -m "chore(release): prepare v${VERSION} metadata"

# 5. Create tag
git tag -a "v${VERSION}" -m "Release v${VERSION}: description"

# 6. Push (branch first, then tag)
git push -u origin claude/devXXX-description-SESSION_ID
git push origin "v${VERSION}"
```

### Procedure E: Handling TSV Data

```bash
# 1. Create TSV file
FILE_PATH="online-resources/raw-text/tables/data-matrix.tsv.txt"

# 2. Format with tabs (not spaces)
HEADER="Column1\tColumn2\tColumn3"
ROW1="Value1\tValue2\tValue3"
ROW2="Value4\tValue5\tValue6"

CONTENT="${HEADER}\n${ROW1}\n${ROW2}"

# 3. Validate
# - Header present
# - Same column count per row
# - Tab separator (\t)
# - Decimal separator is period (.)
# - No thousand separators
# - No formulas

# 4. Write and commit
echo -e "${CONTENT}" > "${FILE_PATH}"
git add "${FILE_PATH}"
git commit -m "feat(tables): add data-matrix table"
```

### Procedure F: Handling FAQ Pairs

```bash
# 1. Create directory for FAQ
FAQ_DIR="online-resources/raw-text/faqs/topic-question"
mkdir -p "${FAQ_DIR}"

# 2. Create q.txt
Q_FILE="${FAQ_DIR}/q.txt"
echo "What is the question?" > "${Q_FILE}"

# 3. Create a.txt
A_FILE="${FAQ_DIR}/a.txt"
echo "This is the answer to the question." > "${A_FILE}"

# 4. Validate both exist
assert [ -f "${Q_FILE}" ] && [ -f "${A_FILE}" ]

# 5. Commit together
git add "${FAQ_DIR}/"
git commit -m "feat(faqs): add topic-question FAQ pair"
```

---

## DECISION TREES

### Tree 1: Content Type Selection

```
Question: What type of content am I creating?

├─ Flowing text for a content box?
│  └─> Use: plaintext/filename.txt
│
├─ Highlighted message/alert?
│  └─> Use: callouts/filename.txt
│
├─ Editorial side note?
│  └─> Use: docks/filename.txt
│
├─ Pros and cons list?
│  └─> Use: tradeoffs/filename.txt
│     Format: Each line starts with + or -
│
├─ Tabular data (visible as table)?
│  └─> Use: tables/filename.tsv.txt
│     Format: TSV with header
│
├─ Data for chart/graph?
│  └─> Use: data/filename.tsv.txt
│     Format: TSV with header
│
├─ Question and answer?
│  └─> Use: faqs/topic/q.txt + faqs/topic/a.txt
│
├─ Diagram/flowchart?
│  └─> Use: diagrams/filename.dot.txt
│     Format: Graphviz DOT
│
├─ Legal/risk warning?
│  └─> Use: disclaimers/filename.txt
│
├─ Metadata/glossary/abbreviations?
│  └─> Use: meta/filename.json.txt
│     Format: Valid JSON
│
└─ None of the above?
   └─> Use: others/filename.txt
```

### Tree 2: Version Bump Required?

```
Question: What version change is needed?

Did I:
├─ Rename/move a file?                      → MAJOR
├─ Remove content without substitute?       → MAJOR
├─ Add new category directory?              → MAJOR
├─ Change semantic meaning incompatibly?    → MAJOR
├─ Break client assumptions?                → MAJOR
│
├─ Add new content file?                    → MINOR
├─ Enhance existing content compatibly?     → MINOR
│
├─ Fix typo/error?                          → PATCH
├─ Clarify without changing meaning?        → PATCH
│
└─ Only update CI/docs/internal?            → NONE
```

### Tree 3: Commit Type Selection

```
Question: What commit type should I use?

Did I:
├─ Add new content file?                    → feat
├─ Add new functionality/capability?        → feat
│
├─ Fix error/bug in content?                → fix
├─ Correct typo?                            → fix
├─ Fix broken reference?                    → fix
│
├─ Update documentation?                    → docs
├─ Update README?                           → docs
│
├─ Restructure without changing meaning?    → refactor
│
├─ Improve performance?                     → perf
│
├─ Update metadata (integrity, tree)?       → chore
├─ Update CI configuration?                 → ci
├─ Update build scripts?                    → build
│
└─ Add/update tests?                        → test
```

---

## ERROR HANDLING

### Error 1: Invalid File Extension

```yaml
ERROR: "File does not end with .txt"
CAUSE: File created with wrong extension
ACTION:
  1. NEVER proceed
  2. Delete invalid file
  3. Recreate with .txt extension
  4. Inform user of correction
```

### Error 2: HTML Content Detected

```yaml
ERROR: "HTML tags detected in content"
CAUSE: Content contains <tag> patterns
ACTION:
  1. NEVER commit HTML
  2. Strip all HTML tags
  3. Convert to plain text
  4. Validate pure text
  5. Inform user of sanitization
```

### Error 3: Path Stability Violation

```yaml
ERROR: "Cannot rename file in same MAJOR version"
CAUSE: Attempting to change path without MAJOR bump
ACTION:
  1. STOP operation
  2. Create DEPRECATIONS.txt entry
  3. Explain MAJOR bump requirement
  4. Ask user to confirm MAJOR bump
  5. Only proceed with explicit confirmation
```

### Error 4: TSV Column Mismatch

```yaml
ERROR: "TSV rows have inconsistent column count"
CAUSE: Tab separator missing or extra columns
ACTION:
  1. NEVER commit invalid TSV
  2. Parse TSV structure
  3. Identify mismatched rows
  4. Fix tab separators
  5. Validate all rows match header count
```

### Error 5: CRLF Line Endings

```yaml
ERROR: "CRLF line endings detected"
CAUSE: Content has \r\n instead of \n
ACTION:
  1. NEVER commit CRLF
  2. Convert all \r\n to \n
  3. Remove all \r characters
  4. Validate LF-only
  5. Inform user of normalization
```

---

## VALIDATION CHECKLIST

### Pre-Write Validation

```yaml
Before writing ANY file under raw-text/:
  - [ ] File path matches pattern: online-resources/raw-text/{category}/{slug}.txt
  - [ ] Category is from approved list (§2 Directory Structure)
  - [ ] Filename is lowercase-slug-with-hyphens
  - [ ] Extension is .txt (or .tsv.txt, .dot.txt, .json.txt)
  - [ ] Content is valid UTF-8
  - [ ] Content has LF line endings only
  - [ ] Content has no BOM
  - [ ] Content has no HTML/JS/CSS
  - [ ] Content has no control characters
  - [ ] Subtype-specific rules validated
```

### Pre-Commit Validation

```yaml
Before committing:
  - [ ] All files validated per Pre-Write checklist
  - [ ] Commit message follows Conventional Commits
  - [ ] Commit type is accurate
  - [ ] Breaking changes marked with !
  - [ ] Scope matches category
  - [ ] Description is imperative, lowercase, no period
  - [ ] No files staged outside raw-text/ (unless release metadata)
```

### Pre-Release Validation

```yaml
Before creating release tag:
  - [ ] Version follows semver (vX.Y.Z)
  - [ ] Version bump matches changes (MAJOR/MINOR/PATCH)
  - [ ] meta/integrity.txt updated with all file checksums
  - [ ] meta/TREE.txt updated with current structure
  - [ ] CHANGELOG.txt updated with release notes
  - [ ] DEPRECATIONS.txt updated if paths changed
  - [ ] All tests pass (if CI configured)
  - [ ] No uncommitted changes
  - [ ] Tag message is descriptive
```

---

## FORBIDDEN OPERATIONS

### NEVER Do These

```yaml
FORBIDDEN_OPERATIONS:
  - Create file without .txt extension under raw-text/
  - Write HTML/JS/CSS content
  - Write binary data
  - Create new category without MAJOR bump
  - Rename/move file without MAJOR bump + DEPRECATIONS.txt
  - Commit with CRLF line endings
  - Commit with BOM
  - Commit files outside raw-text/ hierarchy (except root metadata)
  - Create TSV without header row
  - Create FAQ without both q.txt and a.txt
  - Use uppercase or spaces in filenames
  - Use relative paths with .. or leading /
  - Embed URLs as content (unless explicitly allowed)
  - Skip integrity/tree/changelog updates in release
  - Push tag without pushing commits first
  - Force push to main branch
  - Amend commits after push
  - Create tag without v prefix
```

---

## COMMUNICATION PROTOCOLS

### When AI Agent Encounters Ambiguity

```yaml
PROTOCOL:
  1. STOP operation
  2. Identify ambiguous element
  3. List possible interpretations
  4. Ask user for clarification
  5. Wait for explicit instruction
  6. Proceed with confirmed approach

NEVER:
  - Guess user intent
  - Proceed with assumption
  - Create files proactively without clarity
```

### When AI Agent Detects Violation

```yaml
PROTOCOL:
  1. STOP operation immediately
  2. Describe violation clearly
  3. Reference specific rule/section
  4. Explain impact
  5. Propose correction
  6. Ask user to confirm correction
  7. Apply correction only after confirmation

NEVER:
  - Silently fix without informing user
  - Proceed with invalid state
  - Ignore validation failures
```

### When AI Agent Completes Task

```yaml
PROTOCOL:
  1. Summarize actions taken
  2. List files created/modified
  3. Show commit message used
  4. Confirm validation passed
  5. Display next steps (if any)
  6. Update TodoWrite with completion

FORMAT:
  "✓ Task completed:
   - Created: {file_path}
   - Validated: {validation_type}
   - Committed: {commit_sha}
   - Message: {commit_message}

   Next: Push to remote branch"
```

---

## EDGE CASES

### Edge Case 1: Empty File

```yaml
SCENARIO: Content file is empty or only whitespace
DECISION:
  - IF release/production: REJECT (empty files provide no value)
  - IF draft/WIP: ALLOW with warning
  - ALWAYS: Add TODO comment in commit message
```

### Edge Case 2: Very Large File

```yaml
SCENARIO: File exceeds size threshold
DECISION:
  1. Check if CI defines max size (respect it)
  2. If no CI limit: warn at 100KB, reject at 1MB
  3. Suggest splitting into multiple files
  4. NEVER commit without user confirmation
```

### Edge Case 3: Special Characters in Content

```yaml
SCENARIO: Content has emoji, math symbols, non-ASCII
DECISION:
  - UTF-8 allows these: PERMIT
  - Validate UTF-8 encoding: MUST be valid
  - Document in commit message if unusual
```

### Edge Case 4: Duplicate Filenames in Different Categories

```yaml
SCENARIO: plaintext/intro.txt and callouts/intro.txt
DECISION:
  - PERMIT (different categories, different purposes)
  - Full path is unique identifier
  - No conflict
```

### Edge Case 5: Removing Last File in Category

```yaml
SCENARIO: Deleting only file in faqs/ leaving empty directory
DECISION:
  - PERMIT (empty directory is harmless)
  - Document in CHANGELOG
  - Consider if category is deprecated
```

---

## PRIORITY MATRIX

### When Rules Conflict

```yaml
PRIORITY_ORDER:
  1. Security rules (no binaries, no scripts)
  2. Format rules (UTF-8, LF, .txt extension)
  3. Path stability rules (no rename without MAJOR)
  4. Validation rules (integrity, checksums)
  5. Style rules (naming conventions)
  6. Convention rules (commit messages)

RESOLUTION:
  Higher priority rule ALWAYS wins
  Example: Security > Style
    → Reject file even if name is perfect
```

---

## EXECUTION CHECKLIST (EVERY OPERATION)

```yaml
BEFORE_EXECUTION:
  - [ ] Read and understand user request
  - [ ] Identify affected categories
  - [ ] Check if operation is FORBIDDEN
  - [ ] Determine validation requirements
  - [ ] Plan commit strategy
  - [ ] Estimate version impact

DURING_EXECUTION:
  - [ ] Apply validation rules
  - [ ] Follow subtype-specific rules
  - [ ] Generate proper commit message
  - [ ] Update TodoWrite tool
  - [ ] Document actions taken

AFTER_EXECUTION:
  - [ ] Verify all validations passed
  - [ ] Confirm commit follows conventions
  - [ ] Check working tree status
  - [ ] Push to correct branch
  - [ ] Report completion to user
```

---

## REFERENCE QUICK LINKS

### Key Contract Sections
- Format rules: server-contract.md §3, §6
- Path stability: server-contract.md §5
- Versioning: server-contract.md §11
- Integrity: server-contract.md §10
- Security: server-contract.md §12

### Key Spec Sections
- MUST requirements: server-contract.spec (all)
- Validation gates: server-contract.spec §9
- Conformance: server-contract.spec §10

### Key Schema Sections
- Examples: contract.schema (Exempla I-XI)
- Structure: contract.schema (Structura)
- Workflow: contract.schema (Gradus Operis)

---

## VERSION HISTORY

- v1.0.0 (2025-11-12): Initial AI agent operational rules

---

**END OF CLAUDE.md - NORMATIVE FOR AI AGENT OPERATION**
