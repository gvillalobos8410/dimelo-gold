import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia de Estado
if 'p' not in st.session_state: st.session_state.p = 1
if 'n' not in st.session_state: st.session_state.n = ''
if 'l' not in st.session_state: st.session_state.l = ''
if 'sec' not in st.session_state: st.session_state.sec = 'Otro'
if 'tip' not in st.session_state: st.session_state.tip = ''

# --- 2. BANCO DE DATOS (TEXTOS CORTOS) ---
EJS = {
    'Agro': 'Ej: Venta de 10 cargas de cafe...',
    'Tecnico': 'Ej: Mantenimiento de motores...',
    'Obra': 'Ej: Remodelacion de bano...',
    'Gastro': 'Ej: Servicio de catering...',
    'Otro': 'Ej: Describe tu servicio...'
}

# --- 3. ESTILO CSS (SCROLL Y ESTÉTICA) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {
        overflow-y: auto !important; height: auto !important;
        min-height: 100vh !important; font-family: 'Montserrat';
        background-color: #f8f9fa;
    }
    [data-testid="stAppViewContainer"] { 
        max-width: 450px; margin: 0 auto; background: white;
        border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    }
    .card { border-left: 10px solid #D4AF37; padding: 25px; margin: 20px 0; }
    .gold { color: #D4AF37; font-weight: 700; }
    div.stButton > button { 
        background: #1a1a1a !important; color: #D4AF37 !important; 
        border-radius: 12px; height: 3.5em; width: 100%; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. LÓGICA DE PANTALLAS ---

# PAGINA 1: BIENVENIDA
if st.session_state.p == 1:
    st.markdown("<h2 style='text-align:center;'>🏆 DIMELO <span class='gold'>GOLD</span></h2>", unsafe_allow_html=True)
    st.markdown('<div class="card"><b>🤝 TU DIMELO, QUE YO HAGO LA MAGIA!</b><br><br>Hola! Esta app es para ti. Recibiras un documento profesional que cumple con la DIAN si decides crecer. Tu solo dimelo, que yo hago la magia.</div>', unsafe_allow_html=True)
    
    nombre = st.text_input("COMO TE LLAMAS?", value=st.session_state.n)
    if st.button("VAMOS CON TODA! ➡️"):
        if nombre:
            st.session_state.n = nombre
            st.session_state.p = 2
            st.rerun()

# PAGINA 2: CONFIGURACIÓN
elif st.session_state.p == 2:
    if st.button("<- VOLVER"):
        st.session_state.p = 1
        st.rerun()
    
    st.markdown(f"### 🛡️ RESPALDO: <span class='gold'>{st.session_state.n.upper()}</span>", unsafe_allow_html=True)
    st.markdown('<div class="card"><b>💡 TU ESCUDO COMERCIAL</b><br>Ponemos autoridad a lo que haces. Tu ruta legal es tu armadura ante la DIAN.</div>', unsafe_allow_html=True)
    
    st.session_state.sec = st.selectbox("Sector:", list(EJS.keys()))
    ej_placeholder = EJS.get(st.session_state.sec)
    
    desc = st.text_input("QUE HACES EXACTAMENTE?", value=st.session_state.tip, placeholder=ej_placeholder)
    if desc: st.session_state.tip = desc

    st.write("---")
    st.write("<b>COMO TE PRESENTAS?</b>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    
    with c1:
        if st.button("CTA COBRO"):
            st.session_state.l = "CTA_COBRO"
    with c2:
        if st.button("COTIZACION"):
            st.session_state.l = "COTIZACION"
            
    if st.session_state.l:
        st.success(f"SELECCIONADO: {st.session_state.l}")

    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 HACER MAGIA!"):
            st.session_state.p = 3
            st.rerun()

# PAGINA 3: MOTOR
elif st.session_state.p == 3:
    st.markdown("<h2 style='text-align:center;'>🎙️ MOTOR DE VOZ</h2>", unsafe_allow_html=True)
    st.write(f"Listo {st.session_state.n}, procesando tu {st.session_state.l}...")
    if st.button("RECONFIGURAR"):
        st.session_state.p = 2
        st.rerun()
