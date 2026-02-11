import streamlit as st

# --- 1. CONFIGURACIÓN DE INGENIERÍA ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia de Estado Blindada (Forzamos inicio en P1)
if 'p' not in st.session_state: st.session_state.p = 1
if 'n' not in st.session_state: st.session_state.n = ''
if 'l' not in st.session_state: st.session_state.l = ''
if 'sec' not in st.session_state: st.session_state.sec = 'Otro'
if 'tip' not in st.session_state: st.session_state.tip = ''

# --- 2. BANCO DE DATOS: SECTORES, EJEMPLOS E IMÁGENES HD ---
# Usamos imágenes de 1080p para máxima claridad visual
contexto = {
    '🌾 Agro (Café, Ganado, Frutas)': {
        'ej': 'Ej: Venta de 10 cargas de café pergamino seco con entrega en bodega central.',
        'img': 'https://images.unsplash.com/photo-1500651230702-0e2d8a49d4ad?auto=format&fit=crop&q=80&w=1080'
    },
    '🛠️ Servicios Técnicos y Mantenimiento': {
        'ej': 'Ej: Mantenimiento preventivo de motor diésel y cambio de kit de distribución.',
        'img': 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&fit=crop&q=80&w=1080'
    },
    '🏗️ Construcción, Obra y Remodelación': {
        'ej': 'Ej: Remodelación de baño principal incluyendo enchape y cambio de tubería.',
        'img': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&q=80&w=1080'
    },
    '🍰 Gastronomía, Eventos y Catering': {
        'ej': 'Ej: Servicio de catering para 50 personas con menú ejecutivo y bebidas.',
        'img': 'https://images.unsplash.com/photo-1555244162-803834f70033?auto=format&fit=crop&q=80&w=1080'
    },
    '⚖️ Consultoría, Asesoría y Freelance': {
        'ej': 'Ej: Elaboración de estados financieros y asesoría tributaria mensual.',
        'img': 'https://images.unsplash.com/photo-1454165833767-027508658d61?auto=format&fit=crop&q=80&w=1080'
    },
    '🚚 Logística, Transporte y Mudanzas': {
        'ej': 'Ej: Transporte de mercancía pesada ruta Armenia-Medellín con seguro incluido.',
        'img': 'https://images.unsplash.com/photo-1519003722824-194d4455a60c?auto=format&fit=crop&q=80&w=1080'
    },
    '✨ Otro': {
        'ej': 'Ej: Describe aquí tu servicio o producto con tus propias palabras...',
        'img': 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80&w=1080'
    }
}

# --- 3. AMBIENTE VISUAL (SCROLL FORZADO Y CSS SUPREME) ---
sec_actual = st.session_state.sec if st.session_state.sec in contexto else 'Otro'
img_fondo = contexto[sec_actual]['img'] if st.session_state.p == 2 else "#ffffff"
bg_style = f"linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)), url('{img_fondo}')" if st.session_state.p == 2 else "#ffffff"

st.markdown(f'''
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {{
        overflow-y: auto !important; height: auto !important; min-height: 100vh !important;
        font-family: 'Montserrat', sans-serif;
    }}

    [data-testid="stAppViewContainer"] {{ 
        max-width: 450px; margin: 0 auto; background: {bg_style}; 
        background-size: cover; background-position: center;
        border-radius: 20px; box-shadow: 0 0 40px rgba(0,0,0,0.1); 
    }}
    
    .mentor-card {{ 
        border-left: 10px solid #D4AF37; background: rgba(255,255,255,0.96); 
        padding: 25px; border-radius: 0 20px 20px 0; margin: 20px 0; line-height: 1.6;
    }}
    
    .gold-text {{ color: #D4AF37; font-weight: 700; }}
    
    div.stButton > button {{ 
        background: #1a1a1a !important; color: #D4AF37 !important; 
        border-radius: 12px; height: 3.8em; width: 100%; 
        font-weight: bold; border: none; text-transform: uppercase;
    }}
    
    .footer-spacer {{ height: 100px; }}
</style>
''', unsafe_allow_html=True)

# --- 4. PÁGINA 1: LA PROMESA (LEY DIMELO) ---
if st.session_state.p == 1:
    st.markdown("<h2 style='text-align:center; padding-top:20px;'>🏆 DIMELO <span class='gold-text'>GOLD</span></h2>", unsafe_allow_html=True)
    st.markdown('''
    <div class="mentor-card">
        <b>🤝 ¡TÚ DÍMELO, QUE YO HAGO LA MAGIA!</b><br><br>
        ¡Hola! No importa si estás empezando hoy o si ya tienes tu negocio andando, <b>esta app es para ti</b>.<br><br>
        Vas a recibir un documento con <b>imagen profesional</b> y un lenguaje tan claro y técnico que tus clientes te verán como una empresa de alto nivel.<br><br>
        Para el emprendedor que quiere dar el siguiente paso, este documento cumple con los requisitos de la <b>DIAN</b>, dejándote la puerta abierta para facturación electrónica si así lo decides. Pero si solo buscas presentarte mejor, ¡estás en el lugar correcto!<br><br>
        <span class="gold-text">Tú solo dímelo</span> como parcero, que <span class="gold-text">yo hago la magia</span> de entregarte una propuesta impecable.
    </div>
    ''', unsafe_allow_html=True)
    
    nombre = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n)
    if st.button("¡ESTOY LISTO, VAMOS CON TODA! ➡️"):
        if nombre:
            st.session_state.n = nombre
            st.session_state.p = 2
            st.rerun()
    st.markdown('<div class="footer-spacer"></div>', unsafe_allow_html=True)

# --- 5. PÁGINA 2: ARQUITECTURA (PEDAGOGÍA COMPLETA Y SECTORES) ---
elif st.session_state.p == 2:
    if st.button("← Volver"):
        st.session_state.p = 1
        st.rerun()
    
    st.markdown(f"<h3 style='text-align:center;'>🛡️ RESPALDO: <span class='gold-text'>{st.session_state.n.upper()}</span></h3>", unsafe_allow_html=True)
    
    st.markdown('''
    <div class="mentor-card">
        <b>💡 TU ESCUDO COMERCIAL</b><br>
        Aquí no hay enredos. Vamos a ponerle <b>autoridad</b> a lo que haces. Elegir tu imagen y tu ruta legal no es una obligación pesada, es tu armadura para que el cliente confíe y tú cobres lo justo.<br><br>
        Vestir tu negocio de gala te abre puertas a mejores clientes y demuestra que tu trabajo tiene respaldo real ante la <b>DIAN</b>. ¡Yo te guío para que sea por beneficio, no por miedo!
    </div>
    ''', unsafe_allow_html=True)
    
    st.subheader("🖼️ TU IDENTIDAD")
    st.file_uploader("Sube tu logo", label_visibility="collapsed")
    
    st.write("---")
    st.subheader("🎯 TU SECTOR")
    st.session_state.sec = st.selectbox("¿En qué campo te destacas?", list(contexto.keys()))
    
    # Ejemplo Dinámico basado en Sector
    ejemplo_ia = contexto[st.session_state.sec]['ej']
    ta = st.text_input("¿QUÉ HACES EXACTAMENTE?", 
                       value=st.session_state.tip, 
                       placeholder=ejemplo_ia)
    if ta: st.session_state.tip = ta

    st.write("---")
    st.subheader("🏛️ TU RUTA COMERCIAL")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📄 CTA CO
