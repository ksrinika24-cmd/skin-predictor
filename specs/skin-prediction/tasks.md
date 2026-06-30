# Skin Prediction Implementation Tasks

## Baseline Verification

- [x] Confirm the application is organized around Streamlit pages and reusable
  Python utility modules.
- [x] Confirm model assets and label metadata are stored under `models/`.
- [x] Confirm recommendation source data is stored locally.
- [x] Confirm runtime upload and report directories are represented with
  `.gitkeep` files.
- [x] Confirm the repository contains automated tests for core workflow modules.

## Application Workflow

- [x] Support local image upload through the Streamlit interface.
- [x] Preprocess uploaded images using the local image processing pipeline.
- [x] Run CPU-based ONNX inference for skin type prediction.
- [x] Map model output to supported skin categories.
- [x] Display recommendations based on local data.
- [x] Generate a downloadable PDF report.

## Quality Tasks

- [x] Maintain tests for preprocessing behavior.
- [x] Maintain tests for prediction behavior.
- [x] Maintain tests for recommendation behavior.
- [x] Maintain tests for PDF generation.
- [x] Maintain tests for local database or persistence utilities.
- [x] Keep code compatible with Python 3.11.

## Compliance Tasks

- [x] Provide repository health files.
- [x] Provide license and security policy files.
- [x] Provide GitLab CI configuration.
- [x] Provide pre-commit configuration.
- [x] Provide Spec-Kit repository structure.
- [x] Keep generated reports and uploaded user files out of Git history.

## Release Tasks

- [x] Ensure the release commit passes automated quality checks.
- [x] Ensure release documentation reflects offline operation and limitations.
- [x] Ensure the release tag points to the latest approved main-branch commit.
- [x] Ensure compliance checker inputs are present in the repository tree.
