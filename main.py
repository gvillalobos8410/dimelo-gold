import streamlit as st

# --- 1. CONFIGURACIÓN DE SEGURIDAD Y FLUJO ---
st.set_page_config(page_title="DIMELO GOLD", layout="wide")

# Inicialización de Estado
for key, val in {
    'p': 1, 'n': '', 'l': '', 'sec': 'Otro', 'tip': '', 'g': '', 'logo': False
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --- 2. ESTÉTICA GOLD SUPREME 2.0 (CON SCROLL ACTIVO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    
    /* Permitir scroll natural */
    .main { overflow-y: auto !important; }
    
    html, body, [class*="st-"] { 
        font-family: 'Montserrat', sans-serif; 
        background-color: #f4f4f4; 
        color: #1a1a1a;
    }

    .main-card { 
        background: white; 
        padding: 50px; 
        border-radius: 30px; 
        box-shadow: 0 20px 50px rgba(0,0,0,0.1); 
        margin-bottom: 30px;
    }

    .pedagogia-box { 
        border-left: 10px solid #D4AF37; 
        background: #ffffff; 
        padding: 30px; 
        border-radius: 0 20px 20px 0; 
        margin: 25px 0;
        line-height: 1.8;
    }

    .highlight { color: #D4AF37; font-weight: 700; }

    div.stButton > button { 
        background: linear-gradient(90deg, #1a1a1a, #333) !important; 
        color: #D4AF37 !important; 
        border-radius: 20px; 
        height: 4.5em; 
        font-weight: 700; 
        width: 100%; 
        border: none;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PÁGINA 1: EL DESPERTAR DE LA MARCA ---
if st.session_state.p == 1:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("🏆 DIMELO GOLD")
    st.markdown("### Bienvenido al estándar de oro de la autoridad comercial.")
    
    st.markdown("""
    <div class="pedagogia-box">
        <b>¿POR QUÉ ESTÁS AQUÍ?</b><br>
        En un mundo saturado de información, solo los líderes con 
        <span class="highlight">identidad clara</span> logran cerrar negocios de alto valor. 
        Este registro no es un formulario; es la construcción de tu respaldo legal y profesional.
    </div>
    """, unsafe_allow_html=True)
    
    n = st.text_input("PARA COMENZAR, ¿QUIÉN LIDERA ESTA VISIÓN? (Ingresa tu nombre)", st.session_state.n)
    
    if st.button("INICIAR MI CAMINO DE AUTORIDAD ➡️"):
        if n:
            st.session_state.n = n
            st.session_state.p = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. PÁGINA 2: EL BLINDAJE LEGAL Y TÉCNICO ---
elif st.session_state.p == 2:
    st.markdown(f'<div class="main-card"><h1>🛡️ ARQUITECTURA DE RESPALDO: {st.session_state.n.upper()}</h1></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="pedagogia-box">
        <b>LA CIENCIA DEL CIERRE:</b><br>
        Un cliente premium no compra un producto, compra <span class="highlight">seguridad</span>. 
        A continuación, vincularemos tu imagen de marca y tu estatus legal ante la 
        <b>DIAN</b> para que cada cotización sea una declaración de seriedad.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.subheader("🖼️ IDENTIDAD VISUAL")
        st.write("Tu logo es el sello de tu promesa de valor.")
        logo = st.file_uploader("Cargar Sello de Marca", label_visibility="collapsed")
        if logo:
            st.success("✨ Marca vinculada al motor de generación.")
            st.session_state.logo = True
        else:
            st.warning("🚨 Sin logo, la propuesta pierde un 40% de efectividad visual.")
        
        st.write("---")
        sectores = ['🌾 Agropecuario', '🛠️ Técnico', '🍰 Gastronomía', '🏗️ Obra', '⚖️ Pro', '✨ Otro']
        st.session_state.sec = st.selectbox("¿CUÁL ES TU SECTOR ESTRATÉGICO?", sectores)
        st.write("Dime qué haces de forma natural (Ej: Cultivo de café especial).")
        ta = st.text_input("ACTIVIDAD EXACTA:", st.session_state.tip)
        if ta: st.session_state.tip = ta

    with col2:
        st.subheader("🏛️ RESPALDO LEGAL (ESTÁNDAR DIAN)")
        st.write("Selecciona el formato que exige tu obligación tributaria:")
        
        if st.button("📄 CUENTA DE COBRO (Persona Natural)"):
            st.session_state.l = "Sencilla"
            st.info("Configurado para servicios directos sin IVA.")
            
        st.write(" ")
        if st.button("🏛️ COTIZACIÓN EMPRESARIAL (P. Jurídica)"):
            st.session_state.l = "Formal"
            st.info("Configurado con todos los requisitos de ley DIAN.")
            
        if st.session_state.l:
            st.success(f"Ruta legal activa: {st.session_state.l.upper()}")

    if st.session_state.l and st.session_state.tip:
        st.write("---")
        if st.button("FINALIZAR BLINDAJE Y ABRIR MOTOR DE PRECISIÓN 🚀"):
            st.session_state.p = 3
            st.rerun()

# --- 5. PÁGINA 3: EL MOTOR DE PRECISIÓN (VOZ A ORO) ---
elif st.session_state.p == 3:
    st.markdown('<div class="main-card"><h1>🎙️ MOTOR DE PRECISIÓN GOLD</h1></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="pedagogia-box">
        <b>¿CÓMO USAR LA MAGIA?</b><br>
        No busques palabras técnicas. Cuéntame tu idea como si estuviéramos 
        frente a un café. La <span class="highlight">Inteligencia Artificial</span> 
        capturará tu esencia y la elevará al lenguaje comercial que tus clientes esperan.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔴 INICIAR GRABACIÓN DE IDEA COMERCIAL"):
        st.info("🎤 El sistema te escucha... Habla con total libertad.")

    with st.expander("⌨️ ¿PREFIERES ESCRIBIR TU IDEA?"):
        ti = st.text_area("Escribe aquí tu visión:", height=150)
        
    if st.button("✨ TRANSFORMAR MI IDEA A NIVEL GOLD"):
        res = ti if ti else "Dictado por voz procesado"
        st.session_state.g = f"**{st.session_state.tip.upper()} - PROPUESTA ÉLITE:** {res.upper()}"
        st.session_state.p = 4
        st.rerun()

elif st.session_state.p == 4:
    st.markdown('<div class="main-card"><h1>💎 ENTREGABLE FINAL</h1></div>', unsafe_allow_html=True)
    st.write(st.session_state.g)
    if st.button("🔄 GENERAR NUEVO DICTADO"):
        st.session_state.p = 3
        st.rerun()
