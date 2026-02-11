import streamlit as st

# --- 1. CONFIGURACIÓN DE ALTO NIVEL ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia Blindada
for key, val in {'p': 1, 'n': '', 'l': '', 'sec': 'Otro', 'tip': '', 'g': '', 'logo': False}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --- 2. INTERFAZ MÓVIL CON SCROLL TOTAL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    
    /* ELIMINAR BLOQUEO DE SCROLL EN TODA LA APP */
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {
        overflow-y: auto !important;
        height: auto !important;
        min-height: 100vh !important;
    }

    /* Contenedor tipo Celular (Máximo 450px de ancho) */
    [data-testid="stAppViewContainer"] {
        max-width: 450px;
        margin: 0 auto;
        background-color: #ffffff;
        box-shadow: 0 0 40px rgba(0,0,0,0.1);
        border-left: 1px solid #eee;
        border-right: 1px solid #eee;
    }
    
    body { background-color: #f0f2f5; font-family: 'Montserrat', sans-serif; }

    .gold-box { 
        border-left: 8px solid #D4AF37; background: #fafafa; 
        padding: 20px; border-radius: 10px; margin: 20px 0;
        line-height: 1.6; font-size: 0.95em;
    }
    
    .highlight { color: #D4AF37; font-weight: 700; }
    
    /* Botonería Shark Tank */
    div.stButton > button {
        background: #1a1a1a !important; color: #D4AF37 !important;
        border-radius: 12px; height: 3.5em; font-weight: 700;
        width: 100%; border: none; text-transform: uppercase;
        margin-bottom: 20px;
    }

    /* Espaciado extra al final para asegurar el scroll */
    .footer-space { height: 100px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PÁGINA 1: EL DESPERTAR DE LA MARCA ---
if st.session_state.p == 1:
    st.markdown('<h2 style="text-align:center; padding-top:20px;">🏆 DIMELO <span class="highlight">GOLD</span></h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="gold-box">
        <b>👋 ¡EPA, EMPRENDEDOR!</b><br>
        Qué bueno tenerte acá. Sabemos que le metes el alma a lo que haces, pero a veces el cliente no ve todo ese esfuerzo. 
        <b>¡Eso se acaba hoy!</b><br><br>
        Yo te voy a acompañar como tu profesor y socio para que tu talento se vea <span class="highlight">impecable</span>.
    </div>
    """, unsafe_allow_html=True)
    
    nombre = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n, placeholder="Tu nombre y apellido")
    
    st.markdown('<br>', unsafe_allow_html=True)
    if st.button("¡LISTO, VAMOS PA' ESA! ➡️"):
        if nombre:
            st.session_state.n = nombre
            st.session_state.p = 2
            st.rerun()
    st.markdown('<div class="footer-space"></div>', unsafe_allow_html=True)

# --- 4. PÁGINA 2: ARQUITECTURA DE RESPALDO (RESTAURADA Y CON SCROLL) ---
elif st.session_state.p == 2:
    st.markdown(f'<h3 style="text-align:center; padding-top:20px;">🛡️ ¡VAMOS CON TODA, <span class="highlight">{st.session_state.n.upper()}</span>!</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="gold-box">
        <b>🛡️ VISTAMOS EL NEGOCIO DE GALA</b><br>
        Un emprendedor con clase sabe que la imagen y la ley no son estorbos, son su escudo. 
        Si tienes un logo y cumples con la <span class="highlight">DIAN</span>, el cliente sabe que eres un profesional de peso.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🖼️ TU IDENTIDAD")
    up = st.file_uploader("Sube tu logo", label_visibility="collapsed")
    if up: st.session_state.logo = True
    
    st.write("---")
    sectores = ['🌾 Agropecuario', '🛠️ Técnico', '🍰 Gastronomía', '🏗️ Construcción', '⚖️ Consultoría', '✨ Otro']
    st.session_state.sec = st.selectbox("¿EN QUÉ SECTOR TE MUEVES?", sectores)
    
    ta = st.text_input("¿QUÉ HACES EXACTAMENTE?", value=st.session_state.tip, placeholder="Ej: Venta de café especial")
    if ta: st.session_state.tip = ta

    st.
