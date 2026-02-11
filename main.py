import streamlit as st

# --- 1. CONFIGURACIÓN Y PERSISTENCIA ---
st.set_page_config(page_title="DIMELO GOLD", layout="wide")

for key, val in {
    'p': 1, 'n': '', 'l': '', 'sec': 'Otro', 'tip': '', 'g': '', 'logo': False
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --- 2. BLINDAJE DE SCROLL Y ESTÉTICA GOLD SUPREME ---
st.markdown("""
    <style>
    /* Forzar scroll en la raíz de Streamlit */
    .stApp { overflow-y: auto !important; }
    .main .block-container { max-width: 900px; padding-top: 2rem; }
    
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Montserrat', sans-serif; }
    
    .card-gold { 
        background: white; padding: 40px; border-radius: 25px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 30px; 
    }
    .pedagogia { 
        border-left: 8px solid #D4AF37; background: #fafafa; 
        padding: 25px; border-radius: 10px; margin: 20px 0; 
    }
    div.stButton > button { 
        background: #1a1a1a !important; color: #D4AF37 !important; 
        font-weight: 700; border-radius: 12px; height: 3.5em; width: 100%; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PÁGINA 1: IDENTIDAD ---
if st.session_state.p == 1:
    st.markdown('<div class="card-gold"><h1>🏆 DIMELO GOLD</h1>', unsafe_allow_html=True)
    st.markdown("""<div class="pedagogia"><b>PEDAGOGÍA DE INICIO:</b><br>
    Tu nombre es el sello de tu liderazgo. Para generar autoridad, 
    debemos saber quién respalda la propuesta.</div>""", unsafe_allow_html=True)
    
    nom = st.text_input("¿CUÁL ES TU NOMBRE?", value=st.session_state.n)
    if st.button("CONTINUAR REGISTRO ➡️"):
        if nom:
            st.session_state.n = nom
            st.session_state.p = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. PÁGINA 2: REGISTRO BLINDADO (DIAN Y SECTORES) ---
elif st.session_state.p == 2:
    st.markdown(f'<div class="card-gold"><h1>🛡️ REGISTRO: {st.session_state.n.upper()}</h1>', unsafe_allow_html=True)
    
    st.markdown("""<div class="pedagogia"><b>ESTÁNDARES DE AUTORIDAD:</b><br>
    La DIAN exige claridad legal y el mercado exige una imagen sólida. 
    Define tus pilares comerciales aquí.</div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("🖼️ IMAGEN DE MARCA")
        up = st.file_uploader("Sube tu logo", label_visibility="collapsed")
        if up: st.session_state.logo = True
        else: st.warning("🚨 Recomendación: No avanzar sin imagen.")
        
        st.write("---")
        # Lista nutrida de sectores
        secs = ['🌾 Agropecuario', '🛠️ Técnico', '🍰 Gastronomía', '🏗️ Obra', '⚖️ Pro', '✨ Otro']
        st.session_state.sec = st.selectbox("SECTOR:", secs)
        ta = st.text_input("¿QUÉ HACES EXACTAMENTE?", value=st.session_state.tip)
        if ta: 
            st.session_state.tip = ta

    with c2:
        st.subheader("🏛️ AVISO LEGAL DIAN")
        st.info("Define tu ruta legal para validar la propuesta.")
        if st.button("📄 CUENTA DE COBRO"):
            st.session_state.l = "Sencilla"
        if st.button("🏛️ COTIZACIÓN EMPRESARIAL"):
            st.session_state.l = "Formal"
        
        if st.session_state.l:
            st.success(f"Ruta activa: {st.session_state.l.upper()}")

    if st.session_state.l and st.session_state.tip:
        if st.button("ABRIR MOTOR DE PRECISIÓN 🚀"):
            st.session_state.p = 3
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 5. PÁGINA 3: MOTOR DE PRECISIÓN (ALMA) ---
elif st.session_state
