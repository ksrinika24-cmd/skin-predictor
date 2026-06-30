# Skin Predictor Project Constitution

## Project Vision

Skin Predictor provides an offline, privacy-conscious skin analysis and skincare
recommendation workflow for local users. The project must remain easy to run,
safe to maintain, and transparent about its limitations: it provides cosmetic
guidance, not medical diagnosis.

## Coding Standards

- Target Python 3.11 and keep configuration centralized in `pyproject.toml`,
  `.pre-commit-config.yaml`, and `.gitlab-ci.yml`.
- Preserve the existing Streamlit application behavior unless a reviewed
  specification explicitly changes it.
- Keep reusable logic in Python modules and keep page code focused on
  presentation and orchestration.
- Use clear names, small functions, and explicit data flow.
- Pass the configured quality tools: Ruff, Black, Flake8, Pylint, Mypy, Bandit,
  Semgrep, Vulture, Pyupgrade, pytest, coverage, and pre-commit.
- Do not weaken application functionality to satisfy tooling.

## Documentation Standards

- User-facing behavior belongs in `README.md`, `USER_MANUAL.md`, or `docs/`.
- Architecture, model, data, recommendation, and report changes must update the
  relevant documentation before release.
- Security reporting expectations must remain documented in `SECURITY.md`.
- Changelog entries must be maintained through the repository changelog process.
- Specifications under `specs/` must describe goals, non-goals, requirements,
  risks, dependencies, acceptance criteria, and verification evidence.

## Testing Requirements

- New or changed behavior must include focused tests under `tests/`.
- The test suite must run with `pytest` and preserve the configured coverage
  threshold.
- Tests must avoid network dependencies and must not require real secrets.
- Regression tests are required for fixes affecting prediction, preprocessing,
  recommendations, PDF generation, persistence, security, or user data handling.
- Manual checks must be documented when UI behavior cannot be fully automated.

## Security Requirements

- Core operation must not require cloud APIs, external uploads, or secrets.
- User uploads, generated reports, local databases, and runtime files are
  sensitive local artifacts and must not be committed.
- Validate user-controlled files before processing them.
- Keep generated files inside intended local directories.
- Secret scanning, dependency audit, Bandit, Semgrep, and CI security checks
  must pass before merge or release.
- Vulnerabilities must be reported and handled according to `SECURITY.md`.

## AI Development Guidelines

- AI assistance may be used for implementation, review, tests, documentation,
  and compliance work, but maintainers remain accountable for correctness.
- AI-generated changes must be reviewed like human-written changes.
- Do not introduce unsupported medical claims, hidden network calls, or model
  behavior changes without an approved specification.
- Preserve privacy expectations: no user images, reports, secrets, or local
  runtime data may be sent to external AI services from the application.
- Validate generated code with the same tooling, tests, and review gates as all
  other code.

## Git Workflow

- Work from `main` or a short-lived feature branch created from the latest
  `main`.
- Keep commits focused and reviewable.
- Stage only intended files.
- Do not rewrite shared history unless maintainers explicitly approve it.
- Preserve existing files and application behavior during compliance-only work.

## Commit Message Convention

- Use concise imperative commit messages, such as `Add Spec-Kit templates`.
- Prefer one logical change per commit.
- Reference issues or specifications when available.
- Avoid vague messages such as `fix`, `updates`, or `misc`.

## Code Review Rules

- Every non-trivial change must be traceable to a specification, issue, or
  documented maintenance objective.
- Reviewers must check behavior, privacy impact, test coverage, documentation,
  dependency changes, and CI results.
- Security-sensitive changes require explicit review of inputs, file handling,
  secrets, logs, and generated artifacts.
- Review comments must be resolved or documented as follow-up work before merge.

## Branch Strategy

- `main` is the protected release branch.
- Feature branches should use descriptive names such as
  `feature/spec-kit-templates` or `fix/report-validation`.
- Release tags must point to commits on `main`.
- Hotfixes should branch from `main`, pass CI, and merge back through the normal
  review process.

## Release Process

- Release only from a clean, reviewed, passing `main` commit.
- Confirm CI, tests, coverage, security scans, dependency audit, and compliance
  checks pass.
- Update release notes or changelog entries.
- Create an annotated release tag when no suitable release tag exists.
- Push the release tag to GitLab after the release commit is accepted.

## Definition of Done

- The approved specification and implementation plan are satisfied.
- Code, tests, documentation, and compliance files are updated as required.
- Automated checks pass locally or in GitLab CI.
- Security and privacy expectations are preserved.
- The change is reviewed and traceable.
- Release notes or changelog entries are ready when the change is user-visible.
