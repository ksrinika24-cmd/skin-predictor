# Spec-Kit

Spec-Kit is the repository workflow for turning ideas into reviewed,
implemented, tested, and released changes. It keeps product intent,
engineering decisions, verification steps, and release readiness visible before
code changes are merged.

## Repository Workflow

1. Start with a feature specification in `specs/`.
2. Review the problem, scope, acceptance criteria, risks, and dependencies.
3. Create an implementation plan from `.specify/templates/implementation-plan.md`.
4. Break the plan into tasks using `.specify/templates/task-list.md`.
5. Implement the change with tests, documentation, and security checks.
6. Open a merge request using `.specify/templates/pull-request.md`.
7. Release only after CI and compliance checks pass.

## Writing a Feature Specification

Use `.specify/templates/feature-spec.md` for new capabilities or meaningful
behavior changes. A good specification explains the problem, goals, non-goals,
functional requirements, non-functional requirements, acceptance criteria,
risks, and dependencies.

Specifications should be precise enough that reviewers can determine whether
the implementation is complete without guessing.

## Implementation Plans

Implementation plans describe how an approved specification will be delivered.
They identify architecture, components, database changes, API changes, UI
changes, testing strategy, and rollback steps.

Implementation plans are required when a change affects application behavior,
data flow, security posture, user experience, deployment, or release risk.

## Task Lists

Task lists convert an implementation plan into actionable checklist items.
They should include implementation, tests, documentation, security review,
CI validation, and release readiness work.

Task lists are living documents: update them as work is completed or as review
uncovers new required tasks.

## Example Workflow

```text
specs/skin-prediction/spec.md
    -> implementation plan
    -> task list
    -> code and tests
    -> pull request
    -> CI and compliance validation
    -> release tag
```

Spec-Kit does not replace code review or CI. It makes them easier to perform
consistently.
