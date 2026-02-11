import streamlit as st

# --- 1. CONFIGURACIÓN DE AUTORIDAD ---
st.set_page_config(page_title="DIMELO GOLD", page_icon="🎙️", layout="centered")

# Estética Neon & Gold Supreme
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
        padding: 30px 10px;
        background: linear-gradient(180deg, rgba(26,11,46,0.8) 0%, rgba(5,5,5,0) 100%);
        border-bottom: 1px solid rgba(157, 78, 221, 0.3);
        margin-bottom: 30px;
    }
    .logo-main { font-size: 38px; font-weight: 800; letter-spacing: -1px; }
    .purple { color: #9d4edd; text-shadow: 0 0 15px rgba(157, 78, 221, 0.5); }
    .gold { color: #D4AF37; text-shadow: 0 0 10px rgba(212, 175, 55, 0.3); }
    .card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(157, 78, 221, 0.2);
        padding: 22px;
        border-radius: 25px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }
    .pedagogia-label {
        color: #D4AF37;
        font-size: 11px;
        font-weight: 800;
        text-transform: uppercase;
        display: block;
        margin-bottom: 10px;
    }
    div.stButton > button {
        background: linear-gradient(90deg, #7b2cbf, #9d4edd) !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        height: 4em !important;
        font-weight: 700 !important;
        width: 100% !important;
        box-shadow: 0 8px 20px rgba(123, 44, 191, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. ENCABEZADO Y LOGO ---
st.markdown("""
<div class="brand-header">
    <div class="logo-main">
        <span class="purple">DIMÉLO</span> <span class="gold">GOLD</span>
    </div>
    <p style='color: #888; font-size: 13px; margin-top: 8px;'>INGENIERÍA DE AUTORIDAD COMERCIAL</p>
</div>
""", unsafe_allow_html=True)

# Inicialización de estado
if 'paso' not in st.session_state:
    st.session_state.paso = 1

# --- 3. FLUJO DE REGISTRO ---

# PASO 1: IDENTIDAD
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<span class="pedagogia-label">🎙️ Identidad del Líder</span>', unsafe_allow_html=True)
    st.write("Tu nombre es la firma que respalda tu visión.")
    nombre = st.text_input("NOMBRE COMPLETO:", key="nombre_lider", placeholder="Ej: Germán Villalobos")
    
    if nombre and st.session_state.paso == 1:
        if st.button("CONFIGURAR IDENTIDAD ➡️"):
            st.session_state.paso = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# PASO 2: BLINDAJE LEGAL
if st.session_state.paso >= 2:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<span class="pedagogia-label">🛡️ Respaldo Legal DIAN</span>', unsafe_allow_html=True)
        sector = st.selectbox
