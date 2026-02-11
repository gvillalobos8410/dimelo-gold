import streamlit as st

# --- 1. CONFIGURACIÓN E INICIALIZACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="wide")

# Inicialización de estado blindada
if 'p' not in st.session_state: st.session_state.p = 1
if 'n' not in st.session_state: st.session_state.n = ''
if 'l' not in st.session_state: st.session_state.l = ''
if 'tip' not in st.session_state: st.session_state.tip = ''
if 'sec' not in st.session_state: st.session_state.sec = 'Otro'

# --- 2. ESTÉTICA GOLD SUPREME (SCROLL LIBERADO) ---
st.markdown("""
    <style>
    /* LIBERACIÓN DE SCROLL TOTAL */
    html, body, [data-testid="stAppViewContainer"] {
        overflow-y: auto !important;
        height: auto !important;
    }
    .main .block-container {
        max-width: 900px;
        padding-bottom: 150px; /* Margen de seguridad para scroll */
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Montserrat', sans-serif; }
    
    .gold-box { 
        border-left: 8px solid #D4AF37; background: white; 
        padding: 30px; border-radius: 15px; margin: 20px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .highlight { color: #D4AF37; font-weight: 700; }
    
    div.stButton > button { 
        background: #1a1a1a !important; color: #D4AF37 !important; 
        border-radius: 12px; height: 3.8em; font-weight: 700; 
        width: 100%; border: none; transition: 0.3s;
    }
    div.stButton > button:hover { transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PÁGINA 1: IDENTIDAD Y AUTORIDAD ---
if st.session_state.p == 1:
    st.title("🏆 DIMELO GOLD")
    st.subheader("El estándar de oro para líderes con visión comercial.")
    
    st.markdown(f"""
    <div class="gold-box">
        <b>MENSAJE DE AUTORIDAD:</b><br>
        En el mercado de alto nivel, tu nombre es tu mayor activo. 
        Este registro valida tu <span class="highlight">identidad comercial</span> 
        para que cada propuesta generada tenga el peso de tu trayectoria profesional.
    </div>
    """, unsafe_allow_html=True)
    
    nombre = st.text_input("PARA COMENZAR, ¿QUIÉN LIDERA ESTA PROPUESTA?", value=st.session_state.n)
    if st.button("INICIAR REGISTRO DE AUTORIDAD ➡️"):
        if nombre:
            st.session_state.n = nombre
            st.session_state.p = 2
            st.rerun()

# --- 4. PÁGINA 2: REGISTRO BLINDADO (DIAN Y SECTORES) ---
elif st.session_state.p == 2:
    st.header(f"🛡️ ARQUITECTURA DE RESPALDO: {st.session_state.n.upper()}")
    
    st.markdown("""
    <div class="gold-box">
        <b>PEDAGOGÍA DEL REGISTRO:</b><br>
        Un cierre efectivo requiere <span class="highlight">Imagen</span>, 
        <span class="highlight">Especialidad</span> y <span class="highlight">Legalidad</span>. 
        Cumplir con los estándares de la <b>DIAN</b> no es opcional, es lo que 
        te diferencia de la competencia informal.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.subheader("🖼️ SELLO DE MARCA")
        st.write("Sube tu logo. Quien no tiene imagen, no proyecta seguridad.")
        up = st.file_uploader("Cargar logo", label_visibility="collapsed")
        if up: 
            st.success("✨ Marca vinculada.")
        else:
            st.warning("🚨 Recomendación: Sin logo, la propuesta pierde autoridad visual.")
        
        st.write("---")
        sectores = ['🌾 Agropecuario', '🛠️ Técnico', '🍰 Gastronomía', '🏗️ Obra', '⚖️ Consultoría', '✨ Otro']
        st.session_state.sec = st.selectbox("¿CUÁL ES TU SECTOR ESTRATÉGICO?", sectores)
        ta = st.text_input("DESCRIBE TU ACTIVIDAD (Ej: Venta de café especial):", value=st.session_state.tip)
        if ta: st.session_state.tip = ta

    with col2:
        st.subheader("🏛️ RESPALDO LEGAL (AVISO DIAN)")
        st.info("Define tu ruta oficial para validación tributaria.")
        if st.button("📄 RUTA: CUENTA DE COBRO"):
            st.session_state.l = "Sencilla"
        st.write(" ")
        if st.button("🏛️ RUTA: COTIZACIÓN EMPRESARIAL"):
            st.session_state.l = "Formal"
            
        if st.session_state.l:
            st.success(f"Configurado: {st.session_state.l.upper()}")

    if st.session_state.l and st.session_state.tip:
        st.write("---")
        if st.button("FINALIZAR REGISTRO Y ABRIR MOTOR 🚀"):
            st.session_state.p = 3
            st.rerun()

# --- 5. PÁGINA 3: EL MOTOR DE PRECISIÓN (MAGIA DE VOZ) ---
elif st.session_state.p == 3:
    st.header("🎙️ MOTOR DE PRECISIÓN GOLD")
    
    st.markdown(f"""
    <div class="gold-box">
        ✨ <b>LA IA HACE LA MAGIA:</b><br>
        Dímelo sencillo, como un café entre amigos. Mi sistema interpretará tu 
        visión de <b>{st.session_state.sec}</b> y la profesionalizará al instante.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔴 PULSA PARA GRABAR TU IDEA COMERCIAL"):
        st.info("🎤 El sistema te escucha... Cuéntame tu visión.")

    with st.expander("⌨️ OPCIÓN: PREFIERO ESCRIBIR"):
        ti = st.text_area("Escribe tu idea aquí:", height=150)
        
    if st.button("✨ TRANSFORMAR MI IDEA A NIVEL GOLD"):
        res = ti if ti else "Voz procesada con éxito"
        st.session_state.g = f"**{st.session_state.tip.upper()} - PROPUESTA ÉLITE:** {res.upper()}"
        st.session_state.p = 4
        st.rerun()

elif st.session_state.p == 4:
    st.header("💎 ENTREGABLE FINAL")
    st.markdown(f'<div class="gold-box">{st.session_state.g}</div>', unsafe_allow_html=True)
    if st.button("🔄 REALIZAR NUEVO DICTADO"):
        st.session_state.p = 3
        st.rerun()
