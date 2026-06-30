import streamlit as st

from skinsense_ui import card, init_page, logo_html, t

init_page("Home", "Home")

left, right = st.columns([1.25, 0.9], gap="large")
with left:
    st.markdown(
        f"""
        <div class="hero">
          {logo_html(86)}
          <p><b>✨ {t('Skin Predictor')}</b></p>
          <h1>{t('AI Powered Skin Analysis')}</h1>
          <h3>{t('Analyze facial skin using AI completely offline.')}</h3>
          <p>{t('Receive personalized skincare recommendations and professional PDF reports while keeping your image on this device.')}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with right:
    st.markdown('<div class="hero-art">🧴😊✨🌿</div>', unsafe_allow_html=True)

st.markdown(f'<h2 class="section-title">{t("Platform Snapshot")}</h2>', unsafe_allow_html=True)
cols = st.columns(4)
stats = [
    ("🤖", "AI Powered", "Offline ONNX CPU pipeline"),
    ("⚡", "Fast Prediction", "Optimized image preprocessing"),
    ("🔒", "Privacy First", "No image upload to cloud"),
    ("🌐", "Offline", "Works without internet"),
]
for col, (icon, title, body) in zip(cols, stats):
    with col:
        st.markdown(f'<div class="metric-card"><div style="font-size:2.1rem">{icon}</div><h3>{t(title)}</h3><p class="muted">{t(body)}</p></div>', unsafe_allow_html=True)

st.markdown(f'<h2 class="section-title">{t("What You Can Do")}</h2>', unsafe_allow_html=True)
grid = st.columns(3)
features = [
    ("Upload Image", "Start from PNG, JPEG, JPG, or camera capture.", "📸", "#F4B400"),
    ("AI Detection", "Predict Normal, Dry, Oily, Combination, or Sensitive skin.", "🤖", "#38BDF8"),
    ("Product Suggestions", "Turn prediction output into a practical routine.", "🧴", "#22C55E"),
    ("PDF Report", "Generate a branded hospital-style AI report.", "📄", "#F97316"),
    ("Confidence Analysis", "Review confidence, runtime, device, and model metadata.", "📊", "#38BDF8"),
    ("Skin Care Tips", "Get lifestyle and ingredient guidance for your skin type.", "💡", "#F4B400"),
]
for idx, item in enumerate(features):
    with grid[idx % 3]:
        card(*item)

st.success(t("Open Skin Analysis from the sidebar to begin."))
