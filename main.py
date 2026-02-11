import streamlit as st

# --- 1. CONFIGURACIÓN DE ESCENARIO ---
st.set_page_config(page_title="DIMELO GOLD", page_icon="🎙️", layout="centered")

# ADN Visual Blindado (Evitando errores de comillas)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap');
    
    .stApp {
        background: radial-gradient(circle at top, #1a0b2e 0%, #050505 100%) !important;
        color: #f0f0f0 !important;
        font-family: 'Montserrat', sans-serif;
    }
    
    .header-logo {
        text-align: center;
        padding: 50px 10px;
    }
    
    .logo-text {
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1px;
    }
    
    .purple { color: #9d4edd; text-shadow: 0 0 15px rgba(157, 78, 221, 0.5); }
    .gold { color: #D4AF37; text-shadow: 0 0 10px rgba(212, 175, 55, 0.3); }

    .card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(157, 78, 221, 0.2);
        padding: 25px;
        border-radius: 25px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }

    .label-gold {
        color: #D4AF37;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 10px;
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
        box-shadow: 0 8px 20px rgba(123, 44, 191, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. INTERFAZ DE INICIO ---

st.markdown("""
<div class="header-logo">
    <div class="logo-text">
        <span class="purple">DIMÉLO</span> <span class="gold">GOLD</span>
    </div>
    <p style='color: #888; font-size: 14px; margin-top: 10px;'>INGENIERÍA DE AUTORIDAD COMERCIAL</p>
</div>
""", unsafe_allow_html=True)

# Lógica de flujo simple
if 'paso' not in st.session_state:
    st.session_state.paso = 1

# --- BLOQUE 1: IDENTIDAD ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<span class="label-gold">🛡️ Paso 1: Identidad del Líder</span>', unsafe_allow_html=True)
st.write("Tu nombre es la firma que respalda tu visión técnica y comercial.")
nombre = st.text_input("NOMBRE COMPLETO:", placeholder="Ej: Germán Villalobos")

if nombre and st.session_state.paso == 1:
    if st.button("REGISTRAR IDENTIDAD ➡️"):
        st.session_state.paso = 2
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# --- BLOQUE 2: BLINDAJE LEGAL ---
if st.session_state.paso >= 2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<span class="label-gold">🏛️ Paso 2: Respaldo DIAN</span>', unsafe_allow_html=True)
    st.write(f"Perfecto, **{nombre}**. Define tu ruta legal para asegurar el estatus de tu oferta.")
    
    sector = st.selectbox("SECTOR ESTRATÉGICO:", ["🌾 Agropecuario", "🛠️ Servicios Técnicos", "⚖️ Consultoría", "✨ Otro"])
    ruta = st.radio("MODALIDAD DE COBRO:", ["Cuenta de Cobro", "Cotización Formal"])
    
    if st.session_state.paso == 2:
        if st.button("ACTIVAR MOTOR DE PRECISIÓN 🚀"):
            st.session_state.paso = 3
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- BLOQUE 3: EL MOTOR ---
if st.session_state.paso >= 3:
    st.markdown("""
    <div class="card" style="border: 2px solid #D4AF37; text-align: center;">
        <span class="label-gold">🎙️ Paso 3: Motor de Precisión Activo</span>
        <h2 style='color: white; margin: 10px 0;'>TE ESCUCHO</h2>
        <p style='font-size: 14px; color: #9d4edd;'>Dicta tu propuesta comercial ahora.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔴 INICIAR GRABACIÓN POR VOZ"):
        st.info("🎤 Procesando tu visión a nivel Gold Supreme...")
