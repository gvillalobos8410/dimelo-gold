import streamlit as st

# --- 1. CONFIGURACIÓN DE NIVEL ÉLITE ---
st.set_page_config(page_title="DIMELO GOLD", page_icon="🎙️", layout="centered")

# Estética Neon y Gold Supreme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap');
    .stApp {
        background: radial-gradient(circle at top, #1a0b2e 0%, #050505 100%) !important;
        color: #f0f0f0 !important;
        font-family: 'Montserrat', sans-serif;
    }
    .main-logo { text-align: center; padding: 30px 0; font-size: 38px; font-weight: 800; }
    .purple { color: #9d4edd; text-shadow: 0 0 15px rgba(157, 78, 221, 0.5); }
    .gold { color: #D4AF37; text-shadow: 0 0 10px rgba(212, 175, 55, 0.3); }
    .card-scroll {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(157, 78, 221, 0.2);
        padding: 25px;
        border-radius: 25px;
        margin-bottom: 30px;
        backdrop-filter: blur(10px);
    }
    .pedagogia-title {
        color: #D4AF37; font-size: 11px; font-weight: 800;
        text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 10px;
    }
    .dimelo-btn {
        background: linear-gradient(135deg, #7b2cbf 0%, #9d4edd 100%);
        width: 100px; height: 100px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        border: 4px solid #D4AF37; margin: 20px auto;
        box-shadow: 0 0 25px rgba(157, 78, 221, 0.5);
    }
    div.stButton > button {
        background: linear-gradient(90deg, #7b2cbf, #9d4edd) !important;
        color: white !important; border: none !important; border-radius: 15px !important;
        height: 3.5em !important; font-weight: 700 !important; width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. ENCABEZADO ---
st.markdown('<div class="main-logo"><span class="purple">DIMÉLO</span><span class="gold">GOLD</span></div>', unsafe_allow_html=True)

# --- 3. SCROLL INMERSIVO (PEDAGOGÍA) ---

# FASE 1: IDENTIDAD
st.markdown('<div class="card-scroll">', unsafe_allow_html=True)
st.markdown('<span class="pedagogia-title">Fase 1: La Firma de Autoridad</span>', unsafe_allow_html=True)
st.write("**CÁTEDRA DEL PROFESOR:** Bienvenido. En el mercado de alto nivel, **tu nombre no es un dato, es tu activo más preciado**. Es la firma que respalda tu visión técnica y espiritual.")
nombre = st.text_input("¿Quién lidera hoy?", placeholder="Ej: Germán Villalobos")
st.markdown('</div>', unsafe_allow_html=True)

# FASE 2: BLINDAJE LEGAL
st.markdown('<div class="card-scroll">', unsafe_allow_html=True)
st.markdown('<span class="pedagogia-title">Fase 2: Blindaje Legal DIAN</span>', unsafe_allow_html=True)
st.write("**AVISO LEGAL - EL ESTÁNDAR DE PODER:** Tu talento es inmenso, pero para que sea cobrable, debe estar blindado. La formalidad ante la DIAN es tu **armadura profesional**.")
sector = st.selectbox("Sector Estratégico:", ["Agro", "Técnico", "Consultoría", "Otro"])
ruta = st.radio("Ruta Legal:", ["Cuenta de Cobro", "Cotización Formal"])
st.markdown('</div>', unsafe_allow_html=True)

# FASE 3: TRANSMUTACIÓN (BOTÓN LOGO)
st.markdown('<div class="card-scroll" style="text-align: center;">', unsafe_allow_html=True)
st.markdown('<span class="pedagogia-title">Fase 3: Transmutación "VOZ A ORO"</span>', unsafe_allow_html=True)
st.write(f"**ESTÁS ACOMPAÑADO:** Háblame con la pasión de tu liderazgo. Mi algoritmo elevará tus palabras al estándar profesional por el cual tus
