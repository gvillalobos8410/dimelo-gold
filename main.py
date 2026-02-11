import streamlit as st

# --- 1. CONFIGURACIÓN DE RECURSOS (VARIABLES CORTAS PARA EVITAR CORTES) ---
# Imágenes de fondo realistas
IMG_AGRO = "https://images.unsplash.com/photo-1500651230702-0e2d8a49d4ad?w=600"
IMG_TECH = "https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=600"
IMG_GAST = "https://images.unsplash.com/photo-1555244162-803834f70033?w=600"
IMG_OBRA = "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=600"
IMG_OTRO = "https://images.unsplash.com/photo-1497366216548-37526070297c?w=600"

# Textos de la Pedagogía (LEY DIMELO)
MSG_P1 = (
    "Hola! No importa si estas empezando hoy o si ya tienes tu negocio andando, "
    "esta app es para ti. Recibiras un documento con imagen profesional y lenguaje "
    "tecnico de alto nivel. Si decides crecer, esto cumple con la DIAN para tu "
    "factura electronica, o simplemente te da el estatus que mereces."
)
MSG_P2 = (
    "Aqui no hay enredos. Vamos a ponerle autoridad a lo que haces. Elegir tu "
    "imagen y tu ruta legal es tu armadura para que el cliente confie y tu cobres lo justo."
)

# --- 2. CONFIGURACIÓN DE STREAMLIT ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia de Estado
for k, v in {'p':1, 'n':'', 'l':'', 'sec':'Otros', 'tip':''}.items():
    if k not in st.session_state: st.session_state[k] = v

# Mapa de Sectores
sectores = {
    'Agro': {'ej': 'Venta de cafe pergamino...', 'img': IMG_AGRO},
    'Tecnico': {'ej': 'Mantenimiento de motores...', 'img': IMG_TECH},
    'Gastro': {'ej': 'Servicio de banquetes...', 'img': IMG_GAST},
    'Obra': {'ej': 'Remodelacion y pintura...', 'img': IMG_OBRA},
    'Otros': {'ej': 'Describe tu servicio...', 'img': IMG_OTRO}
}

# --- 3. AMBIENTE VISUAL (CSS CON SCROLL FORZADO) ---
img_actual = sectores[st.session_state.sec]['img'] if st.session_state.p == 2 else ""
bg_style = f"linear-gradient(rgba(255,255,255,0.9),rgba(255,255,255,0.9)),url('{img_actual}')" if img_actual else "#ffffff"

st.markdown(f'''
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"], .main {{
        overflow-y: auto !important; height: auto !important; min-height: 100vh !important;
        font-family: 'Montserrat', sans-serif;
    }}
    [data-testid="stAppViewContainer"] {{ 
        max-width: 450px; margin: 0 auto; background: {bg_style}; 
        background-size: cover; background-position: center;
        border-radius: 20px; box-shadow: 0 0 40px rgba(0,0,0,0.1); 
    }}
    .card {{ border-left: 10px solid #D4AF37; background: rgba(255,255,255,0.95); padding: 25px; border-radius: 0 20px 20px 0; margin: 15px 0; }}
    .gold {{ color: #D4AF37; font-weight: 700; }}
    div.stButton > button {{ background: #1a1a1a !important; color: #D4AF37 !important; border-radius: 12px; height: 3.5em; width: 100%; font-weight: bold; border: none; }}
</style>
''', unsafe_allow_html=True)

# --- 4. LÓGICA DE PÁGINAS ---
if st.session_state.p == 1:
    st.markdown("## 🏆 DIMELO <span class='gold'>GOLD</span>", unsafe_allow_html=True)
    st.markdown(f'<div class="card"><b>🤝 TU DIMELO, QUE YO HAGO LA MAGIA!</b><br><br>{MSG_P1}</div>', unsafe_allow_html=True)
    nombre_usuario = st.text_input("COMO TE LLAMAS?", value=st.session_state.n)
    if st.button("ESTOY LISTO! ➡️"):
        if nombre_usuario:
            st.session_state.n = nombre_usuario
            st.session_state.p = 2
            st.rerun()

elif st.session_state.p == 2:
    if st.button("<- VOLVER"):
        st.session_state.p = 1
        st.rerun()
    st.markdown(f"### 🛡️ RESPALDO: <span class='gold'>{st.session_state.n.upper()}</span>", unsafe_allow_html=True)
    st.markdown(f'<div class="card"><b>💡 TU ESCUDO COMERCIAL</b><br>{MSG_P2}</div>', unsafe_allow_html=True)
    st.session_state.sec = st.selectbox("Sector:", list(sectores.keys()))
    ej_text = sectores[st.session_state.sec]['ej']
    desc_negocio = st.text_input("QUE HACES EXACTAMENTE?", value=st.session_state.tip, placeholder=ej_text)
    if desc_negocio: st.session_state.tip = desc_negocio
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📄 CTA COBRO"): st.session_state.l = "Cuenta de Cobro"
    with c2:
        if st.button("🏛️ COTIZACION"): st.session_state.l = "Cotizacion"
    if st.session_state.l: st.info(f"Ruta: {st.session_state.l}")
    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 HACER MAGIA!"):
            st.session_state.p = 3
            st.rerun()

elif st.session_state.p == 3:
    st.markdown("## 🎙️ MOTOR DE VOZ", unsafe_allow_html=True)
    st.markdown('<div class="card">Tu solo dimelo, que yo hago la magia. Habla ahora...</div>', unsafe_allow_html=True)
    if st.button("<- RECONFIGURAR"):
        st.session_state.p = 2
        st.rerun()
