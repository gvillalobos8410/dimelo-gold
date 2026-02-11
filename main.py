import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia Blindada
for k, v in {'p':1, 'n':'', 'l':'', 'sec':'Otros', 'tip':''}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 2. MAPA DE SECTORES ---
sectores = {
    'Agro': {'ej': 'Ej: Venta de 10 cargas de cafe...', 'img': 'https://images.unsplash.com/photo-1500651230702-0e2d8a49d4ad?w=800'},
    'Tecnico': {'ej': 'Ej: Mantenimiento de motores...', 'img': 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=800'},
    'Gastronomia': {'ej': 'Ej: Banquetes para eventos...', 'img': 'https://images.unsplash.com/photo-1555244162-803834f70033?w=800'},
    'Construccion': {'ej': 'Ej: Remodelacion y pintura...', 'img': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=800'},
    'Otros': {'ej': 'Ej: Describe tu servicio...', 'img': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800'}
}

# --- 3. AMBIENTE VISUAL (SCROLL Y FONDO) ---
img = sectores[st.session_state.sec]['img'] if st.session_state.p == 2 else ""
bg = f"linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9)), url('{img}')" if img else "#fff"

st.markdown(f'''
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"], .main {{
        overflow-y: auto !important; height: auto !important; min-height: 100vh !important;
        font-family: 'Montserrat', sans-serif;
    }}
    [data-testid="stAppViewContainer"] {{ 
        max-width: 450px; margin: 0 auto; background: {bg}; 
        background-size: cover; border-radius: 20px; box-shadow: 0 0 40px rgba(0,0,0,0.1); 
    }}
    .card {{ border-left: 10px solid #D4AF37; background: rgba(255,255,255,0.95); padding: 25px; border-radius: 0 20px 20px 0; margin: 20px 0; }}
    .gold {{ color: #D4AF37; font-weight: 700; }}
    div.stButton > button {{ background: #1a1a1a !important; color: #D4AF37 !important; border-radius: 12px; height: 3.8em; width: 100%; font-weight: bold; border: none; }}
</style>
''', unsafe_allow_html=True)

# --- 4. PÁGINA 1: LA PROMESA ---
if st.session_state.p == 1:
    st.markdown("<h2 style='text-align:center; padding-top:20px;'>🏆 DIMELO <span class='gold'>GOLD</span></h2>", unsafe_allow_html=True)
    st.markdown('''<div class="card"><b>🤝 ¡TÚ DÍMELO, QUE YO HAGO LA MAGIA!</b><br><br>No importa si estás empezando hoy o si ya tienes tu negocio andando, <b>esta app es para ti</b>.<br><br>Vas a recibir un documento con <b>imagen profesional</b> y un lenguaje claro y técnico. Cumple con la <b>DIAN</b> si decides crecer, o simplemente te da el estatus que mereces.<br><br><span class="gold">Tú solo dímelo</span>, que yo hago la magia.</div>''', unsafe_allow_html=True)
    n = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n)
    if st.button("¡ESTOY LISTO! ➡️"):
        if n:
            st.session_state.n = n
            st.session_state.p = 2
            st.rerun()

# --- 5. PÁGINA 2: ARQUITECTURA ---
elif st.session_state.p == 2:
    if st.button("← Volver"):
        st.session_state.p = 1
        st.rerun()
    st.markdown(f"<h3 style='text-align:center;'>🛡️ RESPALDO: <span class='gold'>{st.session_state.n.upper()}</span></h3>", unsafe_allow_html=True)
    st.markdown('<div class="card"><b>💡 TU ESCUDO COMERCIAL</b><br>La imagen y la ruta legal son tu armadura para cobrar lo justo y que el cliente confíe.</div>', unsafe_allow_html=True)
    st.session_state.sec = st.selectbox("Sector:", list(sectores.keys()))
    ta = st.text_input("¿QUÉ HACES EXACTAMENTE?", value=st.session_state.tip, placeholder=sectores[st.session_state.sec]['ej'])
    if ta: st.session_state.tip = ta
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📄 CTA COBRO"): st.session_state.l = "Cuenta de Cobro"
    with c2:
        if st.button("🏛️ COTIZACION"): st.session_state.l = "Cotizacion"
    if st.session_state.l: st.info(f"Ruta: {st.session_state.l.upper()}")
    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 ¡A HACER MAGIA!"):
            st.session_state.p = 3
            st.rerun()

# --- 6. PÁGINA 3: MOTOR ---
elif st.session_state.p == 3:
    st.markdown("<h2 style='text-align:
