import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia de Estado
if 'p' not in st.session_state: st.session_state.p = 1
if 'n' not in st.session_state: st.session_state.n = ''
if 'l' not in st.session_state: st.session_state.l = ''
if 'sec' not in st.session_state: st.session_state.sec = '✨ Otro'
if 'tip' not in st.session_state: st.session_state.tip = ''

# --- 2. BANCO DE DATOS (EJEMPLOS DINÁMICOS) ---
ejemplos = {
    '🌾 Agro': 'Ej: Venta de 10 cargas de cafe pergamino seco...',
    '🛠️ Tecnico': 'Ej: Mantenimiento preventivo de motor diesel...',
    '🏗️ Obra': 'Ej: Remodelacion de bano y cambio de tuberia...',
    '🍰 Gastro': 'Ej: Servicio de catering para 50 personas...',
    '✨ Otro': 'Ej: Describe tu producto o servicio...'
}

# --- 3. ESTILO CSS (SCROLL FORZADO Y ESTÉTICA GOLD) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    
    /* LIBERACIÓN TOTAL DEL SCROLL */
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {
        overflow-y: auto !important;
        height: auto !important;
        min-height: 100vh !important;
        font-family: 'Montserrat', sans-serif;
        background-color: #f4f4f4 !important;
    }

    [data-testid="stAppViewContainer"] { 
        max-width: 450px; 
        margin: 0 auto; 
        background: #ffffff;
        border-radius: 20px; 
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        padding-bottom: 50px; /* Espacio extra al final */
    }
    
    .mentor-card { 
        border-left: 10px solid #D4AF37; 
        background: #ffffff; 
        padding: 25px; 
        margin: 20px 0; 
        line-height: 1.6;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.02);
    }
    
    .gold-text { color: #D4AF37; font-weight: 700; }
    
    div.stButton > button { 
        background: #1a1a1a !important; 
        color: #D4AF37 !important; 
        border-radius: 12px; 
        height: 3.5em; width: 100%; 
        font-weight: bold; border: none;
        text-transform: uppercase;
    }
    
    .spacer { height: 80px; }
</style>
""", unsafe_allow_html=True)

# --- 4. PÁGINA 1: LA PROMESA ---
if st.session_state.p == 1:
    st.markdown("<h2 style='text-align:center; padding-top:20px;'>🏆 DIMELO <span class='gold-text'>GOLD</span></h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="mentor-card">
        <b>🤝 ¡TÚ DÍMELO, QUE YO HAGO LA MAGIA!</b><br><br>
        ¡Hola! No importa si estás empezando hoy o si ya tienes tu negocio andando, <b>esta app es para ti</b>.<br><br>
        Vas a recibir un documento con <b>imagen profesional</b> y un lenguaje tan claro y técnico que tus clientes te verán como una empresa de alto nivel.<br><br>
        Para el emprendedor que quiere dar el siguiente paso, este documento cumple con los requisitos de la <b>DIAN</b>, dejándote la puerta abierta para facturación electrónica si así lo decides. Pero si solo buscas presentarte mejor, ¡estás en el lugar correcto!<br><br>
        <span class="gold-text">Tú solo dímelo</span> como parcero, que yo hago la magia.
    </div>
    """, unsafe_allow_html=True)
    
    n = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n)
    if st.button("¡VAMOS CON TODA! ➡️"):
        if n:
            st.session_state.n, st.session_state.p = n, 2
            st.rerun()
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    
