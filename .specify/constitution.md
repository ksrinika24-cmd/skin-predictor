# Skin Predictor Engineering Constitution

## Purpose

Skin Predictor is a privacy-first Python application for local skin type prediction, skincare guidance, and report generation. This constitution defines the repository standards required to keep the project maintainable, secure, testable, and suitable for production-style review.

## Coding Standards

- Python code must be compatible with Python 3.11.
- Application behavior must remain local-first; uploaded or captured images must not be sent to external services unless a future specification explicitly approves that change.
- Source code should be readable, modular, and consistent with the existing package layout.
- Formatting must be enforced with Ruff Format.
- Linting must be enforced with Ruff, Flake8, Pylint, Vulture, Pyupgrade, and Bandit.
- Type checking must be enforced with Mypy.
- Configuration should be centralized in standard project files such as `pyproject.toml`, `.pre-commit-config.yaml`, and `.gitlab-ci.yml`.
- Application functionality must not be removed or weakened to satisfy tooling.

## Testing Policy

- Automated tests must be written for prediction helpers, preprocessing, recommendation logic, PDF/report generation, and any new user-facing workflow.
- The test suite must run with `pytest`.
- Coverage reporting must generate `coverage.xml` using `pytest-cov`.
- Tests should avoid network dependencies and should not require real secrets.
- Regression tests should be added for bug fixes whenever practical.
- CI must fail when tests fail.

## Documentation Policy

- User-facing behavior must be documented in `README.md` or `USER_MANUAL.md`.
- Contributor workflows must remain documented in `CONTRIBUTING.md` and `AGENTS.md`.
- Security reporting must remain documented in `SECURITY.md`.
- Notable changes must be recorded in `CHANGELOG.md` or generated through the configured Git-Cliff workflow.
- New features must include a specification under `specs/` before implementation.
- Specifications must describe goals, user stories, functional requirements, non-functional requirements, acceptance criteria, test scenarios, risks, dependencies, and future improvements.

## Security Policy

- Secrets, tokens, credentials, private keys, and production configuration values must never be committed.
- `.env.example` may contain variable names and safe placeholder values only.
- Secret scanning must run with Gitleaks.
- Dependency auditing must run with `pip-audit`.
- Static security analysis must run with Bandit and Semgrep.
- Any dependency with a known vulnerability must be reviewed and upgraded, pinned, or documented with a temporary exception.
- Generated reports and uploaded images should be treated as sensitive user data and should not be committed.

## CI Requirements

- GitLab CI must include the following stages: `lint`, `format`, `type_check`, `test`, and `coverage`.
- CI jobs must install project dependencies before executing checks.
- The lint stage must run Ruff and include security and dependency audit jobs.
- The format stage must run `ruff format --check .`.
- The type check stage must run `mypy .`.
- The test stage must run `pytest`.
- The coverage stage must run `pytest --cov=. --cov-report=xml --cov-report=term` and publish `coverage.xml`.
- CI configuration must be deterministic and suitable for a clean GitLab runner.

## Review Policy

- Merge requests should be small enough to review safely.
- Reviewers should verify that application behavior, privacy guarantees, and documentation remain consistent.
- Changes that affect prediction, reporting, recommendations, security, or CI must include a clear explanation and validation evidence.
- New dependencies must be justified and must pass dependency audit.
- A release tag should point to the latest production-ready commit before release.
