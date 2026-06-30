import streamlit as st
from skinsense_ui import init_page, t, PALETTE, ingredients_for, risk_badge, routines_for, build_pdf_report
from recommendations import products_for, recommendation_profile

init_page("Report", "Report")

result = st.session_state.get("prediction")
if result is None:
    st.warning(t("No report available. Analyze your skin first."))
    st.stop()

skin = result["skin"]
profile = result["profile"]
rec = recommendation_profile(skin)
translated_skin = t(skin)

st.markdown(
    f"""
    <div class="hero">
      <p><b>📄 {t('Report')}</b></p>
      <h1>{translated_skin} {t('Skin Report')}</h1>
      <p>{t('Prediction ID')} {result['prediction_id']} · {t('Confidence')} {result['confidence']}% · {t('Health Score')} {result['health_score']}/100</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(f'<h2 class="section-title">{t("Patient Summary")}</h2>', unsafe_allow_html=True)
summary = [
    ("Date", result["timestamp"].strftime("%d %b %Y")), ("Time", result["timestamp"].strftime("%I:%M %p")),
    ("Prediction ID", result["prediction_id"]), ("Detected Skin Type", translated_skin), ("Confidence", f"{result['confidence']}%"),
    ("Health Score", f"{result['health_score']} /100"), ("Model Version", result["ai_version"]), ("CPU Runtime", t(str(result["runtime"]))),
    ("Inference Time", f"{result['inference_ms']} ms"),
]
cols = st.columns(3)
for idx, (label, value) in enumerate(summary):
    with cols[idx % 3]:
        st.markdown(f'<div class="metric-card"><p class="muted">{t(label)}</p><h3>{value}</h3></div>', unsafe_allow_html=True)

left, right = st.columns([1, 1], gap="large")
with left:
    st.markdown(f'<h2 class="section-title">{t("Skin Analysis")}</h2>', unsafe_allow_html=True)
    st.markdown(f"""<div class="report-panel">
    <p><b>{t('Skin Type')}:</b> {translated_skin}</p>
    <p><b>{t('Oil Level')}:</b> {t(profile['oil'])}</p>
    <p><b>{t('Hydration Level')}:</b> {t(profile['hydration'])}</p>
    <p><b>{t('Sensitivity Level')}:</b> {t(profile['sensitivity'])}</p>
    <p><b>{t('Texture')}:</b> {t(profile['texture'])}</p>
    <p><b>{t('AI Explanation')}:</b> {t(profile['explanation'])}</p>
    <p><b>{t('Characteristics')}:</b> {", ".join(t(item) for item in profile['characteristics'])}</p>
    </div>""", unsafe_allow_html=True)
with right:
    st.markdown(f'<h2 class="section-title">{t("Risk Assessment")}</h2>', unsafe_allow_html=True)
    risk_lines = []
    for name, level in profile["risks"].items():
        risk_lines.append(f"<p><b>{t(name)} {t('Risk')}:</b> {risk_badge(level)}</p>")
    st.markdown(f'<div class="report-panel">{"".join(risk_lines)}</div>', unsafe_allow_html=True)

st.markdown(f'<h2 class="section-title">{t("Recommended Routine")}</h2>', unsafe_allow_html=True)
routine_cols = st.columns(3)
for col, (name, steps) in zip(routine_cols, routines_for(skin).items()):
    with col:
        st.markdown(f'<div class="glass-card"><h3>{t(name)}</h3><p>{" > ".join(t(step) for step in steps)}</p></div>', unsafe_allow_html=True)

st.markdown(f'<h2 class="section-title">{t("Recommended Ingredients")}</h2>', unsafe_allow_html=True)
st.markdown(f'<div class="glass-card">' + "".join([f'<span class="chip">{t(item)}</span>' for item in ingredients_for(skin)]) + "</div>", unsafe_allow_html=True)

st.markdown(f'<h2 class="section-title">{t("Lifestyle Advice")}</h2>', unsafe_allow_html=True)
life_cols = st.columns(3)
for col, (title, items) in zip(life_cols, [("Lifestyle", rec["lifestyle"]), ("Use", rec["use"]), ("Avoid", rec["avoid"])]):
    with col:
        st.markdown(f'<div class="glass-card"><h3>{t(title)}</h3>' + "".join([f'<span class="chip">{t(item)}</span>' for item in items]) + '</div>', unsafe_allow_html=True)

st.markdown(f'<h2 class="section-title">{t("Products Included in PDF")}</h2>', unsafe_allow_html=True)
product_cols = st.columns(3)
for idx, product in enumerate(products_for(skin)[:6]):
    with product_cols[idx % 3]:
        benefits = t(product["benefits"])
        usage = t(product["usage"])
        if benefits == product["benefits"]:
            benefits = t("Supports your skin routine")
        if usage == product["usage"]:
            usage = t("Use as directed")
        st.markdown(f"""<div class="product-card">
        <div class="product-image">🧴</div>
        <h4>{product['name']}</h4>
        <p><b>{t(product['category'])}</b></p>
        <p class="muted">{benefits} · {usage}</p>
        </div>""", unsafe_allow_html=True)

st.markdown(f'<h2 class="section-title">{t("Medical Disclaimer")}</h2>', unsafe_allow_html=True)
st.info(t("This report is AI-generated and intended for informational purposes only. It is not a medical diagnosis or a substitute for consultation with a licensed dermatologist."))

try:
    pdf = build_pdf_report(result)
    st.download_button(
        f"📥 {t('Download Premium PDF')}",
        data=pdf,
        file_name=f"Skin_Predictor_{result['prediction_id']}.pdf",
        mime="application/pdf",
        use_container_width=True
    )
except Exception:
    st.error(t("PDF generation is unavailable. Please install reportlab: pip install reportlab"))
