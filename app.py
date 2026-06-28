import streamlit as st

st.set_page_config(
    page_title="SkinSense AI",
    page_icon="🧴",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧴 SkinSense AI")
st.subheader("Offline AI Skin Type Predictor")

st.markdown("""
Welcome to **SkinSense AI**

This application predicts your skin type from a facial image using an **offline AI model** running entirely on **CPU**.

### Features

- 📸 Upload Face Image
- 🤖 AI Skin Type Prediction
- 🧴 Product Recommendations
- 📄 Download PDF Report
- 💻 CPU Only
- 🔒 Works Completely Offline

Select a page from the sidebar to begin.
""")

st.info("✅ Offline Mode Enabled")