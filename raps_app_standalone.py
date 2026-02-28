"""
RAPS GmbH – Dashboard Estratégico de Transformación Digital
Caso: "How RAPS Spiced Up the German Butcher's Trade"
Versión STANDALONE: datos embebidos directamente, sin archivos externos.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ─────────────────────────────────────────────────────────────────────
# 1. CONFIGURACIÓN DE PÁGINA
# ─────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="RAPS | Dashboard Estratégico",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────────────────────────────
# 2. ESTILOS CSS
# ─────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  .kpi-card {
    background: white;
    border-left: 5px solid #8B1A1A;
    border-radius: 8px;
    padding: 16px 18px;
    margin-bottom: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  }
  .kpi-value { font-size: 1.9rem; font-weight: 700; color: #2C3E50; }
  .kpi-label { font-size: 0.82rem; color: #6C757D; text-transform: uppercase; letter-spacing: 0.05em; }
  .kpi-meta  { font-size: 0.78rem; color: #6C757D; margin-top: 4px; }
  .okr-box {
    background: #FFF8F0;
    border-left: 3px solid #E67E22;
    border-radius: 4px;
    padding: 8px 12px;
    font-size: 0.80rem;
    color: #2C3E50;
    margin-top: 6px;
  }
  .section-header {
    background: linear-gradient(90deg, #8B1A1A, #2C3E50);
    color: white;
    padding: 10px 18px;
    border-radius: 6px;
    margin: 18px 0 14px 0;
    font-size: 1.05rem;
    font-weight: 600;
  }
  .badge-green  { background:#d4edda; color:#155724; border-radius:4px; padding:2px 8px; font-size:0.76rem; font-weight:600; }
  .badge-yellow { background:#fff3cd; color:#856404; border-radius:4px; padding:2px 8px; font-size:0.76rem; font-weight:600; }
  .badge-red    { background:#f8d7da; color:#721c24; border-radius:4px; padding:2px 8px; font-size:0.76rem; font-weight:600; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────
# 3. DATOS EMBEBIDOS (sin archivos externos)
# ─────────────────────────────────────────────────────────────────────
MESES = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
TRIM  = ["Q1","Q2","Q3","Q4"]

# — Usuarios mensuales
df_users = pd.DataFrame({
    "mes":                 MESES,
    "usuarios":            [1150,1310,1490,1680,1870,2060,2240,2430,2620,2800,2990,3180],
    "meta_usuarios":       [1500,1700,1900,2100,2300,2500,2700,2900,3100,3300,3500,3500],
    "mau_rate":            [52,54,55,57,58,59,61,62,63,63,64,65],
    "meta_mau":            [60]*12,
})

# — Pedidos mensuales
df_orders = pd.DataFrame({
    "mes":            MESES,
    "pedidos":        [210,265,320,380,440,490,545,600,650,695,745,800],
    "meta_pedidos":   [800]*12,
    "ticket":         [185,190,193,197,200,205,208,212,215,218,222,225],
})

# — KPIs operativos mensuales
df_kpi_m = pd.DataFrame({
    "mes":                   MESES,
    "recetas":               [310,340,365,388,405,422,440,455,468,480,490,500],
    "meta_recetas":          [500]*12,
    "sync_erp":              [52,56,60,63,66,69,72,74,76,78,80,80],
    "meta_sync":             [80]*12,
    "incidencias":           [72,75,78,80,82,84,86,87,89,90,91,92],
    "meta_incidencias":      [90]*12,
    "onboarding":            [6.5,6.0,5.5,5.1,4.8,4.5,4.2,3.9,3.7,3.5,3.3,3.0],
    "meta_onboarding":       [3.0]*12,
    "kpis_auto":             [40,50,58,65,70,75,80,85,90,95,98,100],
    "meta_kpis_auto":        [100]*12,
    "csat":                  [3.7,3.8,3.9,4.0,4.0,4.1,4.1,4.2,4.2,4.3,4.3,4.4],
    "meta_csat":             [4.2]*12,
    "labeling":              [28,30,33,36,38,40,43,45,47,49,51,53],
    "meta_labeling":         [50]*12,
    "funciones":             [1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,2.2,2.3,2.3,2.4],
    "meta_funciones":        [2.3]*12,
    "visitas_datos":         [30,35,40,44,48,52,56,60,63,66,69,72],
    "meta_visitas_datos":    [70]*12,
    "procesos_digital":      [38,42,47,52,56,60,64,67,70,72,74,76],
    "meta_procesos":         [75]*12,
})

# — KPIs estratégicos trimestrales
df_kpi_q = pd.DataFrame({
    "trim":                   TRIM,
    "pedidos_digital_pct":    [12,19,27,35],
    "meta_pedidos_digital":   [35]*4,
    "menciones":              [2,4,7,10],
    "meta_menciones":         [12]*4,
    "nps":                    [28,33,38,43],
    "meta_nps":               [45]*4,
    "empleados_formados":     [18,38,60,82],
    "meta_formados":          [80]*4,
    "churn":                  [8.5,7.2,6.1,5.3],
    "meta_churn":             [5.0]*4,
    "clientes_ticket":        [120,210,310,420],
    "meta_clientes_ticket":   [400]*4,
    "features":               [0,1,2,3],
    "meta_features":          [3]*4,
    "posiciones":             [1,2,3,4],
    "meta_posiciones":        [4]*4,
    "retencion_talento":      [100,90,87,88],
    "meta_retencion":         [85]*4,
    "mercados_int":           [0,1,2,3],
    "meta_mercados":          [3]*4,
    "reps_int":               [15,35,55,72],
    "meta_reps":              [70]*4,
})

# ─────────────────────────────────────────────────────────────────────
# 4. FUNCIONES GRÁFICAS REUTILIZABLES
# ─────────────────────────────────────────────────────────────────────
def gauge(value, target, title, suffix="", higher_better=True):
    pct = value / target * 100 if target else 0
    if higher_better:
        color = "#27AE60" if pct >= 90 else ("#E67E22" if pct >= 70 else "#8B1A1A")
    else:
        color = "#27AE60" if value <= target * 1.05 else ("#E67E22" if value <= target * 1.2 else "#8B1A1A")

    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        delta={"reference": target, "valueformat": ".1f"},
        title={"text": title, "font": {"size": 12}},
        number={"suffix": suffix},
        gauge={
            "axis": {"range": [0, target * 1.3] if higher_better else [target * 1.6, 0]},
            "bar":  {"color": color},
            "threshold": {
                "line": {"color": "#2C3E50", "width": 3},
                "thickness": 0.8,
                "value": target
            }
        }
    ))
    fig.update_layout(height=210, margin=dict(t=40, b=5, l=10, r=10))
    return fig

def line_chart(df, x, y, meta, title, y_label, color="#8B1A1A"):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df[x], y=df[y], mode="lines+markers",
        name="Real", line=dict(color=color, width=3), marker=dict(size=7)
    ))
    if meta and meta in df.columns:
        fig.add_trace(go.Scatter(
            x=df[x], y=df[meta], mode="lines",
            name="Meta", line=dict(color="#6C757D", dash="dash", width=2)
        ))
    fig.update_layout(
        title=dict(text=title, font=dict(size=13)),
        yaxis_title=y_label, height=270,
        legend=dict(orientation="h", y=-0.25),
        margin=dict(t=40, b=50, l=40, r=10),
        plot_bgcolor="white", paper_bgcolor="white"
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(gridcolor="#F0F0F0")
    return fig

def bar_chart(df, x, cols, names, title, colors=None):
    colors = colors or ["#8B1A1A","#6C757D"]
    fig = go.Figure()
    for col, name, clr in zip(cols, names, colors):
        fig.add_trace(go.Bar(x=df[x], y=df[col], name=name, marker_color=clr))
    fig.update_layout(
        title=dict(text=title, font=dict(size=13)),
        barmode="group", height=270,
        legend=dict(orientation="h", y=-0.3),
        margin=dict(t=40, b=55, l=40, r=10),
        plot_bgcolor="white", paper_bgcolor="white"
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(gridcolor="#F0F0F0")
    return fig

def okr_note(objetivo_codigo, kr_codigo, owner, texto):
    st.markdown(f"""
    <div class="okr-box">
    <strong>{objetivo_codigo} · {kr_codigo}</strong> | Owner: {owner}<br>
    📌 {texto}
    </div>""", unsafe_allow_html=True)

def section(titulo):
    st.markdown(f'<div class="section-header">{titulo}</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────
# 5. SIDEBAR
# ─────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🌿 RAPS GmbH")
    st.markdown("**Dashboard Estratégico**\n\n*Transformación Digital DeliCo*")
    st.divider()
    pagina = st.radio("Navegación", [
        "🏠 Resumen Ejecutivo",
        "⚙️ Alineamiento Dinámico",
        "💡 Liderazgo Digital",
        "🤝 Innovación Centrada en el Cliente",
    ])
    st.divider()
    st.markdown("""
    **Período:** Ene–Dic 2024
    **Cadencia:** Mensual / Trimestral
    
    **Fuentes:**
    - myRAzept (in-app)
    - SAP ERP
    - Google Analytics
    - App Stores
    """)

# ─────────────────────────────────────────────────────────────────────
# ── PÁGINA 1: RESUMEN EJECUTIVO ───────────────────────────────────────
# ─────────────────────────────────────────────────────────────────────
if pagina == "🏠 Resumen Ejecutivo":
    st.title("🌿 RAPS GmbH – Dashboard Estratégico")
    st.markdown("**Caso:** *How RAPS Spiced Up the German Butcher's Trade* &nbsp;|&nbsp; **Plataforma:** myRAzept &nbsp;|&nbsp; **Segmento:** DeliCo")
    st.divider()

    section("📊 KPIs Ejecutivos – Vista Board")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.plotly_chart(gauge(3180, 3500, "Usuarios myRAzept", " users"), use_container_width=True)
    with c2:
        st.plotly_chart(gauge(35, 35, "Pedidos vía App", "%"), use_container_width=True)
    with c3:
        st.plotly_chart(gauge(43, 45, "NPS Imagen Digital", " pts"), use_container_width=True)
    with c4:
        st.plotly_chart(gauge(5.3, 5.0, "Churn DeliCo", "%", higher_better=False), use_container_width=True)

    st.divider()
    section("📈 Tendencias Clave – 12 Meses")
    c5, c6 = st.columns(2)
    with c5:
        st.plotly_chart(line_chart(df_users, "mes", "usuarios", "meta_usuarios",
                                   "Usuarios registrados myRAzept vs Meta", "Usuarios"), use_container_width=True)
    with c6:
        st.plotly_chart(line_chart(df_orders, "mes", "pedidos", "meta_pedidos",
                                   "Pedidos mensuales via App vs Meta", "Pedidos", "#E67E22"), use_container_width=True)

    st.divider()
    section("🧭 Scorecard Estratégico – Estado de Pivotes")
    sc = pd.DataFrame({
        "Pivote":              ["Alineamiento Dinámico","Liderazgo Digital","Innovación Centrada en el Cliente"],
        "OKRs Activos":        [3, 4, 4],
        "KRs Totales":         [7, 9, 9],
        "KRs ✅ En Meta":      [4, 6, 5],
        "KRs ⚠️ En Riesgo":   [2, 2, 3],
        "KRs 🔴 Rezagados":    [1, 1, 1],
        "Estado":              ["🟡 En Riesgo","🟢 En Meta","🟡 En Riesgo"],
    })
    st.dataframe(sc, use_container_width=True, hide_index=True)

    st.divider()
    st.markdown("""
    <div style="background:#2C3E50;color:white;padding:14px 20px;border-radius:8px;font-size:0.85rem;">
    <strong>🏁 Estado de la Transformación Digital RAPS – Cierre de Período</strong><br>
    myRAzept activo · 3.180 usuarios · 800 pedidos/mes · Churn 5.3% · NPS imagen 43 pts · 3 mercados internacionales en curso
    </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────
