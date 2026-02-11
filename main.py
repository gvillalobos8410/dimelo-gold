import streamlit as st

# 1. CONFIGURACIÓN DE ENTORNO ÉLITE
st.set_page_config(page_title="DIMELO GOLD", page_icon="🎙️", layout="centered")

# 2. CEREBRO DE FLUJO (UX DIRIGIDA)
if 'paso' not in st.session_state:
    st.session_state.paso = 1

# 3. ENCABEZADO DE AUTORIDAD
st.title("🎙️ DIMÉLO GOLD")
st.markdown("---")

# --- PASO 1: LA IDENTIDAD (EL CIMIENTO) ---
if st.session_state.paso == 1:
    st.subheader("Fase 1: La Firma de Autoridad")
    
    st.info("""
    **CÁTEDRA DEL PROFESOR:** Bienvenido al entorno donde tu palabra cobra valor. 
    Antes de activar la ingeniería de transformación, debemos establecer quién firma el éxito. 
    En el mercado de alto nivel, **tu nombre no es un dato, es tu activo más preciado**. 
    Es la firma que respalda tu visión técnica y espiritual.
    """)
    
    nombre = st.text_input("¿Quién lidera esta propuesta hoy?", placeholder="Ej: Germán Villalobos")
    
    if st.button("ESTABLECER MI AUTORIDAD ➡️"):
        if nombre:
            st.session_state.nombre = nombre
            st.session_state.paso = 2
            st.rerun()
        else:
            st.error("Líder, el sistema requiere tu nombre para proceder.")

# --- PASO 2: EL BLINDAJE (EL RESPALDO DIAN) ---
elif st.session_state.paso == 2:
    st.subheader(f"Fase 2: Blindaje Legal, {st.session_state.nombre}")
    
    st.warning("""
    **AVISO LEGAL DIAN - EL ESTÁNDAR DE PODER:** Tu talento es inmenso, pero para que sea cobrable, debe estar blindado. 
    La formalidad ante la DIAN no es una carga, es tu **armadura profesional**. 
    Definir tu ruta legal asegura que tu propuesta sea respetada por empresas de alto nivel.
    """)
    
    sector = st.selectbox("Sector Estratégico de Influencia:", 
                          ["🌾 Agropecuario (Café/Tomate)", 
                           "🛠️ Servicios Técnicos y Mantenimiento", 
                           "⚖️ Consultoría y Marketing Pro", 
                           "✨ Otro Sector de Autoridad"])
    
    ruta = st.radio("Modalidad de Respaldo Jurídico:", 
                    ["Cuenta de Cobro (Persona Natural)", 
                     "Cotización Formal (Empresa/Régimen Común)"])
    
    if st.button("ACTIVAR MOTOR DE TRANSFORMACIÓN 🚀"):
        st.session_state.sector = sector
        st.session_state.paso = 3
        st.rerun()

# --- PASO 3: LA TRANSMUTACIÓN (VOZ A ORO) ---
elif st.session_state.paso == 3:
    st.subheader("Fase 3: Transmutación de Lenguaje")
    
    st.success(f"""
    **ESTÁS ACOMPAÑADO:** {st.session_state.nombre}, tienes frente a ti una herramienta de 
    ingeniería poderosa. No te preocupes por la técnica ahora; **háblame con la pasión de tu 
    liderazgo**. Mi algoritmo tomará tus palabras básicas y las elevará a un documento 
    profesional de élite. **Por esta precisión es que tu cliente paga.**
    """)
    
    st.markdown("### 🔴 TE ESCUCHO")
    st.caption(f"Configuración activa para el sector: {st.session_state.sector}")
    
    if st.button("INICIAR GRABACIÓN POR VOZ 🎤"):
        st.info("Escuchando tu visión... Preparando la autoridad comercial.")
    
    st.write("---")
    with st.expander("⌨️ ¿PREFIERES UN BORRADOR ESCRITO?"):
        idea_texto = st.text_area("Describe tu propuesta aquí:")
        if st.button("TRANSFORMAR A NIVEL GOLD ✨"):
            st.success(f"Analizando propuesta... Elevando el lenguaje de {st.session_state.nombre} a estándar global.")

    if st.button("⬅️ Reiniciar Registro"):
        st.session_state.paso = 1
        st.rerun()
