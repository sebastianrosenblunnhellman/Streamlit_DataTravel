import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import pyarrow.parquet as pq

st.set_page_config(page_title="Mapa temporal", page_icon="🕒", layout="wide")

# Título de la página Streamlit
st.title("Visualización temporal rápida")

#Línea divisoria
st.markdown("---")

# Cargar los datos desde el archivo Parquet
file_path = 'data/data_grafico_temporal.parquet'
table = pq.read_table(file_path)
df = table.to_pandas()

# Selecciona categorías únicas
categories = df['category'].unique()

fig = go.Figure()

# Agrupa los datos por categoría
grouped = df.groupby('category')

# Inicializa las trazas visibles con la primera categoría
initial_category = categories[0]

for category, group in grouped:
    # Ordena los datos por fecha
    group = group.sort_values('date')

    # Añade los trazos (lines) al gráfico para la categoría actual
    trace_score = go.Scatter(x=group['date'], y=group['score'], name=category, line=dict(width=2, dash='solid'), visible=True if category == initial_category else False)
    trace_ema = go.Scatter(x=group['date'], y=group['ema'], name=f'EMA de {category}', line=dict(width=2, dash='dot'), visible=True if category == initial_category else False)

    fig.add_trace(trace_score)
    fig.add_trace(trace_ema)

# Establece las propiedades del gráfico
fig.update_layout(
    title=f'Score - Categoría {initial_category}',
    xaxis_title='Fecha',
    yaxis_title='Score',
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label=category, method='update', args=[{'visible': [True if category in trace.name else False for trace in fig.data]}, {'title': f"Score - Category {category}"}])
                for category in categories
            ]),
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.1,
            xanchor="left",
            y=1.2,
            yanchor="top"
        )
    ]
)

# Muestra el gráfico en Streamlit
st.plotly_chart(fig)

# Agrega el encabezado y la línea divisoria para la sección "Búsqueda Detallada"
st.header("Búsqueda Detallada")
st.markdown("---")