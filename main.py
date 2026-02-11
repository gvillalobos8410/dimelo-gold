import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia
for k, v in {'p': 1, 'n': '', 'l': '', 'sec': 'Otro', 'tip': '', 'g': '', 'logo': False}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 2. INTERFAZ MÓVIL Y ESTILO FRESCO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {
        overflow-y: auto !important; height: auto !important;
    }
    [data-testid="stAppViewContainer"] {
        max-width: 450px; margin: 0 auto; background: #fff;
        box-shadow: 0 0 40px rgba(0,0,0,0.05); border-radius: 20px;
    }
    .gold-box { 
        border-left: 6px solid #D4AF37; background: #f9f9f9; 
        padding: 20px; border-radius: 10px; margin: 20px 0;
        line-height: 1.5; font-size: 0.95em;
    }
    .highlight { color: #D4AF37; font-weight: 700; }
    div.stButton > button {
        background: #1a1a1a !important; color: #D4AF37 !important;
        border-radius: 12px; height: 3.8em; font-weight: 700; width: 100%; border: none;
    }
    /* Botón Volver Sutil */
    .stButton > button[key="back"] {
        background: transparent !important; color: #999 !important;
        border: 1px solid #eee !important; border-radius: 30px !important;
        font-size: 0.8em !important; height: 2.5em !important;
    }
    .footer { height: 80px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PÁGINA 1: EL INICIO ---
if st.session_state.p == 1:
    st.markdown('<h2 style="text-align:center; padding-top:20px;">🏆 DIMELO <span class="highlight">GOLD</span></h2>', unsafe_allow_html=True)
    st.markdown('<div class="gold-box"><b>👋 ¡EPA, EMPRENDEDOR!</b><br>Soy tu profesor para que tu talento se vea impecable.</div>', unsafe_allow_html=True)
    n = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n)
    if st.button("¡VAMOS PA' ESA! ➡️"):
        if n: 
            st.session_state.n = n
            st.session_state.p = 2
            st.rerun()

# --- 4. PÁGINA 2: ESTRATEGIA Y BLINDAJE ---
elif st.session_state.p == 2:
    if st.button("← Volver", key="back"):
        st.session_state.p = 1
        st.rerun()

    st.markdown(f'<h3 style="text-align:center;">🛡️ ¡CON TODA, <span class="highlight">{st.session_state.n.upper()}</span>!</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="gold-box">
        <b>💡 CONSEJO DEL PROFESOR:</b><br>
        Viste tu negocio de gala. Una <span class="highlight">imagen seria</span> te abre puertas a mejores clientes. 
        Formalizarte paso a paso te evita líos con la <b>DIAN</b> y demuestra que tu trabajo es de verdad. ¡Yo te guío!
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🖼️ TU IDENTIDAD")
    st.file_uploader("Logo", label_visibility="collapsed")
    
    st.write("---")
    st.session_state.sec = st.selectbox("¿SECTOR?", ['🌾 Agro', '🛠️ Técnico', '🍰 Gastronomía', '🏗️ Construcción', '⚖️ Consultoría', '✨ Otro'])
    
    ta = st
