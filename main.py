import streamlit as st

# --- 1. CONFIGURACIÓN MÓVIL Y ESTÉTICA NEON ---
st.set_page_config(
    page_title="DIMELO GOLD", 
    page_icon="🎙️", 
    layout="centered", # Centrado para mejor vista en celular
    initial_sidebar_state="collapsed"
)

# Estética Neon Night + Gold Supreme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    
    /* Fondo oscuro profundo */
    .stApp {
        background-color: #0d0d0f;
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Encabezado con Logo y Estilo */
    .header-container {
        text-align: center;
        padding: 20px 0;
        background: linear-gradient(180deg, #1a1a1f 0%, #0d0d0f 100%);
        border-bottom: 1px solid #3c096c;
        margin-bottom: 20px;
    }
    
    .logo-text {
        font-size: 28px;
        font-weight: 700;
        letter-spacing: 2px;
        color: white;
    }
    
    .gold-word { color: #D4AF37; }
    .purple-word { color: #9d4edd; }

    /* Burbujas de Pedagogía Estilo Chat */
    .bubble {
        background: #16161a;
        border: 1px solid #3c096c;
        padding: 20px;
        border-radius: 20px 20px 20px 5px;
        margin: 15px 0;
        color: #e0e0e0;
        font-size: 14px;
        line-height: 1.6;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }

    /* Botón Neon Principal */
    div.stButton > button {
        background: linear-gradient(90deg, #7b2cbf, #5a189a) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px;
        height: 3.8em;
        font-weight: 700;
        width: 100%;
        margin-top: 10px;
        box-shadow: 0 4px 15px rgba(123, 44, 191, 0.4);
    }

    /* Caja del Micrófono (Foco Visual) */
    .mic-section {
        border: 2px solid #9d4edd;
        background: rgba(157, 78, 221, 0.05);
        border-radius: 25px;
        padding: 30px;
        text-align: center;
        margin: 20px 0;
    }

    /* Ajustes de inputs para celular */
    .stTextInput input {
        background-color: #1a1a20 !important;
        color: white !important;
        border: 1px solid #3c096c !important;
        border-radius: 12px !important;
    }
    
    h3 { color: #9d4edd; font-size: 18px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ---
