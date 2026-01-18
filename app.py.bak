import streamlit as st
from modules.config_manager import get_config
from modules.styles import HIDE_ST_STYLE, GLOBAL_CSS
from modules.calculator import calculate_korea, calculate_china

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

# --- COMMON VARIABLES ---
admin_go = config.get('admin_go', 6000)

# --- KOREA TAB ---
with tab_kr:
    rate_kr = config.get('rate_kr', 11.75)
    jasa_tf_kr = config.get('jasa_tf_kr', 6000)
    ongkir_kr_default = config.get('ongkir_kr_default', 2000)

    st.markdown(f"""
    <div class="glass-pill" style="color: #702459;">
        💱 Exchange Rate: 1 KRW = {rate_kr} IDR
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        kr_price_input = st.number_input(
            "💰 Harga Produk (0.1 = 1,000 Won)",
            min_value=0.0,
            step=0.01,
            format="%.2f",
            help="Masukkan 1.0 untuk 10,000 KRW",
            key="kr_price"
        )

        kr_ongkir_input = st.number_input(
            "🚚 Ongkir Lokal Korea (Won)",
            min_value=0,
            value=int(ongkir_kr_default),
            step=500,
            help="Biasanya 2000-4000 Won. Ubah jika beda.",
            key="kr_ongkir"
        )

    with col2:
        kr_people = st.slider(
            "👥 Jumlah Sharing (Orang)",
            min_value=1,
            max_value=50,
            value=1,
            step=1,
            help="Jumlah orang dalam Group Order",
            key="kr_people"
        )

    # Calculation
    kr_total, kr_item_idr, kr_shared_fees = calculate_korea(
        kr_price_input, kr_ongkir_input, kr_people, rate_kr, jasa_tf_kr, admin_go
    )
    kr_total_rounded = round(kr_total, -2)

    st.markdown(f"""
    <div class="glass-card-kr">
        <p class="label">🇰🇷 Estimated Total</p>
        <h1>Rp {kr_total_rounded:,.0f}</h1>
        <div class="breakdown-pill">
            <span>📦 Price: {kr_item_idr:,.0f}</span>
            <span>•</span>
            <span>✈️ Fees: {kr_shared_fees + admin_go:,.0f}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- CHINA TAB ---
with tab_ch:
    rate_ch = config.get('rate_ch', 2450)
    jasa_tf_ch = config.get('jasa_tf_ch', 10000)
    ongkir_ch_default = config.get('ongkir_ch_default', 100)

    st.markdown(f"""
    <div class="glass-pill" style="color: #9B2C2C;">
        💱 Exchange Rate: 1 CNY = {rate_ch} IDR
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        cn_price_input = st.number_input(
            "💰 Harga Produk (Yuan)",
            min_value=0.0,
            step=1.0,
            format="%.2f",
            help="Masukkan harga dalam Yuan (RMB)",
            key="cn_price"
        )

        cn_ongkir_input = st.number_input(
            "🚚 Ongkir Lokal China (Yuan)",
            min_value=0,
            value=int(ongkir_ch_default),
            step=1,
            help="Range: 1-1000 Yuan",
            key="cn_ongkir"
        )

    with col2:
        cn_people = st.slider(
            "👥 Jumlah Sharing (Orang)",
            min_value=1,
            max_value=50,
            value=1,
            step=1,
            help="Jumlah orang dalam Group Order",
            key="cn_people"
        )

    # Calculation
    cn_total, cn_item_idr, cn_shared_fees = calculate_china(
        cn_price_input, cn_ongkir_input, cn_people, rate_ch, jasa_tf_ch, admin_go
    )
    cn_total_rounded = round(cn_total, -2)

    st.markdown(f"""
    <div class="result-card-cn">  <h3 style="margin:0; color: #c53030;">🇨🇳 Total Estimation</h3>
    <p style="font-size: 24px; font-weight: bold; margin: 10px 0;">
        Rp {cn_total_rounded:,.0f}
    </p>
    <p style="margin:0; font-size: 14px; opacity: 0.8;">
        Rate: {rate_ch} | Ongkir: {cn_ongkir_input} Yuan
    </p>
    </div>
    """, unsafe_allow_html=True)