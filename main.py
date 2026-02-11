import streamlit as st

# --- 1. CONFIGURACIÓN DE INGENIERÍA ---
st.set_page_config(page_title="DIMELO GOLD | Estación de Autoridad", layout="centered")

# Persistencia de Estado Blindada
if 'p' not in st.session_state: st.session_state.p = 1
if 'n' not in st.session_state: st.session_state.n = ''
if 'l' not in st.session_state: st.session_state.l = ''
if 'sec' not in st.session_state: st.session_state.sec = 'Otro'
if 'tip' not in st.session_state: st.session_state.tip = ''
if 'logo' not in st.session_state: st.session_state.logo = False

# --- 2. AMBIENTE DE INTERFAZ ELITE (SCROLL & CELULAR) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    
    /* Configuración del Lienzo Celular */
    [data-testid="stAppViewContainer"] {
        max-width: 460px;
        margin: 0 auto;
        background-color: #ffffff;
        box-shadow: 0 0 60px rgba(0,0,0,0.07);
        border-left: 1px solid #f0f0f0;
        border-right: 1px solid #f0f0f0;
    }

    /* Liberación de Scroll Total */
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {
        overflow-y: auto !important;
        height: auto !important;
        font-family: 'Montserrat', sans-serif;
    }

    /* Caja de Pedagogía Gold Supreme */
    .mentor-card {
        border-left: 10px solid #D4AF37;
        background: #fdfdfd;
        padding: 30px;
        border-radius: 0 20px 20px 0;
        margin: 25px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
        line-height: 1.7;
    }

    .highlight { color: #D4AF37; font-weight: 700; }
    
    /* Botonera de Cierre */
    div.stButton > button {
        background: linear-gradient(135deg, #1a1a1a 0%, #333 100%) !important;
        color: #D4AF37 !important;
        border-radius: 15px;
        height: 4.2em;
        font-weight: 700;
        width: 100%;
        border: none;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: 0.3s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(212, 175, 55, 0.2);
    }

    /* Botón Volver Contemporáneo */
    .back-link button {
        background: transparent !important;
        color: #999 !important;
        border: 1px solid #eee !important;
        border-radius: 30px !important;
        height: 2.8em !important;
        font-size: 0.85em !important;
        padding: 0 25px !important;
    }
    
    .footer-spacer { height: 120px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PÁGINA 1: EL DESPERTAR DE LA MARCA (RESTAURADA) ---
if st.session_state.p == 1:
    st.markdown('<h2 style="text-align:center; padding-top:20px; color:#1a1a1a;">🏆 DIMELO <span class="highlight">GOLD</span></h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mentor-card">
        <h3 style="margin-top:0;">👋 ¡EPA, EMPRENDEDOR!</h3>
        Qué bueno tenerte acá. Sabemos que le metes el alma a lo que haces, pero a veces el cliente no ve todo ese esfuerzo porque la propuesta se ve "floja" o muy informal. 
        <b>¡Eso se acaba hoy!</b><br><br>
        Yo te voy a acompañar como tu <span class="highlight">profesor y socio</span> para que tu talento se vea impecable. Vamos a traducir esa idea que tienes en la cabeza a un documento que inspire respeto y cierre el negocio de una.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Tu nombre es tu firma")
    n = st.text_input("¿Cómo te llamas?", value=st.session_state.n, placeholder="Tu nombre y apellido")
    
    if st.button("¡LISTO, VAMOS PA' ESA! ➡️"):
        if n:
            st.session_state.n = n
            st.session_state.p = 2
            st.rerun()
    st.markdown('<div class="footer-spacer"></div>', unsafe_allow_html=True)

# --- 4. PÁGINA 2: ARQUITECTURA DE RESPALDO (REINGENIERÍA TOTAL) ---
elif st.session_state.p == 2:
    # Botón Volver Contemporáneo
    col_back, _ = st.columns([1, 1])
    with col_back:
        if st.button("← Volver", key="back_btn"):
            st.session_state.p = 1
            st.rerun()

    st.markdown(f'<h3 style="text-align:center; padding-top:10px;">🛡️ ¡CON TODA, <span class="highlight">{st.session_state.n.upper()}</span>!</h3>', unsafe_allow_html=True)
    
    # Pedagogía Estratégica Blindada
    st.markdown("""
    <div class="mentor-card">
        <h3 style="margin-top:0;">💡 CONSEJO DEL PROFESOR</h3>
        Para que un negocio crezca de verdad, hay que <b>"vestirlo de gala"</b>. No es solo por cumplir, es porque tener una 
        <span class="highlight">imagen seria</span> te abre puertas a clientes que pagan mejor.<br><br>
        Si te formalizas (aunque sea paso a paso), te evitas dolores de cabeza con la <b>DIAN</b> a futuro y demuestras que tu trabajo tiene respaldo real. ¡Yo te guío para que no sea un enredo y lo hagas por beneficio, no por miedo!
    </div>
    """, unsafe_allow_html=True)

    # Sección Identidad
    st.subheader("🖼️ TU IDENTIDAD")
    st.write("<small>Sube tu logo para que la propuesta lleve tu sello de calidad único.</small>", unsafe_allow_html=True)
    up = st.file_uploader("Cargar logo", label_visibility="collapsed")
    if up: 
        st.session_state.logo = True
        st.success("✨ ¡Ese logo se ve excelente!")
    
    st.write("---")
    
    # Selección de Sector Nutrida
    st.subheader("🎯 TU SECTOR")
    st.write("<small>Dime en qué campo te mueves para darte los mejores ejemplos.</small>", unsafe_allow_html=True)
    sectores = [
        '