# ── PÁGINA 2: ALINEAMIENTO DINÁMICO ──────────────────────────────────
# ─────────────────────────────────────────────────────────────────────
elif pagina == "⚙️ Alineamiento Dinámico":
    st.title("⚙️ Alineamiento Dinámico")
    st.markdown("*Integración de estrategia, procesos internos y cadena de valor en torno a la digitalización DeliCo.*")
    st.divider()

    # ── OBJ-AD-01
    section("OBJ-AD-01 | myRAzept como eje del modelo DeliCo")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.plotly_chart(gauge(35, 35, "Pedidos vía App (%)"), use_container_width=True)
        okr_note("OBJ-AD-01","KR-AD-01.1","Dir. Comercial",
                 "La migración a canal digital genera trazabilidad transaccional y reduce la fricción de pedidos analógicos (teléfono/fax).")
    with c2:
        st.plotly_chart(gauge(490, 500, "Recetas con imagen", " rec"), use_container_width=True)
        okr_note("OBJ-AD-01","KR-AD-01.2","Head of IT + Marketing",
                 "El contenido es el principal driver de retención; sin masa crítica de recetas de calidad, myRAzept pierde diferenciación frente a ERP genéricos.")
    with c3:
        st.plotly_chart(gauge(3.3, 3.0, "Onboarding (días)", " días", False), use_container_width=True)
        okr_note("OBJ-AD-01","KR-AD-01.3","Dir. de Ventas",
                 "En industrias con baja madurez digital, un onboarding largo es la primera causa de abandono; reducirlo protege la inversión en adquisición.")

    c4, c5 = st.columns(2)
    with c4:
        st.plotly_chart(line_chart(df_kpi_m, "mes", "recetas", "meta_recetas",
                                   "Recetas activas con imagen – evolución mensual", "N° Recetas"), use_container_width=True)
    with c5:
        st.plotly_chart(line_chart(df_kpi_m, "mes", "onboarding", "meta_onboarding",
                                   "Tiempo de onboarding – evolución mensual (↓ mejor)", "Días", "#E67E22"), use_container_width=True)

    # ── OBJ-AD-02
    section("OBJ-AD-02 | Alineamiento interdepartamental IT – Marketing – Ventas")
    c6, c7 = st.columns(2)
    with c6:
        st.plotly_chart(line_chart(df_kpi_m, "mes", "sync_erp", "meta_sync",
                                   "% Recetas ERP sincronizadas en myRAzept", "%"), use_container_width=True)
        okr_note("OBJ-AD-02","KR-AD-02.1","Head of IT",
                 "La calidad del ERP alimenta el etiquetado nutricional; errores generan riesgo legal para el carnicero y reputacional para RAPS.")
    with c7:
        st.plotly_chart(line_chart(df_kpi_m, "mes", "incidencias", "meta_incidencias",
                                   "% Incidencias técnicas resueltas en < 48h", "%", "#27AE60"), use_container_width=True)
        okr_note("OBJ-AD-02","KR-AD-02.3","Head of IT",
                 "La velocidad de respuesta técnica es crítica en una industria escéptica de tecnología; un soporte lento rompe la confianza digital.")

    # ── OBJ-AD-03
    section("OBJ-AD-03 | Escalamiento internacional")
    c8, c9 = st.columns(2)
    with c8:
        st.plotly_chart(bar_chart(df_kpi_q, "trim",
                                  ["mercados_int","meta_mercados"], ["Real","Meta"],
                                  "Mercados internacionales con myRAzept activo"), use_container_width=True)
        okr_note("OBJ-AD-03","KR-AD-03.1","CEO",
                 "Replicar el modelo en otros países monetiza la inversión de desarrollo ya realizada y amplía la ventaja de primer movimiento.")
    with c9:
        st.plotly_chart(bar_chart(df_kpi_q, "trim",
                                  ["reps_int","meta_reps"], ["Real","Meta"],
                                  "% Representantes internacionales capacitados en myRAzept",
                                  ["#E67E22","#6C757D"]), use_container_width=True)
        okr_note("OBJ-AD-03","KR-AD-03.2","Dir. de Ventas",
                 "El canal de ventas fue el principal driver de adopción en Alemania; sin fuerza de ventas capacitada, el escalamiento fracasa.")


