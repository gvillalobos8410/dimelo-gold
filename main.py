import streamlit as st

# --- 1. CONFIGURACIÓN DE NIVEL ÉLITE ---
st.set_page_config(page_title="DIMELO GOLD", page_icon="🎙️", layout="centered")

# Inyectamos el diseño Neon y Gold de forma blindada
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap');
    .stApp {
        background: radial-gradient(circle at top, #1a0b2e 0%, #050505 100%) !important;
        color: #f0f0f0 !important;
        font-family: 'Montserrat', sans-serif;
    }
    .brand-header {
        text-align: center;
        padding: 40px 10px;
        background: linear-gradient(180deg, rgba(26,11,46,0.8) 0%, rgba(5,5,5,0) 100%);
        border-bottom: 1px solid rgba(157, 78, 221, 0.3);
        margin-bottom: 30px;
    }
    .logo-main {
        font-size: 38px;
        font-weight: 800;
        letter-spacing: -1px;
    }
    .purple { color: #9d4edd; text-shadow: 0 0 15px rgba(157, 78, 221, 0.5); }
    .gold { color: #D4AF37; text-shadow: 0 0 10px rgba(212, 175, 55, 0.3); }
    .chat-bubble {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(157, 78, 221, 0.2);
        padding: 22px;
        border-radius: 25px 25px 25px 5px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }
    .pedagogia-label {
        color: #D4AF37;
        font-size: 11px;
        font-weight: 800;
        text-transform: uppercase;
        margin-bottom: 8px;
        display: block;
    }
    div.stButton > button {
        background: linear-gradient(90deg, #7b2cbf, #9d4edd) !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        height: 4em !important;
        font-weight: 700 !important;
        width: 100% !important;
        box-shadow: 0 8px 20px rgba(123, 44, 191,
