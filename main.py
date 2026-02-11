import streamlit as st

# --- 1. BANCO DE DATOS (LEY DIMELO) ---
P1_CARD = '<div class="card"><b>🤝 ¡TÚ DÍMELO, QUE YO HAGO LA MAGIA!</b><br><br>No importa si estás empezando hoy o si ya tienes tu negocio andando, esta app es para ti.<br><br>Recibirás un documento con <b>imagen profesional</b> y un lenguaje claro y técnico. Cumple con la <b>DIAN</b> si decides crecer, o simplemente te da el estatus que mereces.<br><br><span class="gold">Tú solo dímelo</span> como parcero, que <span class="gold">yo hago la magia</span>.</div>'

P2_CARD = '<div class="card"><b>💡 TU ESCUDO COMERCIAL</b><br>Aquí no hay enredos. Vamos a ponerle <b>autoridad</b> a lo que haces. Tu imagen y tu ruta legal son tu armadura para que el cliente confíe y tú cobres lo justo.<br><br>Vestir tu negocio de gala te abre puertas ante la <b>DIAN</b>. ¡Yo te guío para que sea por beneficio!</div>'

SECTORES = {
    '🌾 Agro': {'ej': 'Ej: Venta de 10 cargas de café...', 'img': 'https://images.unsplash.com/photo-1500651230702-0e2d8a49d4ad?w=1080'},
    '🛠️ Técnico': {'ej': 'Ej: Mantenimiento de motor diésel...', 'img': 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=1080'},
    '🏗️ Obra': {'ej': 'Ej: Remodelación de baño...', 'img': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1080'},
    '🍰 Gastro': {'ej': 'Ej: Servicio de catering...', 'img': 'https://images.unsplash.com/photo-1555244162-803834f70033?w=1080'},
    '⚖️ Legal': {'ej': 'Ej: Asesoría contable...', 'img': 'https://images.unsplash.com/photo-1454165833767-027508658d61?w=1080'},
    '✨ Otro': {'ej': 'Ej: Describe tu servicio...', 'img': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=1080'}
}

# --- 2. CONFIGURACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")
for k, v in {'p':1, 'n':'', 'l':'', 'sec':'✨ Otro', 'tip':''}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 3. CSS FRAGMENTADO (ANTIERRORES) ---
img_f = SECTORES.get(st.session_state.sec, SECTORES['✨ Otro'])['img']
bg_f = f"linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)), url('{img_f}')" if st.session_state.p == 2 else "#ffffff"

css_lines = [
    "<style>",
    "@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');",
    "html, body, [data-testid='stAppViewContainer'], .main { overflow-y: auto !important; height: auto !important; min-height: 100vh !important; font-family: 'Montserrat', sans-serif; }",
    f"[data-testid='stAppViewContainer'] {{ max-width: 450px; margin: 0 auto; background: {bg_f}; background-size: cover; background-position: center; border-radius: 20px; }}",
    ".card { border-left: 10px solid #D4AF37; background: rgba(255,255,255,0.96); padding: 25px; margin: 20px 0; }",
    ".gold { color: #D4AF37; font-weight: 700; }",
    "div.stButton > button { background: #1a1a1a !important; color: #D4AF37 !important; border-radius: 12px; height: 3.5em; width: 100%; font-weight: bold; border: none; }",
    "</style>"
]
st.markdown("".join(css_lines), unsafe_allow_html=True)

# --- 4. LÓGICA DE PANTALLAS ---
if st.session_state.p == 1:
    st.markdown("<h2 style='text-align:center; padding-top:20px;'>🏆 DIMELO <span class='gold'>GOLD</span></h2>", unsafe_allow_html=True)
    st.markdown(P1_CARD, unsafe_allow_html=True)
    n = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n)
    if st.button("¡VAMOS CON TODA! ➡️"):
        if n:
            st.session_state.n, st.session_state.p = n, 2
            st.rerun()

elif st.session_state.p == 2:
    if st.button("← Volver"):
        st.session_state.p = 1
        st.rerun()
    st.markdown(f"### 🛡️ RESPALDO: <span class='gold'>{st.session_state.n.upper()}</span>", unsafe_allow_html=True)
    st.markdown(P2_CARD, unsafe_allow_html=True)
    st.session_state.sec = st.selectbox("Sector:", list(SECTORES.keys()))
    ta = st.text_input("¿QUÉ HACES?", value=st.session_state.tip, placeholder=SECTORES[st.session_state.sec]['ej'])
    if ta: st.session_state.tip = ta
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📄 CTA COBRO"): st.session_state.l = "Cuenta de Cobro"
    with c2:
        if st.button("🏛️ COTIZACION"): st.session_state.l = "Cotización"
    if st.session_state.l: st.info(f"Ruta: {st.session_state.l.upper()}")
    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 ¡A HACER MAGIA!"):
            st.session_state.p = 3
            st.rerun()

elif st.session_state.p == 3:
    st.markdown("<h2 style='text-align:center;'>🎙️ MOTOR DE VOZ</h2>", unsafe_allow_html=True)
    st.markdown('<div class="card">Suéltalo todo, que yo hago la magia...</div>', unsafe_allow_html=True)
    if st.button("⬅️ VOLVER"):
        st.session_state.p = 2
        st.rerun()
