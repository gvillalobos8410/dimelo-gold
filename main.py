import streamlit as st

# --- 1. CONFIGURACIÓN DE AUTORIDAD Y ESTÉTICA ---
st.set_page_config(
    page_title="DIMELO GOLD", 
    page_icon="🎙️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inyección de ADN Visual (Púrpura, Oro y Profundidad)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap');
    
    .stApp {
        background: radial-gradient(circle at top, #1a0b2e 0%, #050505 100%) !important;
        color: #f0f0f0 !important;
        font-family: 'Montserrat', sans-serif;
    }

    /* Encabezado con Logo Adherido */
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
        margin: 0;
        line-height: 1;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 5px;
    }
    
    .purple { color: #9d4edd; text-shadow: 0 0 15px rgba(157, 78, 221, 0.5); }
    .gold { color: #D4AF37; text-shadow: 0 0 10px rgba(212, 175, 55, 0.3); }

    /* Burbujas de Pedagogía (Chat de Autoridad) */
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
        letter-spacing: 1.5px;
        margin-bottom: 8px;
        display: block;
    }

    /* Botón Neon Gold Supreme */
    div.stButton > button {
        background: linear-gradient(90deg, #7b2cbf, #9d4edd) !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        height: 4em !important;
        font-weight: 700 !important;
        width: 100% !important;
        box-shadow: 0 8px 20px rgba(123, 44, 191, 0.3) !important;
        text-transform: uppercase;
    }

    /* Estilo para Inputs en Móvil */
    input, .stSelectbox {
        background-color: rgba(0,0,0,0.4) !important;
        border: 1px solid #3c096c !important;
        border-radius: 12px !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. PÁGINA DE INICIO: EL DESPERTAR DE DIMELO ---

st.markdown("""
    <div class="brand-header">
