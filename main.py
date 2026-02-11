import streamlit as st

# --- 1. CONFIGURACION Y ESTADO ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia de Estado
for k, v in {'p':1, 'n':'', 'l':'', 'sec':'✨ Otro', 'tip':''}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 2. DICCIONARIO DE CONTEXTO ---
contexto = {
    'Agro': {
        'ej': 'Ej: Venta de 10 cargas de cafe pergamino...',
        'img': 'https://images.unsplash.com/photo-1500651230702-0e2d8a49d4ad?w=800'
    },
    'Tecnico': {
        'ej': 'Ej: Mantenimiento de motor diesel...',
        'img': 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=800'
    },
    'Gastronomia': {
        'ej': 'Ej: Servicio de catering para 50 personas...',
        'img': 'https://images.unsplash.com/photo-1555244162-803834f70033?w=800'
    },
    'Construccion': {
        'ej': 'Ej: Remodelacion de fachada...',
        'img': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=800'
    },
    'Consultoria': {
        'ej': 'Ej: Asesoria contable mensual...',
        'img': 'https://images.unsplash.com/photo-1454165833767-027508658d61?w=800'
    },
    'Otro': {
        'ej': 'Ej: Describe tu servicio...',
        'img': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800'
    }
}

# --- 3. AMBIENTE VISUAL ---
# Simplificamos claves para evitar errores de tildes en CSS
sec_ref = st.session_state.sec.split(' ')[0] if ' ' in st.session_state.sec else st.session_state.sec
if sec_ref not in contexto: sec_ref = 'Otro'

img_url = contexto[sec_ref]['img'] if st.session_state.p == 2 else ""
bg_style = f"background-image: linear-gradient(rgba(255,255,255,0.88), rgba(255,255,255,0.88)), url('{img_url}');" if st.session_state.p == 2 else "background-color: #ffffff;"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    [data-testid="stAppViewContainer"] {{
        max-width: 460px; margin: 0 auto; {bg_style} background-size: cover;
        box-shadow: 0 0 60px rgba(0,0,0,0.1); border-radius: 20px; transition: all 0.5s ease;
    }}
    html, body, .main {{ overflow-y: auto !important; height: auto !important; font-family: 'Montserrat'; }}
    .mentor-card {{ border-left: 10px solid #D4AF37; background: rgba(253,253,253,0.95); padding: 25px; margin: 20px 0; border-radius: 0 20px 20px 0; }}
    .highlight {{ color: #D4AF37; font-weight: 700; }}
    div.stButton > button {{ background: #1a1a1a !important; color: #D4AF37 !important; border-radius: 12px; height: 3.8em; font-weight: 700; width: 100%; border: none; text-transform: uppercase; }}
</style>
""", unsafe_allow_html=True)

# --- 4. PAGINA 1: LA PROMESA ---
if st.session_state.p == 1:
    st.markdown('<h2 style="text-align:center; padding-top:20px;">🏆 DIMELO <span class="highlight">GOLD</span></h2>', unsafe_allow_html=True)
    st.markdown("""<div class="mentor-card">
    <h3 style="margin-top:0;">🤝 TU DIMELO, QUE YO HAGO LA MAGIA!</h3>
    No importa si estas empezando hoy o si ya tienes tu negocio andando, esta app es para ti.<br><br>
    Recibiras un documento con imagen profesional y lenguaje tecnico de alto nivel. Si decides crecer, esto cumple con la DIAN para tu factura electronica.
    <br><br><span class="highlight">Tu solo dimelo</span>, que yo me encargo.</div>""", unsafe_allow_html=True)
    
    n = st.text_input("COMO TE LLAMAS?", value=st.session_state.n)
    if st.button("EST
