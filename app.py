import streamlit as st
from modules.config_manager import get_config
from modules.styles import HIDE_ST_STYLE, GLOBAL_CSS
from modules.ui_components import render_korea_tab, render_china_tab

st.set_page_config(page_title="PICHU GO CALCULATOR", page_icon="🇰🇷")

# --- APPLY STYLES ---
st.markdown(HIDE_ST_STYLE, unsafe_allow_html=True)
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# --- CONFIGURATION ---
config, status = get_config()

# --- HEADER ---
st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="
            background: -webkit-linear-gradient(45deg, #702459, #D53F8C, #B83280);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3.5rem;
            font-weight: 800;
            margin: 0;
            line-height: 1.2;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
        ">
            PICHU GO CALCULATOR
        </h1>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR STATUS ---
if "Live" in status:
    st.sidebar.success(f"Data Source: {status}")
else:
    st.sidebar.warning(f"Data Source: {status}")

try:
    if not st.secrets.get("SHEET_ID") or st.secrets.get("SHEET_ID") == "YOUR_SHEET_ID_HERE":
        st.sidebar.warning("⚠️ SHEET_ID is missing. Using default configuration.")
except Exception:
    st.sidebar.warning("⚠️ Secrets not found. Using default configuration.")

# --- TABS ---
tab_kr, tab_ch = st.tabs(["🇰🇷 Korea", "🇨🇳 China"])

# --- KOREA TAB ---
with tab_kr:
    render_korea_tab(config)

# --- CHINA TAB ---
with tab_ch:
    render_china_tab(config)
