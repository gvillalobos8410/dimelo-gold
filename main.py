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
        color: #D4AF37 !important; border-radius: 12px; height: 4.2em;
        font-weight: 700; width: 100%; border: none; text-transform: uppercase;
        letter-spacing: 1px;
    }
    .spacer { height: 100px; }
</style>
"""
st.markdown(estilo_celular, unsafe_allow_html=True)

# --- 3. PÁGINA 1: EL SOCIO DE TODOS LOS EMPRENDEDORES ---
if st.session_state.p == 1:
    st.markdown('<h2 style="text-align:center; padding-top:20px;">🏆 DIMELO <span class="highlight">GOLD</span></h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mentor-card">
        <h3 style="margin-top:0;">🤝 ¡TÚ DÍMELO, QUE YO HAGO LA MAGIA!</h3>
        ¡Hola! No importa si estás empezando hoy o si ya tienes tu negocio andando, <b>esta app es para ti</b>.<br><br>
        <span class="highlight">¿Qué vas a lograr conmigo?</span><br>
        Vas a recibir un documento con <b>imagen profesional</b> y un lenguaje tan claro y técnico que tus clientes te verán como una empresa de alto nivel. <br><br>
        Para el emprendedor que quiere dar el siguiente paso, este documento cumple con los requisitos de la <b>DIAN</b>, dejándote la puerta abierta para facturación electrónica si así lo decides. Pero si solo buscas presentarte mejor, ¡estás en el lugar correcto!<br><br>
        <span class="highlight">Tú solo dímelo</span> como parcero, que <span class="highlight">yo hago la magia</span> de entregarte una propuesta impecable.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Empecemos esta alianza...")
    n = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n, placeholder="Tu nombre y apellido")
    
    if st.button("¡ESTOY LISTO, VAMOS CON TODA! ➡️"):
        if n:
            st.session_state.n = n
            st.session_state.p = 2
            st.rerun()
        else:
            st.warning("Oye, para que el documento salga a tu nombre, necesito saber quién eres.")
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- 4. PÁGINA 2: ARQUITECTURA PARA CUALQUIER NIVEL ---
elif st.session_state.p == 2:
    if st.button("← Volver"):
        st.session_state.p = 1
        st.rerun()

    st.markdown(f'<h3 style="text-align:center;">🛡️ RESPALDO: <span class="highlight">{st.session_state.n.upper()}</span></h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mentor-card">
        <h3 style="margin-top:0;">💡 TU ESCUDO COMERCIAL</h3>
        Aquí no hay enredos. Vamos a ponerle <b>autoridad</b> a lo que haces. Elegir tu imagen y tu ruta legal no es una obligación pesada, es tu armadura para que el cliente confíe y tú cobres lo justo.<br><br>
        Yo te guío para que elijas la opción que más te convenga hoy, sin complicaciones.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🖼️ TU IDENTIDAD")
    st.write("<small>Sube tu logo para que tu propuesta tenga sello propio.</small>", unsafe_allow_html=True)
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
    
    ta = st.text_input("¿QUÉ HACES EXACTAMENTE?", value=st.session_state.tip, placeholder="Ej: Venta de productos agro")
    if ta: st.session_state.tip = ta

    st.write("---")
    st.subheader("🏛️ ¿CÓMO QUIERES PRESENTARTE?")
    st.write("<small>Escoge la opción más cómoda para tu negocio hoy:</small>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📄 CTA. COBRO"): 
            st.session_state.l = "Cuenta de Cobro"
            st.toast("Opción sencilla y rápida.")
    with c2:
        if st.button("🏛️ COTIZACIÓN"): 
            st.session_state.l = "Cotización"
            st.toast("Opción formal de alto nivel.")
            
    if st.session_state.l:
        st.info(f"Ruta elegida: **{st.session_state.l.upper()}**")

    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 TODO LISTO, ¡A HACER MAGIA!"):
            st.session_state.p = 3
            st.rerun()
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
