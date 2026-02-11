import streamlit as st

# 1. TÍTULO DE AUTORIDAD (Sin estilos complejos para evitar errores)
st.title("🎙️ DIMELO GOLD")
st.subheader("Ingeniería de Autoridad Comercial")

# 2. INICIALIZACIÓN DE ESTADO (El cerebro de la App)
if 'paso' not in st.session_state:
    st.session_state.paso = 1

# 3. FLUJO DE INFORMACIÓN (UX)

# --- BLOQUE 1: IDENTIDAD ---
st.info("PEDAGOGÍA: Tu nombre es la firma de tu éxito.")
nombre = st.text_input("¿Quién lidera esta propuesta?", key="nombre_user")

if nombre and st.session_state.paso == 1:
    if st.button("Siguiente: Blindaje Legal ➡️"):
        st.session_state.paso = 2
        st.rerun()

# --- BLOQUE 2: BLINDAJE LEGAL ---
if st.session_state.paso >= 2:
    st.write("---")
    st.warning("AVISO DIAN: Define tu estatus legal para asegurar el cierre.")
    
    sector = st.selectbox("Sector Estratégico:", 
                          ["Agropecuario (Café/Tomate)", "Servicios Técnicos", "Consultoría", "Otro"])
    
    ruta = st.radio("Modalidad Legal:", ["Cuenta de Cobro", "Cotización Formal"])
    
    if st.session_state.paso == 2:
        if st.button("Siguiente: Motor de Voz 🚀"):
            st.session_state.paso = 3
            st.rerun()

# --- BLOQUE 3: MOTOR DE PRECISIÓN ---
if st.session_state.paso >= 3:
    st.write("---")
    st.success(f"Motor Activo para: {nombre}")
    st.header("TE ESCUCHO")
    st.write("Dicta tu idea comercial ahora.")
    
    if st.button("🔴 INICIAR GRABACIÓN"):
        st.write("🎤 Procesando tu voz a nivel Gold...")
