# Skin Prediction Feature Specification

## Goal

Skin Predictor should allow a user to provide a facial image, run local skin type analysis, and receive a clear result with confidence, skin profile details, recommendations, and a downloadable report. The feature must preserve user privacy by keeping image processing inside the application environment.

## User Stories

- As a skincare user, I want to upload a facial image so that I can understand my likely skin type.
- As a privacy-conscious user, I want analysis to run locally so that my image is not sent to a cloud service.
- As a user, I want confidence and supporting details so that I can understand how reliable the result appears.
- As a user, I want skincare recommendations based on the detected skin type so that I can plan a practical routine.
- As a user, I want a PDF report so that I can save the analysis summary for personal reference or discussion with a dermatologist.

## Functional Requirements

- The application must accept PNG, JPG, and JPEG image inputs.
- The application must convert uploaded images into the preprocessing format required by the prediction pipeline.
- The prediction pipeline must return a skin type from the supported label set.
- The result view must display the detected skin type, confidence score, prediction identifier, model metadata, image resolution, and face detection status when available.
- The recommendations view must use the detected skin type to show morning, night, and weekly routine guidance.
- The recommendations view must show ingredient guidance, lifestyle advice, common concerns, and product suggestions.
- The report view must show a structured patient-style summary of the prediction result.
- The report view must provide a downloadable PDF generated locally in the application session.
- If no analysis has been completed, recommendation and report pages must ask the user to run skin analysis first.
- The feature must preserve existing Streamlit navigation and page behavior.

## Non-functional Requirements

- Image analysis must run locally and must not upload user images to external services.
- The feature must remain usable without internet access after dependencies and model files are available.
- The user interface should provide understandable labels, warnings, and status messages.
- The feature should handle invalid or unreadable image files safely without crashing the application.
- The prediction workflow should complete quickly enough for interactive use on a CPU-based environment.
- Generated reports must include an informational-use disclaimer and must not claim to provide medical diagnosis.
- CI must validate the feature through linting, formatting checks, type checks, tests, security scans, dependency audit, and coverage generation.

## Acceptance Criteria

- Given a supported image file, when the user starts analysis, then the application displays a detected skin type and confidence score.
- Given an image has been analyzed, when the user opens the recommendations page, then the page displays skin-type-specific routine and care guidance.
- Given an image has been analyzed, when the user opens the report page, then the page displays prediction details and offers a PDF download.
- Given no image has been analyzed, when the user opens recommendations or report, then the application displays a clear instruction to analyze skin first.
- Given an invalid image file, when processing fails, then the application shows a safe error message and does not expose a stack trace to the user.
- Given CI is run for the repository, when the pipeline reaches the coverage stage, then `coverage.xml` is generated.

## Test Scenarios

- Verify image preprocessing returns the expected model input shape and numeric format.
- Verify prediction helpers return a supported skin type and confidence value.
- Verify recommendation lookup returns routine, ingredient, lifestyle, and product data for every supported skin type.
- Verify report generation creates PDF bytes for a completed prediction.
- Verify pages that require an existing prediction stop safely when no prediction is available.
- Verify CI jobs execute Ruff, Ruff Format, Mypy, Bandit, Semgrep, Gitleaks, pip-audit, pytest, and coverage reporting.

## Future Improvements

- Add calibrated model confidence based on a larger validation dataset.
- Add optional progress tracking for changes in skin score over time.
- Add broader concern detection for acne, pigmentation, redness, and texture.
- Add dermatologist review mode with cleaner export formatting.
- Add expanded accessibility checks for multilingual UI output.
- Add model card documentation describing training data assumptions, limitations, and intended use.
