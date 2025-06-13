from sqlalchemy import create_engine
import pandas as pd
import streamlit as st
import plotly.express as px

# CONEXÃO DOCKER INTERNO: usamos o nome do container do PostgreSQL
engine = create_engine("postgresql://postgres:123456@postgres-iot:5432/iotdb")

def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

st.title("📊 Dashboard de Temperaturas IoT")

st.header("🌡️ Média de Temperatura por Dispositivo")
df_avg = load_data("avg_temp_por_dispositivo")
st.plotly_chart(px.bar(df_avg, x="device_id", y="avg_temp"))

st.header("🕓 Leituras por Hora")
df_hora = load_data("leituras_por_hora")
st.plotly_chart(px.line(df_hora, x="hora", y="contagem"))

st.header("📅 Temperaturas Máximas e Mínimas por Dia")
df_dia = load_data("temp_max_min_por_dia")
st.plotly_chart(px.line(df_dia, x="data", y=["temp_max", "temp_min"]))
