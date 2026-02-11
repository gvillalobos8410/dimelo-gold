import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia de Estado
if 'p' not in st.session_state: st.session_state.p = 1
if 'n' not in st.session_state: st.session_state.n = ''
if 'l' not in st.session_state: st.session_state.l = ''
if 'sec' not in st.session_state: st.session_state.sec = 'Otro'
if 'tip' not in st.session_state: st.session_state.tip = ''

# --- 2. BANCO DE DATOS (EJEMPLOS DINÁMICOS) ---
ejemplos = {
    '🌾 Agro': 'Ej: Venta de 10 cargas de cafe pergamino seco...',
    '🛠️ Tecnico': 'Ej: Mantenimiento preventivo de motor diesel...',
    '🏗️ Obra': 'Ej: Remodelacion de bano y cambio de tuberia...',
    '🍰 Gastro': 'Ej: Servicio de catering para 50 personas...',
    '✨ Otro': 'Ej: Describe tu producto o servicio...'
}

# --- 3. ESTILO CSS (MINIMALISTA Y ESTABLE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], .main {
        font-family: 'Montserrat', sans-serif;
        background-color: #f8f9fa !important;
    }

    [data-testid="stAppViewContainer"] { 
        max-width: 450px; margin: 0 auto; 
        background: #ffffff;
        border-radius: 20px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }
    
    .mentor-card { 
        border-left: 10px solid #D4AF37; 
        background: #ffffff; 
        padding: 25px; 
        margin: 20px 0; 
        box-shadow: 2px 2px 15px rgba(0,0,0,0.02);
    }
    
    .gold-text { color: #D4AF37; font-weight: 700; }
    
    div.stButton > button { 
        background: #1a1a1a !important; 
        color: #D4AF37 !important; 
        border-radius: 12px; 
        height: 3.5em; width: 100%; 
        font-weight: bold; border: none;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. PÁGINA 1: LA PROMESA ---
if st.session_state.p == 1:
    st.markdown("<h2 style='text-align:center; padding-top:20px;'>🏆 DIMELO <span class='gold-text'>GOLD</span></h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="mentor-card">
        <b>🤝 ¡TÚ DÍMELO, QUE YO HAGO LA MAGIA!</b><br><br>
        ¡Hola! No importa si estás empezando hoy o si ya tienes tu negocio andando, <b>esta app es para ti</b>.<br><br>
        Vas a recibir un documento con <b>imagen profesional</b> y un lenguaje claro y técnico. Cumple con la <b>DIAN</b> si decides crecer, o simplemente te da el estatus que mereces.
        <br><br><span class="gold-text">Tú solo dímelo</span> como parcero, que yo hago la magia.
    </div>
    """, unsafe_allow_html=True)
    
    n = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n)
    if st.button("¡VAMOS CON TODA! ➡️"):
        if n:
            st.session_state.n, st.session_state.p = n, 2
            st.rerun()

# --- 5. PÁGINA 2: ARQUITECTURA ---
elif st.session_state.p == 2:
    if st.button("← Volver"):
        st.session_state.p = 1
        st.rerun()
    
    st.markdown(f"<h3 style='text-align:center;'>🛡️ RESPALDO: <span class='gold-text'>{st.session_state.n.upper()}</span></h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mentor-card">
        <b>💡 TU ESCUDO COMERCIAL</b><br>
        Aquí no hay enredos. Vamos a darle <b>autoridad</b> a lo que haces. Tu imagen y tu ruta legal son tu armadura para cobrar lo justo y demostrar respaldo ante la <b>DIAN</b>.
    </div>
    """, unsafe_allow_html=True)
    
    st.session_state.sec = st.selectbox("Sector de negocio:", list(ejemplos.keys()))
    
    ta = st.text_input("¿QUÉ HACES EXACTAMENTE?", 
                       value=st.session_state.tip, 
                       placeholder=ejemplos[st.session_state.sec])
    if ta: st.session_state.tip = ta

    st.write("---")
    st.write("<b>¿CÓMO TE PRESENTAS HOY?</b>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📄 CTA COBRO"): st.session_state.l = "Cuenta de Cobro"
    with c2:
        if st.button("🏛️ COTIZACION"): st.session_state.l = "Cotizacion"
            
    if st.session_state.l:
        st.info(f"Ruta: {st.session_state.l.upper()}")

    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 TODO LISTO, ¡A HACER MAGIA!"):
            st.session_state.p = 3
            st.rerun()

# --- 6. PÁGINA 3: MOTOR ---
elif st.session_state.p == 3:
    st.markdown("<h2 style='text-align:center;'>🎙️ MOTOR DE VOZ</h2>", unsafe_allow_html=True)
    st.markdown('<div class="mentor-card">Suéltalo todo, que yo hago la magia de transformarlo en un documento profesional.</div>', unsafe_allow_html=True)
    if st.button("⬅️ RECONFIGURAR"):
        st.session_state.p = 2
        st.rerun()
