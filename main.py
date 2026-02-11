import streamlit as st

# --- 1. CONFIGURACIÓN E INICIALIZACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Forzamos inicio en Página 1 si no hay nombre (Cero memoria de sesión)
if 'n' not in st.session_state or st.session_state.n == "":
    st.session_state.n = ""
    st.session_state.p = 1

# Estados de la app
for k, v in {'l': '', 'sec': '✨ Otros', 'tip': ''}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 2. PEDAGOGÍA DE LEY (COMPLETA Y APROBADA) ---
P1_PED = """
¡Hola! No importa si estás empezando hoy o si ya tienes tu negocio andando, <b>esta app es para ti</b>. 
Vas a recibir un documento con <b>imagen profesional</b> y un lenguaje tan claro y técnico que tus clientes te verán como una empresa de alto nivel. 
Para el emprendedor que quiere dar el siguiente paso, este documento cumple con los requisitos de la <b>DIAN</b>, dejándote la puerta abierta para facturación electrónica si así lo decides. Pero si solo buscas presentarte mejor, ¡estás en el lugar correcto! 
<br><br><span class="gold">Tú solo dímelo</span> como parcero, que <span class="gold">yo hago la magia</span> de entregarte una propuesta impecable.
"""

P2_PED = """
Aquí no hay enredos. Vamos a darle <b>autoridad</b> a lo que haces. Elegir tu imagen y tu ruta legal no es una obligación pesada, es tu armadura para que el cliente confíe y tú cobres lo justo. 
Vestir tu negocio de gala te abre puertas a mejores clientes y demuestra que tu trabajo tiene respaldo real ante la <b>DIAN</b>. ¡Yo te guío para que sea por beneficio, no por miedo!
"""

# --- 3. ESTILO CSS (ESTÉTICA GOLD SUPREME + SCROLL TOTAL) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {
        overflow-y: auto !important;
        height: auto !important;
        min-height: 100vh !important;
        font-family: 'Montserrat', sans-serif;
        background-color: #f4f4f4 !important;
    }

    [data-testid="stAppViewContainer"] { 
        max-width: 450px; margin: 0 auto; background: white;
        border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        padding-bottom: 50px;
    }
    
    .mentor-card { 
        border-left: 10px solid #D4AF37; background: #ffffff; 
        padding: 25px; margin: 20px 0; line-height: 1.6;
    }
    
    .gold { color: #D4AF37; font-weight: 700; }
    
    div.stButton > button { 
        background: #1a1a1a !important; color: #D4AF37 !important; 
        border-radius: 12px; height: 3.5em; width: 100%; 
        font-weight: bold; border: none; text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. LÓGICA DE PANTALLAS ---

# PÁGINA 1: BIENVENIDA
if st.session_state.p == 1:
    st.markdown("<h2 style='text-align:center; padding-top:20px;'>🏆 DIMELO <span class='gold'>GOLD</span></h2>", unsafe_allow_html=True)
    st.markdown(f'<div class="mentor-card"><b>🤝 ¡TÚ DÍMELO, QUE YO HAGO LA MAGIA!</b><br><br>{P1_PED}</div>', unsafe_allow_html=True)
    
    nombre = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n)
    if st.button("¡ESTOY LISTO, VAMOS CON TODA! ➡️"):
        if nombre:
            st.session_state.n = nombre
            st.session_state.p = 2
            st.rerun()

# PÁGINA 2: CONFIGURACIÓN
elif st.session_state.p == 2:
    if st.button("← VOLVER AL INICIO"):
        st.session_state.n = ""
        st.session_state.p = 1
        st.rerun()
    
    st.markdown(f"<h3 style='text-align:center;'>🛡️ RESPALDO: <span class='gold'>{st.session_state.n.upper()}</span></h3>", unsafe_allow_html=True)
    st.markdown(f'<div class="mentor-card"><b>💡 TU ESCUDO COMERCIAL</b><br><br>{P2_PED}</div>', unsafe_allow_html=True)
    
    st.session_state.sec = st.selectbox("¿En qué sector te mueves?", ["🌾 Agro", "🛠️ Técnico", "🏗️ Obra", "🍰 Gastro", "✨ Otros"])
    
    actividad = st.text_input("¿QUÉ HACES EXACTAMENTE?", value=st.session_state.tip, placeholder="Ej: Venta de café, mantenimiento...")
    if actividad: st.session_state.tip = actividad

    st.write("---")
    st.write("<b>¿CÓMO TE PRESENTAS HOY?</b>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📄 CTA COBRO"): st.session_state.l = "Cuenta de Cobro"
    with c2:
        if st.button("🏛️ COTIZACIÓN"): st.session_state.l = "Cotización"
            
    if st.session_state.l:
        st.info(f"Ruta seleccionada: {st.session_state.l.upper()}")

    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 ¡A HACER MAGIA!"):
            st.session_state.p = 3
            st.rerun()

# PÁGINA 3: MOTOR (DICTADO)
elif st.session_state.p == 3:
    st.markdown("<h2 style='text-align:center;'>🎙️ MOTOR DE VOZ</h2>", unsafe_allow_html=True)
    st.markdown(f'<div class="mentor-card">Listo <span class="gold">{st.session_state.n}</span>, suéltalo todo que yo hago la magia.</div>', unsafe_allow_html=True)
    if st.button("⬅️ VOLVER"):
        st.session_state.p = 2
        st.rerun()
