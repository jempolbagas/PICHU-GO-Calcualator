# modules/config_manager.py
import streamlit as st
import pandas as pd

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

# Cache TTL in seconds (5 minutes)
CACHE_TTL_SECONDS = 300

@st.cache_data(ttl=CACHE_TTL_SECONDS) # Check for updates every 5 minutes
def get_config():
    try:
        sheet_id = st.secrets.get("SHEET_ID")
    except Exception:
        sheet_id = None

    if not sheet_id or sheet_id == "YOUR_SHEET_ID_HERE":
        print("⚠️ SHEET_ID is missing. Using default configuration.")
        return DEFAULT_CONFIG, "⚠️ Default (Sheet ID Not Set)"
    
    csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
    
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