from __future__ import annotations

from typing import Any

import streamlit as st
from PIL import Image

# Re-export from utils
from utils.state_utils import APP_NAME, APP_VERSION, PALETTE, LANGUAGES, TRANSLATIONS, SKIN_COLORS
from utils.state_utils import t, t_value, init_page
from utils.image_utils import detect_face_status, preprocess_image
from utils.model_utils import get_onnx_session, load_labels, predict_skin

# Import recommendations
from recommendations import RECOMMENDATION_DATA, SKIN_PROFILES, PRODUCTS
from recommendations import routines_for, recommendation_profile, ingredients_for, products_for

# Import charts
from charts.charts import gauge_chart, risk_pie_chart, radar_chart, plotly_template

# Import PDF
from pdf.report import build_pdf_report


def save_prediction(result: dict[str, Any], image: Image.Image) -> None:
    result["resolution"] = f"{image.size[0]} x {image.size[1]}"
    st.session_state.skin = result["skin"]
    st.session_state.prediction = result
    history = st.session_state.setdefault("history", [])
    history.insert(0, result.copy())
    st.session_state.history = history[:10]


def risk_badge(level: str) -> str:
    color = {"Low": PALETTE["accent"], "Medium": PALETTE["warning"], "High": PALETTE["danger"]}.get(level, PALETTE["primary"])
    return f'<span class="badge" style="background:{color}">{t(level)}</span>'


def logo_html(size: int = 90) -> str:
    return f'<div class="brand-logo" style="width:{size}px;height:{size}px;font-size:{int(size*.38)}px">🧴✨</div>'


def html_block(markup: str) -> None:
    st.markdown(markup, unsafe_allow_html=True)


def card(title: str, body: str, icon: str = "✨", accent: str = None) -> None:
    color = accent or PALETTE["primary"]
    html_block(f'<div class="feature-card" style="border-top:5px solid {color}"><div style="font-size:2rem">{icon}</div><h3>{t_value(title)}</h3><p class="muted">{t_value(body)}</p></div>')
