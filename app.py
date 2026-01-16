import streamlit as st
import pandas as pd

# --- CONFIGURATION ---
# 1. Create a Google Sheet (See INSTRUCTIONS.md)
# 2. Paste the ID (the text between /d/ and /edit in the URL) here:
SHEET_ID = "1_x-6kUiAe5UJh0iTNXbm13bUiLiZwPfBiE305q2vZgQ" 

# Defaults (Used if sheet is unreachable or internet is down)
DEFAULT_CONFIG = {
    'rate': 15,        # 1 KRW = 15 IDR
    'admin_go': 5000,  # Fee Tetap per Barang
    'jasa_tf': 10000,  # Fee Transfer (Shared)
    'ongkir_kr': 2000  # Default Shipping KRW (Standard)
}

st.set_page_config(page_title="Kalkulator Jastip", page_icon="🇰🇷")

# --- HELPER: FETCH DATA FROM GOOGLE SHEET ---
@st.cache_data(ttl=300) # Check for updates every 5 minutes
def get_config():
    if SHEET_ID == "YOUR_SHEET_ID_HERE":
        return DEFAULT_CONFIG, "⚠️ Default (Sheet ID Not Set)"
    
    csv_url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"
    
    try:
        # Read CSV. Expecting Column A (Name) and Column B (Value)
        df = pd.read_csv(csv_url, header=None, names=['key', 'value'])
        config = pd.Series(df.value.values, index=df.key).to_dict()
        
        # Ensure values are numbers
        for key in config:
            try:
                config[key] = float(config[key])
            except:
                pass 
        return config, "✅ Live from Google Sheet"
    except:
        return DEFAULT_CONFIG, "⚠️ Connection Failed (Using Defaults)"

# --- APP START ---
config, status = get_config()

st.title("🇰🇷 Kalkulator Jastip Pro")
st.caption(f"Status: {status}")

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
    # New Input: Ongkir Korea (Defaults to value from Sheet)
    default_ongkir = config.get('ongkir_kr', 2000)
    ongkir_input = st.number_input(
        "🚚 Ongkir Lokal Korea (Won)",
        min_value=0,
        value=int(default_ongkir),
        step=500,
        help="Biasanya 2000-4000 Won. Ubah jika beda."
    )

with col2:
    pembeli = st.number_input(
        "👥 Jumlah Sharing (Orang)", 
        min_value=1, 
        value=1, 
        step=1,
        help="Jumlah orang dalam Group Order"
    )

# --- CALCULATION LOGIC ---
if st.button("Hitung Harga Bersih", type="primary", use_container_width=True):
    # 1. Fetch Variables from Sheet
    rate = config.get('rate', 15)
    admin_go = config.get('admin_go', 5000)
    jasa_tf = config.get('jasa_tf', 10000)

    # 2. Logic
    item_krw = harga_input * 10000 
    item_idr = item_krw * rate
    
    # Shared Costs (Using the INPUT ongkir, not the fixed one)
    shipping_idr = ongkir_input * rate 
    total_shared_cost = shipping_idr + jasa_tf 
    shared_cost_per_person = total_shared_cost / pembeli 
    
    # Total
    total = item_idr + admin_go + shared_cost_per_person
    total_rounded = round(total, -2)

    # --- DISPLAY ---
    st.markdown(f"""
    <div style="text-align: center; padding: 20px; background-color: #e6fffa; border: 1px solid #b2f5ea; border-radius: 10px; margin-bottom: 20px;">
        <h2 style="color: #2c7a7b; margin:0;">Rp {total_rounded:,.0f}</h2>
        <p style="margin:0; font-size: 0.9rem; color: #285e61;">Harga Bersih per Item</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("📝 Rincian Biaya (Klik untuk lihat)"):
        st.write(f"Harga Barang: Rp {item_idr:,.0f} (Rate {rate})")
        st.write(f"Admin GO: Rp {admin_go:,.0f}")
        st.write(f"Sharing ({pembeli} org): Rp {shared_cost_per_person:,.0f}/org")
        st.caption(f"(Ongkir {ongkir_input} KRW + Jasa TF {jasa_tf}) ÷ {pembeli}")