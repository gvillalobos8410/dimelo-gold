import streamlit as st

# --- 1. BANCO DE DATOS Y PEDAGOGÍA (LEY DIMELO) ---
P1_CARD = """<div class="card"><b>🤝 ¡TÚ DÍMELO, QUE YO HAGO LA MAGIA!</b><br><br>¡Hola! No importa si estás empezando hoy o si ya tienes tu negocio andando, <b>esta app es para ti</b>.<br><br>Vas a recibir un documento con <b>imagen profesional</b> y un lenguaje tan claro y técnico que tus clientes te verán como una empresa de alto nivel.<br><br>Para el emprendedor que quiere dar el siguiente paso, este documento cumple con los requisitos de la <b>DIAN</b>, dejándote la puerta abierta para facturación electrónica si así lo decides. Pero si solo buscas presentarte mejor, ¡estás en el lugar correcto!<br><br><span class="gold">Tú solo dímelo</span> como parcero, que <span class="gold">yo hago la magia</span> de entregarte una propuesta impecable.</div>"""

P2_CARD = """<div class="card"><b>💡 TU ESCUDO COMERCIAL</b><br>Aquí no hay enredos. Vamos a ponerle <b>autoridad</b> a lo que haces. Elegir tu imagen y tu ruta legal no es una obligación pesada, es tu armadura para que el cliente confíe y tú cobres lo justo.<br><br>Vestir tu negocio de gala te abre puertas a mejores clientes y demuestra que tu trabajo tiene respaldo real ante la <b>DIAN</b>. ¡Yo te guío para que sea por beneficio, no por miedo!</div>"""

SECTORES = {
    '🌾 Agro': {'ej': 'Ej: Venta de 10 cargas de café pergamino seco...', 'img': 'https://images.unsplash.com/photo-1500651230702-0e2d8a49d4ad?w=1080'},
    '🛠️ Técnico': {'ej': 'Ej: Mantenimiento preventivo de motor diésel...', 'img': 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=1080'},
    '🏗️ Obra': {'ej': 'Ej: Remodelación de baño y cambio de tubería...', 'img': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1080'},
    '🍰 Gastro': {'ej': 'Ej: Servicio de catering para 50 personas...', 'img': 'https://images.unsplash.com/photo-1555244162-803834f70033?w=1080'},
    '⚖️ Legal': {'ej': 'Ej: Asesoría contable y cierre tributario...', 'img': 'https://images.unsplash.com/photo-1454165833767-027508658d61?w=1080'},
    '✨ Otro': {'ej': 'Ej: Describe tu servicio o producto...', 'img': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=1080'}
}

# --- 2. CONFIGURACIÓN ---
st.set_page_config(page_title="DIMELO GOLD", layout="centered")

for k, v in {'p':1, 'n':'', 'l':'', 'sec':'✨ Otro', 'tip':''}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 3. ESTILO CSS (SINTAXIS SEGURA) ---
img_fondo = SECTORES.get(st.session_state.sec, SECTORES['✨ Otro'])['img']
bg_final = f"linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)), url('{img_fondo}')" if st.session_state.p == 2 else "#ffffff"

css_base = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"], .main {
        overflow-y: auto !important; height: auto !important; min-height: 100vh !important;
        font-family: 'Montserrat', sans-serif;
    }
