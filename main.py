import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="wide")

# Inicialización de estado
keys = {'p':1, 'n':'', 'l':'', 'sec':'Otro', 'tip':'', 'g':'', 'logo':False}
for k, v in keys.items():
    if k not in st.session_state:
        st.session_state[k] = v

# --- 2. ESTILO GOLD SUPREME (CON SCROLL) ---
st.markdown("""
<style>
    .stApp { overflow-y: auto !important; }
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Montserrat', sans-serif; }
    .card { background: white; padding: 30px; border-radius: 20px; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 25px; }
    .ped { border-left: 8px solid #D4AF37; background: #fafafa; 
           padding: 20px; border-radius: 10px; margin: 15px 0; }
    div.stButton > button { background: #1a1a1a !important; color: #D4AF37 !important; 
                            font-weight: 700; border-radius: 12px; height: 3.5em; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- 3. PÁGINA 1: IDENTIDAD ---
if st.session_state.p == 1:
    st.markdown('<div class="card"><h1>🏆 DIMELO GOLD</h1>', True)
    st.markdown('<div class="ped"><b>PEDAGOGÍA:</b> Tu nombre valida tu autoridad profesional.</div>', True)
    nom = st.text_input("¿NOMBRE?", value=st.session_state.n)
    if st.button("SIGUIENTE ➡️"):
        if nom:
            st.session_state.n = nom
            st.session_state.p = 2
            st.rerun()
    st.markdown('</div>', True)

# --- 4. PÁGINA 2: REGISTRO BLINDADO (DIAN) ---
elif st.session_state.p == 2:
    st.markdown(f'<div class="card"><h1>🛡️ REGISTRO: {st.session_state.n.upper()}</h1>', True)
    st.markdown('<div class="ped"><b>AVISO DIAN:</b> Define tu estatus legal para cotizar con peso de ley.</div>', True)

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("🖼️ MARCA")
        up = st.file_uploader("Logo", label_visibility="collapsed")
        if up: st.session_state.logo = True
        else: st.warning("🚨 Sugerencia: El logo genera confianza.")
        
        st.write("---")
        # Lista nutrida de sectores
        sl = ['🌾 Agro', '🛠️ Técnico', '🍰 Gastronomía', '🏗️ Obra', '⚖️ Pro', '✨ Otro']
        st.session_state.sec = st.selectbox("SECTOR:", sl)
        ta = st.text_input("¿QUÉ HACES?", value=st.session_state.tip)
        if ta: st.session_state.tip = ta

    with c2:
        st.subheader("🏛️ RUTA LEGAL")
        if st.button("📄 CUENTA DE COBRO"):
            st.session_state.l = "Sencilla"
        if st.button("🏛️ COTIZACIÓN EMPRESARIAL"):
            st.session_state.l = "Formal"
        
        if st.session_state.l:
            st.success(f"Activo: {st.session_state.l}")

    if st.session_state.l and st.session_state.tip:
        if st.button("ABRIR MOTOR 🚀"):
            st.session_state.p = 3
            st.rerun()
    st.markdown('</div>', True)

# --- 5. PÁGINA 3: MOTOR (ALMA Y MAGIA) ---
elif st.session_state.p == 3:
    st.markdown('<div class="card"><h1>🎙️ MOTOR DE PRECISIÓN</h1>', True)
    st.markdown('<div class="ped">✨ <b>LA IA HACE LA MAGIA:</b> Cuéntame tu idea sencillo, como un café.</div>', True)
    
    if st.button("🔴 GRABAR"):
        st.info("🎤 Escuchando... Habla ahora.")
    
    with st.expander("⌨️ ESCRIBIR"):
        ti = st.text_area("Idea:", height=100)
        
    if st.button("✨ TRANSFORMAR A GOLD"):
        res = ti if ti else "Voz procesada"
        st.session_state.g = f"**PROPUESTA:** {res.upper()}"
        st.session_state.p = 4
        st.rerun()
    st.markdown('</div>', True)

# --- 6. PÁGINA 4: ENTREGABLE ---
elif st.session_state.p == 4:
    st.title("💎 ENTREGABLE")
    st.write(st.session_state.g)
    if st.button("🔄 VOLVER"):
        st.session_state.p = 3
        st.rerun()
