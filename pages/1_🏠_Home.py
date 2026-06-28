import streamlit as st

st.title("🏠 SkinSense AI")

st.markdown("""
# Welcome to SkinSense AI

### Offline AI Skin Analysis

Predict your skin type using AI running entirely on your CPU.

## Features

✅ Skin Type Prediction

✅ Product Recommendation

✅ PDF Report

✅ Offline

✅ CPU Powered
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("AI Runtime", "CPU")

with col2:
    st.metric("Internet", "Not Required")

with col3:
    st.metric("Mode", "Offline")

st.success("Select Skin Analysis from the sidebar to begin.")