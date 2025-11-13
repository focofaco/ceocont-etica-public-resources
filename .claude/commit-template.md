# CONVENTIONAL COMMITS TEMPLATE - AI AGENT ONLY

## META-TEMPLATE INSTRUCTIONS

**TARGET**: Claude AI Sonnet 4.5 autonomous commit generation
**PRIORITY**: Deterministic, machine-parseable, zero ambiguity
**CONSTRAINTS**: No bloat, no optional fluff, exact pattern matching

## MANDATORY STRUCTURE

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## TYPE TAXONOMY (EXHAUSTIVE)

```yaml
fix: # patches bug (PATCH in semver)
feat: # new functionality (MINOR in semver)
build: # build system/external deps (webpack, npm, etc)
chore: # maintenance, no production code change
ci: # CI config/scripts (GitHub Actions, etc)
docs: # documentation only
perf: # performance improvement
refactor: # neither fix nor feature
revert: # reverts previous commit
style: # formatting, no code logic change
test: # add/update tests
```

## BREAKING CHANGE MARKERS

- Append `!` after type/scope: `feat!:` or `feat(api)!:`
- OR include `BREAKING CHANGE:` footer
- TRIGGERS: Major version bump (MAJOR in semver)

## SCOPE RULES

- Optional but recommended
- Use parentheses: `feat(parser):`
- Lowercase, single word or hyphenated
- Examples: `api`, `auth`, `database`, `ui-button`

## DESCRIPTION RULES

- Imperative mood: "add" not "added" or "adds"
- Lowercase first letter
- No period at end
- Max 72 characters
- Complete the sentence: "This commit will..."

## BODY RULES (OPTIONAL)

- Blank line after description
- Explain WHAT and WHY, not HOW
- Wrap at 72 characters
- Multiple paragraphs allowed

## FOOTER RULES (OPTIONAL)

- Blank line before footer
- Format: `<token>: <value>` or `<token> #<issue>`
- Common tokens:
  - `BREAKING CHANGE:`
  - `Fixes:` or `Closes:`
  - `Refs:`
  - `Co-authored-by:`

## AI EXECUTION PATTERNS

### Pattern A: Simple commit

```
feat: add user authentication endpoint
```

### Pattern B: With scope

```
fix(parser): handle null values in JSON input
```

### Pattern C: Breaking change (method 1)

```
feat(api)!: restructure response format

BREAKING CHANGE: API now returns data in envelope structure
```

### Pattern D: Breaking change (method 2)

```
refactor!: drop support for Node 12

BREAKING CHANGE: minimum Node version is now 14.0.0
```

### Pattern E: With body

```
fix: prevent race condition in file uploads

Add mutex lock to ensure sequential file processing.
Previous implementation allowed concurrent writes causing corruption.
```

### Pattern F: With footer

```
feat: add PDF export functionality

Closes: #123
Refs: #456
```

### Pattern G: Full structure

```
feat(export)!: replace CSV with JSON format

Export API now returns JSON instead of CSV for better structure.
Includes nested data support and metadata fields.

BREAKING CHANGE: clients must update parsers from CSV to JSON
Closes: #789
Co-authored-by: Bot <bot@example.com>
```

## DECISION TREE FOR TYPE SELECTION

```
Does it fix a bug? → fix
Does it add functionality? → feat
Does it break compatibility? → append !
Is it only docs? → docs
Is it only formatting? → style
Is it refactoring? → refactor
Is it performance? → perf
Is it tests? → test
Is it CI/build? → ci or build
Is it maintenance? → chore
```

## VALIDATION CHECKLIST

- [ ] Type is from approved list
- [ ] Description is imperative, lowercase, no period
- [ ] Scope is lowercase, hyphenated if needed
- [ ] Breaking changes have `!` OR footer
- [ ] Body separated by blank line (if present)
- [ ] Footer separated by blank line (if present)
- [ ] Commit message is ASCII-safe

## ANTI-PATTERNS (FORBIDDEN)

```
❌ Added feature X                    # Past tense
❌ Fix: bug in parser                 # Capital F
❌ feat: Add user login.              # Capital A, period
❌ feature: new export                # Invalid type
❌ fix (parser): handle null          # Space before scope
❌ feat:add export                    # No space after colon
❌ fix: fixes the bug                 # Redundant "fixes"
```

## CORRECT PATTERNS (REQUIRED)

```
✓ feat: add user login
✓ fix(parser): handle null values
✓ docs: update API documentation
✓ feat!: change authentication method
✓ refactor(core): simplify error handling
```

## SEMVER MAPPING

```
fix:     → 0.0.x (PATCH)
feat:    → 0.x.0 (MINOR)
*!: or BREAKING CHANGE → x.0.0 (MAJOR)
```

## COMMIT GENERATION ALGORITHM

```python
def generate_commit(changes_analyzed):
    # 1. Determine type from decision tree
    type = classify_change_type(changes_analyzed)

    # 2. Extract scope from files changed
    scope = extract_primary_scope(changes_analyzed.files)

    # 3. Check breaking change
    is_breaking = detect_breaking_change(changes_analyzed)

    # 4. Generate description (imperative, concise)
    description = summarize_change(changes_analyzed, max_length=72)

    # 5. Construct message
    message = f"{type}"
    if scope:
        message += f"({scope})"
    if is_breaking:
        message += "!"
    message += f": {description}"

    # 6. Add body if complex
    if changes_analyzed.complexity > threshold:
        message += f"\n\n{generate_body(changes_analyzed)}"

    # 7. Add footer if issues referenced
    if changes_analyzed.issues:
        message += f"\n\nCloses: {changes_analyzed.issues}"

    return message
```

## PRIORITY EXECUTION RULES

1. ALWAYS use imperative mood
2. ALWAYS lowercase description first letter
3. NEVER use period at end of description
4. ALWAYS include `!` for breaking changes
5. ALWAYS separate body/footer with blank lines
6. PREFER single-line commits when possible
7. USE body only when description insufficient
8. INCLUDE issue references in footer when applicable

---

**END OF TEMPLATE - VERSION 1.0.0**
