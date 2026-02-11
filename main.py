import streamlit as st

# --- 1. CONFIGURACION E INICIO FORZADO ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Si no hay nombre en la sesion, forzar siempre Pagina 1
if 'n' not in st.session_state or st.session_state.n == "":
    st.session_state.n = ""
    st.session_state.p = 1

# Inicializar estados adicionales
for k, v in {'l': '', 'sec': 'Otros', 'tip': ''}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 2. PEDAGOGIA COMPLETA (LEY DIMELO) ---
P1_PED = (
    "Hola! No importa si estas empezando hoy o si ya tienes tu negocio andando, "
    "esta app es para ti. Vas a recibir un documento con imagen profesional y un "
    "lenguaje tan claro y tecnico que tus clientes te veran como una empresa de alto nivel. "
    "Para el emprendedor que quiere dar el siguiente paso, este documento cumple con los "
    "requisitos de la DIAN, dejandote la puerta abierta para facturacion electronica si "
    "asi lo decides. Pero si solo buscas presentarte mejor, ¡estas en el lugar correcto! "
    "Tu solo dimelo como parcero, que yo hago la magia."
)

P2_PED = (
    "Aqui no hay enredos. Vamos a darle autoridad a lo que haces. Elegir tu imagen y tu "
    "ruta legal no es una obligacion pesada, es tu armadura para que el cliente confie "
    "y tu cobres lo justo. Vestir tu negocio de gala te abre puertas a mejores clientes "
    "y demuestra que tu trabajo tiene respaldo real ante la DIAN. Beneficio, no miedo!"
)

# --- 3. ESTILO CSS (SCROLL FLUIDO Y ESTETICA GOLD) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"], .main {
        overflow-y: auto !important; height: auto !important;
        font-family: 'Montserrat', sans-serif; background-color: #f8f9fa;
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

# --- 4. LOGICA DE PANTALLAS ---

# PAGINA 1: BIENVENIDA
if st.session_state.p == 1:
    st.markdown("<h2 style='text-align:center;'>DIMELO GOLD</h2>", unsafe_allow_html=True)
    st.markdown(f'<div class="card"><b>TU DIMELO, YO HAGO LA MAGIA</b><br><br>{P1_PED}</div>', unsafe_allow_html=True)
    
    nombre_i = st.text_input("COMO TE LLAMAS?", value=st.session_state.n)
    if st.button("VAMOS AHORA! ->"):
        if nombre_i:
            st.session_state.n = nombre_i
            st.session_state.p = 2
            st.rerun()

# PAGINA 2: CONFIGURACION
elif st.session_state.p == 2:
    if st.button("<- VOLVER AL INICIO"):
        st.session_state.n = ""
        st.session_state.p = 1
        st.rerun()
    
    st.markdown(f"<h3 style='text-align:center;'>RESPALDO: {st.session_state.n.upper()}</h3>", unsafe_allow_html=True)
    st.markdown(f'<div class="card"><b>ESCUDO COMERCIAL</b><br><br>{P2_PED}</div>', unsafe_allow_html=True)
    
    st.session_state.sec = st.selectbox("Sector:", ["Agro", "Tecnico", "Obra", "Gastro", "Otros"])
    act = st.text_input("QUE HACES EXACTAMENTE?", value=st.session_state.tip)
    if act: st.session_state.tip = act

    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("CTA COBRO"): st.session_state.l = "Cuenta de Cobro"
    with c2:
        if st.button("COTIZACION"): st.session_state.l = "Cotizacion"
            
    if st.session_state.l:
        st.success(f"SELECCIONADO: {st.session_state.l.upper()}")

    if st.session_state.l and st.session_state.tip:
        if st.button("HACER MAGIA!"):
            st.session_state.p = 3
            st.rerun()

# PAGINA 3: MOTOR
elif st.session_state.p == 3:
    st.markdown("<h2 style='text-align:center;'>MOTOR DE VOZ</h2>", unsafe_allow_html=True)
    st.markdown(f'<div class="card">Listo {st.session_state.n}, sueltalo todo.</div>', unsafe_allow_html=True)
    if st.button("RECONFIGURAR"):
        st.session_state.p = 2
        st.rerun()
