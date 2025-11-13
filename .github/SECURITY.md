# Security Policy

## Project Security Context

This repository is a **text-only content repository** for ethical accounting guidelines. While the content itself is public and not security-sensitive, the infrastructure (validation scripts, CI/CD workflows, and Python dependencies) could introduce security vulnerabilities.

## Supported Versions

We actively maintain the following versions with security updates:

| Version | Supported          | Status                          |
| ------- | ------------------ | ------------------------------- |
| 1.2.x   | :white_check_mark: | Current stable                  |
| 1.1.x   | :white_check_mark: | Security fixes only             |
| 1.0.x   | :x:                | No longer supported             |
| < 1.0   | :x:                | Deprecated                      |

## Security Scope

### In Scope

Security issues in the following components are in scope:

- **Python validation scripts** (`.claude/hooks/*.py`, `.claude/models/*.py`)
- **Shell scripts** (`.claude/hooks/*.sh`)
- **GitHub Actions workflows** (`.github/workflows/*.yml`)
- **Python dependencies** (`requirements.txt`)
- **Pre-commit hooks** (`.pre-commit-config.yaml`)

Examples of security issues we care about:
- Code injection vulnerabilities in validation scripts
- Path traversal issues in file handling
- Malicious package dependencies
- Workflow permission escalation
- Secret exposure in logs or artifacts

### Out of Scope

The following are **not** security issues:

- Content typos or factual errors (use GitHub Issues)
- Documentation improvements (use Pull Requests)
- Feature requests (use GitHub Discussions)
- Performance issues (unless DoS-related)

## Reporting a Vulnerability

### Private Disclosure (Preferred)

For security vulnerabilities, please use **GitHub Private Vulnerability Reporting**:

1. Go to: https://github.com/focofacofoco/ceocont-etica-public-resources/security/advisories/new
2. Fill out the advisory form with:
   - Affected component (script/workflow/dependency)
   - Vulnerability description
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if known)

**Response time**: We aim to acknowledge within **48 hours** and provide an initial assessment within **7 days**.

### Public Disclosure

For low-severity issues or if private reporting is unavailable:

- **Email**: [Create a placeholder email or remove this section]
- **GitHub Issue**: Only for non-sensitive security improvements

⚠️ **Do not** publicly disclose high-severity vulnerabilities before coordinated disclosure.

## Security Update Process

When a security vulnerability is confirmed:

1. **Triage** (24-48 hours)
   - Assess severity (Critical, High, Medium, Low)
   - Determine affected versions
   - Assign CVE if applicable

2. **Fix Development** (depends on severity)
   - Critical: 24-48 hours
   - High: 1 week
   - Medium: 2 weeks
   - Low: Next release cycle

3. **Testing & Validation**
   - Fix validated in isolated environment
   - Pre-commit hooks and CI/CD tests pass
   - No regressions introduced

4. **Coordinated Disclosure**
   - Security advisory published on GitHub
   - CHANGELOG.txt updated with security note
   - New version released (PATCH for security fixes)
   - Dependabot/users notified if dependency-related

5. **Public Disclosure**
   - After fix is released and users have time to update
   - Typically 7-14 days after release
   - Full details published in security advisory

## Security Best Practices

### For Contributors

When submitting code to this repository:

- ✅ **Validate inputs**: All file paths, filenames, and content must be validated
- ✅ **Avoid shell injection**: Use Python `subprocess` with `args` list, not shell strings
- ✅ **No hardcoded secrets**: Use environment variables or GitHub Secrets
- ✅ **Minimal permissions**: Workflows should request only necessary permissions
- ✅ **Pin dependency versions**: Use exact versions or `>=X.Y.Z` with upper bounds

### For Users

When consuming content from this repository:

- ✅ **Verify checksums**: Use `meta/integrity.txt` to verify content integrity
- ✅ **Pin release tags**: Reference specific versions (e.g., `v1.2.0`) not `main`
- ✅ **Monitor advisories**: Subscribe to repository security advisories
- ✅ **Update regularly**: Apply security patches within 30 days

## Dependency Security

### Automated Monitoring

We use:
- **Dependabot**: Automatic dependency updates (weekly)
- **Dependency Review**: PR-based vulnerability scanning
- **CodeQL**: Static analysis for Python code
- **GitHub Advisory Database**: CVE monitoring

### Manual Audits

We perform manual dependency audits:
- **Quarterly**: Review all dependencies for known issues
- **Before major releases**: Comprehensive security review
- **On-demand**: When high-severity CVE is disclosed

## Security Hall of Fame

We recognize security researchers who responsibly disclose vulnerabilities:

<!-- Contributors will be listed here after coordinated disclosure -->

*No security issues have been reported yet.*

---

## Questions?

For security questions that don't involve active vulnerabilities:
- Open a [GitHub Discussion](https://github.com/focofacofoco/ceocont-etica-public-resources/discussions)
- Tag with `security` label

**Last Updated**: 2025-11-13
**Policy Version**: 1.0
