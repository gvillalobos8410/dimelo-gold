import streamlit as st

# --- CONFIGURACIÓN DE NIVEL ÉLITE ---
st.set_page_config(page_title="DIMELO GOLD", page_icon="🏆", layout="wide")

# Estética Gold Supreme y Scroll Fluido
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Montserrat', sans-serif; }
    .main { background-color: #ffffff; }
    .gold-card { 
        padding: 30px; border-radius: 20px; border-left: 10px solid #D4AF37;
        background: #fdfdfd; box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 20px;
    }
    .stButton>button { 
        background-color: #1a1a1a; color: #D4AF37; border-radius: 12px; 
        font-weight: bold; width: 100%; height: 3em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NARRATIVA DE PEDAGOGÍA (EL SCROLL) ---

st.title("🏆 DIMELO: Tu Talento en Autoridad")

# SECCIÓN 1: IDENTIDAD
with st.container():
    st.markdown('<div class="gold-card">', unsafe_allow_html=True)
    st.subheader("1. Identidad del Líder")
    st.write("La base de cualquier negocio exitoso es quién lo respalda.")
    nombre = st.text_input("¿Quién lidera esta propuesta?", placeholder="Tu nombre aquí")
    st.markdown('</div>', unsafe_allow_html=True)

# SECCIÓN 2: RESPALDO LEGAL (DIAN)
if nombre:
    with st.container():
        st.markdown('<div class="gold-card">', unsafe_allow_html=True)
        st.subheader("2. Blindaje Legal")
        st.write("Para que tu talento sea cobrable, debe ser formal.")
        sector = st.selectbox("Sector Estratégico:", ["Agropecuario", "Técnico", "Consultoría", "Gastronomía", "Otro"])
        ruta = st.radio("Ruta Legal DIAN:", ["Cuenta de Cobro (Persona Natural)", "Cotización Formal (Empresa)"])
        st.markdown('</div>', unsafe_allow_html=True)

# SECCIÓN 3: EL MOTOR DE PRECISIÓN
    with st.container():
        st.markdown('<div class="gold-card">', unsafe_allow_html=True)
        st.subheader("3. El Motor: Tu Voz a Oro")
        st.write("Dicta tu idea con naturalidad. Yo me encargo de la técnica.")
        st.button("🔴 INICIAR GRABACIÓN")
        idea = st.text_area("O descríbelo brevemente:")
        if st.button("✨ GENERAR PROPUESTA GOLD"):
            st.success(f"Propuesta generada para {nombre} en el sector {sector}")
        st.markdown('</div>', unsafe_allow_html=True)
