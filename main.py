import streamlit as st

# --- 1. ESTADO Y CONFIGURACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="wide")

for k, v in {
    'p': 1, 'n': '', 'l': '', 'sec': 'Otro', 'tip': '', 'g': '', 'logo': False
}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# --- 2. ESTÉTICA GOLD SUPREME ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Montserrat', sans-serif; }
    .main-card { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
    .ped-box { border-left: 6px solid #D4AF37; background: #fff; padding: 20px; border-radius: 12px; margin: 15px 0; }
    div.stButton > button { background: #1a1a1a !important; color: #D4AF37 !important; font-weight: 700; width: 100%; height: 3.5em; border-radius: 12px; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. REGISTRO (P1 Y P2) ---

if st.session_state.p == 1:
    st.markdown('<div class="main-card"><h1>🏆 DIMELO GOLD</h1></div>', True)
    st.markdown('<div class="ped-box"><h3>REGISTRO</h3>Paso 1: Identidad</div>', True)
    nom = st.text_input("¿CUAL ES TU NOMBRE?", value=st.session_state.n)
    if st.button("CONTINUAR ➡️"):
        if nom:
            st.session_state.n = nom
            st.session_state.p = 2
            st.rerun()

elif st.session_state.p == 2:
    st.markdown(f'<h1>🛡️ PERFIL: {st.session_state.n.upper()}</h1>', True)
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown('<div class="ped-box"><b>🖼️ IMAGEN</b><br>Sin logo no hay autoridad.</div>', True)
        l_up = st.file_uploader("Logo", label_visibility="collapsed")
        if l_up:
            st.session_state.logo = True
        else:
            st.warning("🚨 RECOMENDACIÓN: No avanzar sin imagen.")
        
        st.write("---")
        sect = ['🌾 Agro', '🛠️ Técnico', '🍰 Gastronomía', '🏗️ Obra', '⚖️ Consultoría', '✨ Otro']
        st.session_state.sec = st.selectbox("¿SECTOR?", sect)
        # Línea 57 simplificada para evitar SyntaxError
        val_act = st.session_state.tip
        act = st.text_input("¿QUÉ HACES?", value=val_act)
        if act: st.session_state.tip = act

    with c2:
        st.markdown('<div class="ped-box"><b>🏛️ RUTA LEGAL (DIAN)</b></div>', True)
        st.write("📌 **CUENTA DE COBRO**")
        if st.button("📄 SELECCIONAR CUENTA"):
            st.session_state.l = "Cuenta de Cobro"
        st.write("📌 **COTIZACIÓN EMPRESARIAL**")
        if st.button("🏛️ SELECCIONAR COTIZACIÓN"):
            st.session_state.l = "Formal"
        if st.session_state.l:
            st.info(f"Activa: {st.session_state.l}")

    if st.session_state.l and st.session_state.tip:
        if st.button("FINALIZAR REGISTRO 🚀"):
            st.session_state.p = 3
            st.rerun()

# --- 4. MOTOR (P3) ---

elif st.session_state.p == 3:
    st.markdown('<h1>🎙️ MOTOR DE PRECISIÓN</h1>', True)
    st.markdown('<div class="ped-box">✨ **LA IA HACE LA MAGIA**<br>Dímelo sencillo, como un café.</div>', True)
    if st.button("🔴 INICIAR GRABACIÓN"):
        st.info("🎤 Escuchando... Habla ahora.")
    with st.expander("⌨️ ESCRIBIR"):
        t_in = st.text_area("Idea:", height=100)
    if st.button("✨ TRANSFORMAR A GOLD"):
        res = t_in if t_in else "Voz"
        st.session_state.g = f"PROPUESTA: {res.upper()}"
        st.session_state.p = 4
        st.rerun()

elif st.session_state.p == 4:
    st.title("💎 ENTREGABLE")
    st.write(st.session_state.g)
    if st.button("🔄 VOLVER"):
        st.session_state.p = 3
        st.rerun()
