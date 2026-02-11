import streamlit as st

# --- 1. CONFIGURACIÓN E INICIALIZACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="wide")

# Persistencia de datos
for key, val in {
    'p': 1, 'n': '', 'l': '', 'sec': 'Otro', 'tip': '', 'g': '', 'logo': False
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --- 2. EL BLINDAJE DE SCROLL Y ESTÉTICA GOLD SUPREME ---
# Este bloque elimina cualquier restricción de altura en la pantalla
st.markdown("""
    <style>
    /* FORZAR SCROLL EN TODAS LAS CAPAS */
    .main, .stApp, .block-container {
        height: auto !important;
        overflow-y: auto !important;
        max-height: none !important;
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    
    html, body, [class*="st-"] { 
        font-family: 'Montserrat', sans-serif; 
        background-color: #f8f9fa; 
    }

    .card-supreme { 
        background: white; 
        padding: 40px; 
        border-radius: 25px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.05); 
        margin-bottom: 40px;
        border: 1px solid #f0f0f0;
    }

    .pedagogia-gold { 
        border-left: 8px solid #D4AF37; 
        background: #fdfdfd; 
        padding: 30px; 
        border-radius: 10px; 
        margin: 25px 0;
        font-size: 1.1em;
    }

    .dian-notice {
        background: #fff3cd;
        color: #856404;
        padding: 15px;
        border-radius: 10px;
        font-size: 0.9em;
        font-weight: bold;
        margin-top: 10px;
    }

    div.stButton > button { 
        background: #1a1a1a !important; 
        color: #D4AF37 !important; 
        border-radius: 15px; 
        height: 4em; 
        font-weight: 700; 
        width: 100%;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PÁGINA 1: IDENTIDAD Y BIENVENIDA ---
if st.session_state.p == 1:
    st.markdown('<div class="card-supreme">', unsafe_allow_html=True)
    st.title("🏆 DIMELO GOLD")
    st.markdown("### Autoridad comercial para líderes de la industria.")
    
    st.markdown("""
    <div class="pedagogia-gold">
        <b>MENSAJE DE AUTORIDAD:</b><br>
        Como líder y experto, sabes que la <b>identidad</b> es el primer paso del éxito. 
        Este sistema no solo captura datos; valida quién eres para que cada palabra 
        que dictes después tenga el peso de tu trayectoria profesional.
    </div>
    """, unsafe_allow_html=True)
    
    n = st.text_input("¿QUIÉN LIDERA ESTA VISIÓN? (Ingresa tu nombre completo)", st.session_state.n)
    if st.button("REFORZAR MI IDENTIDAD ➡️"):
        if n:
            st.session_state.n = n
            st.session_state.p = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. PÁGINA 2: REGISTRO BLINDADO Y PEDAGOGÍA DINÁMICA ---
elif st.session_state.p == 2:
    st.markdown(f'<div class="card-supreme"><h1>🛡️ ARQUITECTURA LEGAL: {st.session_state.n.upper()}</h1></div>', unsafe_allow_html=True)
    
    # Pedagogía extendida del Registro
    st.markdown("""
    <div class="pedagogia-gold">
        <b>PEDAGOGÍA DEL REGISTRO:</b><br>
        Un negocio sólido se basa en tres pilares: 
        1. <b>Imagen:</b> Tu marca es tu sello de calidad.<br>
        2. <b>Sector:</b> Define tu campo de batalla para ejemplos dinámicos.<br>
        3. <b>Legalidad:</b> Cumplir con los estándares de la <b>DIAN</b> genera confianza inmediata.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.subheader("🖼️ SELLO DE MARCA")
        logo = st.file_uploader("Sube tu logo para validar autoridad", label_visibility="collapsed")
        if logo:
            st.success("✨ Marca vinculada al sistema.")
            st.session_state.logo = True
        else:
            st.warning("🚨 Recomendación: Sin imagen no hay autoridad comercial.")
        
        st.write("---")
        # Lista nutrida de sectores
        sectores = ['🌾 Agro (Café, Ganado)', '🛠️ Servicios Técnicos', '🍰 Gastronomía', '🏗️ Obra y Construcción', '⚖️ Consultoría Pro', '✨ Otro']
        st.session_state.sec = st.selectbox("¿CUÁL ES TU SECTOR?", sectores)
        
        st.info("💡 **EJEMPLO:** Si vendes café, dinos 'Cultivo de café especial'")
        ta = st.text_input("DESCRIBE TU ACTIVIDAD:", st.session_state.tip)
        if ta: st.session_state.tip =
