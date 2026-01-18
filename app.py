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

st.title("PICHU GO CALCULATOR")

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
