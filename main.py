import streamlit as st

# --- 1. CONFIGURACION INICIAL ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# RESET FORZADO: Si no hay nombre, siempre Pagina 1
if "n" not in st.session_state or st.session_state.n == "":
    st.session_state.n = ""
    st.session_state.p = 1

# Inicializar otros estados
for k, v in {"l":"", "sec":"Otros", "tip":""}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 2. PEDAGOGIA (BLOQUES CORTOS) ---
P1_TEXTO = (
    "Hola! No importa si estas empezando hoy o ya tienes tu negocio andando, "
    "esta app es para ti. Recibiras un documento con imagen profesional y "
    "lenguaje tecnico. Cumple con la DIAN si decides crecer. "
    "Tu solo dimelo como parcero, que yo hago la magia."
)

P2_TEXTO = (
    "Aqui no hay enredos. Vamos a darle autoridad a lo que haces. "
    "Tu imagen y ruta legal son tu armadura para cobrar lo justo y "
    "demostrar respaldo ante la DIAN. Beneficio, no miedo!"
)

# --- 3. ESTILO CSS (SCROLL LIBRE) ---
CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"], .main {
        overflow-y: auto !important; height: auto !important;
        font-family: 'Montserrat'; background-color: #f8f9fa;
    }
    [data-testid="stAppViewContainer"] { 
        max-width: 450px; margin: 0 auto; background: white;
        border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    }
    .card { border-left: 10px solid #D4AF37; padding: 20px; margin: 15px 0; }
    .gold { color: #D4AF37; font-weight: 700; }
    div.stButton > button { 
        background: #1a1a1a !important; color: #D4AF37 !important; 
        border-radius: 12px; height: 3.5em; width: 100%; font-weight: bold;
    }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# --- 4. LOGICA DE PANTALLAS ---

# PAGINA 1: BIENVENIDA
if st.session_state.p == 1:
    st.markdown("<h2 style='text-align:center;'>🏆 DIMELO GOLD</h2>", True)
    st.markdown(f'<div class="card"><b>MAGIA DIMELO</b><br><br>{P1_TEXTO}</div>', True)
    
    nom = st.text_input("COMO TE LLAMAS?", value=st.session_state.n)
    if st.button("VAMOS! ➡️"):
        if nom:
            st.session_state.n = nom
            st.session_state.p = 2
            st.rerun()

# PAGINA 2: CONFIGURACION
elif st.session_state.p == 2:
    if st.button("<- VOLVER"):
        st.session_state.n = ""
        st.session_state.p = 1
        st.rerun()
    
    st.markdown(f"<h3 style='text-align:center;'>HOLA, <span class='gold'>{st.session_state.n.upper()}</span></h3>", True)
    st.markdown(f'<div class="card"><b>ESCUDO COMERCIAL</b><br>{P2_TEXTO}</div>', True)
    
    st.session_state.sec = st.selectbox("Sector:", ["Agro", "Tecnico", "Obra", "Gastro", "Otros"])
    ta = st.text_input("QUE HACES EXACTAMENTE?", value=st.session_state.tip)
    if ta: st.session_state.tip = ta

    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("CTA COBRO"): st.session_state.l = "Cuenta de Cobro"
    with c2:
        if st.button("COTIZACION"): st.session_state.l = "Cotizacion"
            
    if st.session_state.l:
        st.info(f"RUTA: {st.session_state.l}")

    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 HACER MAGIA!"):
            st.session_state.p = 3
            st.rerun()

# PAGINA 3: MOTOR
elif st.session_state.p == 3:
    st.markdown("<h2 style='text-align:center;'>🎙️ MOTOR DE VOZ</h2>", True)
    st.write("Listo para procesar...")
    if st.
