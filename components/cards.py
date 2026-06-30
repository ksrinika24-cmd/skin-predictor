import streamlit as st
from utils.state_utils import PALETTE


def glass_card(content: str, accent: str = None) -> None:
    color = accent or PALETTE["primary"]
    st.markdown(f'<div class="glass-card" style="border-top:4px solid {color}">{content}</div>', unsafe_allow_html=True)


def metric_card(icon: str, title: str, body: str) -> None:
    st.markdown(f'<div class="metric-card"><div style="font-size:2rem">{icon}</div><h3>{title}</h3><p class="muted">{body}</p></div>', unsafe_allow_html=True)


def feature_card(title: str, body: str, icon: str = "✨", accent: str = None) -> None:
    color = accent or PALETTE["primary"]
    st.markdown(f'<div class="feature-card" style="border-top:4px solid {color}"><div style="font-size:2rem">{icon}</div><h3>{title}</h3><p class="muted">{body}</p></div>', unsafe_allow_html=True)


def badge(text: str, color: str = None) -> str:
    bg = color or PALETTE["primary"]
    return f'<span class="badge" style="background:{bg}">{text}</span>'


def chip(text: str) -> str:
    return f'<span class="chip">{text}</span>'


def hero_section(title: str, subtitle: str, description: str, icon: str = "🧴✨") -> str:
    return f'''<div class="hero">
    <div class="brand-logo" style="width:86px;height:86px;font-size:32px">{icon}</div>
    <p><b>{title}</b></p>
    <h1>{subtitle}</h1>
    <p>{description}</p>
    </div>'''
