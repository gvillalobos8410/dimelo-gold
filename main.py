import streamlit as st

# --- 1. CONFIGURACIÓN DE NIVEL ÉLITE ---
st.set_page_config(page_title="DIMELO GOLD", page_icon="🎙️", layout="centered")

# Estética Neon, Gold y Scroll Fluido
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap');
    
    .stApp {
        background: radial-gradient(circle at top, #1a0b2e 0%, #050505 100%) !important;
        color: #f0f0f0 !important;
        font-family: 'Montserrat', sans-serif;
    }
    
    .main-logo {
        text-align: center;
        padding: 40px 0;
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1.5px;
    }
    .purple { color: #9d4edd; text-shadow: 0 0 20px rgba(157, 78, 221, 0.6); }
    .gold { color: #D4AF37; text-shadow: 0 0 15px rgba(212, 175, 55, 0.4); }

    .card-scroll {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(157, 78, 221, 0.2);
        padding: 30px;
        border-radius: 30px;
        margin-bottom: 40px;
        backdrop-filter: blur(15px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }

    .pedagogia-title {
        color: #D4AF37;
        font-size: 12px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 15px;
        display: block;
    }

    /* Botón Logo DIMELO (Sustituye al micrófono) */
    .dimelo-btn-container {
        text-align: center;
        margin: 30px 0;
    }
    
    .dimelo-logo-btn {
        background: linear-gradient(135deg, #7b2cbf 0%, #9d4edd 100%);
        width: 100px;
        height: 100px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border: 4px solid #D4AF37;
        box-shadow: 0 0 30px rgba(157, 78, 221, 0.5);
        cursor: pointer;
        transition: 0.3s;
    }
    
    .dimelo-logo-btn:hover {
        transform: scale(1.1);
        box-shadow: 0 0 50px rgba(212, 175, 55, 0.6);
    }

    div.stButton > button {
        background: linear-gradient(90deg, #7b2cbf, #9d4edd) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        height: 3.5em !important;
        font-weight: 700 !important;
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. ENCABEZADO DIMELO ---
st.markdown("""
<div class="main-logo">
    <span class="purple">DIMÉLO</span><span class="gold">GOLD</span>
</div>
<p style='text-align: center; color: #888; font-size: 14px;'>INGENIERÍA DE AUTORIDAD COMERCIAL</p>
""", unsafe_allow_html=True)

# --- 3. SCROLL INMERSIVO (PEDAGOGÍA BLINDADA) ---

# FASE 1: IDENTIDAD
st.markdown('<div class="card-scroll">', unsafe_allow_html=True)
st.markdown('<span class="pedagogia-title">Fase 1: La Firma de Autoridad</span>', unsafe_allow_html=True)
st.markdown("""
**CÁTEDRA DEL PROFESOR:** Bienvenido al entorno donde tu palabra cobra valor. 
En el mercado de alto nivel, **tu nombre no es un dato, es tu activo más preciado**. 
Es la firma que respalda tu visión técnica y espiritual. Sin ella, no hay puente de confianza.
""")
nombre = st.text_input("¿Quién lidera hoy?", placeholder="Ej: Germán Villalobos")
st.markdown('</div>', unsafe_allow_html=True)

# FASE 2: BLINDAJE LEGAL
st.markdown('<div class="card-scroll">', unsafe_allow_html=True)
st.markdown('<span class="pedagogia-title">Fase 2: Blindaje Legal DIAN</span>', unsafe_allow_html=True)
st.markdown("""
**AVISO LEGAL - EL ESTÁNDAR DE PODER:** "Tu talento es inmenso, pero para que sea cobrable, debe estar blindado. 
La formalidad ante la DIAN no es una carga, es tu **armadura profesional**. 
Definir tu ruta legal asegura que tu
