import streamlit as st
from skinsense_ui import init_page, t, PALETTE, products_for, routines_for
from recommendations import recommendation_profile, ingredients_for

init_page("Recommendations", "Recommendations")

skin = st.session_state.get("skin")
if skin is None:
    st.warning(t("Analyze your skin first."))
    st.stop()

translated_skin = t(skin)

st.markdown(
    f"""
    <div class="hero">
      <p><b>🧴 {t('Recommendations')}</b></p>
      <h1>{translated_skin} {t('Skin Care Plan')}</h1>
      <p>{t('Generated using AI based on your detected skin type.')}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

routines = routines_for(skin)
profile = recommendation_profile(skin)
icons = {"Morning": "☀️", "Night": "🌙", "Weekly": "✨"}
colors_routine = {"Morning": "#F4B400", "Night": "#38BDF8", "Weekly": "#22C55E"}
cols = st.columns(3)
for col, (name, steps) in zip(cols, routines.items()):
    with col:
        st.markdown(f"""<div class="glass-card" style="border-top:5px solid {colors_routine[name]}">
        <div style="font-size:2.3rem">{icons[name]}</div>
        <h3>{t(name)} {t('Routine')}</h3>
        {"".join([f'<p><span class="badge">{t(step)}</span></p>' for step in steps])}
        <p class="muted">{t('AI recommends this for your skin profile.')}</p>
        </div>""", unsafe_allow_html=True)

st.markdown(f'<h2 class="section-title">{t("Ingredient Strategy")}</h2>', unsafe_allow_html=True)
use_col, avoid_col = st.columns(2, gap="large")
with use_col:
    chips = "".join([f'<span class="chip">{t(item)}</span>' for item in ingredients_for(skin)])
    st.markdown(f'<div class="glass-card"><h3>{t("Use")}</h3>{chips}</div>', unsafe_allow_html=True)
with avoid_col:
    chips = "".join([f'<span class="chip">{t(item)}</span>' for item in profile["avoid"]])
    st.markdown(f'<div class="glass-card"><h3>{t("Avoid")}</h3>{chips}</div>', unsafe_allow_html=True)

st.markdown(f'<h2 class="section-title">{t("Lifestyle, Diet, and Dermatologist Advice")}</h2>', unsafe_allow_html=True)
life_cols = st.columns(3)
sections = [
    ("Lifestyle Tips", profile["lifestyle"]),
    ("Common Skin Problems", profile["problems"]),
    ("Do's", profile["dos"]),
]
for col, (title, items) in zip(life_cols, sections):
    with col:
        st.markdown(f'<div class="glass-card"><h3>{t(title)}</h3>' + "".join([f'<span class="chip">{t(tip)}</span>' for tip in items]) + '</div>', unsafe_allow_html=True)

advice_left, advice_right = st.columns(2, gap="large")
with advice_left:
    donts_title = t("Don'ts")
    st.markdown(f'<div class="glass-card"><h3>{donts_title}</h3>' + "".join([f'<span class="chip">{t(tip)}</span>' for tip in profile["donts"]]) + '</div>', unsafe_allow_html=True)
with advice_right:
    st.markdown(f'<div class="glass-card"><h3>{t("Dermatologist Advice")}</h3><p>{t(profile["advice"])}</p></div>', unsafe_allow_html=True)

st.markdown(f'<h2 class="section-title">{t("Product Recommendations")}</h2>', unsafe_allow_html=True)
products = products_for(skin)
if products:
    product_cols = st.columns(3)
    for idx, product in enumerate(products):
        with product_cols[idx % 3]:
            description = t(product["description"])
            benefits = t(product["benefits"])
            usage = t(product["usage"])
            if description == product["description"]:
                description = t("Recommended skincare option")
            if benefits == product["benefits"]:
                benefits = t("Supports your skin routine")
            if usage == product["usage"]:
                usage = t("Use as directed")
            st.markdown(f"""<div class="product-card" style="border-top:4px solid {PALETTE['primary']}">
            <div class="product-image">💄</div>
            <h4>{product['name']}</h4>
            <p><b>{t('Category')}:</b> {t(product['category'])}</p>
            <p class="muted"><b>{t('Description')}:</b> {description}</p>
            <p class="muted"><b>{t('Benefits')}:</b> {benefits}</p>
            <p class="muted"><b>{t('Usage')}:</b> {usage}</p>
            </div>""", unsafe_allow_html=True)

recommendation_text = "\n".join([f"{t(name)}: " + " > ".join(t(step) for step in steps) for name, steps in routines.items()])
st.download_button(f"📋 {t('Copy Recommendations')}", recommendation_text, file_name=f"{skin}_recommendations.txt", use_container_width=True)
