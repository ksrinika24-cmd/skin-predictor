# Skin Prediction Acceptance Checklist

## Functional Acceptance

- [x] Users can open the Streamlit application locally.
- [x] Users can upload a supported facial image.
- [x] Uploaded images are preprocessed before prediction.
- [x] Prediction uses the local ONNX model with CPU runtime.
- [x] Prediction output maps to a supported skin type.
- [x] Recommendations are generated from local project data.
- [x] Users can generate a local PDF report.
- [x] The workflow does not require cloud APIs or internet connectivity.

## Quality Acceptance

- [x] Core workflow behavior is covered by automated tests.
- [x] Linting and formatting checks are configured.
- [x] Typing checks are configured.
- [x] Security checks are configured.
- [x] Coverage checks are part of repository compliance.
- [x] Runtime artifacts are excluded from version control.

## Security and Privacy Acceptance

- [x] No application secret is required for offline operation.
- [x] User uploads are treated as local runtime artifacts.
- [x] Generated reports are treated as local runtime artifacts.
- [x] Secret scanning must pass before release.
- [x] Dependency audit must pass before release.
- [x] Static security analysis must pass before release.

## Documentation Acceptance

- [x] README documents the purpose, setup, workflow, and supported skin types.
- [x] Architecture documentation describes the offline system design.
- [x] User documentation explains how to operate the application.
- [x] Security reporting expectations are documented.
- [x] Spec-Kit documentation captures project governance and release readiness.

## Release Acceptance

- [x] GitLab CI configuration is present.
- [x] Pre-commit configuration is present.
- [x] Git-Cliff changelog workflow is represented by repository compliance.
- [x] The `v1.0.0` release tag must point to the newest compliance commit.
- [x] `git ls-tree -r HEAD` must include all Spec-Kit files.
