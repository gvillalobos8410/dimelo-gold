import streamlit as st

# --- 1. CONFIGURACION ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia de Estado (Siempre inicia en P1 si es sesion nueva)
for k, v in {'p':1, 'n':'', 'l':'', 'sec':'Otro', 'tip':''}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 2. BANCO DE DATOS (IMAGENES HD Y EJEMPLOS) ---
contexto = {
    'Agro': {
        'txt': '🌾 Agro (Cafe, Ganado, Frutas)',
        'ej': 'Ej: Venta de 10 cargas de cafe pergamino seco...',
        'img': 'https://images.unsplash.com/photo-1500651230702-0e2d8a49d4ad?w=1080'
    },
    'Tecnico': {
        'txt': '🛠️ Servicios Tecnicos y Mantenimiento',
        'ej': 'Ej: Mantenimiento preventivo de motor diesel...',
        'img': 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=1080'
    },
    'Obra': {
        'txt': '🏗️ Construccion y Remodelacion',
        'ej': 'Ej: Remodelacion de bano y cambio de tuberia...',
        'img': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1080'
    },
    'Gastro': {
        'txt': '🍰 Gastronomia y Eventos',
        'ej': 'Ej: Servicio de catering para 50 personas...',
        'img': 'https://images.unsplash.com/photo-1555244162-803834f70033?w=1080'
    },
    'Otro': {
        'txt': '✨ Otro Sector',
        'ej': 'Ej: Describe tu producto o servicio...',
        'img': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=1080'
    }
}

# --- 3. CSS SUPREME (SCROLL Y ESTETICA) ---
img_fondo = contexto.get(st.session_state.sec, contexto['Otro'])['img']
bg_style = f"linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)), url('{img_fondo}')" if st.session_state.p == 2 else "#ffffff"

st.markdown(f'''
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"], .main {{
        overflow-y: auto !important; height: auto !important; min-height: 100vh !important;
        font-family: 'Montserrat', sans-serif;
    }}
    [data-testid="stAppViewContainer"] {{ 
        max-width: 450px; margin: 0 auto; background: {bg_style}; 
        background-size: cover; background-position: center; border-radius: 20px;
    }}
    .card {{ border-left: 10px solid #D4AF37; background: rgba(255,255,255,0.96); padding: 25px; margin: 20px 0; }}
    .gold {{ color: #D4AF37; font-weight: 700; }}
    div.stButton > button {{ background: #1a1a1a !important; color: #D4AF37 !important; border-radius: 12px; height: 3.8em; width: 100%; font-weight: bold; border: none; }}
</style>
''', unsafe_allow_html=True)

# --- 4. LOGICA DE PANTALLAS ---

if st.session_state.p == 1:
    st.markdown("## 🏆 DIMELO <span class='gold'>GOLD</span>", unsafe_allow_html=True)
    st.markdown('''<div class="card"><b>🤝 TU DIMELO, QUE YO HAGO LA MAGIA!</b><br><br>
    No importa si estas empezando hoy o ya tienes tu negocio andando, <b>esta app es para ti</b>.<br><br>
    Vas a recibir un documento con <b>imagen profesional</b> y un lenguaje claro y tecnico. 
    Cumple con los requisitos de la <b>DIAN</b> si decides crecer, o simplemente te da el estatus que mereces.
    <br><br><span class="gold">Tu solo dimelo</span> como parcero, que yo hago la magia.</div>''', unsafe_allow_html=True)
    n = st.text_input("COMO TE LLAMAS?", value=st.session_state.n)
    if st.button("ESTOY LISTO! ➡️"):
        if n:
            st.session_state.n = n
            st.session_state.p = 2
            st.rerun()

elif st.session_state.p == 2:
    if st.button("← Volver"):
        st.session_state.p = 1
        st.rerun()
    st.markdown(f"### 🛡️ RESPALDO: <span class='gold'>{st.session_state.n.upper()}</span>", unsafe_allow_html=True)
    st.markdown('''<div class="card"><b>💡 TU ESCUDO COMERCIAL</b><br>
    Vamos a ponerle <b>autoridad</b> a lo que haces. Tu imagen y ruta legal son tu armadura para cobrar lo justo y demostrar respaldo ante la <b>DIAN</b>. Beneficio, no miedo!</div>''', unsafe_allow_html=True)
    
    opciones = {v['txt']: k for k, v in contexto.items()}
    seleccion = st.selectbox("Sector de negocio:", list(opciones.keys()))
    st.session_state.sec = opciones[seleccion]
    
    ej_ia = contexto[st.session_state.sec]['ej']
    ta = st.text_input("QUE HACES EXACTAMENTE?", value=st.session_state.tip, placeholder=ej_ia)
    if ta: st.session_state.tip = ta
    
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("
