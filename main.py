import streamlit as st

# --- 1. DATOS Y TEXTOS ---
INFO_P1 = "Hola! No importa si estas empezando o ya tienes camino recorrido, esta app es para ti. Recibiras un documento con imagen pro y lenguaje tecnico. Si decides crecer, esto cumple con la DIAN. Tu solo dimelo, que yo hago la magia!"
INFO_P2 = "Tu imagen y tu ruta legal son tu armadura para cobrar lo justo y que el cliente confie en ti. Yo te guio!"

sectores_map = {
    'Agro': {'ej': 'Ej: Venta de cafe pergamino...', 'img': 'https://images.unsplash.com/photo-1500651230702-0e2d8a49d4ad?w=800'},
    'Tecnico': {'ej': 'Ej: Mantenimiento de motores...', 'img': 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=800'},
    'Gastronomia': {'ej': 'Ej: Banquetes para eventos...', 'img': 'https://images.unsplash.com/photo-1555244162-803834f70033?w=800'},
    'Construccion': {'ej': 'Ej: Remodelacion y pintura...', 'img': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=800'},
    'Otros': {'ej': 'Ej: Describe tu servicio...', 'img': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800'}
}

# --- 2. CONFIGURACION ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

if 'p' not in st.session_state: st.session_state.p = 1
if 'n' not in st.session_state: st.session_state.n = ''
if 'l' not in st.session_state: st.session_state.l = ''
if 'sec' not in st.session_state: st.session_state.sec = 'Otros'
if 'tip' not in st.session_state: st.session_state.tip = ''

# --- 3. ESTILO CSS DINAMICO ---
img_url = sectores_map[st.session_state.sec]['img'] if st.session_state.p == 2 else ""
bg = f"background-image: linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9)), url('{img_url}');" if st.session_state.p == 2 else "background-color: #ffffff;"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    [data-testid="stAppViewContainer"] {{ max-width: 450px; margin: 0 auto; {bg} background-size: cover; border-radius: 20px; box-shadow: 0 0 40px rgba(0,0,0,0.1); }}
    .card {{ border-left: 8px solid #D4AF37; background: rgba(255,255,255,0.95); padding: 20px; border-radius: 0 15px 15px 0; margin: 15px 0; font-family: 'Montserrat'; }}
    div.stButton > button {{ background: #1a1a1a !important; color: #D4AF37 !important; border-radius: 10px; height: 3.5em; width: 100%; font-weight: bold; border: none; }}
</style>
""", unsafe_allow_html=True)

# --- 4. LOGICA DE NAVEGACION ---
if st.session_state.p == 1:
    st.markdown("<h2 style='text-align:center;'>🏆 DIMELO GOLD</h2>", unsafe_allow_html=True)
    st.markdown(f'<div class="card"><b>TU DIMELO, QUE YO HAGO LA MAGIA!</b><br><br>{INFO_P1}</div>', unsafe_allow_html=True)
    nombre = st.text_input("COMO TE LLAMAS?", value=st.session_state.n)
    if st.button("VAMOS CON TODA! ➡️"):
        if nombre:
            st.session_state.n = nombre
            st.session_state.p = 2
            st.rerun()

elif st.session_state.p == 2:
    if st.button("<- Volver"):
        st.session_state.p = 1
        st.rerun()
    
    st.markdown(f"<h3 style='text-align:center;'>🛡️ RESPALDO: {st.session_state.n.upper()}</h3>", unsafe_allow_html=True)
    st.markdown(f'<div class="card">{INFO_P2}</div>', unsafe_allow_html=True)
    
    st.session_state.sec = st.selectbox("Sector de negocio:", list(sectores_map.keys()))
    ej_text = sectores_map[st.session_state.sec]['ej']
    
    desc = st.text_input("QUE HACES EXACTAMENTE?", value=st.session_state.tip, placeholder=ej_text)
    if desc:
        st.session_state.tip = desc

    st.write("---")
    st.write("<b>COMO TE PRESENTAS HOY?</b>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("CTA COBRO"):
            st.session_state.l = "Cuenta de Cobro"
    with c2:
        if st.button("COTIZACION"):
            st.session_state.l = "Cotizacion"
            
    if st.session_state.l and st.session_state.tip:
        if st.button("🚀 HACER MAGIA!"):
            st.session_state.p = 3
            st.
