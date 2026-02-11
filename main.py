import streamlit as st

# --- 1. VARIABLES DE IDENTIDAD (PARA EVITAR CORTES) ---
E_GOLD = "🏆"
E_MIC = "🎙"
E_ESC = "🛡️"
E_AGRO = "🌾"
E_TEC = "🛠️"
E_OBRA = "🏗️"
E_GAS = "🍰"
E_OTRO = "✨"

# --- 2. PEDAGOGIA (LINEAS CORTAS) ---
P1_T = (
    "Hola! No importa si estas empezando hoy o ya tienes "
    "tu negocio andando, esta app es para ti. Vas a recibir "
    "un documento con imagen profesional y un lenguaje "
    "claro y tecnico. Cumple con la DIAN si decides crecer."
)

P2_T = (
    "Aqui no hay enredos. Vamos a darle autoridad a lo "
    "que haces. Tu ruta legal es tu armadura para cobrar "
    "lo justo y demostrar respaldo ante la DIAN. "
    "Hazlo por beneficio, no por miedo!"
)

# --- 3. CONFIGURACION ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

if 'n' not in st.session_state or st.session_state.n == "":
    st.session_state.n = ""
    st.session_state.p = 1

for k, v in {'l': '', 'sec': 'Otros', 'tip': ''}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 4. ESTILO CSS (SINTAXIS PLANA) ---
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"], .main {
        overflow-y: auto !important; height: auto !important;
        font-family: sans-serif; background-color: #f8f9fa;
    }
    [data-testid="stAppViewContainer"] { 
        max-width: 450px; margin: 0 auto; background: white;
        border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    }
    .card { border-left: 10px solid #D4AF37; padding: 25px; margin: 20px 0; }
    .gold { color: #D4AF37; font-weight: bold; }
    div.stButton > button { 
        background: #1a1a1a !important; color: #D4AF37 !important; 
        border-radius: 12px; height: 3.5em; width: 100%; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- 5. LOGICA DE PANTALLAS ---

if st.session_state.p == 1:
    st.markdown(f"<h2 style='text-align:center;'>{E_GOLD} DIMELO GOLD</h2>", True)
    st.markdown(f'<div class="card"><b>MAGIA DIMELO</b><br><br>{P1_T}</div>', True)
    nom = st.text_input("COMO TE LLAMAS?", value=st.session_state.n)
    if st.button("VAMOS! ->"):
        if nom:
            st.session_state.n = nom
            st.session_state.p = 2
            st.rerun()

elif st.session_state.p == 2:
    if st.button("<- VOLVER"):
        st.session_state.n = ""
        st.session_state.p = 1
        st.rerun()
    st.markdown(f"<h3 style='text-align:center;'>{E_ESC} {st.session_state.n.upper()}</h3>", True)
    st.markdown(f'<div class="card"><b>ESCUDO COMERCIAL</b><br><br>{P2_T}</div>', True)
    sec_list = [f"{E_AGRO} Agro", f"{E_TEC} Tecnico", f"{E_OBRA} Obra", f"{E_GAS} Gastro", f"{E_OTRO} Otros"]
    st.session_state.sec = st.selectbox("Sector:", sec_list)
    ta = st.text_input("QUE HACES EXACTAMENTE?", value=st.session_state.tip)
    if ta: st.session_state.tip = ta
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("CTA COBRO"): st.session_state.l = "Cuenta de Cobro"
    with c2:
        if st.button("COTIZACION"): st.session_state.l = "Cotizacion"
    if st.session_state.l and st.session_state.tip:
        if st.button("HACER MAGIA!"):
            st.session_state.p = 3
            st.rerun()

elif st.session_state.p == 3:
    st.markdown(f"<h2 style='text-align:center;'>{E_MIC} MOTOR</h2>", True)
    st.markdown(f'<div class="card">Listo {st.session_state.n}. Habla ahora...</div>', True)
    if st.button("REGRESAR"):
        st.session_state.p = 2
        st.rerun()
