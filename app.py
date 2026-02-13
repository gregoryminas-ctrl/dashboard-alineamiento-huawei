import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Título y descripción
st.set_page_config(page_title="Radar Estratégico - Huawei",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.title("Radar Estratégico: Detección (Sensing) | Aprovechamiento (Seizing) | Configuración (Configuring)")
st.markdown("""
Dashboard ejecutiv o interactivo para supervisar la alineación entre Lógica Dominante (eficiencia y control)
y Lógica Digital (adaptabilidad y velocidad). Visualiza señales débiles, movilización de recursos y
transformación organizacional, con simulaciones de datos coherentes para la toma de decisiones.
""")

# ---------------------------
# Generación de datos simulados
# ---------------------------

np.random.seed(42)

# Periodo de simulación (años)
years = list(range(1998, 2024))

# 1) Detección (Sensing) - Indicadores de detección de tendencias y requisitos locales
# Simulación de "Índice de Inteligencia de Mercado" (0-100)
market_intel = []
# Simulación de "Tasa de Detección de Tecnologías Emergentes" (días desde tendencia a evaluación)
tech_emergence = []

for y in years:
    base = 60 + (y - 1998) * 0.8  # crecimiento suave
    # añadir ruido
    mi = min(100, max(0, base + np.random.normal(0, 6)))
    market_intel.append(mi)

    te = max(5, 120 - (y - 1998) * 2 + np.random.normal(0, 5))  # tiempo en días/hito
    tech_emergence.append(max(1, te))

sensing_df = pd.DataFrame({
    "Year": years,
    "Market_Intelligence_Index": market_intel,
    "Emerging_Tech_Detection_Time": tech_emergence
})

# 2) Seizing - Indicadores de ejecución y co-creación
# "Time-to-Market" (semana)
time_to_market = []
# "Co-creación" (% de ingresos derivados de co-creación)
co_creation = []
# "Speed to Presence in New Market" (días para establecer presencia en un mercado)
periphery_speed = []

for i, y in enumerate(years):
    # mejora gradual en TTMs
    ttm_base = 54 - (i * 0.9)  # desde 1998 hacia 2023
    ttm = max(12, ttm_base + np.random.normal(0, 2))
    time_to_market.append(ttm)

    # co-creación creciente
    cc = min(100, max(0, 20 + (i * 2.2) + np.random.normal(0, 3)))
    co_creation.append(cc)

    p_speed = 60 - (i * 0.7) + np.random.normal(0, 3)
    periphery_speed.append(max(10, p_speed))

seizing_df = pd.DataFrame({
    "Year": years,
    "Time_to_Market_weeks": time_to_market,
    "Co_creation_PercentRevenue": co_creation,
    "Periphery_Deployment_Speed_days": periphery_speed
})

# 3) Configuring - Transformación organizacional
# "Descentralización" (índice 0-100)
decentralization = []
# "Blue Army" planes ajustados (número)
blue_army_plans = []
# Simulación de "Des-rutinización" (índice 0-100 de madurez de procesos)
desrutinizacion = []

for i, y in enumerate(years):
    base_dec = 40 + i * 0.9
    dec = min(100, max(0, base_dec + np.random.normal(0, 4)))
    decentralization.append(dec)

    blue = 5 + i * 0.9 + np.random.normal(0, 1.5)
    blue_army_plans.append(max(0, round(blue)))

    rut = min(100, max(0, 20 + i * 1.2 + np.random.normal(0, 3)))
    desrutinizacion.append(rut)

config_df = pd.DataFrame({
    "Year": years,
    "Descentralization_Index": decentralization,
    "Blue_Army_Plans_Adjusted": blue_army_plans,
    "Desrutinizacion_Index": desrutinizacion
})

# KPI global (simulación de valores actuales para la última versión)
latest = {
    "Year": years[-1],
    "Market_Intelligence_Index": sensing_df.loc[sensing_df["Year"] == years[-1], "Market_Intelligence_Index"].values[0],
    "Emerging_Tech_Detection_Time": sensing_df.loc[sensing_df["Year"] == years[-1], "Emerging_Tech_Detection_Time"].values[0],
    "Time_to_Market_weeks": time_to_market[-1],
    "Co_creation_PercentRevenue": co_creation[-1],
    "Periphery_Deployment_Speed_days": periphery_speed[-1],
    "Descentralization_Index": decentralization[-1],
    "Blue_Army_Plans_Adjusted": blue_army_plans[-1],
    "Desrutinizacion_Index": desrutinizacion[-1]
}
latest_df = pd.DataFrame([latest])

# ---------------------------
# Funciones auxiliares
# ---------------------------

def w_avg(data, weights):
    return np.average(data, weights=weights)

# ---------------------------
# Layout: tres secciones principales
# ---------------------------

st.subheader("Sección 1: Sensing (Anticipación estratégica)")
st.markdown("Monitoreo de señales débiles para evitar desalineamientos y orientar I+D.")

# Gráfico de línea: Índice de Inteligencia de Mercado y Tiempo de Detección de Tecnologías Emergentes
col1, col2 = st.columns([2, 1])

with col1:
    fig_line_sensing = px.line(
        sensing_df,
        x="Year",
        y=["Market_Intelligence_Index", "Emerging_Tech_Detection_Time"],
        labels={
            "value": "Valor",
            "Year": "Año"
        },
        color_discrete_map={
            "Market_Intelligence_Index": "royalblue",
            "Emerging_Tech_Detection_Time": "orange"
        },
        title="Tendencias: Índice de Inteligencia de Mercado (línea) vs Tiempos de Detección de Tecnologías Emergentes (línea)"
    )
    fig_line_sensing.update_yaxes(title="Valor / Días")
    st.plotly_chart(fig_line_sensing, use_container_width=True)

with col2:
    # KPI destacados
    kpi1 = latest_df["Market_Intelligence_Index"].iloc<a href="" class="citation-link" target="_blank" style="vertical-align: super; font-size: 0.8em; margin-left: 3px;">[0]</a>
    kpi2 = latest_df["Emerging_Tech_Detection_Time"].iloc<a href="" class="citation-link" target="_blank" style="vertical-align: super; font-size: 0.8em; margin-left: 3px;">[0]</a>
    kpi3 = latest_df["Descentralization_Index"].iloc<a href="" class="citation-link" target="_blank" style="vertical-align: super; font-size: 0.8em; margin-left: 3px;">[0]</a>  # mostrado como referencia adicional
    st.metric(label="Índice Inteligencia de Mercado (latest)", value=f"{kpi1:.1f}")
    st.metric(label="Tiempo de Detección de Tecnologías Emergentes (latest)", value=f"{kpi2:.1f} días")
    st.metric(label="Descentralización (latest)", value=f"{kpi3:.1f}")

st.markdown("Comentario estratégico: Este panel habilita decisiones sobre qué señales débiles priorizar para roadmap de I+D y ajustes de tecnología emergente. Si el Market Intelligence es alto pero la detección de tecnologías emergentes es lenta, la Junta debe impulsar aceleradores de evaluación y prototipado rápido.")

st.markdown("---")

st.subheader("Sección 2: Seizing (Movilización y ejecución)")

st.markdown("Medición de la capacidad de convertir oportunidades en soluciones comerciales y de desplegar en nuevos mercados.")

# Gráficos: Time-to-Market y Co-creación
colA, colB = st.columns(2)

with colA:
    fig_bar_ttm = px.bar(
        seizing_df,
        x="Year",
        y="Time_to_Market_weeks",
        labels={"Time_to_Market_weeks": "Time-to-Market (semanas)", "Year": "Año"},
        title="Time-to-Market histórico (semanas)"
    )
    st.plotly_chart(fig_bar_ttm, use_container_width=True)

with colB:
    fig_bar_co = px.bar(
        seizing_df,
        x="Year",
        y="Co_creation_PercentRevenue",
        labels={"Co_creation_PercentRevenue": "Ingreso por Co-creación (%)", "Year": "Año"},
        title="Participación de ingresos por co-creación"
    )
    st.plotly_chart(fig_bar_co, use_container_width=True)

st.markdown("""
Comentario estratégico: Reducción de Time-to-Market y aumento de ingresos por soluciones co-creadas son indicadores críticos de que la organización está moviéndose hacia una ejecución ágil y orientada al cliente.
La Junta debe vigilar si estas mejoras se sostienen al incorporar alianzas y alianzas estratégicas con startups y centros de innovación.
""")

st.markdown("---")

st.subheader("Sección 3: Configuring (Transformación organizacional)")

st.markdown("Rastrea la transformación organizacional hacia descentralización y gobernanza democrática, manteniendo coherencia estratégica.")

colC, colD = st.columns(2)

with colC:
    fig_line_dec = go.Figure()
    fig_line_dec.add_trace(go.Scatter(
        x=config_df["Year"],
        y=config_df["Descentralization_Index"],
        mode="lines+markers",
        name="Descentralización",
        line=dict(color="green")
    ))
    fig_line_dec.add_trace(go.Scatter(
        x=config_df["Year"],
        y=config_df["Desrutinizacion_Index"],
        mode="lines+markers",
        name="Des-rutinización",
        line=dict(color="purple")
    ))
    fig_line_dec.update_layout(title="Descentralización y Des-rutinización a lo largo del tiempo",
                             xaxis_title="Año", yaxis_title="Índice")
    st.plotly_chart(fig_line_dec, use_container_width=True)

with colD:
    fig_bar_blue = px.bar(
        config_df,
        x="Year",
        y="Blue_Army_Plans_Adjusted",
        labels={"Blue_Army_Plans_Adjusted": "Planes de Blue Army (ajustados)", "Year": "Año"},
        title="Ajuste de planes estratégicos de la Red Army"
    )
    st.plotly_chart(fig_bar_blue, use_container_width=True)

st.markdown("""
Comentario estratégico: La gobernanza descentralizada y la reducción de cuellos de botella deben ir acompañadas de mecanismos de aprendizaje y compensaciones por innovación colaborativa. La Junta evalúa la madurez de la des-rutinización y la alfabetización digital para cuestionar recomendaciones algorítmicas cuando sea necesario.
""")

st.markdown("---")

# Indicadores clave globales (KPI ejecutivos)
st.subheader("Indicadores ejecutivos (KPIs) - en tiempo real")
kpi_cols = st.columns(3)

with kpi_cols<a href="" class="citation-link" target="_blank" style="vertical-align: super; font-size: 0.8em; margin-left: 3px;">[0]</a>:
    st.metric(label="Time-to-Market (último año)", value=f"{latest['Time_to_Market_weeks']:.1f} semanas")

with kpi_cols<a href="" class="citation-link" target="_blank" style="vertical-align: super; font-size: 0.8em; margin-left: 3px;">[1]</a>:
    st.metric(label="Inversión en I+D / Ventas (simulado ≥ 10%)", value="> 10% de ingresos")

with kpi_cols<a href="" class="citation-link" target="_blank" style="vertical-align: super; font-size: 0.8em; margin-left: 3px;">[2]</a>:
    st.metric(label="Descentralización (Índice)", value=f"{latest['Descentralization_Index']:.1f}")

st.markdown("---")

# Simulación de datos para la visualización adicional: Tendencias históricas de Talento y Gestión de Inversiones
# Histograma de Talento (46k a 81k entre 2006-2008, pero adaptado a rango 1998-2023)
talent_years = list(range(1998, 2024))
talent = []
base = 46000
for i, y in enumerate(talent_years):
    # crecimiento con estacionalidad
    growth = 0.0
    if 2006 <= y <= 2008:
        growth = (y - 2006) * 8000  # salto
    else:
        growth = (i * 1500)  # crecimiento suave
    val = base + growth + np.random.normal(0, 3000)
    talent.append(max(40000, int(val)))

talent_df = pd.DataFrame({"Year": talent_years, "Talent_International": talent})

# Gráfico: Histogram de Talento
fig_hist_talent = px.bar(
    talent_df,
    x="Year",
    y="Talent_International",
    labels={"Talent_International": "Número de talentos internacionales", "Year": "Año"},
    title="Crecimiento de talento internacional (simulado)"
)
st.plotly_chart(fig_hist_talent, use_container_width=True)

st.markdown("""
Comentario: El crecimiento del talento internacional es clave para romper la "Liability of Foreignness" y fortalecer la capacidad de ejecución global.
La visualización de distribución de talento permite verificar la diversidad y presencia en regiones claves (Europa y Latinoamérica).
""")

# Gráfico de Inversión sostenida en I+D vs Competidores (simulado)
# Generar serie de inversión como % de ingresos
years_arr = np.array(years)
r_and_d_pct = 10 + 0.1 * (years_arr - years_arr<a href="" class="citation-link" target="_blank" style="vertical-align: super; font-size: 0.8em; margin-left: 3px;">[0]</a>) + np.random.normal(0, 0.6, size=len(years_arr))
r_and_d_pct = np.clip(r_and_d_pct, 9, 13)

competitor_pct = 11 + np.random.normal(0, 0.8, size=len(years_arr))
fig_invest = go.Figure()
fig_invest.add_trace(go.Scatter(x=years_arr, y=r_and_d_pct, mode='lines', name='Huawei I+D % de Ingresos', line=dict(color='blue')))
fig_invest.add_trace(go.Scatter(x=years_arr, y=competitor_pct, mode='lines', name='Competidores', line=dict(color='gray', dash='dash')))
fig_invest.update_layout(title="Inversión en I+D como % de ingresos (simulado)",
                         xaxis_title="Año", yaxis_title="I+D / Ingresos (%)",
                         legend_title="Comparación")
st.plotly_chart(fig_invest, use_container_width=True)

st.markdown("""
Nota: Los datos son simulados con coherencia temática. Ajuste de inputs y fuentes reales debe hacerse al conectar con data lake corporativo.
""")

# Footer de interfaz
st.markdown("---")
st.markdown("Este dashboard cubre tres módulos dinámicos (Sensing, Seizing, Configuring) y está listo para desplegarse en Streamlit Cloud.")
