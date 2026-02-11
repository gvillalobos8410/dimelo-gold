import streamlit as st

# --- 1. CONFIGURACIÓN Y ESTADO INICIAL ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

for k, v in {'p':1, 'n':'', 'l':'', 'sec':'✨ Otro', 'tip':''}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 2. DICCIONARIO DE AMBIENTACIÓN (AGRO, TÉCNICO, ETC.) ---
contexto = {
    '🌾 Agro (Café, Ganado, Frutas)': {
        'ej': 'Ej: Venta de 10 cargas de café pergamino seco...',
        'img': 'https://images.unsplash.com/photo-1500651230702-0e2d8a49d4ad?w=800'
    },
    '🛠️ Servicios Técnicos / Mantenimiento': {
        'ej': 'Ej: Mantenimiento preventivo de motor diesel...',
        'img': 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=800'
    },
    '🍰 Gastronomía y Eventos': {
        'ej': 'Ej: Servicio de catering para 50 personas...',
        'img': 'https://images.unsplash.com/photo-1555244162-803834f70033?w=800'
    },
    '🏗️ Construcción y Obra': {
        'ej': 'Ej: Remodelación de fachada con pintura acrílica...',
        'img': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=800'
    },
    '⚖️ Consultoría Profesional': {
        'ej': 'Ej: Asesoría contable mensual y cierre fiscal...',
        'img': 'https://images.unsplash.com/photo-1454165833767-027508658d61?w=800'
    },
    '✨ Otro': {
        'ej': 'Ej: Describe aquí tu servicio...',
        'img': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800'
    }
}

# --- 3. CSS DINÁMICO MÓVIL ---
img_url = contexto[st.session_state.sec]['img'] if st.session_state.p == 2 else ""
bg_style = f"background-image: linear-gradient(rgba(255,255,255,0.88), rgba(255,255,255,0.88)), url('{img_url}');" if st.session_state.p == 2 else "background-color: #ffffff;"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    [data-testid="stAppViewContainer"] {{
        max-width: 460px; margin: 0 auto; {bg_style} background-size: cover; background-position: center;
        box-shadow: 0 0 60px rgba(0,0,0,0.1); border-radius: 20px; transition: all 0.5s ease;
    }}
    html, body, .main {{ overflow-y: auto !important; height: auto !important; font-family: 'Montserrat'; }}
    .mentor-card {{ border-left: 10px solid #D4AF37; background: rgba(253,253,253,0.95); padding: 25px; margin: 20px 0; border-radius: 0 20px 20px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
    .highlight {{ color: #D4AF37; font-weight: 700; }}
    div.stButton > button {{ background: #1a1a1a !important; color: #D4AF37 !important; border-radius: 12px; height: 3.8em; font-weight: 700; width: 100%; border: none; text-transform: uppercase; }}
    .stSelectbox, .stTextInput {{ margin-bottom: 15px; }}
</style>
""", unsafe_allow_html=True)

# --- 4. PÁGINA 1: EL SOCIO DE TRANSFORMACIÓN ---
if st.session_state.p == 1:
    st.markdown('<h2 style="text-align:center; padding-top:20px;">🏆 DIMELO <span class="highlight">GOLD</span></h2>', unsafe_allow_html=True)
    st.markdown("""<div class="mentor-card"><h3 style="margin-top:0;">🤝 ¡TÚ DÍMELO, QUE YO HAGO LA MAGIA!</h3>
    ¡Hola! No importa si estás empezando hoy o si ya tienes tu negocio andando, <b>esta app es para ti</b>.<br><br>
    Vas a recibir un documento con <b>imagen profesional</b> y un lenguaje tan claro y técnico que tus clientes te verán como una empresa de alto nivel.<br><br>
    <span class="highlight">Tú solo dímelo</span> como parcero, que <span class="highlight">yo hago la magia</span> de entregarte una propuesta impecable.</div>""", unsafe_allow_html=True)
    
    n = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n, placeholder="Tu nombre y apellido")
    if st.button("¡ESTOY LISTO, VAMOS CON TODA! ➡️"):
        if n:
            st.session_state.n = n
            st.session_state.p = 2
            st.rerun()

# --- 5. PÁGINA 2: ARQUITECTURA AMBIENTADA ---
elif st.session_state.p == 2:
    if st.button("← Volver al inicio"):
        st.session_state.p = 1
        st.rerun()
    
    st.markdown(f'<h3 style="text-align:center;">🛡️ RESPALDO: <span class="highlight">{st.session_state.n.upper()}</span></h3>', unsafe_allow_html=True)
    st.markdown("""<div class="mentor-card"><h3 style="margin-top:0;">💡 TU ESCUDO COMERCIAL</h3>
    Vamos a ponerle <b>autoridad</b> a lo que haces. Tu imagen y tu ruta legal son tu armadura para que el cliente confíe y tú cobres lo justo.</div>""", unsafe_allow_html=True)
    
    st.subheader("🖼️ TU IDENTIDAD")
    st.file_uploader("Sube tu logo", label_visibility="collapsed")
    
    st.write("---")
    st.subheader("🎯 TU SECTOR")
    secs = list(contexto.keys())
    st.session_state.sec = st.selectbox("¿En qué sector te mueves?", secs, index=secs.index(st.session_state.sec))
    
    # Ejemplo Dinámico
    ej_dinamico = contexto[st.session_state.sec]['ej']
    ta = st.text_input("¿QUÉ HACES EXACTAMENTE?", value=st.session_state.tip, placeholder=ej_dinamico)
    if ta: st.session_state.tip = ta

    st.write("---")
    st.subheader("🏛️ ¿CÓ
