# Implementation Tasks Template

## Task Plan Identity

- Feature name:
- Owner:
- Target release:
- Related specification:

## Planning

- [ ] Confirm the approved feature specification.
- [ ] Identify affected modules, tests, documentation, and CI checks.
- [ ] Confirm compatibility with offline operation.
- [ ] Identify security and privacy review needs.

## Implementation

- [ ] Update application modules within the approved scope.
- [ ] Keep UI orchestration separate from reusable business logic.
- [ ] Validate all user-controlled inputs.
- [ ] Preserve existing behavior outside the feature scope.
- [ ] Update data files or model metadata only when required by the spec.

## Testing

- [ ] Add or update unit tests.
- [ ] Add regression tests for bug fixes.
- [ ] Run the repository test suite.
- [ ] Run formatting, linting, typing, and security checks.
- [ ] Document manual UI verification when automated coverage is insufficient.

## Documentation

- [ ] Update README or user guide content.
- [ ] Update architecture documentation if system structure changes.
- [ ] Update model, data, or recommendation documentation when relevant.
- [ ] Add release-note text.

## Review and Release

- [ ] Verify the implementation matches the specification.
- [ ] Verify the QA checklist is complete.
- [ ] Confirm GitLab CI passes.
- [ ] Stage only intended files.
- [ ] Commit with a clear message.
- [ ] Tag and release from the approved main-branch commit.
