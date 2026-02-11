"""
DIMELO - Tu voz, nuestras palabras.
App Streamlit para comerciantes MIPYME en Colombia.
Ejecutar con: streamlit run dimelo_app.py
"""

import streamlit as st
import json
import datetime
import re

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="DIMELO – Solo habla, yo hago la magia",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# GLOBAL CSS  – paleta morada/oscura de las maquetas
# ─────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,500;0,700;1,400&family=Syne:wght@700;800&display=swap');

/* ── Variables ── */
:root {
  --bg-dark:       #0D0B1A;
  --bg-card:       #161228;
  --bg-card2:      #1E1834;
  --accent:        #9B5DE5;
  --accent-light:  #BF8BFF;
  --accent-glow:   rgba(155,93,229,0.35);
  --accent-soft:   rgba(155,93,229,0.12);
  --text-primary:  #F0EAFF;
  --text-muted:    #8B7FA8;
  --border:        rgba(155,93,229,0.25);
  --success:       #6DD5C0;
  --warning:       #F7B731;
  --radius:        18px;
  --radius-sm:     10px;
}

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
  background: var(--bg-dark) !important;
  color: var(--text-primary) !important;
  font-family: 'DM Sans', sans-serif !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
.stDeployButton { display: none !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg-dark); }
::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 3px; }

/* ── Main container ── */
[data-testid="stAppViewContainer"] > .main {
  background: var(--bg-dark) !important;
  padding: 0 !important;
}
.main .block-container {
  max-width: 900px !important;
  padding: 2rem 1.5rem 4rem !important;
  margin: 0 auto !important;
}

/* ── Typography ── */
h1, h2, h3 {
  font-family: 'Syne', sans-serif !important;
  color: var(--text-primary) !important;
}

/* ── Streamlit widgets override ── */

/* Buttons */
.stButton > button {
  background: linear-gradient(135deg, var(--accent), #6A0DAD) !important;
  color: #fff !important;
  border: none !important;
  border-radius: 50px !important;
  font-family: 'DM Sans', sans-serif !important;
  font-weight: 700 !important;
  font-size: 1rem !important;
  padding: 0.7rem 2rem !important;
  cursor: pointer !important;
  transition: all 0.3s ease !important;
  box-shadow: 0 4px 20px var(--accent-glow) !important;
  letter-spacing: 0.02em !important;
}
.stButton > button:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 30px var(--accent-glow) !important;
  filter: brightness(1.1) !important;
}
.stButton > button:active { transform: scale(0.97) !important; }

/* Secondary button */
.btn-secondary > button {
  background: var(--accent-soft) !important;
  border: 1.5px solid var(--border) !important;
  color: var(--accent-light) !important;
  box-shadow: none !important;
}
.btn-secondary > button:hover {
  background: var(--border) !important;
  box-shadow: none !important;
}

/* Text inputs */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stNumberInput > div > div > input {
  background: var(--bg-card2) !important;
  border: 1.5px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
  color: var(--text-primary) !important;
  font-family: 'DM Sans', sans-serif !important;
  font-size: 1rem !important;
  padding: 0.75rem 1rem !important;
  transition: border-color 0.3s !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 3px var(--accent-soft) !important;
}

/* Selectbox */
.stSelectbox > div > div {
  background: var(--bg-card2) !important;
  border: 1.5px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
  color: var(--text-primary) !important;
}

/* Labels */
.stTextInput > label, .stTextArea > label,
.stSelectbox > label, .stNumberInput > label {
  color: var(--text-muted) !important;
  font-size: 0.82rem !important;
  font-weight: 500 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.08em !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
  background: var(--bg-card) !important;
  border-radius: 50px !important;
  padding: 4px !important;
  border: 1px solid var(--border) !important;
  gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
  background: transparent !important;
  border-radius: 50px !important;
  color: var(--text-muted) !important;
  font-family: 'DM Sans', sans-serif !important;
  font-weight: 600 !important;
  padding: 0.5rem 1.2rem !important;
  transition: all 0.3s !important;
}
.stTabs [aria-selected="true"] {
  background: var(--accent) !important;
  color: #fff !important;
  box-shadow: 0 4px 15px var(--accent-glow) !important;
}
.stTabs [data-baseweb="tab-panel"] {
  padding: 1.5rem 0 !important;
}

/* Expander */
.streamlit-expanderHeader {
  background: var(--bg-card) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
  color: var(--text-primary) !important;
  font-family: 'DM Sans', sans-serif !important;
  font-weight: 600 !important;
}
.streamlit-expanderContent {
  background: var(--bg-card2) !important;
  border: 1px solid var(--border) !important;
  border-top: none !important;
  border-radius: 0 0 var(--radius-sm) var(--radius-sm) !important;
}

/* Divider */
hr { border-color: var(--border) !important; }

/* Metrics */
[data-testid="stMetricValue"] {
  color: var(--accent-light) !important;
  font-family: 'Syne', sans-serif !important;
}
[data-testid="stMetricLabel"] { color: var(--text-muted) !important; }

/* Radio */
.stRadio > div { gap: 8px !important; }
.stRadio > div > label {
  background: var(--bg-card) !important;
  border: 1.5px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
  padding: 0.6rem 1.2rem !important;
  color: var(--text-muted) !important;
  cursor: pointer !important;
  transition: all 0.2s !important;
}
.stRadio > div > label:has(input:checked) {
  border-color: var(--accent) !important;
  background: var(--accent-soft) !important;
  color: var(--accent-light) !important;
}

/* Checkbox */
.stCheckbox > label { color: var(--text-primary) !important; }

/* ── Custom component classes ── */

.dimelo-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 2.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--border);
}
.dimelo-logo-icon {
  width: 52px; height: 52px;
  background: linear-gradient(135deg, var(--accent), #6A0DAD);
  border-radius: 14px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.6rem;
  box-shadow: 0 8px 24px var(--accent-glow);
}
.dimelo-logo-text {
  font-family: 'Syne', sans-serif;
  font-size: 1.8rem;
  font-weight: 800;
  background: linear-gradient(135deg, #fff 40%, var(--accent-light));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.dimelo-tagline {
  color: var(--text-muted);
  font-size: 0.85rem;
  margin-top: -2px;
}

.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.5rem;
  margin-bottom: 1.2rem;
  transition: border-color 0.3s, box-shadow 0.3s;
}
.card:hover {
  border-color: var(--accent);
  box-shadow: 0 4px 24px var(--accent-glow);
}

.card-glow {
  background: linear-gradient(135deg, var(--bg-card), var(--bg-card2));
  border: 1px solid var(--accent);
  border-radius: var(--radius);
  padding: 1.5rem;
  box-shadow: 0 0 0 1px var(--accent-glow), 0 8px 32px var(--accent-glow);
}

.tip-box {
  background: linear-gradient(135deg, rgba(109,213,192,0.08), rgba(109,213,192,0.04));
  border: 1px solid rgba(109,213,192,0.3);
  border-left: 4px solid var(--success);
  border-radius: var(--radius-sm);
  padding: 1rem 1.2rem;
  margin: 1rem 0;
}
.tip-box .tip-title {
  color: var(--success);
  font-weight: 700;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 0.3rem;
}
.tip-box p { color: var(--text-primary); font-size: 0.92rem; margin: 0; }

.step-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px; height: 32px;
  background: var(--accent);
  border-radius: 50%;
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 0.9rem;
  color: #fff;
  box-shadow: 0 4px 12px var(--accent-glow);
  flex-shrink: 0;
}

.section-title {
  font-family: 'Syne', sans-serif;
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.3rem;
}
.section-sub {
  color: var(--text-muted);
  font-size: 0.9rem;
  margin-bottom: 1.2rem;
}

