# QA Checklist Template

## Checklist Identity

- Feature name:
- Reviewer:
- Review date:
- Release target:

## Specification Review

- [ ] Goals and non-goals are documented.
- [ ] Functional requirements are testable.
- [ ] Acceptance criteria are complete.
- [ ] Security and privacy expectations are documented.
- [ ] Documentation requirements are identified.

## Implementation Review

- [ ] Implementation matches the approved specification.
- [ ] Existing application behavior is preserved unless explicitly changed.
- [ ] Code follows repository style and quality standards.
- [ ] Dependencies are necessary and approved.
- [ ] Error handling is clear and user appropriate.

## Testing Review

- [ ] Unit tests cover new or changed logic.
- [ ] Regression tests cover fixed defects.
- [ ] Edge cases and invalid inputs are tested.
- [ ] Coverage remains within the required threshold.
- [ ] Manual UI checks are documented when applicable.

## Security Review

- [ ] User-controlled files are validated before processing.
- [ ] Sensitive local data is not exposed in logs or reports unexpectedly.
- [ ] No secrets are committed.
- [ ] Static analysis and dependency audit pass.
- [ ] Offline operation is preserved.

## Documentation Review

- [ ] README or user documentation reflects user-visible changes.
- [ ] Architecture documentation reflects system changes.
- [ ] Limitations and assumptions are documented.
- [ ] Release notes are ready.

## Release Readiness

- [ ] GitLab CI passes on the release commit.
- [ ] Pre-commit checks pass.
- [ ] Compliance checks pass.
- [ ] Version tag points to the intended commit.
- [ ] Maintainer approval is recorded.
