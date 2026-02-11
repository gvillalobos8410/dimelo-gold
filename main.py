import streamlit as st

# --- 1. CONFIGURACIÓN DE AUTORIDAD ---
st.set_page_config(
    page_title="DIMELO GOLD", 
    page_icon="🎙️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ADN Visual: Púrpura Neon y Oro Supreme
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
        padding: 40px 10px 20px 10px;
        background: linear-gradient(180deg, rgba(26,11,46,0.8) 0%, rgba(5,5,5,0) 100%);
        border-bottom: 1px solid rgba(157, 78, 221, 0.3);
        margin-bottom: 30px;
    }
    .logo-main {
        font-size: 38px;
        font-weight: 800;
        letter-spacing: -1.5px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 5px;
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
        
