import streamlit as st

# --- 1. CONFIGURACIÓN DE ALTO NIVEL ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia de Estado Blindada
for k, v in {'p':1, 'n':'', 'l':'', 'sec':'Otro', 'tip':'', 'logo':False}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 2. AMBIENTE DE INTERFAZ (CSS MODULAR) ---
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
        color: #D4AF37 !important; border-radius: 12px; height: 4em;
        font-weight: 700; width: 100%; border: none; text-transform: uppercase;
    }
    .spacer { height: 100px; }
</style>
"""
st.markdown(estilo_celular, unsafe_allow_html=True)

# --- 3. PÁGINA 1: EL SOCIO TECNOLÓGICO (REDISEÑADA) ---
if st.session_state.p == 1:
    st.markdown('<h2 style="text-align:center; padding-top:20px;">🏆 DIMELO <span class="highlight">GOLD</span></h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mentor-card">
        <h3 style="margin-top:0;">🚀 ¡LLEVEMOS TU NEGOCIO A OTRO NIVEL!</h3>
        Bienvenido a tu nueva estación de trabajo. Aquí no estás solo; somos tus <b>compañeros de crecimiento</b>.<br><br>
        ¿Alguna vez has sentido que tu idea es genial pero te falta "labia" técnica para cobrar lo que vales? 
        Nuestra <span class="highlight">Inteligencia Artificial</span> está aquí para facilitar tus cotizaciones: 
        toma tu lenguaje natural, lo pule, le da un tono profesional y técnico, y lo convierte en un documento poderoso.<br><br>
        <i>¡Prepárate para cerrar negocios como los grandes!</i>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Para empezar esta alianza...")
    n = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n, placeholder="Tu nombre y apellido")
    
    if st.button("¡VAMOS A FACILITAR TU NEGOCIO! ➡️"):
        if n:
            st.session_state.n = n
            st.session_state.p = 2
            st.rerun()
        else:
            st.warning("Oye, un buen socio siempre se presenta. Dime tu nombre.")
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- 4. PÁGINA 2: ARQUITECTURA DE RESPALDO ---
elif st.session_state.p == 2:
    if st.button("← Volver al inicio"):
        st.session_state.p = 1
        st.rerun()

    st.markdown(f'<h3 style="text-align:center;">🛡️ ¡CON TODA, <span class="highlight">{st.session_state.n.upper()}</span>!</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mentor-card">
        <h3 style="margin-top:0;">💡 EL ESCUDO COMERCIAL</h3>
        Para que esa IA trabaje con fuerza, necesitamos darle <b>autoridad</b>. 
        Vestir tu negocio de gala con un logo y una ruta legal clara (DIAN) no es un trámite, 
        es tu armadura para que los clientes confíen en ti de inmediato. ¡Yo te guío!
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
    st.session_state.sec = st.selectbox("¿En qué campo eres experto?", sectores)
    
    ta = st.text_input("¿QUÉ HACES EXACTAMENTE?", value=st.session_state.tip, placeholder="Ej: Venta de equipos industriales")
    if ta: st.session_state.tip = ta

    st.write("---")
    st.subheader("🏛️ ¿CÓMO QUIERES RESPALDARTE?")
    st.write("<small>Dales seguridad a tus clientes con la ruta legal que prefieras hoy.</small>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📄 CTA. COBRO"): st.session_state.l = "Cuenta de Cobro"
    with c2:
        if st.button("🏛️ COTIZACIÓN"): st.session_state.l = "Cotización"
            
    if st.session_state.l:
        st.info(f"Ruta seleccionada: **{st.session_state.l.upper()}**")

    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 ABRIR MOTOR DE PRECISIÓN"):
            st.session_state.p = 3
            st.rerun()
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
