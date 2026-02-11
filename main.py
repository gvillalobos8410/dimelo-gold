import streamlit as st

# --- 1. CONFIGURACIÓN DE RECURSOS ---
IMG_AGRO = "https://images.unsplash.com/photo-1500651230702-0e2d8a49d4ad?w=600"
IMG_TECH = "https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=600"
IMG_GAST = "https://images.unsplash.com/photo-1555244162-803834f70033?w=600"
IMG_OBRA = "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=600"
IMG_OTRO = "https://images.unsplash.com/photo-1497366216548-37526070297c?w=600"

# --- 2. CONFIGURACIÓN DE STREAMLIT ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

# Persistencia de Estado con Blindaje
for k, v in {'p':1, 'n':'', 'l':'', 'sec':'Otros', 'tip':''}.items():
    if k not in st.session_state: st.session_state[k] = v

# Diccionario de Sectores (Usado para ambientación)
sectores = {
    'Agro': {'ej': 'Venta de cafe pergamino...', 'img': IMG_AGRO},
    'Tecnico': {'ej': 'Mantenimiento de motores...', 'img': IMG_TECH},
    'Gastro': {'ej': 'Servicio de banquetes...', 'img': IMG_GAST},
    'Obra': {'ej': 'Remodelacion y pintura...', 'img': IMG_OBRA},
    'Otros': {'ej': 'Describe tu servicio...', 'img': IMG_OTRO}
}

# --- 3. AMBIENTE VISUAL (SCROLL FORZADO Y FONDO DINÁMICO) ---
# Prevención de KeyError: Usamos .get() con un valor por defecto
sec_info = sectores.get(st.session_state.sec, sectores['Otros'])
img_actual = sec_info['img'] if st.session_state.p == 2 else ""
bg_style = f"linear-gradient(rgba(255,255,255,0.9),rgba(255,255,255,0.9)),url('{img_actual}')" if img_actual else "#ffffff"

st.markdown(f'''
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    
    /* SCROLL TOTAL PARA MÓVIL */
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
    
    .card {{ 
        border-left: 10px solid #D4AF37; background: rgba(255,255,255,0.95); 
        padding: 25px; border-radius: 0 20px 20px 0; margin: 20px 0; 
        line-height: 1.6; 
    }}
    
    .gold {{ color: #D4AF37; font-weight: 700; }}
    
    div.stButton > button {{ 
        background: #1a1a1a !important; color: #D4AF37 !important; 
        border-radius: 12px; height: 3.5em; width: 100%; 
        font-weight: bold; border: none; text-transform: uppercase;
    }}
    
    .footer-spacer {{ height: 100px; }}
</style>
''', unsafe_allow_html=True)

# --- 4. LÓGICA DE PÁGINAS ---

# PÁGINA 1: LA PROMESA
if st.session_state.p == 1:
    st.markdown("## 🏆 DIMELO <span class='gold'>GOLD</span>", unsafe_allow_html=True)
    st.markdown(f'''
    <div class="card">
        <b>🤝 ¡TÚ DÍMELO, QUE YO HAGO LA MAGIA!</b><br><br>
        ¡Hola! No importa si estás empezando hoy o si ya tienes tu negocio andando, <b>esta app es para ti</b>.<br><br>
        Vas a recibir un documento con <b>imagen profesional</b> y un lenguaje tan claro y técnico que tus clientes te verán como una empresa de alto nivel.<br><br>
        Para el emprendedor que quiere dar el siguiente paso, este documento cumple con los requisitos de la <b>DIAN</b>, dejándote la puerta abierta para facturación electrónica si así lo decides. Pero si solo buscas presentarte mejor, ¡estás en el lugar correcto!<br><br>
        <span class="gold">Tú solo dímelo</span> como parcero, que <span class="gold">yo hago la magia</span> de entregarte una propuesta impecable.
    </div>
    ''', unsafe_allow_html=True)
    
    n = st.text_input("¿CÓMO TE LLAMAS?", value=st.session_state.n)
    if st.button("¡ESTOY LISTO! ➡️"):
        if n:
            st.session_state.n = n
            st.session_state.p = 2
            st.rerun()
    st.markdown('<div class="footer-spacer"></div>', unsafe_allow_html=True)

# PÁGINA 2: ARQUITECTURA
elif st.session_state.p == 2:
    if st.button("← VOLVER"):
        st.session_state.p = 1
        st.rerun()
        
    st.markdown(f"### 🛡️ RESPALDO: <span class='gold'>{st.session_state.n.upper()}</span>", unsafe_allow_html=True)
    st.markdown('''
    <div class="card">
        <b>💡 TU ESCUDO COMERCIAL</b><br>
        Aquí no hay enredos. Vamos a ponerle <b>autoridad</b> a lo que haces. Elegir tu imagen y tu ruta legal es tu armadura para que el cliente confíe y tú cobres lo justo.
    </div>
    ''', unsafe_allow_html=True)
    
    st.session_state.sec = st.selectbox("Sector de negocio:", list(sectores.keys()))
    
    # Ejemplo dinámico seguro
    ej_placeholder = sectores.get(st.session_state.sec, sectores['Otros'])['ej']
    
    ta = st.text_input("¿QUÉ HACES EXACTAMENTE?", value=st.session_state.tip, placeholder=ej_placeholder)
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
    st.markdown('<div class="footer-spacer"></div>', unsafe_allow_html=True)

# PÁGINA 3: MOTOR (Mantenimiento de flujo)
elif st.session_state.p == 3:
    st.markdown("## 🎙️ MOTOR DE VOZ", unsafe_allow_html=True)
    st.markdown('<div class="card">¡Aquí comienza la magia! Suéltalo todo que yo me encargo.</div>', unsafe_allow_html=True)
    if st.button("⬅️ VOLVER"):
        st.session_state.p = 2
        st.rerun()
        
