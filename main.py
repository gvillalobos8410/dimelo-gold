import streamlit as st

# --- 1. CONFIGURACIÓN DE AMBIENTE ---
st.set_page_config(page_title="DIMELO GOLD | Estación de Trabajo", layout="wide")

# Cerebro de persistencia
for key, val in {
    'p': 1, 'n': '', 'l': '', 'sec': 'Otro', 'tip': '', 'g': '', 'logo': False
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --- 2. INGENIERÍA DE INTERFAZ (CSS SHARK) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&family=Playfair+Display:ital,wght@1,700&display=swap');
    
    /* Configuración del Lienzo */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #f4f7f6;
        overflow-y: auto !important;
    }
    
    .stApp {
        max-width: 1100px;
        margin: 0 auto;
    }

    /* Tarjetas de Trabajo */
    .work-card {
        background: white;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.03);
        border: 1px solid #e1e8e5;
        margin-bottom: 25px;
    }

    /* Cuadro del Profesor (Pedagogía Amigable) */
    .profesor-box {
        background: #1a1a1a;
        color: #D4AF37;
        padding: 30px;
        border-radius: 15px;
        margin-bottom: 30px;
        border-left: 10px solid #D4AF37;
    }

    .profesor-box h3 { color: #D4AF37 !important; margin-top:0; }
    .profesor-box p { color: #ffffff; font-size: 1.1em; line-height: 1.6; }

    /* Estilo de Inputs y Selects */
    .stSelectbox, .stTextInput, .stFileUploader {
        margin-bottom: 20px;
    }

    /* Botonera de Acción */
    div.stButton > button {
        background: #D4AF37 !important;
        color: #1a1a1a !important;
        border-radius: 12px;
        height: 3.8em;
        font-weight: 700;
        width: 100%;
        border: none;
        transition: 0.4s;
        text-transform: uppercase;
    }
    div.stButton > button:hover {
        background: #1a1a1a !important;
        color: #D4AF37 !important;
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LÓGICA DE NAVEGACIÓN ---

# PÁGINA 1: EL INICIO (BREVE REPASO)
if st.session_state.p == 1:
    st.markdown('<div class="work-card">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #1a1a1a;'>🏆 DIMELO GOLD</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Transformando ideas en documentos de autoridad.</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="profesor-box">
        <h3>👋 ¡Epa, Emprendedor!</h3>
        <p>Soy tu profesor de negocios. Estoy aquí para que esa idea que tienes se convierta en una propuesta que dé gusto leer. 
        Primero, dime tu nombre para saber con quién voy a trabajar hoy.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.session_state.n = st.text_input("MI NOMBRE ES:", value=st.session_state.n, placeholder="Escribe aquí...")
    
    if st.button("EMPEZAR LA REINGENIERÍA ➡️"):
        if st.session_state.n:
            st.session_state.p = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# PÁGINA 2: ARQUITECTURA DE MARCA (EL CORAZÓN DE LA INTERFAZ)
elif st.session_state.p == 2:
    st.markdown(f"### 📍 ESTACIÓN DE TRABAJO: {st.session_state.n.upper()}")
    
    st.markdown("""
    <div class="profesor-box">
        <h3>🛡️ VISTAMOS EL NEGOCIO DE GALA</h3>
        <p>Un emprendedor con clase sabe que <b>la imagen y la ley</b> no son estorbos, son su escudo. 
        Si tienes un logo y cumples con la DIAN, el cliente sabe que no eres un aparecido. ¡Vamos a blindar esa confianza!</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown('<div class="work-card">', unsafe_allow_html=True)
        st.subheader("🖼️ TU IDENTIDAD")
        st.write("Tu logo es tu promesa de calidad.")
        up = st.file_uploader("Sube tu logo", label_visibility="collapsed")
        if up: st.session_state.logo = True
        
        st.write("---")
        sectores = ['🌾 Agropecuario', '🛠️ Técnico', '🍰 Gastronomía', '🏗️ Construcción', '⚖️ Consultoría', '✨ Otro']
        st.session_state.sec = st.selectbox("¿EN QUÉ SECTOR TE MUEVES?", sectores)
        ta = st.text_input("¿QUÉ HACES EXACTAMENTE?", value=st.session_state.tip, placeholder="Ej: Mantenimiento de plantas eléctricas")
        if ta: st.session_state.tip = ta
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="work-card">', unsafe_allow_html=True)
        st.subheader("🏛️ RESPALDO LEGAL (DIAN)")
        st.write("¿Cómo vamos a presentar este cobro?")
        
        st.markdown("""
        <small>💡 <b>Nota del Profesor:</b> 
        - <b>Cuenta de Cobro:</b> Si eres persona natural.
        - <b>Cotización:</b> Si ya tienes empresa formal.</small>
        """, unsafe_allow_html=True)
        
        st.write("")
        if st.button("📄 RUTA: CUENTA DE COBRO"):
            st.session_state.l = "Cuenta de Cobro"
            
        if st.button("🏛️ RUTA: COTIZACIÓN FORMAL"):
            st.session_state.l = "Cotización"
            
        if st.session_state.l:
            st.success(f"Ruta elegida: {st.session_state.l}")
        st.markdown('</div>', unsafe_allow_html=True)

    # Botón de paso final
    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 TODO LISTO, VAMOS AL MOTOR DE VOZ"):
            st.session_state.p = 3
            st.rerun()

    if st.button("⬅️ VOLVER AL INICIO"):
        st.session_state.p = 1
        st.rerun()
