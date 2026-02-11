import streamlit as st

# --- 1. CONFIGURACIÓN DE ALTO NIVEL ---
st.set_page_config(page_title="DIMELO GOLD | Business Elite", layout="wide")

# Persistencia de Estado (El cerebro de la App)
for key, val in {
    'p': 1, 'n': '', 'l': '', 'sec': 'Otro', 'tip': '', 'g': '', 'logo': False
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --- 2. INTERFAZ GOLD SUPREME (SCROLL TOTAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        overflow-y: auto !important;
        height: auto !important;
        font-family: 'Montserrat', sans-serif;
        background-color: #fcfcfc;
    }

    .mentor-box {
        border-left: 10px solid #D4AF37;
        background: white;
        padding: 40px;
        border-radius: 0 25px 25px 0;
        box-shadow: 0 15px 45px rgba(0,0,0,0.05);
        margin: 30px 0;
    }

    .gold-title {
        color: #1a1a1a;
        font-weight: 700;
        letter-spacing: -1px;
        line-height: 1.1;
    }

    .highlight { color: #D4AF37; font-weight: 700; }

    /* Botón Estilo Shark Tank */
    div.stButton > button {
        background: linear-gradient(135deg, #1a1a1a 0%, #333 100%) !important;
        color: #D4AF37 !important;
        border-radius: 12px;
        height: 4.5em;
        font-weight: 700;
        width: 100%;
        border: none;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.4s;
    }
    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(212, 175, 55, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PÁGINA 1: EL UMBRAL DE LA AUTORIDAD ---
if st.session_state.p == 1:
    # Encabezado de Marca
    st.markdown('<h1 class="gold-title">🏆 DIMELO <span class="highlight">GOLD</span></h1>', unsafe_allow_html=True)
    st.write("---")

    # Bloque del Mentor (Pedagogía Shark)
    st.markdown("""
    <div class="mentor-box">
        <h3>🎙️ HABLA EL MENTOR:</h3>
        <p>Bienvenido al sistema que dejará atrás la informalidad. Como PYME, tu mayor debilidad no es el tamaño, es la 
        <span class="highlight">percepción de riesgo</span> del cliente. Si tu cotización parece amateur, tu precio será castigado.</p>
        <p><b>REGLA DE ORO:</b> La autoridad comercial comienza con una firma responsable. En este paso inicial, establecemos 
        quién lidera la visión detrás de esta propuesta.</p>
    </div>
    """, unsafe_allow_html=True)

    # Input de Autoridad
    with st.container():
        st.subheader("IDENTIFICACIÓN DEL LÍDER")
        nombre = st.text_input(
            "¿Cuál es el nombre del profesional responsable de este negocio?", 
            value=st.session_state.n,
            placeholder="Ej: Germán Villalobos"
        )
        
        st.write("")
        if st.button("VALIDAR IDENTIDAD Y AVANZAR AL BLINDAJE ➡️"):
            if nombre:
                st.session_state.n = nombre
                st.session_state.p = 2
                st.rerun()
            else:
                st.error("🚨 Un líder no avanza en el anonimato. Por favor, ingresa tu nombre.")

# --- 4. SIGUIENTES PÁGINAS (ESTRUCTURA DE ESPERA) ---
elif st.session_state.p == 2:
    st.info(f"🛡️ {st.session_state.n}, estamos listos para la arquitectura legal. Próximo paso: Sello de Marca y DIAN.")
    if st.button("ATRÁS"): st.session_state.p = 1; st.rerun()