# ─────────────────────────────────────────────────────────────────────
# ── PÁGINA 3: LIDERAZGO DIGITAL ───────────────────────────────────────
# ─────────────────────────────────────────────────────────────────────
elif pagina == "💡 Liderazgo Digital":
    st.title("💡 Liderazgo Digital")
    st.markdown("*Posicionamiento de RAPS como referente digital en la industria cárnica y construcción de capacidades internas.*")
    st.divider()

    # ── OBJ-LD-01
    section("OBJ-LD-01 | Imagen innovadora de RAPS ante la industria")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.plotly_chart(gauge(10, 12, "Menciones medios sector", "/año"), use_container_width=True)
        okr_note("OBJ-LD-01","KR-LD-01.1","Dir. Marketing",
                 "La visibilidad gremial construye legitimidad institucional y genera demanda orgánica de myRAzept entre carniceros no-clientes de RAPS.")
    with c2:
        st.plotly_chart(gauge(43, 45, "NPS Imagen Digital", " pts"), use_container_width=True)
        okr_note("OBJ-LD-01","KR-LD-01.2","Dir. Marketing",
                 "Un NPS alto correlaciona con menor sensibilidad al precio y mayor fidelidad; mide percepción real vs aspiracional de la marca digital.")
    with c3:
        st.plotly_chart(gauge(3, 3, "Ponencias en ferias", "/año"), use_container_width=True)
        okr_note("OBJ-LD-01","KR-LD-01.3","CEO",
                 "Las apariciones en eventos sectoriales posicionan a RAPS como referente ante reguladores, asociaciones y competidores.")

    c4, _ = st.columns([1,1])
    with c4:
        st.plotly_chart(bar_chart(df_kpi_q, "trim",
                                  ["menciones","meta_menciones"], ["Real","Meta"],
                                  "Menciones trimestrales en medios especializados"), use_container_width=True)

    # ── OBJ-LD-02
    section("OBJ-LD-02 | Capacidades digitales internas sostenibles")
    c5, c6 = st.columns(2)
    with c5:
        st.plotly_chart(bar_chart(df_kpi_q, "trim",
                                  ["empleados_formados","meta_formados"], ["Real","Meta"],
                                  "Empleados formados en competencias digitales",
                                  ["#E67E22","#6C757D"]), use_container_width=True)
        okr_note("OBJ-LD-02","KR-LD-02.1","Head of IT",
                 "La transformación sostenible requiere capacidades en las personas; sin masa crítica formada, la empresa depende indefinidamente de consultores externos.")
    with c6:
        st.plotly_chart(line_chart(df_kpi_m, "mes", "procesos_digital", "meta_procesos",
                                   "% Procesos internos digitalizados", "%", "#27AE60"), use_container_width=True)
        okr_note("OBJ-LD-02","KR-LD-02.3","Head of IT",
                 "La digitalización de procesos internos genera datos estructurados que alimentan decisiones basadas en evidencia y reduce costos operativos.")

    # ── OBJ-LD-03
    section("OBJ-LD-03 | Performance tracking digital integrado")
    c7, _ = st.columns([1,1])
    with c7:
        st.plotly_chart(line_chart(df_kpi_m, "mes", "kpis_auto", "meta_kpis_auto",
                                   "% KPIs de myRAzept reportados automáticamente", "%"), use_container_width=True)
        okr_note("OBJ-LD-03","KR-LD-03.1","Head of IT",
                 "Automatizar la recolección de datos (App Stores, Analytics, SAP) elimina latencia y sesgo; libera tiempo directivo para análisis estratégico.")

    # ── OBJ-LD-04
    section("OBJ-LD-04 | Talento digital especializado")
    c8, c9 = st.columns(2)
    with c8:
        st.plotly_chart(bar_chart(df_kpi_q, "trim",
                                  ["posiciones","meta_posiciones"], ["Real","Meta"],
                                  "Posiciones digitales especializadas cubiertas"), use_container_width=True)
        okr_note("OBJ-LD-04","KR-LD-04.1","CEO",
                 "Cubrir posiciones digitales clave es la condición habilitadora de todas las iniciativas de transformación futuras de RAPS.")
    with c9:
        st.plotly_chart(bar_chart(df_kpi_q, "trim",
                                  ["retencion_talento","meta_retencion"], ["Real","Meta"],
                                  "Tasa de retención de talento digital (%)",
                                  ["#27AE60","#6C757D"]), use_container_width=True)
        okr_note("OBJ-LD-04","KR-LD-04.2","CEO",
                 "La rotación en perfiles digitales destruye conocimiento acumulado del modelo de negocio; retener talento es más estratégico que reclutarlo.")


