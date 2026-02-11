import streamlit as st

# --- 1. CONFIGURACIÓN DE ESCENARIO PRO ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered", initial_sidebar_state="collapsed")

# Colores extraídos del Logo: Púrpura (#8a2be2) y Oro (#D4AF37)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap');
    
    .stApp {
        background: radial-gradient(circle at top, #1a0b2e 0%, #050505 100%) !important;
        color: #f0f0f0 !important;
        font-family: 'Montserrat', sans-serif;
    }

    /* Encabezado con el Logo */
    .brand-container {
        text-align: center;
        padding: 20px 0;
        margin-bottom: 10px;
    }
    
    .logo-main {
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1.5px;
        margin: 0;
        line-height: 1;
    }
    
    .purple-brand { color: #9d4edd; text-shadow: 0 0 20px rgba(157, 78, 221, 0.6); }
    .gold-brand { color: #D4AF37; text-shadow: 0 0 15px rgba(212, 175, 55, 0.4); }

    /* Tarjetas de Proceso (Estilo Celular) */
    .pro-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(157, 78, 221, 0.3);
        padding: 22px;
        border-radius: 24px;
        margin-bottom: 18px;
        backdrop-filter: blur(12px);
    }

    /* Pedagogía con los colores del logo */
    .pedagogia-text {
        color: #D4AF37;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
        display: block;
    }

    /* Botón Neon con el Púrpura del Logo */
    div.stButton > button {
        background: linear-gradient(90deg, #7b2cbf 0%, #9d4edd 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 18px !important;
        height: 3.8em !important;
        font-weight: 800 !important;
        width: 100% !important;
        box-shadow: 0 10px 25px rgba(123, 44, 191, 0.4) !important;
        transition: 0.3s;
    }
    
    /* Inputs Estilizados */
    input { 
        background-color: rgba(0,0,0,0.3) !important; 
        color: white !important; 
        border: 1px solid #3c096c !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. PÁGINA DE INICIO (LOGO ADHERIDO) ---

st.markdown("""
    <div class="brand-container">
        <div class="logo-main">
            <span class="purple-brand">DIMÉLO</span><span class="gold-brand">GOLD</span>
        </div>
        <p style="color: #9d4edd; font-weight: 600; font-size: 12px; margin-top: 5px; opacity: 0.8;">
            INGENIERÍA DE AUTORIDAD COMERCIAL
        </p>
    </div>
    """, unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 1

# --- 3. FLUJO INMERSIVO ---