.doc-output {
  background: #fefefe;
  color: #1a1a2e;
  border-radius: var(--radius);
  padding: 2rem;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.95rem;
  line-height: 1.7;
  border: 2px solid var(--accent);
  box-shadow: 0 8px 40px rgba(0,0,0,0.4);
}
.doc-output h2 {
  font-family: 'Syne', sans-serif !important;
  color: var(--accent) !important;
  font-size: 1.2rem !important;
  margin-bottom: 1rem !important;
  border-bottom: 2px solid rgba(155,93,229,0.2);
  padding-bottom: 0.5rem;
}
.doc-output p { color: #2d2d4e; margin-bottom: 0.8rem; }
.doc-output table {
  width: 100%; border-collapse: collapse; margin: 1rem 0;
}
.doc-output table th {
  background: rgba(155,93,229,0.12);
  color: var(--accent);
  padding: 0.6rem 1rem;
  text-align: left;
  font-weight: 700;
  font-size: 0.85rem;
  text-transform: uppercase;
  border-bottom: 2px solid rgba(155,93,229,0.2);
}
.doc-output table td {
  padding: 0.6rem 1rem;
  border-bottom: 1px solid #e8e4f5;
  color: #2d2d4e;
}
.doc-output table tr:last-child td { border-bottom: none; }

.progress-steps {
  display: flex;
  gap: 8px;
  align-items: center;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}
.ps-item {
  display: flex; align-items: center; gap: 6px;
  font-size: 0.8rem; font-weight: 600;
  color: var(--text-muted);
}
.ps-item.active { color: var(--accent-light); }
.ps-item.done { color: var(--success); }
.ps-dot {
  width: 8px; height: 8px;
  border-radius: 50%;
  background: var(--text-muted);
}
.ps-item.active .ps-dot { background: var(--accent); box-shadow: 0 0 8px var(--accent-glow); }
.ps-item.done .ps-dot { background: var(--success); }
.ps-line {
  flex: 1; height: 1px;
  background: var(--border);
  min-width: 20px;
}

.big-cta {
  background: linear-gradient(135deg, var(--bg-card), var(--bg-card2));
  border: 2px dashed var(--border);
  border-radius: var(--radius);
  padding: 2.5rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s;
}
.big-cta:hover {
  border-color: var(--accent);
  background: var(--accent-soft);
  box-shadow: 0 8px 32px var(--accent-glow);
}
.big-cta .icon { font-size: 3rem; margin-bottom: 0.8rem; }
.big-cta h3 {
  font-family: 'Syne', sans-serif;
  font-size: 1.4rem;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}
.big-cta p { color: var(--text-muted); font-size: 0.95rem; }

.badge {
  display: inline-block;
  padding: 0.2rem 0.7rem;
  border-radius: 50px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}
.badge-purple { background: var(--accent-soft); color: var(--accent-light); border: 1px solid var(--border); }
.badge-green  { background: rgba(109,213,192,0.12); color: var(--success); border: 1px solid rgba(109,213,192,0.3); }
.badge-yellow { background: rgba(247,183,49,0.12); color: var(--warning); border: 1px solid rgba(247,183,49,0.3); }

.history-item {
  display: flex; align-items: flex-start; gap: 12px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 1rem 1.2rem;
  margin-bottom: 0.7rem;
  cursor: pointer;
  transition: all 0.2s;
}
.history-item:hover {
  border-color: var(--accent);
  background: var(--accent-soft);
  transform: translateX(4px);
}
.history-icon { font-size: 1.2rem; margin-top: 2px; flex-shrink: 0; }
.history-text { flex: 1; }
.history-text .ht-title { font-weight: 600; font-size: 0.92rem; color: var(--text-primary); }
.history-text .ht-meta { font-size: 0.78rem; color: var(--text-muted); margin-top: 2px; }

.onboarding-step {
  display: flex; align-items: flex-start; gap: 14px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.3rem;
  margin-bottom: 0.8rem;
}
.onboarding-step .os-icon {
  font-size: 2rem; flex-shrink: 0;
  width: 52px; height: 52px;
  background: var(--accent-soft);
  border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
}
.onboarding-step h4 {
  font-family: 'DM Sans', sans-serif !important;
  font-weight: 700; font-size: 1rem;
  color: var(--text-primary); margin-bottom: 0.3rem;
}
.onboarding-step p { color: var(--text-muted); font-size: 0.88rem; margin: 0; }

.wave-btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 90px; height: 90px;
  background: linear-gradient(135deg, var(--accent), #6A0DAD);
  border-radius: 50%;
  cursor: pointer;
  font-size: 2.2rem;
  box-shadow: 0 0 0 12px var(--accent-glow), 0 0 0 24px rgba(155,93,229,0.1);
  transition: all 0.3s;
  margin: 1.5rem auto;
  display: block;
}
.wave-btn:hover {
  transform: scale(1.08);
  box-shadow: 0 0 0 16px var(--accent-glow), 0 0 0 32px rgba(155,93,229,0.1);
}

/* Alert / info boxes */
[data-testid="stAlert"] {
  background: var(--accent-soft) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
  color: var(--text-primary) !important;
}

/* Dataframe / tables */
[data-testid="stDataFrame"] {
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
}

/* Number input */
.stNumberInput button {
  background: var(--bg-card2) !important;
  border-color: var(--border) !important;
  color: var(--text-primary) !important;
}

/* Download button */
.stDownloadButton > button {
  background: var(--accent-soft) !important;
  color: var(--accent-light) !important;
  border: 1.5px solid var(--border) !important;
  box-shadow: none !important;
}
.stDownloadButton > button:hover {
  background: var(--border) !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 4px 12px var(--accent-glow) !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
  background: var(--bg-card) !important;
  border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-primary) !important; }

</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HELPERS / DOCUMENT GENERATORS
# ─────────────────────────────────────────────

def fmt_cop(valor: float) -> str:
    """Formatea un número como pesos colombianos."""
    return f"${valor:,.0f} COP"

def calcular_iva(subtotal: float, tarifa: float = 19.0) -> float:
    return subtotal * tarifa / 100

def num_a_texto(n: float) -> str:
    """Convierte número a texto simplificado (hasta millones)."""
    n = int(n)
    millones = n // 1_000_000
    resto = n % 1_000_000
    miles = resto // 1_000
    unidades = resto % 1_000
    partes = []
    if millones:
        partes.append(f"{millones} millón{'es' if millones > 1 else ''}")
    if miles:
        partes.append(f"{miles} mil")
    if unidades:
        partes.append(str(unidades))
    if not partes:
        return "cero"
    return " ".join(partes) + " pesos"

