import streamlit as st

# --- 1. CONFIGURACIÓN DE SEGURIDAD Y ESTADO ---
st.set_page_config(page_title="DIMELO GOLD", layout="wide")

# Inicialización de persistencia de datos
for key, val in {
    'p': 1, 'n': '', 'l': '', 'sec': 'Otro', 'tip': '', 'g': '', 'logo': False
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --- 2. ESTÉTICA GOLD SUPREME (Blindada) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Montserrat', sans-serif; background-color: #f4f7f6; }
    .main-card { background: white; padding: 35px; border-radius: 25px; border: 1px solid #e0e0e0; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
    .ped-box { border-left: 6px solid #D4AF37; background: #ffffff; padding: 25px; border-radius: 15px; margin: 20px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.02); }
    div.stButton > button { background: #1a1a1a !important; color: #D4AF37 !important; border-radius: 12px; height: 3.8em; font-weight: 700; width: 100%; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PROCESO DE REGISTRO BLINDADO (Páginas 1 y 2) ---

if st.session_state.p == 1:
    st.markdown('<div class="main-card"><h1>🏆 DIMELO GOLD</h1><p>Software de Autoridad Comercial</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="ped-box"><h3>REGISTRO DE IDENTIDAD</h3>🛡️ Paso 1: Configura tu perfil de liderazgo.</div>', unsafe_allow_html=True)
    nombre = st.text_input("¿CUÁL ES TU NOMBRE?", value=st.session_state.n)
    if st.button("INICIAR MI CAMINO GOLD ➡️"):
        if nombre:
            st.session_state.n = nombre
            st.session_state.p = 2
            st.rerun()

elif st.session_state.p == 2:
    st.markdown(f'<div class="main-card"><h1>🛡️ PERFIL PROFESIONAL: {st.session_state.n.upper()}</h1></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown('<div class="ped-box"><b>🖼️ PEDAGOGÍA DE IMAGEN</b><br>Quien no tiene imagen no existe en el mercado de élite. Tu logo es el sello de tu calidad.</div>', unsafe_allow_html=True)
        logo = st.file_uploader("Vincular Marca Personal", label_visibility="collapsed")
        if logo:
            st.success("✨ Marca respaldada profesionalmente.")
            st.session_state.logo = True
        else:
            st.warning("🚨 RECOMENDACIÓN: No avanzar sin logo. La autoridad empieza en lo visual.")
        
        st.write("---")
        sectores = [
            '🌾 Agropecuario (Café, Ganadería)', '🛠️ Servicios Técnicos', 
            '🍰 Gastronomía', '🏗️ Construcción y Obras', 
            '⚖️ Consultoría y Liderazgo', '🚚 Logística', '✨ Otro'
        ]
        st.session_state.sec = st.selectbox("¿EN QUÉ SECTOR TRABAJAS?", sectores)
        st.info("💡 **GUÍA:** Describe tu actividad de forma simple.")
        actividad = st.text_input("¿QUÉ HACES EXACTAMENTE?", value
