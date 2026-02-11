import streamlit as st

# --- 1. BANCO DE TEXTOS (VARIABLES CORTAS PARA CERO CORTES) ---
T1 = "🏆 DIMELO GOLD"
T2 = "🛡️ TU ESCUDO COMERCIAL"
P1_A = "¡Hola! No importa si estás empezando hoy o si ya tienes "
P1_B = "tu negocio andando, esta app es para ti. Recibirás un "
P1_C = "documento con imagen profesional y lenguaje técnico. "
P1_D = "Cumple con la DIAN si decides crecer. ¡Tú solo dímelo!"

P2_A = "Aquí no hay enredos. Vamos a darle autoridad a lo que haces. "
P2_B = "Tu imagen y ruta legal son tu armadura para cobrar lo justo "
P2_C = "y demostrar respaldo ante la DIAN. ¡Beneficio, no miedo!"

# --- 2. CONFIGURACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

if 'n' not in st.session_state or st.session_state.n == "":
    st.session_state.n = ""
    st.session_state.p = 1

for k, v in {'l':'', 'sec':'Otros', 'tip':''}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 3. ESTILO CSS (SINTAXIS BLINDADA) ---
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

# --- 4. NAVEGACIÓN ---

# PÁGINA 1
if st.session_state.p == 1:
    st.markdown(f"<h2 style='text-align:center;'>{T1}</h2>", True)
    c1 = f'<div class="card"><b>MAGIA DIMELO</b><br><br>{P1_A}{P1_B}{P1_C}{P1_D}</div>'
    st.markdown(c1, True)
    
    nom = st.text_input("COMO TE LLAMAS?", value=st.session_state.n)
    if st.button("VAMOS! ➡️"):
        if nom:
            st.session_state.n = nom
            st.session_state.p = 2
            st.rerun()

# PÁGINA 2
elif st.session_state.p == 2:
    if st.button("<- VOLVER"):
        st.session_state.n = ""
        st.session_state.p = 1
        st.rerun()
    
    st.markdown(f"<h3 style='text-align:center;'>{T2}</h3>", True)
    user = st.session_state.n.upper()
    st.markdown(f"<h4 style='text-align:center;'>HOLA, <span class='gold'>{user}</span></h4>", True)
    
    c2 = f'<div class="card"><b>ESCUDO</b><br>{P2_A}{P2_B}{P2_C}</div>'
    st.markdown(c2, True)
    
    st.session_state.sec = st.selectbox("Sector:", ["Agro", "Tecnico", "Obra", "Gastro", "Otros"])
    
    ta = st.text_input("QUE HACES EXACTAMENTE?", value=st.session_state.tip)
    if ta: st.session_state.tip = ta

    st.write("---")
    c_1, c_2 = st.columns(2)
    with c_1:
        if st.button("CTA COBRO"): st.session_state.l = "Cuenta de Cobro"
    with c_2:
        if st.button("COTIZACION"): st.session_state.l = "Cotizacion"
            
    if st.session_state.l:
        st.info(f"RUTA: {st.session_state.l}")

    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 HACER MAGIA!"):
            st.session_state.p = 3
            st.rerun()
