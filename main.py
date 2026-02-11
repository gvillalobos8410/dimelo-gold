import streamlit as st

# --- 1. CONFIGURACIÓN DE INGENIERÍA ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia de Estado Blindada
if 'p' not in st.session_state: st.session_state.p = 1
if 'n' not in st.session_state: st.session_state.n = ''
if 'l' not in st.session_state: st.session_state.l = ''
if 'sec' not in st.session_state: st.session_state.sec = 'Otro'
if 'tip' not in st.session_state: st.session_state.tip = ''
if 'logo' not in st.session_state: st.session_state.logo = False

# --- 2. DICCIONARIO DE AMBIENTACIÓN (MAGIA DE SECTORES) ---
# Aquí definimos el ejemplo y la imagen de fondo por sector
contexto_sectores = {
    '🌾 Agro (Café, Ganado, Frutas)': {
        'ejemplo': 'Ej: Venta de 10 cargas de café pergamino seco con entrega en bodega.',
        'img': 'https://images.unsplash.com/photo-1500651230702-0e2d8a49d4ad?auto=format&fit=crop&q=80&w=600'
    },
    '🛠️ Servicios Técnicos / Mantenimiento': {
        'ejemplo': 'Ej: Mantenimiento preventivo de motor diesel y cambio de filtros.',
        'img': 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&fit=crop&q=80&w=600'
    },
    '🍰 Gastronomía y Eventos': {
        'ejemplo': 'Ej: Servicio de catering para 50 personas con menú de tres tiempos.',
        'img': 'https://images.unsplash.com/photo-1555244162-803834f70033?auto=format&fit=crop&q=80&w=600'
    },
    '🏗️ Construcción y Obra': {
        'ejemplo': 'Ej: Remodelación de fachada con pintura acrílica y resane de grietas.',
        'img': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&q=80&w=600'
    },
    '⚖️ Consultoría Profesional': {
        'ejemplo': 'Ej: Asesoría contable mensual y cierre de estados financieros.',
        'img': 'https://images.unsplash.com/photo-1454165833767-027508658d61?auto=format&fit=crop&q=80&w=600'
    },
    '✨ Otro': {
        'ejemplo': 'Ej: Describe aquí tu servicio o producto...',
        'img': 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80&w=600'
    }
}

# --- 3. AMBIENTE DE INTERFAZ (CSS MODULAR CON FONDO DINÁMICO) ---
# Obtenemos la imagen según lo que haya seleccionado el usuario
img_fondo = contexto_sectores.get(st.session_state.sec, contexto_sectores['✨ Otro'])['img']

estilo_celular = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    [data-testid="stAppViewContainer"] {{
        max-width: 460px; margin: 0 auto; 
        background-image: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)), url('{img_fondo}');
        background-size: cover; background-position: center;
        box-shadow: 0 0 60px rgba(0,0,0,0.07); border-radius: 20px;
        transition: background-image 0.5s ease-in-out;
    }}
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {{
        overflow-y: auto !important; height: auto !important; font-family: 'Montserrat', sans-serif;
    }}
    .mentor-card {{
        border-left: 10px solid #D4AF37; background: rgba(253, 253, 253, 0.95); padding: 25px;
        border-radius: 0 20px 20px 0; margin: 20px 0; line-height: 1.6;
    }}
    .highlight {{ color: #D4AF37; font-weight: 700; }}
    div.stButton > button {{
        background: linear-gradient(135deg, #1a1a1a 0%, #333 100%) !important;
        color: #D4AF37 !important; border-radius: 12px; height: 4.2em;
        font-weight: 700; width: 100%; border: none; text-transform: uppercase;
    }}
    .spacer {{ height: 100px; }}
</style>
"""
st.markdown(estilo_celular, unsafe_allow_html=True)

# --- 4. PÁGINA 1: (BLINDADA POR LEY) ---
if st.session_state.p == 1:
    st.markdown('<h2 style="text-align:center; padding-top:20px;">🏆 DIMELO <span class="highlight">GOLD</span></h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="mentor-card">
        <h3 style="margin-top:0;">🤝 ¡TÚ DÍMELO, QUE YO HAGO LA MAGIA!</h3>
        ¡Hola! No importa si estás empezando hoy o si ya tienes tu negocio andando, <b>esta app es para ti</b>.<br><br>
        <span class="highlight">¿Qué vas a lograr conmigo?</span><br>
        Vas a recibir un documento con <b>imagen profesional</b> y un lenguaje tan claro y técnico que tus clientes te verán como una empresa de alto nivel. <br><br>
        <span class="highlight">Tú solo dímelo</span> como parcero, que <span class="highlight">yo hago la magia</span> de entregarte una propuesta impecable.
    </div>
    """, unsafe_allow_html=True)
    n = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n, placeholder="Tu nombre y apellido")
    if st.button("¡ESTOY LISTO, VAMOS CON TODA! ➡️"):
        if n:
            st.session_state.n = n
            st.session_state.p = 2
            st.rerun()

# --- 5. PÁGINA 2: ARQUITECTURA AMBIENTADA ---
elif st.session_state.p == 2:
    if st.button("← Volver"):
        st.session_state.p = 1
        st.rerun()

    st.markdown(f'<h3 style="text-align:center;">🛡️ RESPALDO: <span class="highlight">{st.session_state.n.upper()}</span></h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mentor-card">
        <h3 style="margin-top:0;">💡 TU ESCUDO COMERCIAL</h3>
        Vamos a ponerle <b>autoridad</b> a lo que haces. Tu imagen y tu ruta legal son tu armadura para que el cliente confíe y tú cobres lo justo.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🖼️ TU IDENTIDAD")
    st.file_uploader("Sube tu logo", label_visibility="collapsed")
    
    st.write("---")
    st.subheader("🎯 TU SECTOR")
    
    # Selector de Sector
    sectores = list(contexto_sectores.keys())
    st.session_state.sec = st.selectbox("¿En qué sector te mueves?", sectores)
    
    # Obtener ejemplo dinámico basado en el sector seleccionado
    ejemplo_dinamico = contexto_sectores[st.session_state.sec]['ejemplo']
    
    ta = st.text_input("¿QUÉ HACES EXACTAMENTE?", 
                       value=st.session_state.tip, 
                       placeholder=ejemplo_dinamico,
                       help="Cuéntame brevemente qué vendes o qué servicio prestas.")
    if ta: st.session_state.tip = ta

    st.write("---")
    st.subheader("🏛️ ¿CÓMO QUIERES PRESENTARTE?")
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📄 CTA. COBRO"): st.session_state.l = "Cuenta de Cobro"
    with c2:
        if st.button("🏛️ COTIZACIÓN"): st.session_state.l = "Cotización"
            
    if st.session_state.l:
        st.info(f"Ruta elegida: **{st.session_state.l.upper()}**")

    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 TODO LISTO, ¡A HACER MAGIA!"):
            st.session_state.p = 3
            st.rerun()
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