def generar_cotizacion(datos: dict) -> str:
    fecha = datetime.date.today()
    vence = fecha + datetime.timedelta(days=datos.get("vigencia_dias", 15))
    
    items_html = ""
    subtotal = 0.0
    for idx, item in enumerate(datos.get("items", []), 1):
        total_item = item["qty"] * item["precio"]
        subtotal += total_item
        items_html += f"""
        <tr>
          <td>{idx}</td>
          <td><strong>{item['nombre']}</strong><br>
              <span style="font-size:0.85rem;color:#888">{item.get('desc','')}</span></td>
          <td style="text-align:center">{item['qty']} {item.get('unidad','und')}</td>
          <td style="text-align:right">{fmt_cop(item['precio'])}</td>
          <td style="text-align:right;font-weight:700">{fmt_cop(total_item)}</td>
        </tr>"""

    aplica_iva = datos.get("aplica_iva", False)
    iva_val = calcular_iva(subtotal) if aplica_iva else 0
    total = subtotal + iva_val

    iva_row = ""
    if aplica_iva:
        iva_row = f"<tr><td colspan='4' style='text-align:right;color:#888'>IVA 19%</td><td style='text-align:right'>{fmt_cop(iva_val)}</td></tr>"

    nota_dian = ""
    if not datos.get("reportar_dian", True):
        nota_dian = "<p style='color:#e07b39;font-size:0.85rem;margin-top:0.5rem'><strong>⚠️ Nota:</strong> Este documento es una orden de compra interna y no reemplaza una factura electrónica ante la DIAN.</p>"

    return f"""
<div class="doc-output">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:1.5rem;flex-wrap:wrap;gap:1rem">
    <div>
      <div style="font-family:Syne,sans-serif;font-size:1.6rem;font-weight:800;background:linear-gradient(135deg,#9B5DE5,#BF8BFF);-webkit-background-clip:text;-webkit-text-fill-color:transparent">◈D DIMELO</div>
      <div style="font-size:0.8rem;color:#888">Tu voz, nuestras palabras</div>
    </div>
    <div style="text-align:right">
      <div style="font-family:Syne,sans-serif;font-size:1.1rem;font-weight:700;color:#9B5DE5">COTIZACIÓN</div>
      <div style="font-size:0.85rem;color:#888">N°: COT-{fecha.strftime('%Y%m%d')}-001</div>
      <div style="font-size:0.85rem;color:#888">Fecha: {fecha.strftime('%d/%m/%Y')}</div>
      <div style="font-size:0.85rem;color:#888">Válida hasta: {vence.strftime('%d/%m/%Y')}</div>
    </div>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:1.5rem;flex-wrap:wrap">
    <div style="background:#f5f3ff;padding:1rem;border-radius:10px">
      <div style="font-size:0.75rem;color:#9B5DE5;font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.5rem">De (Proveedor)</div>
      <div style="font-weight:700;color:#1a1a2e">{datos.get('vendedor_nombre','Mi Empresa')}</div>
      <div style="color:#555;font-size:0.88rem">{datos.get('vendedor_tel','')}</div>
      <div style="color:#555;font-size:0.88rem">{datos.get('vendedor_ciudad','')}</div>
    </div>
    <div style="background:#f5f3ff;padding:1rem;border-radius:10px">
      <div style="font-size:0.75rem;color:#9B5DE5;font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.5rem">Para (Cliente)</div>
      <div style="font-weight:700;color:#1a1a2e">{datos.get('cliente_nombre','Cliente')}</div>
      <div style="color:#555;font-size:0.88rem">{datos.get('cliente_tel','')}</div>
      <div style="color:#555;font-size:0.88rem">{datos.get('cliente_ciudad','')}</div>
    </div>
  </div>

  <h2>📦 Productos / Servicios</h2>
  <table>
    <thead>
      <tr><th>#</th><th>Descripción</th><th>Cant.</th><th>V. Unitario</th><th>V. Total</th></tr>
    </thead>
    <tbody>
      {items_html}
    </tbody>
    <tfoot>
      <tr style="border-top:2px solid #e8e4f5">
        <td colspan="4" style="text-align:right;font-weight:700;color:#1a1a2e">Subtotal</td>
        <td style="text-align:right;font-weight:700">{fmt_cop(subtotal)}</td>
      </tr>
      {iva_row}
      <tr style="background:#f5f3ff">
        <td colspan="4" style="text-align:right;font-family:Syne,sans-serif;font-weight:800;color:#9B5DE5;font-size:1.05rem">TOTAL A PAGAR</td>
        <td style="text-align:right;font-family:Syne,sans-serif;font-weight:800;color:#9B5DE5;font-size:1.05rem">{fmt_cop(total)}</td>
      </tr>
    </tfoot>
  </table>
  <p style="font-size:0.85rem;color:#888;margin-top:0.5rem">Son: {num_a_texto(total)}</p>

  {f'<div style="background:#fff3e0;padding:1rem;border-radius:8px;margin-top:1rem"><div style="font-size:0.75rem;font-weight:700;text-transform:uppercase;color:#e07b39;margin-bottom:.3rem">💳 Forma de Pago</div><div style="color:#555;font-size:.9rem">{datos.get("forma_pago","Acordar con el cliente")}</div></div>' if datos.get("forma_pago") else ""}

  {f'<div style="background:#e8f5e9;padding:1rem;border-radius:8px;margin-top:.8rem"><div style="font-size:0.75rem;font-weight:700;text-transform:uppercase;color:#388e3c;margin-bottom:.3rem">📝 Observaciones</div><div style="color:#555;font-size:.9rem">{datos.get("observaciones","")}</div></div>' if datos.get("observaciones") else ""}

  {nota_dian}

  <div style="margin-top:2rem;padding-top:1rem;border-top:1px solid #e8e4f5;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.5rem">
    <div style="font-size:0.78rem;color:#aaa">Generado con DIMELO · Solo habla, yo hago la magia 🎙️</div>
    <div style="font-size:0.78rem;color:#9B5DE5;font-weight:600">www.dimelo.app</div>
  </div>
</div>
"""

def generar_recibo(datos: dict) -> str:
    fecha = datetime.date.today()
    return f"""
<div class="doc-output">
  <div style="text-align:center;margin-bottom:1.5rem">
    <div style="font-family:Syne,sans-serif;font-size:1.6rem;font-weight:800;background:linear-gradient(135deg,#9B5DE5,#BF8BFF);-webkit-background-clip:text;-webkit-text-fill-color:transparent">◈D DIMELO</div>
    <div style="font-family:Syne,sans-serif;font-size:1.2rem;font-weight:700;color:#1a1a2e;margin-top:.5rem">RECIBO DE PAGO</div>
    <div style="font-size:0.82rem;color:#888">N° {datos.get('numero','001')} · {fecha.strftime('%d de %B de %Y')}</div>
  </div>
  <div style="background:#f5f3ff;padding:1.2rem;border-radius:10px;margin-bottom:1rem">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.5rem">
      <div><span style="font-size:.75rem;color:#9B5DE5;font-weight:700;text-transform:uppercase">Recibí de</span><div style="font-weight:700;color:#1a1a2e;margin-top:.2rem">{datos.get('pagador','')}</div></div>
      <div><span style="font-size:.75rem;color:#9B5DE5;font-weight:700;text-transform:uppercase">La suma de</span><div style="font-weight:800;color:#9B5DE5;font-size:1.15rem;margin-top:.2rem">{fmt_cop(datos.get('valor',0))}</div></div>
    </div>
    <div style="margin-top:.8rem;font-size:.88rem;color:#555">Son: {num_a_texto(datos.get('valor',0))}</div>
  </div>
  <div style="background:#fff;border:1px solid #e8e4f5;padding:1rem;border-radius:10px;margin-bottom:1rem">
    <div style="font-size:.75rem;color:#888;font-weight:700;text-transform:uppercase;margin-bottom:.3rem">Por concepto de</div>
    <div style="color:#1a1a2e;font-size:.95rem">{datos.get('concepto','')}</div>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:.8rem;margin-bottom:1rem">
    <div style="background:#f5f3ff;padding:.8rem;border-radius:8px">
      <div style="font-size:.75rem;color:#888;font-weight:700;text-transform:uppercase">Forma de pago</div>
      <div style="font-weight:600;color:#1a1a2e;margin-top:.2rem">{datos.get('forma_pago','Efectivo')}</div>
    </div>
    <div style="background:#f5f3ff;padding:.8rem;border-radius:8px">
      <div style="font-size:.75rem;color:#888;font-weight:700;text-transform:uppercase">Recibió</div>
      <div style="font-weight:600;color:#1a1a2e;margin-top:.2rem">{datos.get('recibidor','')}</div>
    </div>
  </div>
  <div style="margin-top:2rem;display:grid;grid-template-columns:1fr 1fr;gap:2rem">
    <div style="text-align:center">
      <div style="border-top:1px solid #ccc;padding-top:.5rem;font-size:.82rem;color:#888">Firma Quien Paga<br><strong style="color:#1a1a2e">{datos.get('pagador','')}</strong></div>
    </div>
    <div style="text-align:center">
      <div style="border-top:1px solid #ccc;padding-top:.5rem;font-size:.82rem;color:#888">Firma Quien Recibe<br><strong style="color:#1a1a2e">{datos.get('recibidor','')}</strong></div>
    </div>
  </div>
  <div style="margin-top:1.5rem;text-align:center;font-size:.75rem;color:#aaa">Generado con DIMELO · Solo habla, yo hago la magia 🎙️</div>
</div>
"""

