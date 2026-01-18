# modules/styles.py

HIDE_ST_STYLE = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

GLOBAL_CSS = """
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

    /* 3. KOREA CARD INNER TYPOGRAPHY */
    .glass-card-kr h1 {
        font-size: 3rem;
        font-weight: 800;
        margin: 10px 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.05);
        background: -webkit-linear-gradient(45deg, #702459, #B83280);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
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

    /* EXISTING CHINA STYLES */
    .result-card-cn {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 16px;
        border: 2px solid #fff5f5;
        border-left: 8px solid #e53e3e;
        box-shadow: 0 10px 25px -5px rgba(229, 62, 62, 0.15);
        margin-top: 20px;
        color: #742a2a;
    }

    /* 4. THE FLOATING ISLAND */
    div[data-baseweb="tab-list"] {
        display: flex !important;
        flex-direction: row !important;
        gap: 10px !important;
        background-color: rgba(255, 255, 255, 0.25) !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        border-radius: 50px !important;
        padding: 6px !important;
    }

    div[data-baseweb="tab"] {
        border-radius: 50px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        border: none !important;
        margin: 0 !important;
    }

    div[data-baseweb="tab"][aria-selected="true"] {
        background: #FFFFFF !important;
        color: #D53F8C !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        position: relative !important;
    }

    div[data-baseweb="tab"][aria-selected="false"] {
        background: transparent !important;
        color: rgba(112, 36, 89, 0.6) !important;
    }

    div[data-baseweb="tab-highlight"], div[data-baseweb="tab-border"] {
        display: none !important;
    }

    /* 5. GLASSY INPUTS */
    div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.5) !important;
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.8) !important;
        border-radius: 12px !important;
    }

    div[data-baseweb="input"] input {
        color: #2D3748 !important;
        font-weight: 600 !important;
    }

    /* 6. EXCHANGE RATE PILL */
    .glass-pill {
        background-color: rgba(255, 255, 255, 0.4);
        border-radius: 50px;
        border: 1px solid rgba(255, 255, 255, 0.5);
        font-size: 0.9rem;
        padding: 10px 20px;
        text-align: center;
        margin-bottom: 15px;
        font-weight: 600;
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
    }
    </style>
"""