# Skin Predictor Constitution

## Purpose

Skin Predictor is a privacy-first Python application that analyzes facial skin images locally and produces practical skincare recommendations and reports. The repository must remain easy to audit, safe to run, and suitable for healthcare-adjacent portfolio demonstration.

## Product Principles

1. Local-first processing is required for image analysis unless a future specification explicitly introduces an external service with user consent.
2. User-facing changes must preserve privacy, accessibility, and clear language.
3. AI output must be framed as informational support, not as medical diagnosis.
4. Existing application behavior must not be removed to satisfy compliance tooling.

## Engineering Principles

1. Changes must be small, reviewable, and covered by the appropriate quality checks.
2. Configuration belongs in standard project files such as `pyproject.toml`, `.gitlab-ci.yml`, and tool-specific config files.
3. CI must run linting, formatting checks, type checks, tests, security scanning, dependency auditing, and coverage reporting.
4. Secrets must never be committed. Use `.env.example` for documented configuration names only.

## Quality Gates

Every merge request should pass:

- Ruff linting
- Ruff formatting check
- Mypy type checking
- Pylint static analysis
- Vulture dead-code scan
- Bandit security scan
- Semgrep security scan
- Gitleaks secret scan
- pip-audit dependency audit
- pytest test suite
- pytest coverage XML generation

## Specification Workflow

New features should start as a document under `specs/`. Each specification should describe the user problem, acceptance criteria, non-goals, privacy impact, test plan, and rollout notes before implementation begins.