def generar_contrato_servicio(datos: dict) -> str:
    fecha = datetime.date.today()
    return f"""
<div class="doc-output">
  <div style="text-align:center;margin-bottom:2rem">
    <div style="font-family:Syne,sans-serif;font-size:1.6rem;font-weight:800;background:linear-gradient(135deg,#9B5DE5,#BF8BFF);-webkit-background-clip:text;-webkit-text-fill-color:transparent">◈D DIMELO</div>
    <div style="font-family:Syne,sans-serif;font-size:1.3rem;font-weight:700;color:#1a1a2e;margin-top:.6rem">CONTRATO DE PRESTACIÓN DE SERVICIOS</div>
    <div style="font-size:.82rem;color:#888;margin-top:.3rem">Ciudad de {datos.get('ciudad','Colombia')}, {fecha.strftime('%d de %B de %Y')}</div>
  </div>

  <p>Los suscritos: <strong>{datos.get('contratante','')}</strong> (en adelante EL CONTRATANTE) y <strong>{datos.get('contratista','')}</strong> (en adelante EL CONTRATISTA), mayores de edad e identificados como aparece al pie de sus firmas, han convenido celebrar el presente contrato de prestación de servicios, regido por las siguientes cláusulas:</p>

  <h2>PRIMERA – OBJETO DEL CONTRATO</h2>
  <p>El CONTRATISTA se obliga a prestar al CONTRATANTE el siguiente servicio: <strong>{datos.get('objeto_contrato','')}</strong></p>

  <h2>SEGUNDA – OBLIGACIONES DEL CONTRATISTA</h2>
  <p>{datos.get('obligaciones','Ejecutar el servicio contratado con diligencia y en los plazos acordados, utilizando los materiales y herramientas necesarias para su correcta realización.')}</p>

  <h2>TERCERA – VALOR Y FORMA DE PAGO</h2>
  <p>El valor total del presente contrato es de <strong>{fmt_cop(datos.get('valor_total',0))}</strong> ({num_a_texto(datos.get('valor_total',0))}). La forma de pago será: {datos.get('forma_pago','acordada entre las partes.')}.</p>

  <h2>CUARTA – PLAZO DE EJECUCIÓN</h2>
  <p>El presente contrato tendrá una duración de <strong>{datos.get('plazo','')}</strong> a partir de la fecha de suscripción.</p>

  <h2>QUINTA – LUGAR DE EJECUCIÓN</h2>
  <p>Los servicios se prestarán en: <strong>{datos.get('lugar_ejecucion',datos.get('ciudad',''))}</strong></p>

  <h2>SEXTA – CLÁUSULA DE INCUMPLIMIENTO</h2>
  <p>En caso de incumplimiento injustificado por cualquiera de las partes, la parte incumplida deberá pagar a la otra una suma equivalente al <strong>{datos.get('penalidad_pct', '10')}%</strong> del valor total del contrato como pena convencional, sin perjuicio de las acciones legales a que haya lugar.</p>

  <h2>SÉPTIMA – CONFIDENCIALIDAD</h2>
  <p>Las partes se comprometen a guardar absoluta reserva sobre la información que conozcan con ocasión del presente contrato.</p>

  <h2>OCTAVA – RESOLUCIÓN DE CONFLICTOS</h2>
  <p>Las diferencias que surjan entre las partes se resolverán, en primera instancia, mediante diálogo directo. De no llegarse a un acuerdo, las partes podrán acudir a los mecanismos alternativos de solución de conflictos.</p>

  <h2>FIRMA DE LAS PARTES</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;margin-top:2rem">
    <div style="text-align:center">
      <div style="border-top:2px solid #9B5DE5;padding-top:.8rem">
        <div style="font-weight:700;color:#1a1a2e">{datos.get('contratante','')}</div>
        <div style="font-size:.8rem;color:#888">EL CONTRATANTE<br>CC/NIT: {datos.get('cc_contratante','_____________')}</div>
      </div>
    </div>
    <div style="text-align:center">
      <div style="border-top:2px solid #9B5DE5;padding-top:.8rem">
        <div style="font-weight:700;color:#1a1a2e">{datos.get('contratista','')}</div>
        <div style="font-size:.8rem;color:#888">EL CONTRATISTA<br>CC/NIT: {datos.get('cc_contratista','_____________')}</div>
      </div>
    </div>
  </div>
  <div style="margin-top:1.5rem;text-align:center;font-size:.75rem;color:#aaa">Generado con DIMELO · Solo habla, yo hago la magia 🎙️</div>
</div>
"""

def generar_permiso_trabajo(datos: dict) -> str:
    fecha = datetime.date.today()
    return f"""
<div class="doc-output">
  <div style="text-align:center;margin-bottom:1.5rem">
    <div style="font-family:Syne,sans-serif;font-size:1.4rem;font-weight:800;background:linear-gradient(135deg,#9B5DE5,#BF8BFF);-webkit-background-clip:text;-webkit-text-fill-color:transparent">◈D DIMELO</div>
    <div style="font-family:Syne,sans-serif;font-size:1.2rem;font-weight:700;color:#1a1a2e;margin-top:.4rem">CONSTANCIA DE TRABAJO</div>
    <div style="font-size:.82rem;color:#888">{fecha.strftime('%d de %B de %Y')}</div>
  </div>
  <p>Yo, <strong>{datos.get('empleador','')}</strong>, propietario(a) de <strong>{datos.get('nombre_negocio','')}</strong>, con establecimiento ubicado en <strong>{datos.get('direccion','')}</strong>, ciudad de <strong>{datos.get('ciudad','')}</strong>,</p>
  <p><strong>HAGO CONSTAR QUE:</strong></p>
  <p><strong>{datos.get('empleado','')}</strong>, identificado(a) con cédula de ciudadanía N° <strong>{datos.get('cc_empleado','')}</strong>, labora en este establecimiento en el cargo de <strong>{datos.get('cargo','')}</strong>, desde el día <strong>{datos.get('fecha_inicio','')}</strong>, devengando un salario de <strong>{fmt_cop(datos.get('salario',0))}</strong> ({num_a_texto(datos.get('salario',0))}) mensuales.</p>
  <p>La presente constancia se expide a solicitud del interesado y para los fines que estime convenientes.</p>
  <div style="margin-top:3rem;display:flex;flex-direction:column;align-items:center;gap:.5rem">
    <div style="font-size:.82rem;color:#888">Firma del empleador</div>
    <div style="width:200px;border-top:2px solid #9B5DE5;padding-top:.8rem;text-align:center">
      <div style="font-weight:700;color:#1a1a2e">{datos.get('empleador','')}</div>
      <div style="font-size:.8rem;color:#888">{datos.get('nombre_negocio','')}</div>
    </div>
  </div>
  <div style="margin-top:1.5rem;text-align:center;font-size:.75rem;color:#aaa">Generado con DIMELO · Solo habla, yo hago la magia 🎙️</div>
</div>
"""


# ─────────────────────────────────────────────
# SESSION STATE INIT
# ─────────────────────────────────────────────
if "historial" not in st.session_state:
    st.session_state.historial = []
if "onboarding_done" not in st.session_state:
    st.session_state.onboarding_done = False
if "tab_activa" not in st.session_state:
    st.session_state.tab_activa = 0
if "doc_generado" not in st.session_state:
    st.session_state.doc_generado = None
if "doc_tipo" not in st.session_state:
    st.session_state.doc_tipo = None


# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="dimelo-header">
  <div class="dimelo-logo-icon">◈</div>
  <div>
    <div class="dimelo-logo-text">DIMELO</div>
    <div class="dimelo-tagline">Solo habla, yo hago la magia 🎙️</div>
  </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# ONBOARDING
