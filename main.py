import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia Blindada
for key, val in {'p': 1, 'n': '', 'l': '', 'sec': 'Otro', 'tip': '', 'g': '', 'logo': False}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --- 2. INTERFAZ MÓVIL (SCROLL Y ESTILO FRESCO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {
        overflow-y: auto !important;
        height: auto !important;
    }

    [data-testid="stAppViewContainer"] {
        max-width: 450px;
        margin: 0 auto;
        background-color: #ffffff;
        box-shadow: 0 0 40px rgba(0,0,0,0.05);
    }
    
    .gold-box { 
        border-left: 6px solid #D4AF37; background: #f9f9f9; 
        padding: 20px; border-radius: 10px; margin: 20px 0;
        line-height: 1.5; font-size: 0.95em; color: #333;
    }
    
    .highlight { color: #D4AF37; font-weight: 700; }
    
    /* Botón Principal Gold */
    div.stButton > button {
        background: #1a1a1a !important; color: #D4AF37 !important;
        border-radius: 12px; height: 3.8em; font-weight: 700;
        width: 100%; border: none; text-transform: uppercase;
    }

    /* Botón de Volver Sutil (Reemplazo de 'kind' por CSS) */
    .stButton > button[key="back_btn"] {
        background: transparent !important;
        color: #999 !important;
        border: 1px solid #eee !important;
        height: 2.5em !important;
        font-size: 0.8em !important;
        border-radius: 30px !important;
        text-transform: none !important;
    }

    .footer-space { height: 80px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PÁGINA 1: EL INICIO ---
if st.session_state.p == 1:
    st.markdown('<h2 style="text-align:center; padding-top:20px;">🏆 DIMELO <span class="highlight">GOLD</span></h2>', unsafe_allow_html=True)
    st.markdown("""<div class="gold-box"><b>👋 ¡EPA, EMPRENDEDOR!</b><br>Yo te voy a acompañar como tu profesor para que tu talento se vea impecable.</div>""", unsafe_allow_html=True)
    nombre = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n)
    if st.button("¡VAMOS PA' ESA! ➡️"):
        if nombre:
            st.session_state.n = nombre
            st.session_state.p = 2
            st.rerun()

# --- 4. PÁGINA 2: ESTRATEGIA Y PEDAGOGÍA ---
elif st.session_state.p == 2:
    # Botón Volver sutil (Sin el parámetro 'kind' que causó el error)
    if st.button("← Volver al inicio"):
        st.session_state.p = 1
        st.rerun()

    st.markdown(f'<h3 style="text-align:center;">🛡️ ¡VAMOS CON TODA, <span class="highlight">{st.session_state.n.upper()}</span>!</h3>', unsafe_allow_html=True)
    
    # Pedagogía Estratégica para el Informal
    st.markdown("""
    <div class="gold-box">
        <b>💡 CONSEJO DEL PROFESOR:</b><br>
        Para que un negocio crezca de verdad, hay que "vestirlo de gala". No es solo por cumplir, es porque tener una 
        <span class="highlight">imagen seria</span> te abre puertas a clientes que pagan mejor.<br><br>
        Si te formalizas paso a paso, te evitas líos con la <b>DIAN</b> después y demuestras que tu trabajo es de verdad. ¡Yo te ayudo a que no sea un enredo!
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🖼️ TU IDENTIDAD")
    st.write("<small>Sube tu logo para que la propuesta lleve tu sello.</small>", unsafe_allow_html=True)
    st.file_uploader("Sube tu logo",
