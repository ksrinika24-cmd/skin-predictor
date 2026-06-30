import streamlit as st

from utils.state_utils import APP_NAME, APP_VERSION, PALETTE, LANGUAGES, TRANSLATIONS


def t(text: str) -> str:
    return TRANSLATIONS.get(st.session_state.get("language", "English"), {}).get(text, text)


def inject_css() -> None:
    dark = st.session_state.get("theme_mode", "Light") == "Dark"
    bg = PALETTE["dark_bg"] if dark else PALETTE["bg"]
    text = "#F8FAFC" if dark else "#1E1F2E"
    card = "rgba(42, 44, 68, .74)" if dark else "rgba(255, 255, 255, .72)"
    muted = "#CBD5E1" if dark else "#667085"
    
    st.markdown(
        f"""
        <style>
        :root {{ --primary:{PALETTE['primary']}; --secondary:{PALETTE['secondary']}; --accent:{PALETTE['accent']};
          --warning:{PALETTE['warning']}; --danger:{PALETTE['danger']}; --bg:{bg}; --text:{text}; --card:{card}; --muted:{muted}; }}
        .stApp {{ background: radial-gradient(circle at 10% 10%, rgba(108,99,255,.20), transparent 28%),
          radial-gradient(circle at 90% 8%, rgba(255,126,179,.20), transparent 24%),
          radial-gradient(circle at 60% 90%, rgba(126,217,87,.14), transparent 28%), var(--bg); color:var(--text); }}
        .block-container {{ max-width:1280px; padding-top:1.25rem; padding-bottom:2rem; }}
        [data-testid="stSidebar"] {{ background:linear-gradient(180deg,#17182A,#2B245D 58%,#1E1F2E); }}
        [data-testid="stSidebarNav"] {{ display:none; }}
        [data-testid="stSidebar"] * {{ color:#F8FAFC !important; }}
        .brand-logo {{ width:78px;height:78px;border-radius:26px;display:grid;place-items:center;font-size:32px;
          background:linear-gradient(135deg,var(--primary),var(--secondary)); box-shadow:0 22px 46px rgba(108,99,255,.34); }}
        .sidebar-title {{ font-size:1.55rem;font-weight:900;letter-spacing:0;line-height:1.1;margin-top:.55rem; }}
        .sidebar-subtitle,.muted {{ color:var(--muted); }}
        .hero {{ position:relative; overflow:hidden; border-radius:30px; min-height:330px; padding:2.2rem;
          background:linear-gradient(135deg,rgba(108,99,255,.95),rgba(255,126,179,.78),rgba(126,217,87,.42));
          box-shadow:0 28px 80px rgba(31,33,62,.20); animation:fadeIn .55s ease both; }}
        .hero:before,.hero:after {{ content:""; position:absolute; border-radius:999px; background:rgba(255,255,255,.26); animation:float 5s ease-in-out infinite; }}
        .hero:before {{ width:120px;height:120px;right:9%;top:12%; }} .hero:after {{ width:72px;height:72px;right:27%;bottom:14%; animation-delay:1.1s; }}
        .hero h1 {{ font-size:clamp(2.4rem,5vw,5.2rem); line-height:1; margin:.25rem 0; color:#fff; }}
        .hero p,.hero h3 {{ color:#fff; max-width:720px; }}
        .hero-art {{ min-height:300px; border-radius:30px; display:grid; place-items:center; font-size:5.8rem;
          background:linear-gradient(135deg,rgba(255,255,255,.75),rgba(255,255,255,.24)); border:1px solid rgba(255,255,255,.6);
          box-shadow:inset 0 0 80px rgba(255,255,255,.28),0 24px 58px rgba(108,99,255,.18); animation:float 4.5s ease-in-out infinite; }}
        .glass-card,.metric-card,.feature-card,.report-panel,.testimonial-card {{ background:var(--card); border:1px solid rgba(255,255,255,.54);
          border-radius:24px; padding:1.2rem; box-shadow:0 18px 48px rgba(31,33,62,.12); backdrop-filter:blur(16px);
          transition:transform .22s ease, box-shadow .22s ease; height:100%; color:var(--text); }}
        .glass-card:hover,.metric-card:hover,.feature-card:hover,.testimonial-card:hover {{ transform:translateY(-5px); box-shadow:0 25px 70px rgba(108,99,255,.22); }}
        .metric-card {{ background:linear-gradient(135deg,rgba(255,255,255,.88),rgba(247,248,255,.58)); color:#1E1F2E; }}
        .feature-card h3,.metric-card h3,.report-panel h3 {{ margin:.35rem 0 .25rem; }}
        .badge {{ display:inline-flex;align-items:center;gap:.35rem;border-radius:999px;padding:.45rem .8rem;font-weight:850;color:#101121;background:#fff; }}
        .chip {{ display:inline-block;margin:.2rem .25rem .2rem 0;padding:.45rem .75rem;border-radius:999px;
          background:linear-gradient(135deg,rgba(108,99,255,.16),rgba(255,126,179,.16)); border:1px solid rgba(108,99,255,.20); color:var(--text); }}
        .upload-box {{ border:2px dashed rgba(108,99,255,.75); border-radius:28px; padding:1.3rem; background:rgba(255,255,255,.52); }}
        .progress-shell {{ height:13px; background:rgba(148,163,184,.22); border-radius:999px; overflow:hidden; }}
        .progress-fill {{ height:100%; border-radius:999px; background:linear-gradient(90deg,var(--primary),var(--secondary),var(--accent)); animation:grow .8s ease both; }}
        .section-title {{ margin-top:1.35rem;margin-bottom:.75rem; color:var(--text); }}
        .stButton>button,.stDownloadButton>button,.stLinkButton>a {{ border-radius:999px !important; border:0 !important;
          background:linear-gradient(135deg,var(--primary),var(--secondary)) !important; color:#fff !important; font-weight:850 !important;
          box-shadow:0 14px 32px rgba(108,99,255,.30); transition:.2s ease; }}
        .stButton>button:hover,.stDownloadButton>button:hover,.stLinkButton>a:hover {{ transform:translateY(-2px); box-shadow:0 22px 48px rgba(255,126,179,.32); }}
        @keyframes fadeIn {{ from {{ opacity:0; transform:translateY(12px); }} to {{ opacity:1; transform:translateY(0); }} }}
        @keyframes float {{ 0%,100% {{ transform:translateY(0); }} 50% {{ transform:translateY(-12px); }} }}
        @keyframes grow {{ from {{ width:0; }} }}
        @keyframes pulse {{ 0%,100% {{ opacity:1; }} 50% {{ opacity:.6; }} }}
        @media (max-width:760px) {{ .hero {{ padding:1.25rem; min-height:260px; }} .hero-art {{ min-height:190px; font-size:3.7rem; }} }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar(current: str) -> None:
    pages = [
        ("Home", "🏠", "pages/1_🏠_Home.py"),
        ("Skin Analysis", "📷", "pages/2_📸_Skin_Analysis.py"),
        ("Recommendations", "💄", "pages/3_🧴_Recommendations.py"),
        ("Report", "📄", "pages/4_📄_Report.py"),
        ("About", "ℹ️", "pages/5_ℹ️_About.py"),
    ]
    
    with st.sidebar:
        st.markdown(f'<div class="brand-logo">🧴✨</div><div class="sidebar-title">{APP_NAME}</div><div class="sidebar-subtitle">{t("AI Powered Skin Analysis")}</div>', unsafe_allow_html=True)
        
        for label, icon, path in pages:
            marker = "● " if label == current else ""
            st.page_link(path, label=f"{marker}{icon} {t(label)}")
        
        st.divider()
        
        st.session_state.theme_mode = st.radio(f"🌞 {t('Theme')}", ["Light", "Dark"], horizontal=True, key="mode_picker", format_func=t)
        st.session_state.language = st.selectbox(f"🌐 {t('Language')}", LANGUAGES, key="language_picker")
        
        st.markdown(f"━━━━━━━━━━━━━━━  \n{t('Version')} {APP_VERSION}  \n{t('Made with')} ❤️  \n{t('Offline AI')}")
