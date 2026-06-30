import streamlit as st
from skinsense_ui import init_page, t, PALETTE

init_page("About", "About")

st.markdown(
    f"""
    <div class="hero">
      <div class="brand-logo" style="width:92px;height:92px;font-size:36px">🧴✨</div>
      <p><b>ℹ {t('About Skin Predictor')}</b></p>
      <h1>{t('Offline AI for Everyday Skincare')}</h1>
      <p>{t('Skin Predictor turns a facial image into skin type insights, practical routines, and polished reports without requiring cloud upload.')}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(f'<h2 class="section-title">{t("Mission, Vision, and Privacy")}</h2>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""<div class="glass-card">
    <h3>🎯 {t('Mission')}</h3>
    <p>{t('Make skin analysis private, accessible, and easy to understand for everyone.')}</p>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""<div class="glass-card">
    <h3>🔮 {t('Vision')}</h3>
    <p>{t('A responsible AI skincare assistant that helps users build consistent routines and better conversations with dermatology professionals.')}</p>
    </div>""", unsafe_allow_html=True)

st.markdown(f'<h2 class="section-title">{t("Privacy")}</h2>', unsafe_allow_html=True)
privacy_cols = st.columns(3)
privacy = [
    ("🔒 Offline AI", "Inference runs on the local CPU using ONNX Runtime."),
    ("🖼 Image Control", "Uploaded and captured images are not sent to cloud APIs."),
    ("📄 Local Reports", "PDF reports are generated inside the app session."),
]
for col, (title, body) in zip(privacy_cols, privacy):
    with col:
        st.markdown(f'<div class="feature-card"><h3>{t(title)}</h3><p class="muted">{t(body)}</p></div>', unsafe_allow_html=True)

st.markdown(f'<h2 class="section-title">{t("Technology Stack")}</h2>', unsafe_allow_html=True)
tech_cols = st.columns(5)
tech = [("Python", "🐍"), ("Streamlit", "⚡"), ("OpenCV", "👁"), ("ONNX Runtime", "🤖"), ("Offline AI", "🔒")]
for col, (name, icon) in zip(tech_cols, tech):
    with col:
        st.markdown(f'<div class="metric-card"><div style="font-size:2rem">{icon}</div><h3>{t(name)}</h3></div>', unsafe_allow_html=True)

st.markdown(f'<h2 class="section-title">{t("AI Workflow")}</h2>', unsafe_allow_html=True)
flow = st.columns(5)
steps_flow = [("Upload", "📸"), ("Detection", "🔍"), ("Prediction", "🤖"), ("Recommendations", "🧴"), ("PDF Report", "📄")]
for col, (step, icon) in zip(flow, steps_flow):
    with col:
        st.markdown(f'<div class="feature-card" style="text-align:center"><div style="font-size:2rem">{icon}</div><h3>{t(step)}</h3><p class="muted">↓</p></div>', unsafe_allow_html=True)

st.markdown(f'<h2 class="section-title">{t("Developer")}</h2>', unsafe_allow_html=True)
dev_col, action_col = st.columns([1.2, 0.8], gap="large")
with dev_col:
    st.markdown(f"""<div class="glass-card">
    <h3>🏆 {t('Built for Innovation')}</h3>
    <p>{t('Designed as a portfolio-ready AI healthcare product with privacy-first offline inference.')}</p>
    </div>""", unsafe_allow_html=True)
with action_col:
    st.link_button("GitHub", "https://github.com/", use_container_width=True)
    st.link_button(t("Contact"), "mailto:hello@skinpredictor.ai", use_container_width=True)

st.markdown(f'<h2 class="section-title">{t("Future Roadmap")}</h2>', unsafe_allow_html=True)
roadmap_cols = st.columns(4)
roadmap = [
    ("Model Calibration", "Continuous validation across more lighting and skin-tone conditions."),
    ("Routine Tracking", "Progress history for routines, ingredients, and skin scores."),
    ("Expanded Concerns", "Dedicated signals for acne, pigmentation, redness, and texture."),
    ("Clinician Mode", "Cleaner exports for consultations with dermatology professionals."),
]
for col, (title, body) in zip(roadmap_cols, roadmap):
    with col:
        st.markdown(f'<div class="glass-card"><h3>{t(title)}</h3><p class="muted">{t(body)}</p></div>', unsafe_allow_html=True)
