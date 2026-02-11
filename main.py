import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="DIMELO GOLD", page_icon="🎙️", layout="centered")

# 2. ENCABEZADO DE MARCA (Identidad Visual Segura)
st.title("🎙️ DIMÉLO GOLD")
st.caption("INGENIERÍA DE AUTORIDAD COMERCIAL | PROYECTO GÉNESIS")

# 3. INICIALIZACIÓN DEL CEREBRO (Estado de la App)
if 'paso' not in st.session_state:
    st.session_state.paso = 1

# --- BLOQUE 1: IDENTIDAD DEL LÍDER ---
st.markdown("### 1. Identidad del Líder")
with st.expander("💡 ¿POR QUÉ ESTE PASO?", expanded=True):
    st.write("""
    **PEDAGOGÍA DE AUTORIDAD:** En el mercado de alto valor, tu nombre es la firma que respalda 
    tu visión técnica y espiritual. Sin identidad clara, no existe el puente de confianza 
    necesario para cerrar negocios de nivel Gold.
    """)

nombre = st.text_input("NOMBRE COMPLETO DEL LIDER ESTRATÉGICO:", placeholder="Ej: Germán Villalobos")

if nombre and st.session_state.paso == 1:
    if st.button("DEFINIR IDENTIDAD Y AVANZAR ➡️"):
        st.session_state.paso = 2
        st.rerun()

# --- BLOQUE 2: BLINDAJE LEGAL Y SECTOR ---
if st.session_state.paso >= 2:
    st.write("---")
    st.markdown("### 2. Blindaje Legal y Sector")
    
    with st.expander("🛡️ PEDAGOGÍA LEGAL (DIAN)", expanded=True):
        st.write("""
        **ESTÁNDAR DE PODER:** La formalidad ante la DIAN no es una carga tributaria, es tu 
        armadura profesional. Definir tu ruta legal asegura que tu talento sea cobrable y 
        respetado por empresas de alto nivel.
        """)
    
    sector = st.selectbox("SECTOR ESTRATÉGICO:", 
                          ["🌾 Agropecuario (Café/Tomate)", 
                           "🛠️ Servicios Técnicos y Mantenimiento", 
                           "⚖️ Consultoría y Marketing", 
                           "✨ Otro Sector de Autoridad"])
    
    st.info(f"**SUGERENCIA PARA {sector.upper()}:** Asegúrate de mencionar la precisión y el valor agregado en tu dictado.")
    
    ruta = st.radio("MODALIDAD DE RESPALDO:", 
                    ["📄 Cuenta de Cobro (Persona Natural)", 
                     "🏛️ Cotización Formal (Empresa/Régimen Común)"])
    
    if st.session_state.paso == 2:
        if st.button("ACTIVAR MOTOR DE PRECISIÓN 🚀"):
            st.session_state.paso = 3
            st.rerun()

# --- BLOQUE 3: MOTOR DE PRECISIÓN (VOZ A ORO) ---
if st.session_state.paso >= 3:
    st.write("---")
    st.markdown("### 3. Motor de Precisión: Voz a Oro")
    
    with st.expander("✨ ¿CÓMO USAR LA MAGIA?", expanded=True):
        st.write(f"""
        **CONSEJO DE LIDERAZGO:** {nombre}, cuéntame tu idea con la pasión de un sermón y la 
        precisión de un ingeniero. La IA capturará tu esencia y la elevará a un estándar 
        comercial de élite.
        """)
    
    st.subheader("🔴
