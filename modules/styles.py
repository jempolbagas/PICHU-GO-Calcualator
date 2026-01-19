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

    /* 3.1. CHINA GLASS CARD CONTAINER */
    .glass-card-cn {
        background: rgba(255, 255, 255, 0.65);
        box-shadow: 0 8px 32px 0 rgba(229, 62, 62, 0.20); /* Red Shadow */
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 24px;
        padding: 30px;
        margin-top: 20px;
        text-align: center;
        font-family: 'Poppins', sans-serif;
    }

    /* 3.2. CHINA CARD TYPOGRAPHY */
    .glass-card-cn h1 {
        font-size: 3rem;
        font-weight: 800;
        margin: 10px 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.05);
        background: -webkit-linear-gradient(45deg, #742a2a, #c53030); /* Red Gradient */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .glass-card-cn p.label {
        color: #9B2C2C; /* Dark Red */
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin: 0;
    }

    .glass-card-cn .breakdown-pill {
        display: inline-flex;
        gap: 15px;
        background: rgba(255,255,255,0.5);
        padding: 8px 20px;
        border-radius: 30px;
        font-size: 0.9rem;
        color: #742a2a;
        margin-top: 10px;
    }

    /* 4. THE FLOATING ISLAND (ROBUST FIX) */

    /* Target the container */
    [data-baseweb="tab-list"] {
        display: flex !important;
        justify-content: center !important;
        background-color: rgba(255, 255, 255, 0.4) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
        padding: 6px !important;
        border-radius: 50px !important;
        gap: 8px !important;
        width: fit-content !important;
        margin: 0 auto 20px auto !important; /* Center the whole pill on screen */
    }

    /* Target the Individual Tab Button (Handles both div and button tags) */
    [data-baseweb="tab"] {
        background-color: transparent !important;
        border: none !important;
        border-radius: 40px !important;
        padding: 8px 30px !important; /* Force wider clickable area */
        color: rgba(112, 36, 89, 0.7) !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
        height: auto !important;
    }

    /* Target Text inside the tab to ensure it inherits color */
    [data-baseweb="tab"] > div, [data-baseweb="tab"] > p {
        color: inherit !important; 
    }

    /* Active Tab State */
    [data-baseweb="tab"][aria-selected="true"] {
        background-color: #D53F8C !important;
        color: white !important;
        box-shadow: 0 4px 10px rgba(213, 63, 140, 0.3) !important;
    }

    /* Remove the default red line Streamlit adds */
    [data-baseweb="tab-highlight"], [data-baseweb="tab-border"] {
        display: none !important;
        visibility: hidden !important;
    }


    /* 5. UNIFIED GLASS CAPSULE INPUT */

    div[data-baseweb="base-input"] {
        background-color: rgba(255, 255, 255, 0.5) !important; /* Glass Background */
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.8) !important; /* White border */
        border-radius: 50px !important; /* Fully rounded capsule */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        padding: 0px 5px; /* Slight padding for inner breathing room */
        gap: 0px !important; /* Remove gap between text and buttons */
    }

        padding: 0 5px; /* Slight padding for inner breathing room */
        gap: 0 !important; /* Remove gap between text and buttons */
    div[data-baseweb="base-input"] input {
        background-color: transparent !important;
        color: #2D3748 !important; /* Dark Slate text */
        font-weight: 700 !important;
        padding-left: 15px !important; /* Center text better */
    }

    /* This removes the "Pink Block" background from the stepper container on the right */
    div[data-baseweb="base-input"] > div:last-child {
        background-color: transparent !important;
        border: none !important; /* Remove the vertical divider line */
        margin-right: 5px; 
    }

    /* 6. BEAUTIFY STEPPER BUTTONS (+ and -) */

    /* Step C: Turn the square buttons into Floating Circles */
    div[data-baseweb="base-input"] [role="button"] {
        background-color: rgba(255, 255, 255, 0.4) !important; /* Subtle white circle */
        border-radius: 50% !important; /* Make them circles */
        color: #702459 !important; /* Deep Pink Icon Color */
        width: 32px !important;
        height: 32px !important;
        min-width: 32px !important; /* Enforce circle shape */
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        border: 1px solid rgba(255,255,255,0.6) !important;
        margin-left: 5px !important; /* Space between the buttons */
        transition: all 0.2s ease !important;
    }

    /* Hover Effect: Bright Pink Glow */
    div[data-baseweb="base-input"] [role="button"]:hover {
        background-color: #D53F8C !important; /* Pink background on hover */
        color: white !important; /* White icon on hover */
        transform: scale(1.1); /* Slight grow effect */
        box-shadow: 0 4px 10px rgba(213, 63, 140, 0.3);
        border-color: #D53F8C !important;
    }

    /* Remove the default focus border (The Blue Ring) */
    div[data-baseweb="base-input"]:focus-within {
        border-color: #D53F8C !important;
        box-shadow: 0 0 0 3px rgba(213, 63, 140, 0.2) !important;
    }

    /* 7. EXCHANGE RATE PILL */
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