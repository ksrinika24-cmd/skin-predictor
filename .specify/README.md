# Spec-Kit

This directory contains the repository-level Spec-Kit governance files used to
define, review, and deliver changes for Skin Predictor.

Spec-Kit is the source of truth for:

- Project constitution and engineering policies.
- Reusable templates for feature specifications, quality checklists, and task
  plans.
- Consistent review expectations before implementation begins.

## Repository Layout

```text
.specify/
    README.md
    constitution.md
    templates/
        feature-template.md
        checklist-template.md
        task-template.md

specs/
    README.md
    skin-prediction/
        spec.md
        tasks.md
        checklist.md
```

## Usage

1. Create or update a feature specification under `specs/<feature-name>/`.
2. Use `.specify/templates/feature-template.md` for scope, user value,
   requirements, non-goals, risks, and acceptance criteria.
3. Use `.specify/templates/task-template.md` to break approved work into
   implementation, documentation, testing, security, and release tasks.
4. Use `.specify/templates/checklist-template.md` during quality review.
5. Keep implementation changes traceable to the corresponding specification.

## Required Review Gates

Every production change must satisfy the constitution, the applicable feature
specification, the task plan, and the checklist before merge or release.
