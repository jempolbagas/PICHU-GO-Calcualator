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

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Result Card Styling */
    .result-card {
        background-color: white;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(213, 63, 140, 0.15); /* Soft pink shadow */
        border: 2px solid #D53F8C; /* Deep Pink Border */
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
    }
    .result-card h2 {
        color: #D53F8C; /* Deep Pink Text */
        margin: 0;
        font-weight: 800;
        font-size: 2.5rem;
    }
    .result-card p {
        margin: 0;
        font-size: 1rem;
        color: #718096; /* Soft Grey for subtitle */
        font-weight: 500;
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

    st.info(f"💱 Exchange Rate: 1 KRW = {rate_kr} IDR")

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
    <div class="result-card">
        <h2>Rp {kr_total_rounded:,.0f}</h2>
        <p>Harga Bersih per Item</p>
    </div>
    """, unsafe_allow_html=True)

# --- CHINA TAB ---
with tab_ch:
    # Configs
    rate_ch = config.get('rate_ch', 2450)
    jasa_tf_ch = config.get('jasa_tf_ch', 10000)
    ongkir_ch_default = config.get('ongkir_ch_default', 100)

    st.info(f"💱 Exchange Rate: 1 CNY = {rate_ch} IDR")

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
    <div class="result-card">
        <h2>Rp {cn_total_rounded:,.0f}</h2>
        <p>Harga Bersih per Item</p>
    </div>
    """, unsafe_allow_html=True)
