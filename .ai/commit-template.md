# Conventional Commits Template for AI Agents

**DIRECTIVE**: This template is FOR AI AGENTS ONLY. Follow this specification exactly when creating commits.

## Core Structure

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Type Selection (MANDATORY)

**INSTRUCTION**: Choose ONE type from this list. Use lowercase only.

- `feat`: New feature for the user (triggers MINOR version bump in SemVer)
- `fix`: Bug fix for the user (triggers PATCH version bump in SemVer)
- `docs`: Documentation changes only (no code changes)
- `style`: Code style changes (formatting, white-space, no logic changes)
- `refactor`: Code refactoring (no feature addition, no bug fixes)
- `perf`: Performance improvements
- `test`: Adding or modifying tests
- `build`: Build system or external dependency changes
- `ci`: CI/CD configuration changes
- `chore`: Other changes that don't modify src or test files
- `revert`: Reverting a previous commit

## Scope (OPTIONAL)

**INSTRUCTION**: Add scope in parentheses after type to specify what part of codebase is affected.

**EXAMPLES**:
- `feat(api): add user authentication endpoint`
- `fix(parser): handle null values correctly`
- `docs(readme): update installation instructions`

## Description (MANDATORY)

**RULES**:
1. Use imperative mood: "add" not "added" or "adds"
2. Don't capitalize first letter
3. No period (.) at the end
4. Maximum 72 characters
5. Be specific and clear

**CORRECT EXAMPLES**:
- `add user authentication endpoint`
- `fix null pointer exception in parser`
- `update installation documentation`

**INCORRECT EXAMPLES** (DO NOT USE):
- `Added user authentication endpoint` (wrong tense)
- `Fix null pointer exception in parser.` (capitalized + period)
- `updates` (wrong tense)

## Body (OPTIONAL BUT RECOMMENDED)

**INSTRUCTION**: Use body to explain WHAT and WHY, not HOW.

**FORMAT**:
- Separate from description with ONE blank line
- Wrap at 72 characters
- Use bullet points with `-` for multiple items
- Be specific about the problem being solved

**EXAMPLE**:
```
feat(auth): add JWT token validation

- Implement token expiration check
- Add signature verification
- Support token refresh mechanism

This prevents unauthorized access and improves security.
```

## Footer (OPTIONAL)

**INSTRUCTION**: Use footer for breaking changes and issue references.

### Breaking Changes (CRITICAL)

**RULE**: ALWAYS mark breaking changes with `BREAKING CHANGE:` footer OR `!` after type/scope.

**EXAMPLES**:
```
feat(api)!: change authentication response format

BREAKING CHANGE: API now returns `access_token` instead of `token`
```

OR

```
feat!: drop support for Node 14
```

### Issue References

**FORMAT**: `Closes #123` or `Fixes #456` or `Refs #789`

**EXAMPLE**:
```
fix(parser): handle edge case in date parsing

Closes #234
```

## Complete Examples (COPY THESE PATTERNS)

### Example 1: Simple Feature
```
feat: add user profile endpoint
```

### Example 2: Bug Fix with Scope
```
fix(api): handle timeout in external service calls
```

### Example 3: Feature with Body
```
feat(auth): implement OAuth2 authentication

- Add Google OAuth2 provider
- Implement token exchange flow
- Store refresh tokens securely

This enables users to sign in with their Google accounts.
```

### Example 4: Breaking Change
```
feat(api)!: restructure user response format

BREAKING CHANGE: User API now returns nested `profile` object instead of flat structure.
Migration guide: Update client code to access `user.profile.name` instead of `user.name`.

Closes #145
```

### Example 5: Documentation
```
docs(readme): add API authentication section
```

### Example 6: Refactoring
```
refactor(database): extract query builder into separate module
```

## Decision Tree for AI Agents

**EXECUTE THIS LOGIC WHEN CREATING COMMITS**:

1. **Does this change add new functionality?**
   - YES → Use `feat`
   - NO → Continue to 2

2. **Does this change fix a bug?**
   - YES → Use `fix`
   - NO → Continue to 3

3. **Does this change only affect documentation?**
   - YES → Use `docs`
   - NO → Continue to 4

4. **Does this change restructure code without changing behavior?**
   - YES → Use `refactor`
   - NO → Continue to 5

5. **Does this change improve performance?**
   - YES → Use `perf`
   - NO → Continue to 6

6. **Does this change affect tests only?**
   - YES → Use `test`
   - NO → Continue to 7

7. **Does this change affect build/dependencies?**
   - YES → Use `build`
   - NO → Use `chore`

8. **Does this break backward compatibility?**
   - YES → Add `!` after type/scope AND add `BREAKING CHANGE:` footer
   - NO → Proceed without breaking change markers

## Validation Checklist (RUN BEFORE COMMIT)

**AI AGENT: Execute this checklist before finalizing commit message**:

- [ ] Type is lowercase and from the approved list
- [ ] Description uses imperative mood (add, fix, update, not added, fixed, updated)
- [ ] Description is lowercase (first letter)
- [ ] Description has no period at end
- [ ] Description is under 72 characters
- [ ] If body exists, it's separated by blank line
- [ ] Breaking changes are marked with `!` AND/OR `BREAKING CHANGE:` footer
- [ ] Body explains WHY, not HOW
- [ ] Issue references use correct format (Closes #X, Fixes #X, Refs #X)

## Anti-Patterns (NEVER DO THIS)

❌ `Updated documentation` - Wrong tense, capitalized
❌ `feat: Added new feature.` - Wrong tense, has period
❌ `Fix bug` - Capitalized
❌ `feature: add user auth` - Wrong type (use `feat` not `feature`)
❌ `feat add user auth` - Missing colon
❌ Breaking change without `!` or `BREAKING CHANGE:` footer

## Command Template for Git

**AI AGENT: Use this exact pattern when executing git commit**:

```bash
git commit -m "$(cat <<'EOF'
<type>[scope]: <description>

[body with explanations]

[footers]
EOF
)"
```

## Final Directive

**AI AGENT**: When in doubt, prefer:
1. **feat** for new capabilities
2. **fix** for corrections
3. **docs** for documentation
4. **refactor** for code restructuring
5. Simple commits over complex ones
6. Clear descriptions over clever ones

**ALWAYS** validate against the checklist above before committing.
