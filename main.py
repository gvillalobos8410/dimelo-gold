import streamlit as st

# --- 1. CONFIGURACIÓN DE INGENIERÍA ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia de Estado Blindada
for k, v in {'p':1, 'n':'', 'l':'', 'sec':'Otros', 'tip':''}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 2. MAPA DE SECTORES (AMBIENTACIÓN REALISTA) ---
# Usamos comillas sencillas dentro de los diccionarios para evitar conflictos
sectores = {
    'Agro': {'ej': 'Ej: Venta de 10 cargas de cafe pergamino...', 'img': 'https://images.unsplash.com/photo-1500651230702-0e2d8a49d4ad?w=800'},
    'Tecnico': {'ej': 'Ej: Mantenimiento de motores diesel...', 'img': 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=800'},
    'Gastronomia': {'ej': 'Ej: Servicio de catering para eventos...', 'img': 'https://images.unsplash.com/photo-1555244162-803834f70033?w=800'},
    'Construccion': {'ej': 'Ej: Remodelacion y pintura...', 'img': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=800'},
    'Otros': {'ej': 'Ej: Describe aqui tu servicio...', 'img': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800'}
}

# --- 3. AMBIENTE DE INTERFAZ (SCROLL FORZADO Y CSS MODULAR) ---
img_fondo = sectores[st.session_state.sec]['img'] if st.session_state.p == 2 else ""
bg_style = f"linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9)), url('{img_fondo}')" if img_fondo else "#ffffff"

st.markdown(f'''
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {{
        overflow-y: auto !important;
        height: auto !important;
        min-height: 100vh !important;
        font-family: 'Montserrat', sans-serif;
    }}

    [data-testid="stAppViewContainer"] {{ 
        max-width: 450px; margin: 0 auto; background: {bg_style}; 
        background-size: cover; background-position: center;
        border-radius: 20px; box-shadow: 0 0 40px rgba(0,0,0,0.1); 
    }}
    
    .mentor-card {{ 
        border-left: 10px solid #D4AF37; background: rgba(255,255,255,0.95); 
        padding: 25px; border-radius: 0 20px 20px 0; margin: 20px 0; 
        line-height: 1.6; 
    }}
    
    .gold-text {{ color: #D4AF37; font-weight: 700; }}
    
    div.stButton > button {{ 
        background: #1a1a1a !important; color: #D4AF37 !important; 
        border-radius: 12px; height: 3.8em; width: 100%; 
        font-weight: bold; border: none; text-transform: uppercase;
    }}
    
    .footer-spacer {{ height: 100px; }}
</style>
''', unsafe_allow_html=True)

# --- 4. PÁGINA 1: LA PROMESA (LEY DIMELO) ---
if st.session_state.p == 1:
    st.markdown("<h2 style='text-align:center; padding-top:20px;'>🏆 DIMELO <span class='gold-text'>GOLD</span></h2>", unsafe_allow_html=True)
    
    st.markdown('''
    <div class="mentor-card">
        <b>🤝 ¡TÚ DÍMELO, QUE YO HAGO LA MAGIA!</b><br><br>
        ¡Hola! No importa si estás empezando hoy o si ya tienes tu negocio andando, <b>esta app es para ti</b>.<br><br>
        Vas a recibir un documento con <b>imagen profesional</b> y un lenguaje tan claro y técnico que tus clientes te verán como una empresa de alto nivel.<br><br>
        Para el emprendedor que quiere dar el siguiente paso, este documento cumple con los requisitos de la <b>DIAN</b>, dejándote la puerta abierta para facturación electrónica si así lo decides. Pero si solo buscas presentarte mejor, ¡estás en el lugar correcto!<br><br>
        <span class="gold-text">Tú solo dímelo</span> como parcero, que <span class="gold-text">yo hago la magia</span> de entregarte una propuesta impecable.
    </div>
    ''', unsafe_allow_html=True)
    
    nombre = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n)
    
    if st.button("¡ESTOY LISTO, VAMOS CON TODA! ➡️"):
        if nombre:
            st.session_state.n = nombre
            st.session_state.p = 2
            st.experimental_rerun() if hasattr(st, 'experimental_rerun') else st.rerun()
    st.markdown('<div class="footer-spacer"></div>', unsafe_allow_html=True)

# --- 5. PÁGINA 2: ARQUITECTURA (LEY DIMELO) ---
elif st.session_state.p == 2:
    if st.button("← Volver"):
        st.session_state.p = 1
        st.experimental_rerun() if hasattr(st, 'experimental_rerun') else st.rerun()
    
    st.markdown(f"<h3 style='text-align:center;'>🛡️ RESPALDO: <span class='gold-text'>{st.session_state.n.upper()}</span></h3>", unsafe_allow_html=True)
    
    st.markdown('''
    <div class="mentor-card">
        <b>💡 TU ESCUDO COMERCIAL</b><br>
        Aquí no hay enredos. Vamos a ponerle <b>autoridad</b> a lo que haces. Elegir tu imagen y tu ruta legal no es una obligación pesada, es tu armadura para que el cliente confíe y tú cobres lo justo.
    </div>
    ''', unsafe_allow_html=True)
    
    st.session_state.sec = st.selectbox("Sector de negocio:", list(sectores.keys()))
    
    ta = st.text_input("¿QUÉ HACES EXACTAMENTE?", 
                       value=st.session_state.tip, 
                       placeholder=sectores[st.session_state.sec]['ej'])
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
            st.experimental_rerun() if hasattr(st, 'experimental_rerun') else st.rerun()
    st.markdown('<div class="footer-spacer"></div>', unsafe_allow_html=True)
