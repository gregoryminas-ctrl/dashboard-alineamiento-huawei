import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Estratégico - Huawei", layout="wide")

# ---------------------------------------------------------
# HEADER ESTRATÉGICO
# ---------------------------------------------------------

st.title("📊 Dashboard Ejecutivo – Pivote 1: Alineamiento Dinámico")

st.markdown("""
### 🎯 Objetivo del Dashboard
Supervisar la coherencia estratégica entre:
- 🔎 Sensing (Detección)
- 🚀 Seizing (Movilización)
- ⚙️ Configuring (Reconfiguración)

Este dashboard funciona como un **Radar Estratégico** para la Junta Directiva.
""")

# ---------------------------------------------------------
# SIMULACIÓN DE DATOS
# ---------------------------------------------------------

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

# ---------------------------------------------------------
# INTERACTIVIDAD – SELECCIÓN DE AÑO
# ---------------------------------------------------------

selected_year = st.selectbox("📅 Selecciona año para análisis estratégico:", years)

latest_sensing = sensing_df[sensing_df["Year"] == selected_year].iloc[0]
latest_seizing = seizing_df[seizing_df["Year"] == selected_year].iloc[0]
latest_config = config_df[config_df["Year"] == selected_year].iloc[0]

# ---------------------------------------------------------
# ÍNDICE GENERAL DE ALINEAMIENTO DINÁMICO
# ---------------------------------------------------------

alignment_index = (
    latest_sensing["Market_Intelligence_Index"] * 0.3 +
    (100 - latest_seizing["Time_to_Market"]) * 0.3 +
    latest_config["Decentralization_Index"] * 0.4
)

st.header("🧭 Índice General de Alineamiento Dinámico")

st.metric("Alineamiento Estratégico Global", round(alignment_index, 1))

# ---------------- SEMÁFORO ESTRATÉGICO ------------------

if alignment_index >= 75:
    st.success("🟢 Alineamiento estratégico sólido. La evolución digital está coherentemente orquestada.")
elif alignment_index >= 60:
    st.warning("🟡 Alineamiento moderado. Existen brechas entre capacidades dinámicas que requieren supervisión.")
else:
    st.error("🔴 Riesgo de desalineamiento estratégico. Se requiere intervención de la Junta Directiva.")

# ---------------- LECTURA EJECUTIVA ----------------------

st.markdown(f"""
### 🧠 Lectura Ejecutiva ({selected_year})

En {selected_year}, Huawei presenta un índice de alineamiento de **{round(alignment_index,1)}**.

- Sensing refleja un nivel de anticipación de **{latest_sensing["Market_Intelligence_Index"]}**.
- Seizing muestra un time-to-market de **{latest_seizing["Time_to_Market"]} semanas**.
- Configuring indica un nivel de descentralización de **{latest_config["Decentralization_Index"]}**.

La Junta debe evaluar si las tres capacidades evolucionan de forma coherente y sincronizada.
""")

st.divider()

# ---------------------------------------------------------
# SECCIÓN 1 – SENSING
# ---------------------------------------------------------

st.header("🔎 Sensing – Anticipación Estratégica")

col1, col2 = st.columns(2)

with col1:
    fig1 = px.line(sensing_df, x="Year", y="Market_Intelligence_Index",
                   title="Índice de Inteligencia de Mercado",
                   markers=True)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.line(sensing_df, x="Year", y="Emerging_Tech_Detection_Time",
                   title="Tiempo de Detección Tecnológica (meses)",
                   markers=True)
    st.plotly_chart(fig2, use_container_width=True)

st.metric("Market Intelligence Index", latest_sensing["Market_Intelligence_Index"])
st.metric("Tiempo Detección (meses)", latest_sensing["Emerging_Tech_Detection_Time"])

st.markdown("""
**Decisión estratégica:**  
Evaluar capacidad de anticipación y alineación con cambios tecnológicos globales.
""")

st.divider()

# ---------------------------------------------------------
# SECCIÓN 2 – SEIZING
# ---------------------------------------------------------

st.header("🚀 Seizing – Movilización y Ejecución")

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

st.metric("Time-to-Market", latest_seizing["Time_to_Market"])
st.metric("Índice Co-Creación", latest_seizing["CoCreation_Index"])

st.markdown("""
**Decisión estratégica:**  
Supervisar velocidad de ejecución y conversión de oportunidades en ventaja competitiva.
""")

st.divider()

# ---------------------------------------------------------
# SECCIÓN 3 – CONFIGURING
# ---------------------------------------------------------

st.header("⚙️ Configuring – Transformación Organizacional")

col5, col6 = st.columns(2)

with col5:
    fig5 = px.line(config_df, x="Year", y="Decentralization_Index",
                   title="Índice de Descentralización",
                   markers=True)
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    fig6 = px.line(config_df, x="Year", y="R&D_Investment_%",
                   title="Inversión en I+D (% ingresos)",
                   markers=True)
    st.plotly_chart(fig6, use_container_width=True)

st.metric("Descentralización", latest_config["Decentralization_Index"])
st.metric("Inversión I+D %", latest_config["R&D_Investment_%"])

st.markdown("""
**Decisión estratégica:**  
Garantizar coherencia organizacional mientras se otorga autonomía operativa.
""")

st.divider()

# ---------------------------------------------------------
# RIESGO ESTRATÉGICO SISTÉMICO
# ---------------------------------------------------------

st.header("⚠️ Riesgo Estratégico Sistémico")

st.markdown("""
- Si Sensing mejora pero Seizing no acelera → se genera brecha competitiva.
- Si Seizing avanza pero Configuring no evoluciona → aparece fricción organizacional.
- Si Configuring cambia sin Sensing sólido → se pierde foco estratégico.

La Junta debe monitorear la sincronización entre las tres capacidades dinámicas.
""")

st.success("Dashboard operativo y alineado con el marco de Evolución Digital.")
