# Skin Predictor Architecture

## Overview

Skin Predictor is an offline AI-powered web application that predicts a user's skin type from a facial image and recommends suitable skincare products. The application runs entirely on the CPU without requiring internet connectivity.

---

## System Architecture

```
                User
                  │
                  ▼
        Streamlit Web Interface
                  │
                  ▼
          Image Upload Module
                  │
                  ▼
         Image Preprocessing
          (OpenCV + NumPy)
                  │
                  ▼
        ONNX Runtime (CPU Only)
                  │
                  ▼
       Skin Type Prediction
                  │
                  ▼
     Recommendation Engine (CSV)
                  │
                  ▼
      PDF Report Generation
                  │
                  ▼
             User Output
```

---

## Components

### Frontend
- Streamlit

### Backend
- Python

### AI Runtime
- ONNX Runtime (CPU)

### Image Processing
- OpenCV

### Database
- SQLite

### Reporting
- ReportLab

---

## Offline Workflow

1. Upload image
2. Preprocess image
3. Predict skin type
4. Recommend products
5. Generate PDF report

No cloud services or APIs are used.