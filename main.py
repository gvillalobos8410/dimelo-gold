import streamlit as st

# --- 1. RESET FORZADO (PAGINA 1 SIEMPRE AL INICIO) ---
if "n" not in st.session_state:
    st.session_state.n = ""
    st.session_state.p = 1

# Si entras y el nombre esta vacio, te devuelvo a la 1
if st.session_state.n == "":
    st.session_state.p = 1

# Otros estados
for k,v in {"l":"","sec":"Otros","tip":""}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 2. PEDAGOGIA LEY DIMELO ---
P1 = (
    "Hola! No importa si estas empezando hoy o ya "
    "tienes tu negocio andando, esta app es para ti. "
    "Recibiras un documento profesional y lenguaje "
    "tecnico. Cumple con la DIAN si decides crecer. "
    "Tu solo dimelo, que yo hago la magia."
)
P2 = (
    "Aqui no hay enredos. Vamos a darle autoridad "
    "a lo que haces. Tu imagen y ruta legal son tu "
    "armadura para cobrar lo justo y demostrar "
    "respaldo ante la DIAN. Beneficio, no miedo!"
)

# --- 3. ESTILO CSS (SCROLL Y ESTETICA) ---
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"], .main {
        overflow-y: auto !important; height: auto !important;
        font-family: sans-serif; background: #f8f9fa;
    }
    .card { border-left: 8px solid #D4AF37; padding: 15px; margin: 10px 0; background: #fff; }
    div.stButton > button { background: #1a1a1a !important; color: #D4AF37 !important; border-radius: 10px; font-weight: bold; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- 4. LOGICA DE PANTALLAS ---

if st.session_state.p == 1:
    st.header("🏆 DIMELO GOLD")
    st.markdown(f'<div class="card"><b>LA MAGIA</b><br>{P1}</div>', True)
    nom = st.text_input("COMO TE LLAMAS?")
    if st.button("VAMOS! ➡️"):
        if nom:
            st.session_state.n = nom
            st.session_state.p = 2
            st.rerun()

elif st.session_state.p == 2:
    if st.button("<- VOLVER AL INICIO"):
        st.session_state.n = ""
        st.session_state.p = 1
        st.rerun()
    st.subheader(f"HOLA, {st.session_state.n.upper()}")
    st.markdown(f'<div class="card">{P2}</div>', True)
    st.session_state.sec = st.selectbox("Sector:", ["Agro", "Tecnico", "Obra", "Gastro", "Otros"])
    ta = st.text_input("QUE HACES EXACTAMENTE?", value=st.session_state.tip)
    if ta: st.session_state.tip = ta
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("CTA COBRO"): st.session_state.l = "Cuenta de Cobro"
    with c2:
        if st.button("COTIZACION"): st.session_state.l = "Cotizacion"
    if st.session_state.l: st.info(f"RUTA: {st.session_state.l}")
    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 HACER MAGIA!"):
            st.session_state.p = 3
            st.rerun()
