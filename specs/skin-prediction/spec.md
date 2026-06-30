# Skin Prediction Feature Specification

## Status

- State: Accepted
- Owner: Skin Predictor maintainers
- Release Baseline: v1.0.0
- Scope: Existing offline skin prediction workflow

## Summary

Skin Predictor allows a user to upload a facial image, run local CPU-based AI
inference, receive a predicted cosmetic skin type, view skincare
recommendations, and generate a PDF report. The workflow is designed for
privacy-conscious and low-connectivity environments because it does not require
cloud APIs or internet access.

## Goals

- Provide an offline skin type prediction workflow for common cosmetic skin
  categories.
- Recommend skincare guidance and product categories based on the predicted
  skin type.
- Generate a user-readable PDF report for local download.
- Preserve user privacy by processing uploaded images locally.
- Maintain a testable and auditable Python implementation.

## Non-Goals

- The application does not provide medical diagnosis.
- The application does not replace advice from a licensed dermatologist.
- The application does not upload user images to external services.
- The application does not require GPU acceleration.
- The application does not personalize recommendations using remote user
  profiles or cloud analytics.

## Users and Use Cases

- A local user uploads a facial image and receives a skin type prediction.
- A local user reviews recommended skincare routines and product suggestions.
- A local user downloads a PDF report for personal reference.
- A maintainer validates the offline model, recommendation, and reporting
  workflow through tests and documentation.

## Functional Requirements

1. The application must accept supported local image uploads through the
   Streamlit interface.
2. The preprocessing pipeline must convert uploaded images into the shape and
   format expected by the ONNX model.
3. The prediction pipeline must run with ONNX Runtime on CPU.
4. The prediction result must map to supported skin categories: oily, dry,
   combination, sensitive, and normal.
5. Recommendation output must be selected from repository-managed local data.
6. The report workflow must generate a PDF containing the prediction and related
   recommendation details.
7. The workflow must provide clear feedback for invalid or unsupported input.
8. The core workflow must run without external network calls.

## Data Requirements

- Model assets must live under `models/` and include enough metadata to explain
  supported labels and expected inputs.
- Recommendation data must live under `data/` or the approved recommendations
  package.
- Uploaded images are local user-provided files and must not be committed.
- Generated reports are local artifacts and must not be committed.
- Runtime directories must keep `.gitkeep` files so Git tracks their intended
  structure without storing user artifacts.

## Security and Privacy Requirements

- The feature must not require secrets for normal operation.
- User uploads must be processed as untrusted input.
- File paths must remain inside intended local application directories.
- Logs and reports must not expose unrelated local file system details.
- Dependency, static analysis, and secret scanning checks must pass before
  release.

## Accessibility and UX Requirements

- Output language must be understandable to non-technical users.
- The interface must clearly distinguish cosmetic guidance from medical advice.
- Error states must explain what the user can do next.
- PDF reports must be readable without requiring access to the running app.

## Testing Requirements

- Preprocessing tests must verify image handling and expected model input shape.
- Predictor tests must verify model interaction, label mapping, and failure
  handling.
- Recommendation tests must verify deterministic selection for supported skin
  types.
- PDF tests must verify report generation without external services.
- Database or persistence tests must verify local state behavior where used.

## Documentation Requirements

- `README.md` must describe installation, offline operation, supported skin
  types, and primary workflow.
- `docs/Architecture.md` must describe Streamlit, preprocessing, ONNX Runtime,
  recommendation, and PDF components.
- `docs/UserGuide.md` must explain user workflow and limitations.
- Security expectations must remain documented in `SECURITY.md`.

## Acceptance Criteria

- A supported image can be uploaded and processed locally.
- A supported skin type prediction is produced through CPU inference.
- Recommendations are generated from local repository data.
- A PDF report can be generated locally.
- Invalid input is handled without crashing the application.
- No cloud API, external upload, or secret is required.
- Automated checks for tests, coverage, linting, typing, security, and
  compliance pass.

## Risks and Mitigations

- Risk: Users may treat cosmetic predictions as medical conclusions.
  Mitigation: Documentation and UI language must avoid diagnostic claims.
- Risk: Uploaded images may contain sensitive personal data.
  Mitigation: Keep processing local and exclude runtime upload directories from
  version control.
- Risk: Model or label changes may break recommendation mapping.
  Mitigation: Require tests and metadata updates for any model or label change.
- Risk: PDF output may drift from the app result.
  Mitigation: Test report generation and keep prediction data passed explicitly.

## Release Notes

Skin Predictor provides an offline workflow for local image-based cosmetic skin
type prediction, skincare recommendations, and PDF report generation using
Python, Streamlit, OpenCV, ONNX Runtime, and local repository data.
