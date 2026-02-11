import streamlit as st

# --- 1. CONFIGURACIÓN DE ALTO NIVEL ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia de Estado Blindada
for k, v in {'p':1, 'n':'', 'l':'', 'sec':'Otro', 'tip':'', 'logo':False}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 2. AMBIENTE DE INTERFAZ (CSS MODULAR SHARK) ---
estilo_celular = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    [data-testid="stAppViewContainer"] {
        max-width: 460px; margin: 0 auto; background: #fff;
        box-shadow: 0 0 60px rgba(0,0,0,0.07); border-radius: 20px;
    }
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {
        overflow-y: auto !important; height: auto !important; font-family: 'Montserrat', sans-serif;
    }
    .mentor-card {
        border-left: 10px solid #D4AF37; background: #fdfdfd; padding: 25px;
        border-radius: 0 20px 20px 0; margin: 20px 0; line-height: 1.6;
    }
    .highlight { color: #D4AF37; font-weight: 700; }
    div.stButton > button {
        background: linear-gradient(135deg, #1a1a1a 0%, #333 100%) !important;
        color: #D4AF37 !important; border-radius: 12px; height: 4.2em;
        font-weight: 700; width: 100%; border: none; text-transform: uppercase;
        letter-spacing: 1px;
    }
    .spacer { height: 100px; }
</style>
"""
st.markdown(estilo_celular, unsafe_allow_html=True)

# --- 3. PÁGINA 1: EL SOCIO DE TRANSFORMACIÓN (ENFOQUE SHARK) ---
if st.session_state.p == 1:
    st.markdown('<h2 style="text-align:center; padding-top:20px;">🏆 DIMELO <span class="highlight">GOLD</span></h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mentor-card">
        <h3 style="margin-top:0;">🤝 ¡TÚ DÍMELO, QUE YO LO HAGO REALIDAD!</h3>
        Bienvenido, emprendedor. Aquí se acaba el camello de redactar propuestas complicadas.<br><br>
        ¿Tienes la idea pero no sabes cómo escribirla para que se vea profesional? <b>¡No te preocupes más!</b> <br><br>
        <span class="highlight">Tú solo me lo dices</span> con tus propias palabras, así de sencillo como si estuviéramos hablando, que <span class="highlight">yo me encargo de transformarlo</span> en un documento técnico, comercial y poderoso para llevar tu negocio a otro nivel.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Empecemos esta alianza...")
    n = st.text_input("¿CON QUIÉN TENGO EL GUSTO?", value=st.session_state.n, placeholder="Escribe tu nombre")
    
    if st.button("¡ESTOY LISTO, VAMOS CON TODA! ➡️"):
        if n:
            st.session_state.n = n
            st.session_state.p = 2
            st.rerun()
        else:
            st.warning("Oye, para cerrar este trato necesito saber tu nombre.")
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- 4. PÁGINA 2: ARQUITECTURA DE RESPALDO (PEDAGOGÍA DE CONFIANZA) ---
elif st.session_state.p == 2:
    if st.button("← Volver"):
        st.session_state.p = 1
        st.rerun()

    st.markdown(f'<h3 style="text-align:center;">🛡️ ARQUITECTURA: <span class="highlight">{st.session_state.n.upper()}</span></h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mentor-card">
        <h3 style="margin-top:0;">💡 EL TOQUE DE AUTORIDAD</h3>
        Para que mi IA transforme tus palabras en una propuesta ganadora, debemos darle un <b>respaldo serio</b>.<br><br>
        Poner tu logo y elegir tu ruta legal no es un enredo, es tu <span class="highlight">escudo comercial</span>. Así el cliente sabe que no eres uno más, sino un profesional que sabe para dónde va. ¡Yo te guío!
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🖼️ TU IDENTIDAD")
    st.file_uploader("Sube tu logo", label_visibility="collapsed")
    
    st.write("---")
    st.subheader("🎯 TU SECTOR")
    sectores = [
        '🌾 Agro (Café, Ganado, Frutas)', 
        '🛠️ Servicios Técnicos / Mantenimiento', 
        '🍰 Gastronomía y Eventos', 
        '🏗️ Construcción y Obra', 
        '⚖️ Consultoría Profesional', 
        '✨ Otro'
    ]
    st.session_state.sec = st.selectbox("¿En qué sector te mueves?", sectores)
    
    ta = st.text_input("¿QUÉ HACES EXACTAMENTE?", value=st.session_state.tip, placeholder="Ej: Mantenimiento de redes")
    if ta: st.session_state.tip = ta

    st.write("---")
    st.subheader("🏛️ ¿CÓMO TE RESPALDAMOS HOY?")
    st.write("<small>Dale seguridad a tu cliente con la ruta legal que mejor te quede.</small>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📄 CTA. COBRO"): st.session_state.l = "Cuenta de Cobro"
    with c2:
        if st.button("🏛️ COTIZACIÓN"): st.session_state.l = "Cotización"
            
    if st.session_state.l:
        st.info(f"Ruta elegida: **{st.session_state.l.upper()}**")

    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 ¡VAMOS AL MOTOR DE VOZ!"):
            st.session_state.p = 3
            st.rerun()
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
