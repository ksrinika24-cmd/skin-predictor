# Specifications

The `specs/` directory stores feature specifications and supporting planning
documents for Skin Predictor.

## Folder Purpose

Specifications capture intended behavior before implementation. They give
maintainers a stable reference for scope, requirements, testing, documentation,
security review, and release readiness.

## Naming Conventions

- Use lowercase directory names.
- Separate words with hyphens.
- Prefer product or workflow names, such as `skin-prediction`.
- Keep primary feature specifications in `spec.md` when using a feature
  subdirectory.
- Use supporting files such as `tasks.md`, `checklist.md`, or
  `implementation-plan.md` when the feature requires them.

## Feature Spec Lifecycle

1. Draft: The idea is being shaped and requirements are incomplete.
2. Review: Maintainers are checking scope, risks, dependencies, and acceptance
   criteria.
3. Accepted: The specification is ready for implementation.
4. Implemented: Code, tests, documentation, and verification are complete.
5. Released: The accepted implementation is included in a tagged release.
6. Superseded: A newer specification replaces the old behavior or design.

## Directory Organization

```text
specs/
    README.md
    feature-name/
        spec.md
        implementation-plan.md
        tasks.md
        checklist.md
```

Existing specifications should be preserved. New specifications should be added
without deleting historical context unless maintainers explicitly approve the
cleanup.
