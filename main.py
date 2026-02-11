import streamlit as st

# --- 1. PEDAGOGÍA DE LEY (VARIABLES CORTAS PARA EVITAR CORTES) ---
P1_PED = (
    "¡Hola! No importa si estás empezando hoy o si ya tienes tu negocio andando, "
    "esta app es para ti. Vas a recibir un documento con imagen profesional y un "
    "lenguaje tan claro y técnico que tus clientes te verán como una empresa de alto nivel. "
    "Para el emprendedor que quiere dar el siguiente paso, este documento cumple con los "
    "requisitos de la DIAN, dejándote la puerta abierta para facturación electrónica si "
    "así lo decides. Pero si solo buscas presentarte mejor, ¡estás en el lugar correcto! "
    "Tú solo dímelo como parcero, que yo hago la magia de entregarte una propuesta impecable."
)

P2_PED = (
    "Aquí no hay enredos. Vamos a darle autoridad a lo que haces. Elegir tu imagen y tu "
    "ruta legal no es una obligación pesada, es tu armadura para que el cliente confíe "
    "y tú cobres lo justo. Vestir tu negocio de gala te abre puertas a mejores clientes "
    "y demuestra que tu trabajo tiene respaldo real ante la DIAN. ¡Yo te guío para que "
    "sea por beneficio, no por miedo!"
)

# --- 2. CONFIGURACIÓN E INICIALIZACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# LÓGICA DE INICIO: Si el nombre está vacío, forzamos página 1
if 'n' not in st.session_state: st.session_state.n = ''
if 'p' not in st.session_state or st.session_state.n == '': 
    st.session_state.p = 1

# Otros estados
for k, v in {'l':'', 'sec':'Otros', 'tip':''}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 3. ESTILO CSS (SCROLL Y ESTÉTICA GOLD) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {
        overflow-y: auto !important; height: auto !important;
        min-height: 100vh !important; font-family: 'Montserrat';
        background-color: #f4f4f4;
    }
    [data-testid="stAppViewContainer"] { 
        max-width: 450px; margin: 0 auto; background: white;
        border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    }
    .card { border-left: 10px solid #D4AF37; padding: 25px; margin: 20px 0; background: #fff; }
    .gold { color: #D4AF37; font-weight: 700; }
    div.stButton > button { 
        background: #1a1a1a !important; color: #D4AF37 !important; 
        border-radius: 12px; height: 3.5em; width: 100%; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. PÁGINA 1: LA PROMESA ---
if st.session_state.p == 1:
    st.markdown("<h2 style='text-align:center; padding-top:20px;'>🏆 DIMELO <span class='gold'>GOLD</span></h2>", unsafe_allow_html=True)
    st.markdown(f'<div class="card"><b>🤝 ¡TÚ DÍMELO, QUE YO HAGO LA MAGIA!</b><br><br>{P1_PED}</div>', unsafe_allow_html=True)
    
    nombre_i = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n)
    if st.button("¡ESTOY LISTO, VAMOS CON TODA! ➡️"):
        if nombre_i:
            st.session_state.n = nombre_i
            st.session_state.p = 2
            st.rerun()

# --- 5. PÁGINA 2: ARQUITECTURA ---
elif st.session_state.p == 2:
    if st.button("← VOLVER"):
        st.session_state.p = 1
        st.rerun()
    
    st.markdown(f"<h3 style='text-align:center;'>🛡️ RESPALDO: <span class='gold'>{st.session_state.n.upper()}</span></h3>", unsafe_allow_html=True)
    st.markdown(f'<div class="card"><b>💡 TU ESCUDO COMERCIAL</b><br><br>{P2_PED}</div>', unsafe_allow_html=True)
    
    st.session_state.sec = st.selectbox("Sector:", ["🌾 Agro", "🛠️ Técnico", "🏗️ Obra", "🍰 Gastro", "✨ Otros"])
    
    # Ejemplo dinámico simplificado para evitar errores de sintaxis
    desc = st.text_input("¿QUÉ HACES EXACTAMENTE?", value=st.session_state.tip, placeholder="Escribe aquí...")
    if desc: st.session_state.tip = desc

    st.write("---")
    st.write("<b>¿CÓMO TE PRESENTAS HOY?</b>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📄 CTA COBRO"): st.session_state.l = "Cuenta de Cobro"
    with c2:
        if st.button("🏛️ COTIZACION"): st.session_state.l = "Cotización"
            
    if st.session_state.l:
        st.info(f"Ruta: {st.session_state.l.upper()}")

    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 TODO LISTO, ¡A HACER MAGIA!"):
            st.session_state.p = 3
            st.rerun()
