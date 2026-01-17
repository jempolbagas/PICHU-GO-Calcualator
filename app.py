import streamlit as st
import pandas as pd

# --- CONFIGURATION ---
try:
    SHEET_ID = st.secrets.get("SHEET_ID")
except Exception:
    SHEET_ID = None

# Defaults (Used if sheet is unreachable or internet is down)
DEFAULT_CONFIG = {
    'rate': 15,        # 1 KRW = 15 IDR
    'admin_go': 6000,  # Fee Tetap per Barang
    'jasa_tf': 6000,  # Fee Transfer (Shared)
    'ongkir_kr': 2000  # Default Shipping KRW (Standard)
}

st.set_page_config(page_title="PICHU GO CALCULATOR", page_icon="🇰🇷")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* Reduce top padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Result Card Styling */
    .result-card {
        background-color: white;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border: 2px solid #319795; /* Teal */
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
    }
    .result-card h2 {
        color: #319795;
        margin: 0;
        font-weight: bold;
    }
    .result-card p {
        margin: 0;
        font-size: 0.9rem;
        color: #2c7a7b;
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

st.title("🇰🇷 PICHU GO CALCULATOR")
st.info(f"💱 Exchange Rate: 1 KRW = {config.get('rate', 15)} IDR")

# --- SIDEBAR STATUS ---
if "Live" in status:
    st.sidebar.success(f"Data Source: {status}")
else:
    st.sidebar.warning(f"Data Source: {status}")

if not SHEET_ID or SHEET_ID == "YOUR_SHEET_ID_HERE":
    st.sidebar.warning("⚠️ SHEET_ID is missing. Using default configuration.")

# --- INPUTS ---
col1, col2 = st.columns(2)

with col1:
    harga_input = st.number_input(
        "💰 Harga Produk (0.1 = 1,000 Won)", 
        min_value=0.0, 
        step=0.01, 
        format="%.2f",
        help="Masukkan 1.0 untuk 10,000 KRW"
    )
    
    default_ongkir = config.get('ongkir_kr', 2000)
    ongkir_input = st.number_input(
        "🚚 Ongkir Lokal Korea (Won)",
        min_value=0,
        value=int(default_ongkir),
        step=500,
        help="Biasanya 2000-4000 Won. Ubah jika beda."
    )

with col2:
    pembeli = st.slider(
        "👥 Jumlah Sharing (Orang)", 
        min_value=1,
        max_value=20,
        value=1, 
        step=1,
        help="Jumlah orang dalam Group Order"
    )

# --- CALCULATION LOGIC ---
# 1. Config Values
rate = config.get('rate', 15)
admin_go = config.get('admin_go', 5000)
jasa_tf = config.get('jasa_tf', 10000)

# 2. Logic
item_krw = harga_input * 10000
item_idr = item_krw * rate

# 3. Sharing Cost
shipping_idr = ongkir_input * rate
total_shared_cost = shipping_idr + jasa_tf
shared_cost_per_person = total_shared_cost / pembeli

# Total
total = item_idr + admin_go + shared_cost_per_person
total_rounded = round(total, -2)

# --- DISPLAY ---
st.markdown(f"""
<div class="result-card">
    <h2>Rp {total_rounded:,.0f}</h2>
    <p>Harga Bersih per Item</p>
</div>
""", unsafe_allow_html=True)

with st.expander("📝 Rincian Biaya (Klik untuk lihat)"):
    st.write(f"Harga Barang: Rp {item_idr:,.0f} (Rate {rate})")
    st.write(f"Admin GO: Rp {admin_go:,.0f}")
    st.write(f"Sharing ({pembeli} org): Rp {shared_cost_per_person:,.0f}/org")
    st.caption(f"(Ongkir {ongkir_input} KRW + Jasa TF {jasa_tf}) ÷ {pembeli}")
