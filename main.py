import streamlit as st

# 1. CONFIGURACION BASE
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# 2. TITULO Y ESTADO
st.title("🎙️ DIMELO GOLD")
st.write("---")

if 'paso' not in st.session_state:
    st.session_state.paso = 1

# 3. BLOQUE 1: IDENTIDAD
st.subheader("1. Identidad del Líder")
st.info("PEDAGOGIA: Tu nombre es la firma que respalda tu visión tecnica y espiritual.")

nombre = st.text_input("NOMBRE COMPLETO:", placeholder="Ej: German Villalobos")

if nombre and st.session_state.paso == 1:
    if st.button("DEFINIR IDENTIDAD ➡️"):
        st.session_state.paso = 2
        st.rerun()

# 4. BLOQUE 2: LEGAL Y SECTOR
if st.session_state.paso >= 2:
    st.write("---")
    st.subheader("2. Blindaje Legal y Sector")
    st.warning("PEDAGOGIA DIAN: La formalidad asegura que tu talento sea cobrable a alto nivel.")
    
    sector = st.selectbox("SECTOR:", ["Agropecuario", "Tecnico", "Consultoria", "Otro"])
    ruta = st.radio("MODALIDAD:", ["Cuenta de Cobro", "Cotizacion Formal"])
    
    if st.session_state.paso == 2:
        if st.button("ACTIVAR MOTOR DE PRECISION 🚀"):
            st.session_state.paso = 3
            st.rerun()

# 5. BLOQUE 3: MOTOR DE VOZ
if st.session_state.paso >= 3:
    st.write("---")
    st.subheader("3. Motor de Precision")
    st.success(f"Liderazgo activo: {nombre}")
    
    st.write("TE ESCUCHO: Dicta tu idea comercial ahora.")
    
    if st.button("INICIAR GRABACION 🎤"):
        st.info("Escuchando... El sistema esta procesando tu autoridad.")