# ─────────────────────────────────────────────
if not st.session_state.onboarding_done:
    st.markdown("""
<div style="text-align:center;padding:1rem 0 2rem">
  <div style="font-family:Syne,sans-serif;font-size:2rem;font-weight:800;color:#fff;margin-bottom:.5rem">
    ¡Bienvenido a DIMELO! 🎉
  </div>
  <div style="color:#8B7FA8;font-size:1.05rem;max-width:520px;margin:0 auto">
    Si tú tienes el talento, <strong style="color:#BF8BFF">DIMELO tiene las palabras.</strong>
    <br>Transformamos tu esfuerzo en documentos que imponen respeto.
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>¿Cómo funciona?</div>", unsafe_allow_html=True)

    pasos = [
        ("🗣️", "Cuéntame qué necesitas", "No importa cómo lo digas — usa tus propias palabras, sin tecnicismos. Yo te entiendo."),
        ("✏️", "Llenas los datos básicos", "Solo lo esencial: nombres, valores, fechas. En menos de 2 minutos ya está."),
        ("🪄", "Yo armo el documento", "Lo visto de gala para que nadie te pague menos de lo que mereces."),
        ("📤", "Descarga y comparte", "Listo para WhatsApp, imprimir o guardar. Tuyo, con tu nombre."),
    ]
    for icon, titulo, desc in pasos:
        st.markdown(f"""
<div class="onboarding-step">
  <div class="os-icon">{icon}</div>
  <div>
    <h4>{titulo}</h4>
    <p>{desc}</p>
  </div>
</div>""", unsafe_allow_html=True)

    st.markdown("""
<div class="tip-box" style="margin-top:1.5rem">
  <div class="tip-title">💡 Recuerda esto</div>
  <p>En DIMELO <strong>no te corregimos, te potenciamos</strong>. Tu forma de hablar es la base de todo. El informal a veces siente que "no sabe", pero la realidad es que sabe mucho de su oficio. Nosotros solo ayudamos a que los demás también lo vean.</p>
</div>
""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 ¡Vamos a crear mi primer documento!", use_container_width=True):
            st.session_state.onboarding_done = True
            st.rerun()
    st.stop()


# ─────────────────────────────────────────────
# MAIN NAVIGATION TABS
# ─────────────────────────────────────────────
tab_cotizacion, tab_recibo, tab_contrato, tab_constancia, tab_historial, tab_aprende = st.tabs([
    "📋 Cotización",
    "💵 Recibo de Pago",
    "🤝 Contrato",
    "📄 Constancia",
    "🕐 Historial",
    "📚 Aprende",
])


# ═══════════════════════════════════════════════════════════
# TAB 1: COTIZACIÓN
# ═══════════════════════════════════════════════════════════
with tab_cotizacion:
    st.markdown("<div class='section-title'>Cotización Profesional</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Cuéntame qué vendes y yo armo el presupuesto que tu cliente no puede rechazar.</div>", unsafe_allow_html=True)

    st.markdown("""
<div class="tip-box">
  <div class="tip-title">🧑‍🏫 Profesor DIMELO dice:</div>
  <p>Una cotización le dice al cliente exactamente qué le vas a dar y cuánto cuesta. Es tu carta de presentación. ¡Con esto nadie te dice "no sabía que era tan caro"!</p>
</div>
""", unsafe_allow_html=True)

    with st.expander("👤 Paso 1 – Mis datos (tu negocio)", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            vend_nombre = st.text_input("Tu nombre o razón social *", placeholder="Ej: Herrería Don Carlos", key="cot_vend_nombre")
            vend_tel = st.text_input("Tu teléfono / WhatsApp", placeholder="Ej: 311 222 3344", key="cot_vend_tel")
        with c2:
            vend_ciudad = st.text_input("Tu ciudad", placeholder="Ej: Medellín, Antioquia", key="cot_vend_ciudad")

    with st.expander("🧑‍💼 Paso 2 – Datos del cliente", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            cli_nombre = st.text_input("Nombre del cliente *", placeholder="Ej: Ferretería El Tornillo", key="cot_cli_nombre")
            cli_tel = st.text_input("Teléfono del cliente", placeholder="Ej: 312 333 4455", key="cot_cli_tel")
        with c2:
            cli_ciudad = st.text_input("Ciudad del cliente", placeholder="Ej: Bogotá, Cundinamarca", key="cot_cli_ciudad")

    with st.expander("📦 Paso 3 – Lo que vas a vender o hacer", expanded=True):
        st.markdown("""
<div style="color:#8B7FA8;font-size:.88rem;margin-bottom:1rem">
  🧑‍🏫 <strong>¿Cómo funciona esto?</strong> Escribe los productos o servicios que ofreces. Añade todos los que necesites.
</div>""", unsafe_allow_html=True)

        if "cot_items" not in st.session_state:
            st.session_state.cot_items = [{"nombre": "", "desc": "", "qty": 1, "precio": 0.0, "unidad": "und"}]

        items_a_borrar = []
        for idx, item in enumerate(st.session_state.cot_items):
            with st.container():
                st.markdown(f"""<div class="card" style="padding:1rem">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:.8rem">
  <div class="step-badge">{idx+1}</div>
  <span style="font-weight:600;color:#BF8BFF">Ítem {idx+1}</span>
</div>""", unsafe_allow_html=True)
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.session_state.cot_items[idx]["nombre"] = st.text_input(
                        "¿Qué es? *", value=item["nombre"],
                        placeholder="Ej: Puertas metálicas de 2m x 0.9m",
                        key=f"item_nom_{idx}")
                    st.session_state.cot_items[idx]["desc"] = st.text_input(
                        "Descripción (opcional)", value=item.get("desc", ""),
                        placeholder="Ej: Con pintura anticorrosiva y acabado negro mate",
                        key=f"item_desc_{idx}")
                with c2:
                    st.session_state.cot_items[idx]["qty"] = st.number_input(
                        "Cantidad", value=float(item["qty"]), min_value=0.1, step=1.0, key=f"item_qty_{idx}")
                    unidades = ["und", "m²", "m", "kg", "litro", "hora", "día", "mes", "servicio"]
                    idx_u = unidades.index(item.get("unidad", "und")) if item.get("unidad", "und") in unidades else 0
                    st.session_state.cot_items[idx]["unidad"] = st.selectbox("Unidad", unidades, index=idx_u, key=f"item_un_{idx}")

                st.session_state.cot_items[idx]["precio"] = st.number_input(
                    "Precio unitario ($COP) *", value=float(item["precio"]),
                    min_value=0.0, step=1000.0, format="%.0f", key=f"item_p_{idx}",
                    help="¿Cuánto cobras por cada uno?")

                total_item = st.session_state.cot_items[idx]["qty"] * st.session_state.cot_items[idx]["precio"]
                st.markdown(f"""<div style="text-align:right;color:#6DD5C0;font-weight:700;font-size:.95rem;margin-top:.3rem">Total: {fmt_cop(total_item)}</div>""", unsafe_allow_html=True)

                if idx > 0:
                    if st.button(f"🗑️ Quitar ítem {idx+1}", key=f"del_{idx}"):
                        items_a_borrar.append(idx)
                st.markdown("</div>", unsafe_allow_html=True)

        for i in sorted(items_a_borrar, reverse=True):
            st.session_state.cot_items.pop(i)

        if st.button("➕ Agregar otro producto o servicio"):
            st.session_state.cot_items.append({"nombre": "", "desc": "", "qty": 1, "precio": 0.0, "unidad": "und"})
            st.rerun()

    with st.expander("⚙️ Paso 4 – Detalles finales", expanded=False):
        c1, c2, c3 = st.columns(3)
        with c1:
            aplica_iva = st.checkbox("¿Incluir IVA 19%?", value=False, key="cot_iva",
                                      help="Activa esto si tu venta está gravada con IVA")
        with c2:
            reportar_dian = st.checkbox("¿Necesita factura electrónica DIAN?", value=False, key="cot_dian",
                                         help="Si tu cliente necesita factura oficial")
        with c3:
            vigencia = st.number_input("Vigencia (días)", value=15, min_value=1, max_value=90, key="cot_vigencia")

        forma_pago = st.text_input("Forma de pago", placeholder="Ej: 50% anticipo, 50% contra entrega", key="cot_fpago")
        observaciones = st.text_area("Observaciones o notas", placeholder="Ej: El precio incluye transporte dentro de la ciudad. Garantía de 1 año.", key="cot_obs", height=80)

    # Subtotal preview
    subtotal_prev = sum(i["qty"] * i["precio"] for i in st.session_state.cot_items)
    if subtotal_prev > 0:
        iva_prev = calcular_iva(subtotal_prev) if st.session_state.get("cot_iva", False) else 0
        total_prev = subtotal_prev + iva_prev
        c1, c2, c3 = st.columns(3)
        c1.metric("Subtotal", fmt_cop(subtotal_prev))
        c2.metric("IVA", fmt_cop(iva_prev))
        c3.metric("💰 Total", fmt_cop(total_prev))

    if not st.session_state.get("cot_dian", False):
        st.markdown("""
<div class="tip-box" style="border-left-color:#F7B731">
  <div class="tip-title" style="color:#F7B731">⚖️ Ventas sin factura DIAN</div>
  <p>Si no marcas factura DIAN, se genera una <strong>Orden de Compra Interna</strong>. Es válida para cobrar entre particulares. <br>Si tu cliente pide factura electrónica o si superas los topes del régimen simple, activa esa opción.</p>
</div>""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generar = st.button("🪄 ¡Generar mi Cotización!", use_container_width=True, key="btn_gen_cot")

    if generar:
        if not vend_nombre or not cli_nombre:
            st.error("⚠️ Por favor escribe tu nombre y el nombre del cliente para continuar.")
        elif not any(i["nombre"] and i["precio"] > 0 for i in st.session_state.cot_items):
            st.error("⚠️ Agrega al menos un producto o servicio con nombre y precio.")
        else:
            datos_cot = {
                "vendedor_nombre": vend_nombre, "vendedor_tel": vend_tel, "vendedor_ciudad": vend_ciudad,
                "cliente_nombre": cli_nombre, "cliente_tel": cli_tel, "cliente_ciudad": cli_ciudad,
                "items": st.session_state.cot_items, "aplica_iva": st.session_state.get("cot_iva", False),
                "reportar_dian": st.session_state.get("cot_dian", False),
                "vigencia_dias": vigencia, "forma_pago": forma_pago, "observaciones": observaciones,
            }
            html_doc = generar_cotizacion(datos_cot)
            st.session_state.doc_generado = html_doc
            st.session_state.doc_tipo = "Cotización"
            # Guardar en historial
            st.session_state.historial.insert(0, {
                "tipo": "📋 Cotización", "resumen": f"Para {cli_nombre}",
                "fecha": datetime.date.today().strftime("%d/%m/%Y"), "html": html_doc
            })
            st.success("✅ ¡Listo! Tu cotización quedó espectacular 🎉")
            st.markdown(html_doc, unsafe_allow_html=True)
            st.download_button(
                "📥 Descargar como HTML", data=f"<html><head><meta charset='UTF-8'><style>body{{font-family:sans-serif;padding:2rem;max-width:800px;margin:0 auto}}</style></head><body>{html_doc}</body></html>",
                file_name=f"cotizacion_{cli_nombre.replace(' ','_')}_{datetime.date.today()}.html",
                mime="text/html", use_container_width=True
            )

    elif st.session_state.doc_tipo == "Cotización" and st.session_state.doc_generado:
        st.markdown(st.session_state.doc_generado, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# TAB 2: RECIBO DE PAGO
# ═══════════════════════════════════════════════════════════
with tab_recibo:
    st.markdown("<div class='section-title'>Recibo de Pago</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Para cuando alguien te paga. ¡Que quede todo por escrito!</div>", unsafe_allow_html=True)

    st.markdown("""
<div class="tip-box">
  <div class="tip-title">🧑‍🏫 Profesor DIMELO dice:</div>
  <p>Un recibo de pago es la prueba de que te pagaron. Protege al que paga y al que cobra. No importa si es en efectivo, transferencia o fiado — siempre deja constancia.</p>
</div>
""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        rec_pagador = st.text_input("¿Quién pagó? *", placeholder="Nombre de quien entregó el dinero", key="rec_pagador")
        rec_valor = st.number_input("Valor pagado ($COP) *", min_value=0.0, step=1000.0, format="%.0f", key="rec_valor")
        rec_fpago = st.selectbox("Forma de pago", ["Efectivo", "Transferencia bancaria", "Nequi/Daviplata", "Cheque", "Consignación", "Otro"], key="rec_fpago")
    with c2:
        rec_recibidor = st.text_input("¿Quién recibió el dinero? *", placeholder="Tu nombre", key="rec_recibidor")
        rec_numero = st.text_input("N° de recibo", value="001", key="rec_numero")
        rec_concepto = st.text_area("¿Por qué le pagaron? *", placeholder="Ej: Pago por instalación de piso de cerámica en cocina y baño", key="rec_concepto", height=90)

    if rec_valor > 0:
        st.markdown(f"""<div class="card" style="text-align:center">
<span style="color:#8B7FA8;font-size:.9rem">Valor del recibo</span><br>
<span style="font-family:Syne,sans-serif;font-size:2rem;font-weight:800;background:linear-gradient(135deg,#9B5DE5,#BF8BFF);-webkit-background-clip:text;-webkit-text-fill-color:transparent">{fmt_cop(rec_valor)}</span>
</div>""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        gen_rec = st.button("🪄 ¡Generar Recibo!", use_container_width=True, key="btn_gen_rec")

    if gen_rec:
        if not rec_pagador or not rec_recibidor or not rec_concepto or rec_valor <= 0:
            st.error("⚠️ Por favor completa todos los campos obligatorios.")
        else:
            datos_rec = {
                "pagador": rec_pagador, "recibidor": rec_recibidor, "valor": rec_valor,
                "concepto": rec_concepto, "forma_pago": rec_fpago, "numero": rec_numero
            }
            html_doc = generar_recibo(datos_rec)
            st.session_state.historial.insert(0, {
                "tipo": "💵 Recibo", "resumen": f"De {rec_pagador} – {fmt_cop(rec_valor)}",
                "fecha": datetime.date.today().strftime("%d/%m/%Y"), "html": html_doc
            })
            st.success("✅ ¡Recibo generado! Guárdalo o compártelo por WhatsApp 📱")
            st.markdown(html_doc, unsafe_allow_html=True)
            st.download_button(
                "📥 Descargar Recibo", data=f"<html><head><meta charset='UTF-8'></head><body>{html_doc}</body></html>",
                file_name=f"recibo_{rec_pagador.replace(' ','_')}_{datetime.date.today()}.html",
                mime="text/html", use_container_width=True
            )


# ═══════════════════════════════════════════════════════════
# TAB 3: CONTRATO
# ═══════════════════════════════════════════════════════════
with tab_contrato:
    st.markdown("<div class='section-title'>Contrato de Servicios</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>El escudo legal de tu negocio. Para que lo que acuerdas de palabra, valga también en papel.</div>", unsafe_allow_html=True)

    st.markdown("""
<div class="tip-box">
  <div class="tip-title">🧑‍🏫 Profesor DIMELO dice:</div>
  <p>No importa si tu cliente es amigo o vecino — un contrato claro evita los "yo nunca dije eso". Te protege a ti y al cliente. Tiene el mismo peso legal que uno de una empresa grande.</p>
</div>
""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        cont_contratante = st.text_input("Nombre del CONTRATANTE (quien paga) *", placeholder="Ej: Juan Carlos Herrera", key="cont_contratante")
        cont_cc_cont = st.text_input("CC o NIT del contratante", placeholder="Ej: 1.234.567.890", key="cont_cc_cont")
    with c2:
        cont_contratista = st.text_input("Nombre del CONTRATISTA (tú, quien presta el servicio) *", placeholder="Ej: Electricidad Ramírez", key="cont_contratista")
        cont_cc_crat = st.text_input("Tu CC o NIT", placeholder="Ej: 9.876.543.210", key="cont_cc_crat")

    cont_objeto = st.text_area("¿Qué servicio vas a prestar? (describe bien) *",
        placeholder="Ej: Instalación eléctrica completa de una bodega de 200m², incluyendo cableado, tablero trifásico, puntos de luz y tomas corrientes según norma RETIE.",
        key="cont_objeto", height=90)

    cont_obligaciones = st.text_area("¿Cuáles son tus compromisos?",
        placeholder="Ej: Ejecutar los trabajos según las normas técnicas vigentes, utilizar materiales de primera calidad, entregar el trabajo en el plazo acordado y corregir sin costo adicional cualquier falla causada por mala instalación.",
        key="cont_obligaciones", height=90)

    c1, c2, c3 = st.columns(3)
    with c1:
        cont_valor = st.number_input("Valor total del contrato ($COP) *", min_value=0.0, step=10000.0, format="%.0f", key="cont_valor")
    with c2:
        cont_plazo = st.text_input("Plazo de ejecución *", placeholder="Ej: 15 días hábiles", key="cont_plazo")
    with c3:
        cont_penalidad = st.number_input("% penalidad por incumplimiento", value=10, min_value=0, max_value=50, key="cont_pen")

    c1, c2 = st.columns(2)
    with c1:
        cont_fpago = st.text_input("Forma de pago *", placeholder="Ej: 40% al firmar, 30% a mitad de obra, 30% al terminar", key="cont_fpago")
    with c2:
        cont_lugar = st.text_input("Lugar de ejecución", placeholder="Ej: Carrera 5 #23-40, Bello", key="cont_lugar")

    cont_ciudad = st.text_input("Ciudad del contrato", placeholder="Ej: Bello, Antioquia", key="cont_ciudad")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        gen_cont = st.button("🪄 ¡Generar Contrato!", use_container_width=True, key="btn_gen_cont")

    if gen_cont:
        if not cont_contratante or not cont_contratista or not cont_objeto or cont_valor <= 0:
            st.error("⚠️ Por favor completa los campos obligatorios (*).")
        else:
            datos_cont = {
                "contratante": cont_contratante, "cc_contratante": cont_cc_cont,
                "contratista": cont_contratista, "cc_contratista": cont_cc_crat,
                "objeto_contrato": cont_objeto, "obligaciones": cont_obligaciones,
                "valor_total": cont_valor, "plazo": cont_plazo,
                "forma_pago": cont_fpago, "lugar_ejecucion": cont_lugar,
                "ciudad": cont_ciudad, "penalidad_pct": cont_penalidad,
            }
            html_doc = generar_contrato_servicio(datos_cont)
            st.session_state.historial.insert(0, {
                "tipo": "🤝 Contrato", "resumen": f"{cont_contratista} → {cont_contratante}",
                "fecha": datetime.date.today().strftime("%d/%m/%Y"), "html": html_doc
            })
            st.success("✅ ¡Contrato listo! Imprímelo en dos copias y firmen ambas partes ✍️")
            st.markdown(html_doc, unsafe_allow_html=True)
            st.download_button(
                "📥 Descargar Contrato", data=f"<html><head><meta charset='UTF-8'></head><body>{html_doc}</body></html>",
                file_name=f"contrato_{cont_contratista.replace(' ','_')}_{datetime.date.today()}.html",
                mime="text/html", use_container_width=True
            )


# ═══════════════════════════════════════════════════════════
# TAB 4: CONSTANCIA DE TRABAJO
# ═══════════════════════════════════════════════════════════
with tab_constancia:
    st.markdown("<div class='section-title'>Constancia de Trabajo</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Para que tu empleado pueda mostrar dónde trabaja ante un banco, arriendo o trámite.</div>", unsafe_allow_html=True)

    st.markdown("""
<div class="tip-box">
  <div class="tip-title">🧑‍🏫 Profesor DIMELO dice:</div>
  <p>Cuando alguien trabaja contigo y necesita sacar crédito, arrendar un apartamento o hacer una diligencia, pide una constancia laboral. Con DIMELO la tienes en minutos.</p>
</div>
""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        cons_empleador = st.text_input("Tu nombre completo (empleador) *", placeholder="Ej: María Cecilia Torres", key="cons_empleador")
        cons_negocio = st.text_input("Nombre de tu negocio *", placeholder="Ej: Confecciones y Modas Cecilia", key="cons_negocio")
        cons_dir = st.text_input("Dirección del negocio", placeholder="Ej: Cll 45 #22-10, local 3", key="cons_dir")
    with c2:
        cons_ciudad = st.text_input("Ciudad", placeholder="Ej: Pereira, Risaralda", key="cons_ciudad")
        cons_empleado = st.text_input("Nombre del empleado *", placeholder="Ej: Pedro Andrés Ríos", key="cons_empleado")
        cons_cc = st.text_input("Cédula del empleado", placeholder="Ej: 1.092.345.678", key="cons_cc")

    c1, c2, c3 = st.columns(3)
    with c1:
        cons_cargo = st.text_input("Cargo o labor *", placeholder="Ej: Operario de costura", key="cons_cargo")
    with c2:
        cons_fecha_ini = st.text_input("Trabaja desde", placeholder="Ej: 01 de marzo de 2023", key="cons_fecha_ini")
    with c3:
        cons_salario = st.number_input("Salario mensual ($COP) *", min_value=0.0, step=10000.0, format="%.0f", key="cons_salario")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        gen_cons = st.button("🪄 ¡Generar Constancia!", use_container_width=True, key="btn_gen_cons")

    if gen_cons:
        if not cons_empleador or not cons_empleado or not cons_cargo or cons_salario <= 0:
            st.error("⚠️ Por favor completa los campos obligatorios (*).")
        else:
            datos_cons = {
                "empleador": cons_empleador, "nombre_negocio": cons_negocio,
                "direccion": cons_dir, "ciudad": cons_ciudad,
                "empleado": cons_empleado, "cc_empleado": cons_cc,
                "cargo": cons_cargo, "fecha_inicio": cons_fecha_ini, "salario": cons_salario
            }
            html_doc = generar_permiso_trabajo(datos_cons)
            st.session_state.historial.insert(0, {
                "tipo": "📄 Constancia", "resumen": f"{cons_empleado} – {cons_negocio}",
                "fecha": datetime.date.today().strftime("%d/%m/%Y"), "html": html_doc
            })
            st.success("✅ ¡Constancia lista! Fírmala y entregásela a tu empleado.")
            st.markdown(html_doc, unsafe_allow_html=True)
            st.download_button(
                "📥 Descargar Constancia",
                data=f"<html><head><meta charset='UTF-8'></head><body>{html_doc}</body></html>",
                file_name=f"constancia_{cons_empleado.replace(' ','_')}_{datetime.date.today()}.html",
                mime="text/html", use_container_width=True
            )


# ═══════════════════════════════════════════════════════════
# TAB 5: HISTORIAL
# ═══════════════════════════════════════════════════════════
with tab_historial:
    st.markdown("<div class='section-title'>Tu Historial</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Todos los documentos que has generado en esta sesión.</div>", unsafe_allow_html=True)

    if not st.session_state.historial:
        st.markdown("""
<div class="big-cta">
  <div class="icon">🗂️</div>
  <h3>Aún no tienes documentos</h3>
  <p>Cuando generes tu primera cotización, recibo o contrato, aparecerá aquí.</p>
</div>
""", unsafe_allow_html=True)
    else:
        st.markdown(f"""<div style="color:#8B7FA8;font-size:.88rem;margin-bottom:1rem">{len(st.session_state.historial)} documento(s) generado(s) hoy</div>""", unsafe_allow_html=True)
        for idx, item in enumerate(st.session_state.historial):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"""
<div class="history-item">
  <div class="history-icon">{item['tipo'].split(' ')[0]}</div>
  <div class="history-text">
    <div class="ht-title">{item['tipo'].split(' ',1)[1]} — {item['resumen']}</div>
    <div class="ht-meta">📅 {item['fecha']}</div>
  </div>
</div>""", unsafe_allow_html=True)
            with col2:
                if st.button("Ver", key=f"hist_ver_{idx}"):
                    st.markdown(item["html"], unsafe_allow_html=True)

        if st.button("🗑️ Limpiar historial", key="limpiar_hist"):
            st.session_state.historial = []
            st.rerun()


# ═══════════════════════════════════════════════════════════
# TAB 6: APRENDE
# ═══════════════════════════════════════════════════════════
with tab_aprende:
    st.markdown("<div class='section-title'>📚 Escuela DIMELO</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Aprende lo que necesitas saber para que tu negocio crezca. Sin palabras raras, sin rodeos.</div>", unsafe_allow_html=True)

    lecciones = [
        {
            "emoji": "💡", "titulo": "¿Qué es el IVA y cuándo me afecta?",
            "badge": "badge-purple", "badge_txt": "Finanzas",
            "contenido": """
**El IVA** (Impuesto al Valor Agregado) es un impuesto del **19%** que se cobra sobre la mayoría de productos y servicios en Colombia.

**¿Cuándo te afecta a ti como comerciante?**
- Si eres **responsable de IVA** (antes llamado Régimen Común): debes cobrarle el IVA a tu cliente y luego pagárselo a la DIAN.
- Si eres **no responsable de IVA** (antes llamado Régimen Simplificado): no cobras IVA, pero tampoco puedes descontarlo en tus compras.

**¿Cómo saber si eres responsable?** Generalmente si tus ingresos brutos en el año superan los **3.500 UVT** (~$162 millones en 2024), debes inscribirte como responsable.

**En lenguaje de amigos:** El IVA es plata que cobras "de paso" para el gobierno. Tú eres como el mensajero — la recoges y la entregas. Si no eres responsable, no tienes que preocuparte por eso.
"""
        },
        {
            "emoji": "📑", "titulo": "Factura electrónica: ¿la necesito?",
            "badge": "badge-yellow", "badge_txt": "Legal",
            "contenido": """
Desde 2022, **todos los comerciantes en Colombia deben emitir factura electrónica** cuando hacen ventas. Sin embargo hay excepciones y alternativas:

**Régimen Simple o No Responsable de IVA:**
- Puedes usar documentos equivalentes (tiquetes, órdenes de compra)
- Las DIMELO Órdenes de Compra Internas son válidas entre personas del sector informal

**¿Cuándo SÍ necesito factura electrónica?**
- Cuando tu cliente es empresa y pide deducir gastos ante la DIAN
- Cuando tus ingresos superan los topes del régimen simplificado
- Cuando quieres profesionalizar tu negocio y acceder a créditos empresariales

**Consejo DIMELO:** Comienza con las órdenes de compra para tus clientes del día a día, y cuando tu negocio crezca, da el paso a la factura electrónica. Hay plataformas gratuitas o muy económicas para hacerlo.
"""
        },
        {
            "emoji": "🤝", "titulo": "¿Por qué firmar contratos aunque sea con amigos?",
            "badge": "badge-green", "badge_txt": "Protección",
            "contenido": """
El refrán dice "las cuentas claras conservan las amistades". Un contrato **no es desconfianza, es respeto mutuo**.

**¿Qué pasa sin contrato?**
- El cliente dice "yo pedí esto" y tú dices "no, yo propuse esto" — y no hay forma de resolverlo
- Si no te pagan, es muy difícil cobrar por vía legal
- Si algo sale mal, no queda claro quién es responsable de qué

**¿Qué pasa con contrato?**
- Ambos saben exactamente qué se acordó
- Tienes respaldo legal para cobrar si no te pagan
- Puedes acceder a seguros, créditos y licitaciones más grandes

**En lenguaje de amigos:** Un contrato es como ponerse de acuerdo antes de arrancar para que después nadie diga "yo no dije eso". Es la herramienta que tiene el mismo escudo legal que una multinacional — y ahora tú también la tienes con DIMELO.
"""
        },
        {
            "emoji": "💳", "titulo": "Cómo calcular el precio de tu trabajo sin quedarte corto",
            "badge": "badge-purple", "badge_txt": "Finanzas",
            "contenido": """
Muchos trabajadores informales cobran por instinto y a veces salen perdiendo. Aquí la fórmula simple:

**Costo real de tu servicio =**
1. 💰 Materiales o insumos
2. ⏰ Tu tiempo (en horas × lo que vale tu hora)
3. 🚗 Transporte y gastos
4. ⚡ Herramientas o desgaste de equipos
5. 📞 Costos fijos (celular, internet, etc.)

**Ganancia mínima:** suma todo lo anterior y agrégale al menos un **30-40%** de ganancia.

**Ejemplo práctico:**
- Materiales: $150.000
- Tu tiempo (8 horas × $25.000/hora): $200.000
- Transporte: $30.000
- **Total costos: $380.000**
- **+ 35% ganancia: $513.000**
- **Precio final: $513.000**

**Truco DIMELO:** Si ya tienes un precio "de memoria", cálcula con esta fórmula para verificar. Muchas veces descubrirás que estás cobrando muy poco.
"""
        },
        {
            "emoji": "🛡️", "titulo": "Tus derechos: lo que el cliente NO puede hacerte",
            "badge": "badge-yellow", "badge_txt": "Legal",
            "contenido": """
Como prestador de servicios en Colombia, tienes derechos que muchos no conocen:

**El cliente NO puede:**
- Pedirte que empieces sin contrato o acuerdo claro y luego cambiar las condiciones
- Retenerte el pago alegando "cosas que no acordaron"
- Pedirte más trabajo del acordado sin pagar extra
- Discriminarte por tu nivel educativo, forma de hablar o tamaño de tu negocio

**Tú SÍ puedes:**
- Cobrar un anticipo antes de empezar (es tu derecho, no te da pena pedirlo)
- Parar el trabajo si no te pagan según lo acordado
- Cobrar intereses por pagos atrasados si lo pactaron en el contrato
- Presentar una queja ante la Superintendencia de Industria y Comercio si te engañan

**Recuerda:** La Ley 1480 (Estatuto del Consumidor) también te protege a ti cuando compras materiales o servicios para tu negocio.
"""
        },
    ]

    for leccion in lecciones:
        with st.expander(f"{leccion['emoji']} {leccion['titulo']}"):
            st.markdown(f"""<span class="badge {leccion['badge']}">{leccion['badge_txt']}</span>""", unsafe_allow_html=True)
            st.markdown(leccion["contenido"])

    st.markdown("""---""")
    st.markdown("""
<div style="text-align:center;padding:1.5rem">
  <div style="font-family:Syne,sans-serif;font-size:1.3rem;font-weight:700;color:#fff;margin-bottom:.5rem">¿Tienes más preguntas?</div>
  <div style="color:#8B7FA8;font-size:.92rem">En DIMELO creemos que el título más importante es el que te das tú mismo con tu esfuerzo.</div>
  <div style="font-size:1.5rem;margin-top:.5rem">🎙️</div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:2rem 0 1rem;border-top:1px solid rgba(155,93,229,0.2);margin-top:2rem">
  <div style="font-family:Syne,sans-serif;font-size:1rem;font-weight:700;background:linear-gradient(135deg,#9B5DE5,#BF8BFF);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:.3rem">DIMELO</div>
  <div style="color:#8B7FA8;font-size:.8rem">Si tú tienes el talento, DIMELO tiene las palabras.</div>
  <div style="color:#8B7FA8;font-size:.75rem;margin-top:.3rem">Hecho con ❤️ para los comerciantes de Colombia</div>
</div>
""", unsafe_allow_html=True)
