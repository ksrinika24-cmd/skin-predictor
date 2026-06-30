# Skin Predictor Constitution

## Purpose

Skin Predictor is an offline AI-powered skin analysis and product
recommendation application. The repository must remain reliable, secure,
auditable, and understandable for contributors while preserving the product's
offline-first user experience.

## Project Principles

- Offline first: Core skin analysis, recommendations, and report generation
  must work without cloud services or external APIs.
- Privacy by design: User images and generated reports must stay local unless a
  future specification explicitly defines an opt-in export path.
- Explainable user outcomes: Predictions, recommendations, and generated
  reports must be presented clearly enough for a non-technical user to
  understand the result.
- Maintainable simplicity: Prefer clear Python modules, small functions, and
  explicit data flow over unnecessary abstraction.
- Reproducible quality: Changes must be verifiable with automated checks and
  documented review evidence.

## Coding Standards

- Python code must target Python 3.11 and follow the repository configuration in
  `pyproject.toml`.
- Code must pass the configured formatting, linting, typing, security, and
  dead-code checks, including Ruff, Flake8, Pylint, Mypy, Bandit, Vulture,
  Semgrep, Pyupgrade, and pre-commit.
- Application logic must be isolated in reusable modules when practical, with
  Streamlit page code focused on presentation and orchestration.
- Public functions and non-obvious behavior must use clear names and concise
  documentation.
- Dependencies must be intentional, pinned or constrained through the approved
  dependency workflow, and compatible with offline execution.
- Application functionality must not be removed, weakened, or hidden to satisfy
  tooling.

## Testing Requirements

- New or changed behavior must include focused automated tests under `tests/`.
- Tests must cover image preprocessing, model loading, prediction boundaries,
  recommendation selection, PDF generation, and persistence behavior when those
  areas are changed.
- Regression tests are required for defects that affect prediction results,
  report output, security, or user data handling.
- Coverage must remain at or above the repository compliance threshold.
- Manual verification steps must be documented in the related specification or
  checklist when UI behavior cannot be fully automated.
- Tests must avoid network dependencies and must not require real secrets.

## Documentation Requirements

- User-facing behavior must be documented in `README.md` or `docs/` when it
  changes installation, usage, supported skin types, outputs, or limitations.
- Architecture-impacting changes must update `docs/Architecture.md`.
- Model, data, and recommendation changes must document source, format,
  expected inputs, and validation assumptions.
- Every feature spec must include goals, non-goals, functional requirements,
  acceptance criteria, risks, and release notes.
- Documentation must avoid unsupported medical claims and must distinguish
  cosmetic guidance from clinical diagnosis.
- Contributor and security workflows must remain documented in repository
  health files.

## Security Requirements

- The application must not require secrets for core offline operation.
- User uploads, reports, and local database files must be treated as sensitive
  local data.
- File handling must validate type, size, path, and expected content before
  processing.
- Generated files must not escape intended local directories.
- Secrets, tokens, credentials, private keys, and production configuration
  values must never be committed.
- Security checks, dependency audits, secret scanning, and static analysis must
  pass before merge.
- Vulnerabilities must be handled according to `SECURITY.md` and must not be
  disclosed publicly before maintainers complete triage.

## CI/CD Policy

- GitLab CI must remain the authoritative automated quality gate.
- The pipeline must run dependency installation, linting, formatting, typing,
  testing, security checks, dependency audits, coverage reporting, and
  compliance checks for merge requests and protected branches.
- Pipeline failures must be fixed before merge unless maintainers document an
  approved temporary exception.
- CI configuration changes require review from a maintainer familiar with the
  affected toolchain.
- Release artifacts and tags must be produced from passing commits on the main
  branch.
- CI configuration must be deterministic and suitable for a clean GitLab runner.

## Review Policy

- Every non-trivial change must be traceable to a spec, issue, or documented
  maintenance objective.
- Reviewers must check correctness, user impact, privacy impact, test coverage,
  documentation, dependency changes, and operational risk.
- Application logic changes require evidence that existing behavior remains
  compatible unless the specification explicitly approves the change.
- Review comments must be resolved before merge or explicitly acknowledged with
  a documented follow-up.
- Compliance-only changes must avoid modifying product behavior.
- New dependencies must be justified and must pass dependency audit.

## Release Policy

- Releases must be cut from the main branch after a passing CI pipeline.
- Release notes must summarize user-visible changes, compatibility notes,
  security fixes, and known limitations.
- Version tags must point to the exact commit being released.
- The `v1.0.0` tag represents the current baseline release unless superseded by
  a newer approved version.
- Changelog updates must be generated or maintained according to the repository
  Git-Cliff workflow.
