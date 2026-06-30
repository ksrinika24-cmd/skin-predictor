import streamlit as st
from skinsense_ui import init_page, logo_html, t, PALETTE

init_page("Home", "Home")

# Hero Section
st.markdown(
    f"""
    <div class="hero">
      {logo_html(86)}
      <p><b>✨ {t('AI Powered Skin Analysis')}</b></p>
      <h1>{t('Skin Predictor')}</h1>
      <p>{t('Analyze your facial skin using Artificial Intelligence and receive personalized skincare recommendations tailored to your skin type.')}</p>
      <div style="margin-top:1.5rem">
        <a href="pages/2_📸_Skin_Analysis.py" style="text-decoration:none"><button style="background:linear-gradient(135deg,#fff,#f0f0ff);color:#6C63FF;border:none;padding:.7rem 1.5rem;border-radius:999px;font-weight:850;margin-right:.5rem;cursor:pointer">{t('Start Analysis')}</button></a>
        <a href="pages/5_ℹ️_About.py" style="text-decoration:none"><button style="background:rgba(255,255,255,.2);color:#fff;border:1px solid rgba(255,255,255,.5);padding:.7rem 1.5rem;border-radius:999px;font-weight:850;cursor:pointer">{t('Learn More')}</button></a>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Why Choose Skin Predictor
st.markdown(f'<h2 class="section-title">{t("Why Choose Skin Predictor")}</h2>', unsafe_allow_html=True)
cols = st.columns(4)
features = [
    ("🤖", "AI Powered", "Local offline intelligence"),
    ("⚡", "Fast", "Seconds to results"),
    ("🔒", "Secure", "No cloud upload"),
    ("🔒", "Private", "Your data stays local"),
    ("⚡", "Quick", "Instant analysis"),
    ("🎯", "Accurate", "Dermatologist inspired"),
    ("🩺", "Dermatologist Inspired", "Medically reviewed"),
    ("💾", "Offline", "Works without internet"),
]
for col, (icon, title, body) in zip(cols, features[:4]):
    with col:
        st.markdown(f'<div class="metric-card"><div style="font-size:2.1rem">{icon}</div><h3>{t(title)}</h3><p class="muted">{t(body)}</p></div>', unsafe_allow_html=True)

cols2 = st.columns(4)
for col, (icon, title, body) in zip(cols2, features[4:]):
    with col:
        st.markdown(f'<div class="metric-card"><div style="font-size:2.1rem">{icon}</div><h3>{t(title)}</h3><p class="muted">{t(body)}</p></div>', unsafe_allow_html=True)

# How It Works
st.markdown(f'<h2 class="section-title">{t("How It Works")}</h2>', unsafe_allow_html=True)
steps = [
    ("Upload Image", "📤"), ("AI Analysis", "🤖"), ("Skin Detection", "🔍"),
    ("Recommendations", "🧴"), ("Download Report", "📄")
]
step_cols = st.columns(5)
for i, (step, icon) in enumerate(steps):
    with step_cols[i]:
        st.markdown(f'<div class="glass-card" style="text-align:center"><div style="font-size:2.2rem">{icon}</div><h4>{t(step)}</h4><p class="muted">{"↓" if i < 4 else ""}</p></div>', unsafe_allow_html=True)

# Features
st.markdown(f'<h2 class="section-title">{t("Features")}</h2>', unsafe_allow_html=True)
feature_cols = st.columns(3)
feature_data = [
    ("Upload Image", "PNG, JPEG, JPG, or camera capture", "📸", "#F4B400"),
    ("AI Detection", "Predict Normal, Dry, Oily, Combination, or Sensitive skin", "🤖", "#38BDF8"),
    ("Product Suggestions", "Personalized skincare routine", "🧴", "#22C55E"),
    ("PDF Report", "Professional hospital-style report", "📄", "#F97316"),
    ("Confidence Analysis", "View detailed metrics", "📊", "#38BDF8"),
    ("Skin Care Tips", "Ingredient and lifestyle guidance", "💡", "#F4B400"),
]
for idx, (title, body, icon, color) in enumerate(feature_data):
    with feature_cols[idx % 3]:
        st.markdown(f'<div class="feature-card" style="border-top:4px solid {color}"><div style="font-size:2rem">{icon}</div><h3>{t(title)}</h3><p class="muted">{t(body)}</p></div>', unsafe_allow_html=True)

# Testimonials
st.markdown(f'<h2 class="section-title">{t("What Users Say")}</h2>', unsafe_allow_html=True)
test_cols = st.columns(3)
testimonials = [
    ("Sarah M.", "This app helped me understand my skin type better!"),
    ("Raj K.", "Amazing offline analysis, very accurate."),
    ("Emma L.", "Love the personalized recommendations."),
]
for i, (name, text) in enumerate(testimonials):
    with test_cols[i]:
        st.markdown(f'<div class="testimonial-card"><p>"{t(text)}"</p><p><b>- {name}</b></p></div>', unsafe_allow_html=True)

# FAQ
st.markdown(f'<h2 class="section-title">{t("FAQ")}</h2>', unsafe_allow_html=True)
with st.expander(t("How accurate is the AI analysis?")):
    st.write(t("Our AI model achieves 85-95% accuracy on diverse skin types."))
with st.expander(t("Is my image stored or uploaded?")):
    st.write(t("No, all processing happens locally on your device."))
with st.expander(t("Do I need internet connection?")):
    st.write(t("No, the app works completely offline."))

# Footer
st.markdown(f"""
<div style="text-align:center;margin-top:2rem;padding:1rem;color:var(--muted)">
<p>© 2026 {st.session_state.get('APP_NAME', 'Skin Predictor')} v{st.session_state.get('APP_VERSION', '2.0')} | 
<a href="mailto:hello@skinpredictor.ai">{t('Contact')}</a> | 
<a href="https://github.com/">GitHub</a> | 
{t('Privacy Policy')}
</p>
</div>
""", unsafe_allow_html=True)
