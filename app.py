import streamlit as st
import pandas as pd

# --- CONFIGURATION ---
try:
    SHEET_ID = st.secrets.get("SHEET_ID")
except Exception:
    SHEET_ID = None

# Defaults (Used if sheet is unreachable or internet is down)
DEFAULT_CONFIG = {
    'admin_go': 6000,
    'rate_kr': 11.75,
    'jasa_tf_kr': 6000,
    'ongkir_kr_default': 2000,
    'rate_ch': 2450,
    'jasa_tf_ch': 10000,
    'ongkir_ch_default': 100
}

st.set_page_config(page_title="PICHU GO CALCULATOR", page_icon="🇰🇷")

hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }
    
    /* 1. GLOBAL AURORA BACKGROUND */
    .stApp {
        background-color: #FFF5F7;
        background-image:
            radial-gradient(at 10% 10%, hsla(333, 100%, 86%, 1) 0, transparent 50%),
            radial-gradient(at 90% 90%, hsla(320, 100%, 90%, 1) 0, transparent 50%);
        background-attachment: fixed;
        background-size: cover;
    }

    /* Clean up the top spacing */
    .block-container {
        padding-top: 2rem;
    }

    /* 2. KOREA GLASS CARD CONTAINER */
    .glass-card-kr {
        background: rgba(255, 255, 255, 0.65);
        box-shadow: 0 8px 32px 0 rgba(213, 63, 140, 0.20);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 24px;
        padding: 30px;
        margin-top: 20px;
        text-align: center;
        font-family: 'Poppins', sans-serif;
    }

    /* 3. KOREA CARD INNER TYPOGRAPHY (Cleaned from Python) */
    .glass-card-kr h1 {
        color: #702459;
        font-size: 3rem;
        font-weight: 800;
        margin: 10px 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    .glass-card-kr p.label {
        color: #97266D;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin: 0;
    }

    .glass-card-kr .breakdown-pill {
        display: inline-flex;
        gap: 15px;
        background: rgba(255,255,255,0.5);
        padding: 8px 20px;
        border-radius: 30px;
        font-size: 0.9rem;
        color: #702459;
        margin-top: 10px;
    }

    /* EXISTING CHINA STYLES (UNTOUCHED) */
    .result-card-cn {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 16px;
        border: 2px solid #fff5f5;
        border-left: 8px solid #e53e3e;
        box-shadow: 0 10px 25px -5px rgba(229, 62, 62, 0.15); /* Red glow */
        margin-top: 20px;
        color: #742a2a;
    }
    </style>
""", unsafe_allow_html=True)

# --- HELPER: FETCH DATA FROM GOOGLE SHEET ---
@st.cache_data(ttl=300) # Check for updates every 5 minutes
def get_config():
    if not SHEET_ID or SHEET_ID == "YOUR_SHEET_ID_HERE":
        print("⚠️ SHEET_ID is missing. Using default configuration.")
        return DEFAULT_CONFIG, "⚠️ Default (Sheet ID Not Set)"
    
    csv_url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"
    
    try:
        df = pd.read_csv(csv_url, header=None, names=['key', 'value'])
        fetched_config = pd.Series(df.value.values, index=df.key).to_dict()
        
        # Start with defaults to ensure all keys exist
        config = DEFAULT_CONFIG.copy()

        # Update with fetched values, validating types
        for key in config:
            if key in fetched_config:
                try:
                    config[key] = float(fetched_config[key])
                except (ValueError, TypeError):
                    print(f"⚠️ Invalid value for '{key}': {fetched_config[key]}. Using default.")
            else:
                print(f"⚠️ Key '{key}' missing in Google Sheet. Using default.")

        return config, "✅ Live from Database"
    except Exception as e:
        print(f"Error fetching Google Sheet: {e}")
        return DEFAULT_CONFIG, "⚠️ Connection Failed (Using Defaults)"

# --- APP START ---
config, status = get_config()

st.title("PICHU GO CALCULATOR")

# --- SIDEBAR STATUS ---
if "Live" in status:
    st.sidebar.success(f"Data Source: {status}")
else:
    st.sidebar.warning(f"Data Source: {status}")

if not SHEET_ID or SHEET_ID == "YOUR_SHEET_ID_HERE":
    st.sidebar.warning("⚠️ SHEET_ID is missing. Using default configuration.")

# --- TABS ---
tab_kr, tab_ch = st.tabs(["🇰🇷 Korea", "🇨🇳 China"])

# --- COMMON VARIABLES ---
admin_go = config.get('admin_go', 6000)

# --- KOREA TAB ---
with tab_kr:
    # Configs
    rate_kr = config.get('rate_kr', 11.75)
    jasa_tf_kr = config.get('jasa_tf_kr', 6000)
    ongkir_kr_default = config.get('ongkir_kr_default', 2000)

    st.markdown(f"""
    <div style="background-color: rgba(255, 255, 255, 0.5); 
                padding: 10px 15px; 
                border-radius: 10px; 
                border: 1px solid #d53f8c; 
                color: #d53f8c; 
                font-weight: 600; 
                text-align: center; 
                margin-bottom: 15px;">
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

    # Logic
    # Item_Price_IDR = (Input_Value * 10000) * rate_kr
    kr_item_idr = (kr_price_input * 10000) * rate_kr
    
    # Shared_Fees_IDR = (Ongkir_Input * rate_kr + jasa_tf_kr) / Number_of_People
    kr_shared_fees = (kr_ongkir_input * rate_kr + jasa_tf_kr) / kr_people

    # Total
    kr_total = kr_item_idr + admin_go + kr_shared_fees
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
    # Configs
    rate_ch = config.get('rate_ch', 2450)
    jasa_tf_ch = config.get('jasa_tf_ch', 10000)
    ongkir_ch_default = config.get('ongkir_ch_default', 100)

    st.markdown(f"""
    <div style="background-color: rgba(255, 255, 255, 0.5); 
                padding: 10px 15px; 
                border-radius: 10px; 
                border: 1px solid #c53030; 
                color: #c53030; 
                font-weight: 600; 
                text-align: center; 
                margin-bottom: 15px;">
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

    # Logic
    # Item_Price_IDR = Input_Value * rate_ch
    cn_item_idr = cn_price_input * rate_ch

    # Shared_Fees_IDR = (Ongkir_Input * rate_ch + jasa_tf_ch) / Number_of_People
    cn_shared_fees = (cn_ongkir_input * rate_ch + jasa_tf_ch) / cn_people

    # Total
    cn_total = cn_item_idr + admin_go + cn_shared_fees
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
