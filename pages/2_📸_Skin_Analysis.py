import streamlit as st
from datetime import datetime
from PIL import Image
from skinsense_ui import SKIN_COLORS, init_page, predict_skin, save_prediction, t, PALETTE, detect_face_status, gauge_chart, radar_chart

init_page("Skin Analysis", "Skin Analysis")

st.markdown(
    f"""
    <div class="hero">
      <p><b>📸 {t('Skin Analysis')}</b></p>
      <h1>{t('Upload. Scan. Understand.')}</h1>
      <p>{t('Use a clear front-facing image. The AI pipeline runs locally on CPU and never sends your image outside this app.')}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

upload_col, tools_col = st.columns([1.25, 0.75], gap="large")
with upload_col:
    st.markdown(f'<div class="upload-box"><h3>📤 {t("Drag & Drop Facial Image")}</h3><p class="muted">{t("Supported formats: PNG, JPEG, JPG")}</p></div>', unsafe_allow_html=True)
    uploaded = st.file_uploader(t("Upload image"), type=["png", "jpeg", "jpg"], label_visibility="collapsed")
    camera = st.camera_input(f"📷 {t('Webcam Capture')}")
with tools_col:
    st.markdown(f'<div class="glass-card"><h3>🖼 {t("Image Comparison")}</h3><p class="muted">{t("Optional: add a second image for visual comparison.")}</p></div>', unsafe_allow_html=True)
    compare = st.file_uploader(t("Comparison image"), type=["png", "jpeg", "jpg"])
    if st.button(f"🔄 {t('Reset Analysis')}", use_container_width=True):
        for key in ["skin", "prediction", "last_image"]:
            st.session_state.pop(key, None)
        st.toast(t("Analysis reset."))
        st.rerun()

source = uploaded or camera
if source:
    try:
        image = Image.open(source).convert("RGB")
        st.session_state.last_image = image
        width, height = image.size
        image_cols = st.columns([1, 1], gap="large")
        with image_cols[0]:
            st.markdown(f'<div class="glass-card"><h3>{t("Primary Image")}</h3>', unsafe_allow_html=True)
            st.image(image, use_container_width=True)
            st.markdown(f'<p class="muted">{t("Size")}: {getattr(source, "size", 0) / 1024:.1f} KB · {t("Resolution")}: {width} x {height} · {t("Upload time")}: {datetime.now().strftime("%I:%M %p")}</p></div>', unsafe_allow_html=True)
        with image_cols[1]:
            if compare:
                compare_image = Image.open(compare).convert("RGB")
                st.markdown(f'<div class="glass-card"><h3>{t("Comparison Image")}</h3>', unsafe_allow_html=True)
                st.image(compare_image, use_container_width=True)
                st.markdown(f'<p class="muted">{t("Resolution")}: {compare_image.size[0]} x {compare_image.size[1]}</p></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="glass-card"><h3>{t("AI Readiness")}</h3><p class="muted">{t("Image loaded successfully. Start the scan to generate prediction metadata, confidence, skin score, and recommendations.")}</p></div>', unsafe_allow_html=True)

        analyze = st.button(f"🔍 {t('Analyze Skin')}", use_container_width=True)
        if analyze:
            steps = ["AI is analyzing your skin...", "Scanning image...", "Extracting features...", "Running ONNX Model...", "Predicting skin type..."]
            progress = st.progress(0)
            status = st.empty()
            for idx, step in enumerate(steps, start=1):
                status.info(f"🔍 {t(step)}")
                progress.progress(idx / len(steps))
            result = predict_skin(image)
            save_prediction(result, image)
            st.toast(t("Prediction complete."))
            st.balloons()
            status.success(t("Analysis complete!"))

    except Exception as e:
        st.error(t("Unable to process image. Please try another file."))

if st.session_state.get("prediction"):
    result = st.session_state.prediction
    skin = result["skin"]
    color = SKIN_COLORS.get(skin, PALETTE["primary"])
    
    translated_skin = t(skin)
    st.markdown(f'<h2 class="section-title">📊 {t("AI Result Dashboard")}</h2>', unsafe_allow_html=True)
    
    a, b, c = st.columns([1.05, 1, 1], gap="large")
    with a:
        st.markdown(f"""<div class="glass-card">
        <span class="badge" style="background:{color}">{t("Detected Skin Type")}</span>
        <h1 style="color:{color};margin:.5rem 0">{translated_skin}</h1>
        <p class="muted">{t("Prediction ID")}: {result['prediction_id']}</p>
        <div class="progress-shell"><div class="progress-fill" style="width:{result['confidence']}%"></div></div>
        <p><b>{t("Confidence")}:</b> {result['confidence']}%</p>
        </div>""", unsafe_allow_html=True)
    with b:
        score = result["health_score"]
        st.plotly_chart(gauge_chart(score, t("Skin Health Score"), "/100"), use_container_width=True)
    with c:
        st.markdown(f"""<div class="glass-card">
        <h3>{t("Model Metadata")}</h3>
        <p><b>{t("Prediction Time")}:</b> {result['inference_ms']} ms</p>
        <p><b>{t("Model Name")}:</b> {result['model']}</p>
        <p><b>{t("Inference Device")}:</b> {t(str(result['device']))}</p>
        <p><b>{t("Image Resolution")}:</b> {result['resolution']}</p>
        <p><b>{t("Face Detection Status")}:</b> {t(str(result['face_status']))}</p>
        <p><b>{t("AI Version")}:</b> {result['ai_version']}</p>
        <p><b>{t("Provider")}:</b> {t(str(result['runtime_note']))}</p>
        </div>""", unsafe_allow_html=True)

    # Charts
    st.markdown(f'<h2 class="section-title">📈 {t("Skin Analysis Charts")}</h2>', unsafe_allow_html=True)
    chart1, chart2 = st.columns(2)
    with chart1:
        st.plotly_chart(gauge_chart(result['confidence'], t("Confidence")), use_container_width=True)
    with chart2:
        st.plotly_chart(radar_chart(result['profile']), use_container_width=True)

if st.session_state.get("history"):
    with st.expander(f"📜 {t('Prediction History')}", expanded=False):
        for item in st.session_state.history:
            st.write(f"{item['timestamp'].strftime('%d %b %Y %I:%M %p')} · {t(item['skin'])} · {item['confidence']}% {t('confidence')}")
else:
    st.info(t("Upload or capture an image to begin."))
