import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Inicialización de Estado (Para que las páginas cambien)
if 'p' not in st.session_state: st.session_state.p = 1
if 'n' not in st.session_state: st.session_state.n = ''
if 'l' not in st.session_state: st.session_state.l = ''
if 'sec' not in st.session_state: st.session_state.sec = '✨ Otro'
if 'tip' not in st.session_state: st.session_state.tip = ''

# --- 2. BANCO DE DATOS ---
ejemplos = {
    '🌾 Agro': 'Ej: Venta de 10 cargas de cafe pergamino seco...',
    '🛠️ Tecnico': 'Ej: Mantenimiento preventivo de motor diesel...',
    '🏗️ Obra': 'Ej: Remodelacion de bano y cambio de tuberia...',
    '🍰 Gastro': 'Ej: Servicio de catering para 50 personas...',
    '✨ Otro': 'Ej: Describe tu producto o servicio...'
}

# --- 3. ESTILO CSS (SCROLL Y ESTÉTICA) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {
        overflow-y: auto !important;
        height: auto !important;
        min-height: 100vh !important;
        font-family: 'Montserrat', sans-serif;
    }

    [data-testid="stAppViewContainer"] { 
        max-width: 450px; margin: 0 auto; background: #ffffff;
        border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    }
    
    .mentor-card { 
        border-left: 10px solid #D4AF37; background: #ffffff; 
        padding: 25px; margin: 20px 0; line-height: 1.6;
    }
    
    .gold-text { color: #D4AF37; font-weight: 700; }
    
    div.stButton > button { 
        background: #1a1a1a !important; color: #D4AF37 !important; 
        border-radius: 12px; height: 3.5em; width: 100%; 
        font-weight: bold; border: none;
    }
    .spacer { height: 80px; }
</style>
""", unsafe_allow_html=True)

# --- 4. LÓGICA DE NAVEGACIÓN ---

# PÁGINA 1
if st.session_state.p == 1:
    st.markdown("<h2 style='text-align:center; padding-top:20px;'>🏆 DIMELO <span class='gold-text'>GOLD</span></h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="mentor-card">
        <b>🤝 ¡TÚ DÍMELO, QUE YO HAGO LA MAGIA!</b><br><br>
        ¡Hola! No importa si estás empezando hoy o si ya tienes tu negocio andando, <b>esta app es para ti</b>.<br><br>
        Vas a recibir un documento con <b>imagen profesional</b> y un lenguaje tan claro y técnico que tus clientes te verán como una empresa de alto nivel.<br><br>
        Cumple con los requisitos de la <b>DIAN</b> si decides crecer, o simplemente te da el estatus que mereces.<br><br>
        <span class="gold-text">Tú solo dímelo</span> como parcero, que yo hago la magia.
    </div>
    """, unsafe_allow_html=True)
    
    nombre_input = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n)
    
    if st.button("¡VAMOS CON TODA! ➡️"):
        if nombre_input:
            st.session_state.n = nombre_input
            st.session_state.p = 2
            st.rerun() # ESTO ACTIVA EL CAMBIO DE PÁGINA

# PÁGINA 2
elif st.session_state.p == 2:
    if st.button("← Volver"):
        st.session_state.p = 1
        st.rerun()
    
    st.markdown(f"<h3 style='text-align:center;'>🛡️ RESPALDO: <span class='gold-text'>{st.session_state.n.upper()}</span></h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mentor-card">
        <b>💡 TU ESCUDO COMERCIAL</b><br>
        Vamos a darle <b>autoridad</b> a lo que haces. Tu imagen y tu ruta legal son tu armadura para cobrar lo justo y demostrar respaldo ante la <b>DIAN</b>.
    </div>
    """, unsafe_allow_html=True)
    
    st.session_state.sec = st.selectbox("Sector de negocio:", list(ejemplos.keys()))
    
    # Campo de descripción con ejemplo dinámico
    ta = st.text_input("¿QUÉ HACES EXACTAMENTE?", 
                       value=st.session_state.tip, 
                       placeholder=ejemplos.get(st.session_state.sec))
    
    if ta: st.session_state.tip = ta

    st.write("---")
    st.write("<b>¿CÓMO TE PRESENTAS HOY?</b>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📄 CTA COBRO"):
            st.session_state.l = "Cuenta de Cobro"
    with c2:
        if st.button("🏛️ COTIZACION"):
            st.session_state.l = "
