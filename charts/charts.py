import streamlit as st
import plotly.graph_objects as go

from utils.state_utils import PALETTE, t


def plotly_template() -> str:
    return "plotly_dark" if st.session_state.get("theme_mode") == "Dark" else "plotly_white"


def gauge_chart(value: float, title: str, suffix: str = "") -> go.Figure:
    fig = go.Figure(go.Indicator(
        mode="gauge+number", value=value, number={"suffix": suffix},
        title={"text": title},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": PALETTE["primary"]},
            "steps": [
                {"range": [0, 50], "color": "rgba(255,92,138,.25)"},
                {"range": [50, 80], "color": "rgba(255,200,87,.28)"},
                {"range": [80, 100], "color": "rgba(126,217,87,.30)"}
            ]
        }
    ))
    fig.update_layout(template=plotly_template(), height=260, margin=dict(l=20, r=20, t=55, b=10), paper_bgcolor="rgba(0,0,0,0)")
    return fig


def risk_pie_chart(risks: dict) -> go.Figure:
    counts = {level: list(risks.values()).count(level) for level in ["Low", "Medium", "High"]}
    fig = go.Figure(go.Pie(labels=[t(level) for level in counts.keys()], values=list(counts.values()), hole=.58, marker_colors=[PALETTE["accent"], PALETTE["warning"], PALETTE["danger"]]))
    fig.update_layout(template=plotly_template(), height=260, margin=dict(l=20, r=20, t=25, b=10), paper_bgcolor="rgba(0,0,0,0)")
    return fig


def radar_chart(profile: dict) -> go.Figure:
    values = {
        "Balanced Oil": 80 if "Balanced" in profile["oil"] else 55,
        "Hydration": 90 if profile["hydration"] == "Healthy" else 58 if profile["hydration"] == "Low" else 72,
        "Low Sensitivity": 90 if "Low" in profile["sensitivity"] else 45,
        "Texture": 82,
        "Barrier": profile["score"]
    }
    fig = go.Figure(go.Scatterpolar(r=list(values.values()), theta=[t(key) for key in values.keys()], fill="toself", line_color=PALETTE["secondary"]))
    fig.update_layout(
        template=plotly_template(),
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        height=310, margin=dict(l=35, r=35, t=35, b=25),
        paper_bgcolor="rgba(0,0,0,0)"
    )
    return fig
