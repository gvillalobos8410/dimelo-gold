
import streamlit as st

# --- 1. CONFIGURACIÓN DE SEGURIDAD ---
st.set_page_config(page_title="DIMELO GOLD", layout="wide", initial_sidebar_state="collapsed")

# Inicialización de Estado Blindada
for key, val in {
    'p': 1, 'n': '', 'l': '', 'sec': 'Otro', 'tip': '', 'g': '', 'logo': False
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --- 2. ESTÉTICA GOLD SUPREME (Lógica de Diseño Profesional) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Montserrat', sans-serif; background-color: #f8f9fa; }
    .main-card { background: white; padding: 40px; border-radius: 30px; border: 1px solid #eee; box-shadow: 0 10px 40px rgba(0,0,0,0.05); }
    .gold-box { border-left: 8px solid #D4AF37; background: #fdfdfd; padding: 25px; border-radius: 15px; margin: 20px 0; }
    div.stButton > button { background: #1a1a1a !important; color: #D4AF37 !important; border-radius: 15px; height: 4em; font-weight: 700; width: 100%; border: none; transition: 0.3s; }
    div.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PÁGINAS DE REGISTRO (Leyes Inamovibles de Germán) ---

if st.session_state.p == 1:
    st.markdown('<div class="main-card"><h1>🏆 DIMELO GOLD</h1><p>Tu talento convertido en autoridad comercial.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="gold-box"><h3>REGISTRO DE IDENTIDAD</h3>Paso 1: Define quién eres ante el mercado.</div>', unsafe_allow_html=True)
    nombre = st.text_input("¿CUAL ES TU NOMBRE?", value=st.session_state.n)
    if st.button("INICIAR REGISTRO PROFESIONAL ➡️"):
        if nombre:
            st.session_state.n = nombre
            st.session_state.p = 2
            st.rerun()

elif st.session_state.p == 2:
    st.markdown(f'<div class="main-card"><h1>🛡️ BIENVENIDO, {st.session_state.n.upper()}</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2, gap="large")
    
    with c1:
        st.markdown('<div class="gold-box"><b>🖼️ IMAGEN DE MARCA</b><br>La marca es la cara de tu calidad. Sin logo no hay autoridad.</div>', unsafe_allow_html=True)
        logo = st.file_uploader("Subir Logo", label_visibility="collapsed")
        if logo:
            st.success("✨ Imagen vinculada exitosamente.")
            st.session_state.logo = True
        else:
            st.warning("🚨 Sugerencia Shark: El logo es vital para el cierre comercial.")
        
        st.write("---")
        sectores = ['🌾 Agropecuario', '🛠️ Técnico', '🍰 Gastronomía', '🏗️ Construcción', '⚖️ Consultoría', '✨ Otro']
        st.session_state.sec = st.selectbox("¿EN QUÉ SECTOR TE DESTACAS?", sectores)
        st.info("💡 **PEDAGOGÍA:** Describe tu actividad en lenguaje simple.")
        tipo = st.text_input("¿QUÉ HACES EXACTAMENTE?", value=st.session_state.tip)
        if tipo: st.session_state.tip = tipo

    with c2:
        st.markdown('<div class="gold-box"><b>🏛️ RESPALDO LEGAL (DIAN)</b><br>Define tu ruta de cobro oficial.</div>', unsafe_allow_html=True)
        st.write("📌 **CUENTA DE COBRO:** Agilidad para servicios directos.")
        if st.button("📄 RUTA: CUENTA DE COBRO"):
            st.session_state.l = "Sencilla"
        st.write(" ")
        st.write("📌 **COTIZACIÓN EMPRESARIAL:** Estándar legal para grandes contratos.")
        if st.button("🏛️ RUTA: COTIZACIÓN EMPRESARIAL"):
            st.session_state.l = "Formal"
        
        if st.session_state.l:
            st.info(f"Ruta activa: **{st.session_state.l.upper()}**")

    if st.session_state.l and st.session_state.tip:
        if st.button("FINALIZAR Y ABRIR MOTOR DE PRECISIÓN 🚀"):
            st.session_state.p = 3
            st.rerun()

# --- 4. MOTOR DE PRECISIÓN (El Alma de la App) ---

elif st.session_state.p == 3:
    st.markdown('<div class="main-card"><h1>🎙️ MOTOR DE PRECISIÓN</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="gold-box">✨ **LA IA HACE LA MAGIA:** Dímelo sencillo, como si estuviéramos tomando un café. No te preocupes por la técnica; yo transformo tu voz en una oferta Gold.</div>', unsafe_allow_html=True)
    
    st.markdown("### 🗣️ PASO 1: TU IDEA EN VOZ")
    if st.button("🔴 INICIAR GRABACIÓN"):
        st.info("🎤 Escuchando... Cuéntame tu propuesta con naturalidad.")
    
    with st.expander("⌨️ OPCIÓN DE EMERGENCIA: ESCRITURA"):
        texto = st.text_area("Si no puedes hablar, escribe tu idea aquí:", height=100)
    
    if st.button("✨ TRANSFORMAR MI IDEA A NIVEL GOLD"):
        idea = texto if texto else "Idea procesada por voz"
        st.session_state.g = f"**{st.session_state.tip.upper()} - NIVEL PROFESIONAL:** {idea.upper()}"
        st.session_state.p = 4
        st.rerun()

elif st.session_state.p == 4:
    st.markdown('<div class="main-card"><h1>💎 PROPUESTA FINAL GENERADA</h1></div>', unsafe_allow_html=True)
    st.write(st.session_state.g)
    if st.button("🔄 REALIZAR NUEVO DICTADO"):
        st.session_state.p = 3
        st.rerun()
