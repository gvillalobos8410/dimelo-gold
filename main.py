import streamlit as st

# --- 1. ESTADO Y CONFIGURACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="wide")

for k, v in {
    'p': 1, 'n': '', 'l': '', 'sec': 'Otro', 'tip': '', 'g': '', 'logo': False
}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# --- 2. ESTÉTICA SUNLIGHT PROFESIONAL ---
# Concatenación segura para evitar errores de comillas triples
CSS = "<style>"
CSS += "@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');"
CSS += "html, body, [class*='st-'] { font-family: 'Montserrat', sans-serif; }"
CSS += ".stApp { background: linear-gradient(180deg, #FFD700 0%, #FFB900 100%); }"
CSS += ".main-card { background: white; padding: 30px; border-radius: 20px; "
CSS += "box-shadow: 0 10px 30px rgba(0,0,0,0.1); margin-bottom: 20px; }"
CSS += ".ped-box { border-left: 8px solid #D4AF37; background: #f9f9f9; "
CSS += "padding: 20px; border-radius: 12px; margin: 15px 0; color: #333; line-height: 1.6; }"
CSS += "div.stButton > button { background: #1a1a1a !important; "
CSS += "color: #D4AF37 !important; font-weight: 700; width: 100%; "
CSS += "height: 3.5em; border-radius: 12px; border: none; }"
CSS += "</style>"
st.markdown(CSS, unsafe_allow_html=True)

# --- 3. REGISTRO CON MÁXIMA PEDAGOGÍA (P1 Y P2) ---

if st.session_state.p == 1:
    st.markdown('<div class="main-card"><h1>🏆 DIMELO GOLD</h1><p>Autoridad comercial para líderes del agro y la industria.</p></div>', True)
    st.markdown('<div class="ped-box"><h3>🛡️ PASO 1: TU IDENTIDAD</h3>Para que el sistema genere autoridad, primero debemos saber quién lidera la propuesta.</div>', True)
    nom = st.text_input("¿CUÁL ES TU NOMBRE?", value=st.session_state.n)
    if st.button("INICIAR REGISTRO ÉPICO ➡️"):
        if nom:
            st.session_state.n = nom
            st.session_state.p = 2
            st.rerun()

elif st.session_state.p == 2:
    st.markdown(f'<div class="main-card"><h1>💎 BIENVENIDO, {st.session_state.n.upper()}</h1></div>', True)
    c1, c2 = st.columns(2, gap="large")
    
    with c1:
        st.markdown('<div class="ped-box"><b>🖼️ PEDAGOGÍA DE IMAGEN</b><br>En el mundo profesional, la imagen es el respaldo de tu promesa. Un logo es el sello de tu calidad.</div>', True)
        l_up = st.file_uploader("Vincular Marca Personal", label_visibility="collapsed")
        if l_up:
            st.success("✨ ¡Marca respaldada profesionalmente!")
            st.session_state.logo = True
        else:
            st.warning("🚨 RECOMENDACIÓN: No avanzar sin logo. La autoridad empieza por los ojos.")
        
        st.write("---")
        sectores = ['🌾 Agropecuario', '🛠️ Técnico', '🍰 Gastronomía', '🏗️ Obra', '⚖️ Consultoría', '✨ Otro']
        st.session_state.sec = st.selectbox("¿EN QUÉ SECTOR TRABAJAS?", sectores)
        st.info("💡 **GUÍA:** Describe tu actividad diaria de forma simple.")
        act = st.text_input("¿QUÉ HACES EXACTAMENTE?", value=st.session_state.tip)
        if act: st.session_state.tip = act

    with c2:
        st.markdown('<div class="ped-box"><b>🏛️ RESPALDO LEGAL (AVISO DIAN)</b><br>La formalidad es la base de los grandes negocios. Define cómo vas a respaldar tu cobro legalmente.</div>', True)
        st.write("📌 **CUENTA DE COBRO:** Servicios directos. Agilidad sin gestión de IVA.")
        if st.button("📄 SELECCIONAR CUENTA DE COBRO"):
            st.session_state.l = "Cuenta de Cobro"
        st.write(" ")
        st.write("📌 **COTIZACIÓN EMPRESARIAL:** Cumple con estándares DIAN. Transmite seriedad.")
        if st.button("🏛️ SELECCIONAR COTIZACIÓN"):
            st.session_state.l = "Formal"
        if st.session_state.l:
            st.info(f"Ruta Legal Activa: **{st.session_state.l.upper()}**")

    if st.session_state.l and st.session_state.tip:
        if st.button("FINALIZAR REGISTRO Y ABRIR MOTOR 🚀"):
            st.session_state.p = 3
            st.rerun()

# --- 4. MOTOR DE PRECISIÓN CON PEDAGOGÍA DINÁMICA (P3) ---

elif st.session_state.p == 3:
    st.markdown('<div class="main-card"><h1>🎙️ MOTOR DE PRECISIÓN</h1></div>', True)
    
    # Ejemplo dinámico según sector
    ej = "Venta de café especial" if "Agro" in st.session_state.sec else "Servicio técnico"
    
    # Construcción de pedagogía sin comillas triples para evitar errores
    ped_html = "✨ **LA IA HACE LA MAGIA:**<br>No busques palabras técnicas. "
    ped_html += f"Dímelo sencillo, como un café. Ejemplo: '{ej}'. "
    ped_html += "Yo lo elevaré a nivel Gold."
    
    st.markdown(f'<div class="ped-box">{ped_html}</div>', True)
    
    if st.button("🔴 PULSA PARA GRABAR TU IDEA"):
        st.info("🎤 Escuchando... Habla con total naturalidad.")
    
    with st.expander("⌨️ OPCIÓN DE EMERGENCIA: ESCRIBIR"):
        t_in = st.text_area("Describe tu propuesta aquí:", height=100)
    
    if st.button("✨ TRANSFORMAR MI IDEA A NIVEL GOLD"):
        res = t_in if t_in else "Idea capturada por voz"
        st.session_state.g = f"**{st.session_state.tip.upper()} - PROPUESTA GOLD:** {res.upper()}"
        st.session_state.p = 4
        st.rerun()

elif st.session_state.p == 4:
    st.markdown('<div class="main-card"><h1>💎 PROPUESTA GENERADA</h1></div>', True)
    st.markdown('<div class="ped-box">Aquí tienes tu idea elevada a autoridad comercial.</div>', True)
    st.write(st.session_state.g)
    if st.button("🔄 NUEVO DICTADO"):
        st.session_state.p = 3
        st.rerun()
