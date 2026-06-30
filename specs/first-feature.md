# Feature Specification: Local Skin Analysis Report

## Summary

Skin Predictor should let a user upload or capture a facial image, run the skin-type prediction locally, and view a clear report with confidence, skin profile details, recommendations, and a downloadable PDF.

## User Problem

Users want quick skincare guidance without sending personal facial images to a cloud service. They need the result to be understandable, practical, and framed as informational rather than medical diagnosis.

## Goals

- Analyze supported image formats using the local Python application.
- Display skin type, confidence, metadata, and recommendation output.
- Generate a local PDF report with summary, routine, ingredients, product suggestions, and disclaimer.
- Preserve user privacy by keeping uploaded images inside the app session.

## Non-Goals

- Diagnosing medical conditions.
- Uploading images to third-party APIs.
- Replacing consultation with a licensed dermatologist.

## User Stories

- As a user, I want to upload a facial image so that I can receive a skin type prediction.
- As a user, I want recommendations based on the detected skin type so that I can plan a skincare routine.
- As a user, I want a PDF report so that I can save or share the analysis summary.

## Acceptance Criteria

- Given a valid PNG, JPEG, or JPG image, when the user starts analysis, then the app displays a skin type and confidence score.
- Given a completed analysis, when the user opens recommendations, then the app displays routine, ingredients, lifestyle advice, and product suggestions.
- Given a completed analysis, when the user opens the report page, then the app displays report sections and allows PDF download.
- Given no completed analysis, when the user opens recommendations or report, then the app asks the user to analyze skin first.

## Privacy and Security

Image processing runs locally. The app must not send uploaded or captured images to external services. Reports are generated in-session. Secrets must not be committed, and dependency/security checks must run in CI.

## Test Plan

- Unit tests for preprocessing, prediction helpers, recommendations, and PDF generation.
- CI checks for linting, formatting, typing, security scanning, dependency audit, and coverage XML.
- Manual check of upload, analysis, recommendation, report, and PDF download flows.

## Rollout Plan

Release through the standard GitLab CI pipeline after all quality gates pass. Roll back by reverting the feature commit if any report generation or analysis flow regression is detected.
