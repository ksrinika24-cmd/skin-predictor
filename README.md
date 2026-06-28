# 🧴 Skin Predictor

An **Offline AI-powered Skin Analysis and Product Recommendation System** built with **Streamlit**, **ONNX Runtime**, and **OpenCV**.

---

## 📌 Problem Statement

Most skincare recommendation applications depend on cloud APIs and internet connectivity, making them inaccessible in low-connectivity environments.

Skin Predictor solves this by performing skin analysis completely offline using CPU-only AI inference.

---

## ✨ Features

- 📸 Upload facial image
- 🤖 AI-based skin type prediction
- 🧴 Personalized skincare recommendations
- 🌞 Morning skincare routine
- 🌙 Night skincare routine
- 📄 Download PDF report
- 💻 Works completely offline
- ⚡ CPU-only inference
- 🔒 No cloud APIs

---

## 🛠 Tech Stack

- Python
- Streamlit
- OpenCV
- ONNX Runtime
- SQLite
- ReportLab

---

## 📂 Project Structure

```text
Skin Predictor/
│
├── app.py
├── pages/
├── utils/
├── models/
├── data/
├── docs/
├── tests/
└── assets/
```

---

## 🚀 Installation

```bash
git clone <repository-url>

cd skin-predictor

pip install -r requirements.txt

streamlit run app.py
```

---

## 🧠 AI Workflow

Image Upload

↓

Face Detection

↓

Image Preprocessing

↓

ONNX Model

↓

Skin Type Prediction

↓

Recommendation Engine

↓

PDF Report

---

## 📊 Supported Skin Types

- Oily
- Dry
- Combination
- Sensitive
- Normal

---

## 🔒 Offline Mode

- No internet required
- No cloud APIs
- CPU-only inference

---

## 📜 License

Licensed under GPL-3.0.