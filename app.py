import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Dashboard Estratégico - Huawei", layout="wide")

st.title("📊 Dashboard Ejecutivo – Pivote 1: Alineamiento Dinámico")
st.markdown("Supervisión estratégica basada en Sensing, Seizing y Configuring.")

# -----------------------------
# SIMULACIÓN DE DATOS
# -----------------------------

years = [2018, 2019, 2020, 2021, 2022, 2023]

sensing_df = pd.DataFrame({
    "Year": years,
    "Market_Intelligence_Index": [60, 65, 70, 75, 80, 85],
    "Emerging_Tech_Detection_Time": [18, 16, 14, 12, 10, 8]
})

seizing_df = pd.DataFrame({
    "Year": years,
    "Time_to_Market": [54, 50, 45, 40, 36, 30],
    "CoCreation_Index": [20, 25, 35, 45, 55, 65]
})

config_df = pd.DataFrame({
    "Year": years,
    "Decentralization_Index": [40, 45, 50, 60, 70, 80],
    "R&D_Investment_%": [10, 11, 12, 13, 14, 15]
})

# -----------------------------
# SECCIÓN 1 – SENSING
# -----------------------------

st.header("🔎 Sensing – Anticipación Estratégica")

col1, col2 = st.columns(2)

with col1:
    fig1 = px.line(sensing_df, x="Year", y="Market_Intelligence_Index",
                   title="Índice de Inteligencia de Mercado",
                   markers=True)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.line(sensing_df, x="Year", y="Emerging_Tech_Detection_Time",
                   title="Tiempo de Detección de Tecnologías Emergentes (meses)",
                   markers=True)
    st.plotly_chart(fig2, use_container_width=True)

latest_sensing = sensing_df.iloc[-1]

st.metric("Market Intelligence Index (2023)", latest_sensing["Market_Intelligence_Index"])
st.metric("Tiempo Detección Tecnología (meses)", latest_sensing["Emerging_Tech_Detection_Time"])

st.markdown("**Decisión estratégica:** Evaluar capacidad de anticipación tecnológica y alineación con mercados globales.")

# -----------------------------
# SECCIÓN 2 – SEIZING
# -----------------------------

st.header("🚀 Seizing – Ejecución y Movilización")

col3, col4 = st.columns(2)

with col3:
    fig3 = px.line(seizing_df, x="Year", y="Time_to_Market",
                   title="Reducción de Time-to-Market (semanas)",
                   markers=True)
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    fig4 = px.bar(seizing_df, x="Year", y="CoCreation_Index",
                  title="Índice de Co-Creación con Clientes")
    st.plotly_chart(fig4, use_container_width=True)

latest_seizing = seizing_df.iloc[-1]

st.metric("Time-to-Market (2023)", latest_seizing["Time_to_Market"])
st.metric("Índice Co-Creación (2023)", latest_seizing["CoCreation_Index"])

st.markdown("**Decisión estratégica:** Supervisar velocidad de ejecución y capacidad de convertir oportunidades en ventaja competitiva.")

# -----------------------------
# SECCIÓN 3 – CONFIGURING
# -----------------------------

st.header("⚙️ Configuring – Transformación Organizacional")

col5, col6 = st.columns(2)

with col5:
    fig5 = px.line(config_df, x="Year", y="Decentralization_Index",
                   title="Índice de Descentralización",
                   markers=True)
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    fig6 = px.line(config_df, x="Year", y="R&D_Investment_%",
                   title="Inversión en I+D (% de ingresos)",
                   markers=True)
    st.plotly_chart(fig6, use_container_width=True)

latest_config = config_df.iloc[-1]

st.metric("Descentralización (2023)", latest_config["Decentralization_Index"])
st.metric("Inversión I+D % (2023)", latest_config["R&D_Investment_%"])

st.markdown("**Decisión estratégica:** Asegurar coherencia organizacional mientras se otorga autonomía operativa.")

st.success("Dashboard operativo y alineado con capacidades dinámicas.")
