import streamlit as st

# --- 1. CONFIGURACIÓN DE ALTO NIVEL ---
st.set_page_config(page_title="DIMELO GOLD | De Emprendedor a Pro", layout="wide")

# Cerebro de la App (Persistencia)
for key, val in {
    'p': 1, 'n': '', 'l': '', 'sec': 'Otro', 'tip': '', 'g': '', 'logo': False
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --- 2. INTERFAZ GOLD SUPREME (AMIGABLE Y FLUIDA) ---
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
        padding: 35px;
        border-radius: 0 20px 20px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        margin: 25px 0;
        line-height: 1.6;
    }

    .gold-title {
        color: #1a1a1a;
        font-weight: 700;
        letter-spacing: -1px;
    }

    .highlight { color: #D4AF37; font-weight: 700; }

    /* Botón con fuerza de cierre */
    div.stButton > button {
        background: linear-gradient(135deg, #1a1a1a 0%, #333 100%) !important;
        color: #D4AF37 !important;
        border-radius: 15px;
        height: 4em;
        font-weight: 700;
        width: 100%;
        border: none;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        transform: scale(1.01);
        box-shadow: 0 8px 20px rgba(212, 175, 55, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PÁGINA 1: EL INICIO DEL CAMINO ---
if st.session_state.p == 1:
    st.markdown('<h1 class="gold-title">🏆 DIMELO <span class="highlight">GOLD</span></h1>', unsafe_allow_html=True)
    st.write("---")

    # Habla el amigo experto (Pedagogía Amigable)
    st.markdown("""
    <div class="mentor-box">
        <h3>👋 ¡Epa, Emprendedor! Qué bueno tenerte acá.</h3>
        <p>Sabemos que le metes el alma a lo que haces, pero a veces el cliente no ve todo ese esfuerzo porque la propuesta se ve "floja" o muy informal. 
        <b>¡Eso se acaba hoy!</b></p>
        <p>Yo te voy a acompañar como tu profesor y socio para que tu talento se vea <span class="highlight">impecable</span>. 
        Vamos a traducir esa idea que tienes en la cabeza a un documento que inspire respeto y cierre el negocio de una.</p>
        <p><i>Primero lo primero: ¿Con quién tengo el gusto? Vamos a ponerle nombre al responsable de este gran proyecto.</i></p>
    </div>
    """, unsafe_allow_html=True)

    # Registro de Identidad
    st.subheader("Tu nombre es tu firma")
    nombre = st.text_input(
        "¿Cómo te llamas?", 
        value=st.session_state.n,
        placeholder="Escribe tu nombre y apellido"
    )
    
    st.write("")
    if st.button("¡LISTO, VAMOS PA' ESA! ➡️"):
        if nombre:
            st.session_state.n = nombre
            st.session_state.p = 2
            st.rerun()
        else:
            st.warning("Oye, no seas tímido. Necesito tu nombre para que la propuesta salga a tu nombre.")

# --- 4. PREPARACIÓN PÁGINA 2 ---
elif st.session_state.p == 2:
    st.markdown(f'<h1 class="gold-title">🛡️ ¡TODO LISTO, <span class="highlight">{st.session_state.n.upper()}</span>!</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div class="mentor-box">
        <p>Ya dimos el primer paso. Ahora vamos a vestir el negocio de gala. 
        Necesito que definamos tu <b>imagen</b> y tu <b>respaldo legal</b> ante la DIAN. 
        No te asustes, que yo te explico por qué esto te hace ver como un profesional de peso.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("⬅️ VOLVER"):
        st.session_state.p = 1
        st.rerun()
