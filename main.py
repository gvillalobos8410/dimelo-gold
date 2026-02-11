import streamlit as st

# --- 1. CONFIGURACIÓN DE IDENTIDAD Y ESTADO ---
st.set_page_config(page_title="DIMELO GOLD", layout="wide")

for k, v in {
    'p': 1, 'n': '', 'l': '', 'sec': 'Otro', 'tip': '', 'g': '', 'logo': False
}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# --- 2. ESTÉTIICA SUNLIGHT PROFESSIONAL (Amarillo & Blanco) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    
    /* Fondo Amarillo Cálido relacionado al sol y el agro */
    .stApp {
        background-color: #FFD700;
        background-image: linear-gradient(180deg, #FFD700 0%, #FFB900 100%);
    }

    /* Tarjetas Blancas para máximo contraste y limpieza */
    .main-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    /* Bloques Pedagógicos con el Dorado DIMELO */
    .ped-box {
        border-left: 8px solid #D4AF37;
        background: #fdfdfd;
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
        color: #333;
        line-height: 1.6;
    }

    /* Botones en Negro para elegancia y jerarquía visual */
    div.stButton > button {
        background: #1a1a1a !important;
        color: #D4AF37 !important;
        border-radius: 15px;
        height: 4em;
        font-weight: 700;
        width: 100%;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    h1, h2, h3, p { font-family: 'Montserrat', sans-serif; color: #1a1a1a; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PROCESO DE REGISTRO BLINDADO (P1 Y P2) ---

if st.session_state.p == 1:
    st.markdown('<div class="main-card"><h1>🏆 DIMELO GOLD</h1><p>Autoridad comercial para líderes del campo y la industria.</p>', unsafe_allow_html=True)
    st.markdown('<div class="ped-box"><h3>🛡️ PASO 1: TU IDENTIDAD</h3>Dime quién lidera la propuesta para personalizar tu motor de IA.</div>', unsafe_allow_html=True)
    nom = st.text_input("¿CUÁL ES TU NOMBRE?", value=st.session_state.n)
    if st.button("INICIAR REGISTRO ÉPICO ➡️"):
        if nom:
            st.session_state.n = nom
            st.session_state.p = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.p == 2:
    st.markdown(f'<div class="main-card"><h1>💎 PERFIL DE LIDERAZGO: {st.session_state.n.upper()}</h1>', unsafe_allow_html=True)
    c1, c2 = st.columns(2, gap="large")
    
    with c1:
        st.markdown('<div class="ped-box"><b>🖼️ IMAGEN DE MARCA</b><br>La marca es el rostro de tu calidad. Quien no tiene imagen, no compite en las grandes ligas.</div>', unsafe_allow_html=True)
        l_up = st.file_uploader("Subir Logo", label_visibility="collapsed")
        if l_up:
            st.success("✨ ¡Marca vinculada con éxito!")
            st.session_state.logo = True
        else:
            st.warning("🚨 RECOMENDACIÓN: No avanzar sin logo. Tu imagen es tu promesa.")
        
        st.write("---")
        sectores = ['🌾 Agropecuario (Café/Ganadería)', '🛠️ Servicios Técnicos', '🏗️ Construcción', '⚖️ Consultoría', '✨ Otro']
        st.session_state.sec = st.selectbox("¿EN QUÉ SECTOR TRABAJAS?", sectores)
        st.info("💡 **PEDAGOGÍA:** Describe qué haces en lenguaje sencillo.")
        act = st.text_input("¿QUÉ HACES EXACTAMENTE?", value=st.session_state.tip)
        if act: st.session_state.tip = act

    with c2:
        st.markdown('<div class="ped-box"><b>🏛️ RESPALDO LEGAL (AVISO DIAN)</b><br>La formalidad genera confianza en el cierre comercial.</div>', unsafe_allow_html=True)
        st.write("📌 **CUENTA DE COBRO:** Agilidad para servicios directos.")
        if st.button("📄 RUTA: CUENTA DE COBRO"):
            st.session_state.l = "Cuenta de Cobro"
        st.write(" ")
        st.write("📌 **COTIZACIÓN EMPRESARIAL:** Peso legal bajo estándares DIAN.")
        if st.button("🏛️ RUTA: COTIZACIÓN EMPRESARIAL"):
            st.session_state.l = "Formal"
        
        if st.session_state.l:
            st.info(f"Ruta Legal Activa: **{st.session_state.l.upper()}**")

    if st.session_state.l and st.session_state.tip:
        if st.button("FINALIZAR REGISTRO Y ABRIR MOTOR 🚀"):
            st.session_state.p = 3
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. MOTOR DE PRECISIÓN (P3) ---

elif st.session_state.p == 3:
    st.markdown('<div class="main-card"><h1>🎙️ MOTOR DE PRECISIÓN</h1>', unsafe_allow_html=True)
    ej = "Venta de café pergamino" if "Agro" in st.session_state.sec else "Mantenimiento industrial"
    
    st.markdown(f"""
    <div class="ped-box">
    ✨ **LA IA HACE LA MAGIA:**<br