# ─────────────────────────────────────────────────────────────────────
# ── PÁGINA 4: INNOVACIÓN CENTRADA EN EL CLIENTE ───────────────────────
# ─────────────────────────────────────────────────────────────────────
elif pagina == "🤝 Innovación Centrada en el Cliente":
    st.title("🤝 Innovación Centrada en el Cliente")
    st.markdown("*Generación continua de valor para el carnicero como socio estratégico de RAPS.*")
    st.divider()

    # ── OBJ-IC-01
    section("OBJ-IC-01 | Escalar base de usuarios myRAzept")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.plotly_chart(gauge(3180, 3500, "Usuarios registrados", " users"), use_container_width=True)
        okr_note("OBJ-IC-01","KR-IC-01.1","Dir. Ventas",
                 "3.500 usuarios (≈35% del mercado alemán) consolida el efecto red y hace la ventaja competitiva difícilmente replicable.")
    with c2:
        st.plotly_chart(gauge(65, 60, "MAU Rate", "%"), use_container_width=True)
        okr_note("OBJ-IC-01","KR-IC-01.2","Dir. Marketing",
                 "El MAU rate mide si la propuesta de valor es relevante para el uso habitual del carnicero, no solo para el registro inicial.")
    with c3:
        st.plotly_chart(gauge(800, 800, "Pedidos vía App/mes", " ped"), use_container_width=True)
        okr_note("OBJ-IC-01","KR-IC-01.3","Dir. Comercial",
                 "Los pedidos via app crean revenue digital directamente atribuible a myRAzept; justifican la inversión ante el Board con datos concretos.")

    c4, c5 = st.columns(2)
    with c4:
        st.plotly_chart(line_chart(df_users, "mes", "usuarios", "meta_usuarios",
                                   "Crecimiento de usuarios registrados myRAzept", "Usuarios"), use_container_width=True)
    with c5:
        st.plotly_chart(line_chart(df_users, "mes", "mau_rate", "meta_mau",
                                   "MAU Rate mensual – % usuarios activos", "%", "#E67E22"), use_container_width=True)

    # ── OBJ-IC-02
    section("OBJ-IC-02 | Profundidad de uso en la operación del carnicero")
    c6, c7, c8 = st.columns(3)
    with c6:
        st.plotly_chart(gauge(53, 50, "Uso semanal etiquetado", "%"), use_container_width=True)
        okr_note("OBJ-IC-02","KR-IC-02.1","Dir. Marketing",
                 "El uso frecuente de etiquetado evidencia que RAPS está resolviendo el problema de compliance más urgente y costoso del sector.")
    with c7:
        st.plotly_chart(gauge(2.4, 2.3, "Funciones activas/usuario", ""), use_container_width=True)
        okr_note("OBJ-IC-02","KR-IC-02.2","Head of IT",
                 "Usar múltiples funciones aumenta el switching cost; convierte myRAzept en infraestructura operativa del carnicero, no solo en consulta.")
    with c8:
        st.plotly_chart(gauge(4.4, 4.2, "CSAT in-app", "/5"), use_container_width=True)
        okr_note("OBJ-IC-02","KR-IC-02.3","Dir. Marketing",
                 "Un CSAT alto en industria analógica prueba que RAPS transfirió exitosamente su reputación de calidad física al canal digital.")

    c9, c10 = st.columns(2)
    with c9:
        st.plotly_chart(line_chart(df_kpi_m, "mes", "labeling", "meta_labeling",
                                   "% usuarios con uso semanal de etiquetado nutricional", "%"), use_container_width=True)
    with c10:
        st.plotly_chart(line_chart(df_kpi_m, "mes", "funciones", "meta_funciones",
                                   "Promedio de funciones activas por usuario", "Funciones", "#27AE60"), use_container_width=True)

    # ── OBJ-IC-03
    section("OBJ-IC-03 | Vínculo relacional carnicero – representante RAPS")
    c11, c12 = st.columns(2)
    with c11:
        st.plotly_chart(line_chart(df_kpi_m, "mes", "visitas_datos", "meta_visitas_datos",
                                   "% visitas de ventas preparadas con datos de myRAzept", "%", "#8B1A1A"), use_container_width=True)
        okr_note("OBJ-IC-03","KR-IC-03.1","Dir. Ventas",
                 "Un representante con datos del carnicero convierte la visita en consultoría de valor; digitaliza la relación sin reemplazar el vínculo personal.")
    with c12:
        st.plotly_chart(bar_chart(df_kpi_q, "trim",
                                  ["clientes_ticket","meta_clientes_ticket"], ["Real","Meta"],
                                  "Clientes DeliCo con ticket incrementado post-adopción",
                                  ["#E67E22","#6C757D"]), use_container_width=True)
        okr_note("OBJ-IC-03","KR-IC-03.3","Dir. Comercial",
                 "El incremento de ticket en usuarios de myRAzept es la prueba de ROI definitiva: el canal digital amplifica ventas físicas sin canibalizarlas.")

    # ── OBJ-IC-04
    section("OBJ-IC-04 | Innovación continua basada en feedback del carnicero")
    c13, _ = st.columns([1,1])
    with c13:
        st.plotly_chart(bar_chart(df_kpi_q, "trim",
                                  ["features","meta_features"], ["Lanzadas","Meta"],
                                  "Nuevas funcionalidades lanzadas por trimestre (feedback documentado)"), use_container_width=True)
        okr_note("OBJ-IC-04","KR-IC-04.1","Dir. Marketing + Head of IT",
                 "Mantener el ciclo de innovación centrado en el usuario garantiza que myRAzept evolucione con las necesidades del sector y no quede obsoleto.")

    st.divider()
    st.markdown("""
    <div style="background:#2C3E50;color:white;padding:14px 20px;border-radius:8px;font-size:0.85rem;">
    <strong>🏁 Cierre de Período – Innovación Centrada en el Cliente</strong><br>
    Usuarios: 3.180 / 3.500 meta &nbsp;·&nbsp; MAU Rate: 65% ✅ &nbsp;·&nbsp; CSAT: 4.4/5 ✅ &nbsp;·&nbsp;
    Labeling semanal: 53% ✅ &nbsp;·&nbsp; Funciones promedio: 2.4 ✅ &nbsp;·&nbsp; Churn: 5.3% (meta 5.0% ⚠️)
    </div>""", unsafe_allow_html=True)
