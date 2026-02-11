import streamlit as st

# --- 1. CONFIGURACIÓN DE INGENIERÍA ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia de Estado Blindada
for k, v in {'p':1, 'n':'', 'l':'', 'sec':'Otro', 'tip':'', 'logo':False}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 2. INTERFAZ MÓVIL ELITE (SCROLL & ESTÉTICA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    [data-testid="stAppViewContainer"] {
        max-width: 460px; margin: 0 auto; background: #fff;
        box-shadow: 0 0 60px rgba(0,0,0,0.07); border-radius: 20px;
    }
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {
        overflow-y: auto !important; height: auto !important; font-family: 'Montserrat', sans-serif;
    }
    .mentor-card {
        border-left: 10px solid #D4AF37; background: #fdfdfd; padding: 30px;
        border-radius: 0 20px 20px 0; margin: 25px 0; line-height: 1.7;
    }
    .highlight { color: #D4AF37; font-weight: 700; }
    div.stButton > button {
        background: linear-gradient(135deg, #1a1a1a 0%, #333 100%) !important;
        color: #D4AF37 !important; border-radius: 15px; height: 4.2em;
        font-weight: 700; width: 100%; border: none; text-transform: uppercase;
    }
    .back-btn button {
        background: transparent !important; color: #999 !important;
        border: 1px solid #eee !important; border-radius: 30px !important;
        font-size: 0.8em !important; height: 2.5em !important;
    }
    .spacer { height: 100px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PÁGINA 1: EL DESPERTAR DE LA MARCA (RESTAURADA) ---
if st.session_state.p == 1:
    st.markdown('<h2 style="text-align:center; padding-top:20px;">🏆 DIMELO <span class="highlight">GOLD</span></h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="mentor-card">
        <h3 style="margin-top:0;">👋 ¡EPA, EMPRENDEDOR!</h3>
        Qué bueno tenerte acá. Sabemos que le metes el alma a lo que haces, pero a veces el cliente no ve todo ese esfuerzo. <b>¡Eso se acaba hoy!</b><br><br>
        Yo te voy a acompañar como tu <span class="highlight">profesor y socio</span> para que tu talento se vea impecable.
    </div>
    """, unsafe_allow_html=True)
    
    n = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n, placeholder="Tu nombre y apellido")
    if st.button("¡LISTO, VAMOS PA' ESA! ➡️"):
        if n:
            st.session_state.n = n
            st.session_state.p = 2
            st.rerun()
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- 4. PÁGINA 2: ARQUITECTURA DE RESPALDO (REINGENIERÍA TOTAL) ---
elif st.session_state.p == 2:
    if st.button("← Volver", key="back"):
        st.session_state.p = 1
        st.rerun()

    st.markdown(f'<h3 style="text-align:center;">🛡️ ¡CON TODA, <span class="highlight">{st.session_state.n.upper()}</span>!</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mentor-card">
        <h3 style="margin-top:0;">💡 CONSEJO DEL PROFESOR</h3>
