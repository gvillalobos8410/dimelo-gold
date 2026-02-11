import streamlit as st

# --- 1. CONFIGURACIÓN DE INTERFAZ NEON PRO ---
st.set_page_config(page_title="DIMELO GOLD", layout="wide", initial_sidebar_state="collapsed")

# Estética basada en tus imágenes: Púrpura, Oscuro y Neon
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    
    html, body, [class*="st-"] { 
        font-family: 'Montserrat', sans-serif; 
        background-color: #0f0f12; 
        color: #e0e0e0;
    }
    
    /* Contenedor principal estilo Chat */
    .main-container {
        max-width: 800px;
        margin: auto;
        padding: 20px;
    }

    /* Burbujas de Pedagogía (Tu Voz de Autoridad) */
    .chat-bubble-ai {
        background: linear-gradient(135deg, #2b1a3d 0%, #1a1a1a 100%);
        border: 1px solid #7b2cbf;
        padding: 25px;
        border-radius: 20px 20px 20px 5px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(123, 44, 191, 0.1);
    }

    /* Botones Neon */
    div.stButton > button {
        background: linear-gradient(90deg, #7b2cbf, #9d4edd) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px;
        height: 3.5em;
        font-weight: 700;
        width: 100%;
        transition: 0.3s;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    div.stButton > button:hover {
        box-shadow: 0 0 20px rgba(157, 78, 221, 0.6);
        transform: translateY(-2px);
    }

    /* Inputs Estilizados */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #1a1a20 !important;
        color: white !important;
        border: 1px solid #3c096c !important;
        border-radius: 12px !important;
    }

    .neon-text { color: #9d4edd; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LÓGICA DE ESTADO (Para no perder información) ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'user_name' not in st.session_state: st.session_state.user_name = ""

# --- 3. FLUJO DE BIENVENIDA Y REGISTRO ---

st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Encabezado con Logo (Usando el nombre de tu proyecto)
st.markdown(f"<h1 style='text-align: center; color: white;'>🎙️ DIMELO <span style='color: #9d4edd;'>GOLD</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.7;'>Tu talento convertido en autoridad comercial.</p>", unsafe_allow_html=True)

# PASO 1: IDENTIDAD
if st.session_state.step >= 1:
    st.markdown("""
    <div class="chat-bubble-ai">
        <b>DIME PRO:</b> Hola. En este entorno de alta ingeniería, tu nombre es la firma de tu éxito. 
        Para que el sistema genere <span class="neon-text">autoridad</span>, primero debemos saber quién lidera la propuesta.
    </div>
    """, unsafe_allow_html=True)
    
    name = st.text_input("¿Cuál es tu nombre?", value=st.session_state.user_name, key="name_input")
    if name and st.session_state.step == 1:
        st.session_state.user_name = name
        if st.button("CONFIGURAR MI IDENTIDAD ➡️"):
            st.session_state.step = 2
            st.rerun()

# PASO 2: BLINDAJE LEGAL Y SECTOR (Solo aparece si el paso 1 está listo)
if st.session_state.step >= 2:
    st.markdown(f"""
    <div class="chat-bubble-ai">
        <b>PEDAGOGÍA:</b> Bienvenido, <span class="neon-text">{st.session_state.user_name}</span>. 
        Ahora, blindemos tu labor. El respaldo legal de la <b>DIAN</b> no es un trámite, 
        es la puerta a facturar como una empresa de alto nivel.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        sector = st.selectbox("Tu Sector Estratégico:", ["🌾 Agropecuario", "🛠️ Técnico", "⚖️ Consultoría", "✨ Otro"])
    with col2:
        ruta = st.radio("Ruta Legal:", ["Cuenta de Cobro", "Cotización Formal"])
    
    if st.session_state.step == 2:
        if st.button("ACTIVAR MOTOR DE PRECISIÓN 🚀"):
            st.session_state.step = 3
            st.rerun()

# PASO 3: EL MOTOR DE PRECISIÓN (El micrófono Neon)
if st.session_state.step >= 3:
    st.markdown("""
    <div class="chat-bubble-ai" style="text-align: center; border: 2px solid #9d4edd;">
        <h2 style='margin:0;'>🟣 TE ESCUCHO</h2>
        <p>Dicta tu idea. La IA transformará tu lenguaje natural en una oferta comercial Élite.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.button("🔴 INICIAR GRABACIÓN POR VOZ")
    
    with st.expander("⌨️ ¿PREFIERES DESCRIBIR TU IDEA POR ESCRITO?"):
        idea = st.text_area("Describe tu propuesta:")
        if st.button("TRANSFORMAR IDEA A NIVEL GOLD ✨"):
            st.success("Analizando lenguaje y aplicando estándares de cierre...")

st.markdown('</div>', unsafe_allow_html=True)
