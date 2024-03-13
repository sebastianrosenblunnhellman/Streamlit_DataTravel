import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import pyarrow.parquet as pq
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Mapa temporal", page_icon="🕒", layout="wide")

# Título de la página Streamlit
st.title("Visualización temporal rápida")
st.header("- Con media movil exponencial - ")

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

# Agrega el encabezado y la línea divisoria para la sección "Prediccion a 5 años"
st.markdown("---")
# Cargar los datos desde el archivo Parquet
file_path = 'data/data_grafico_temporal.parquet'
table = pq.read_table(file_path)
df = table.to_pandas()

# Ajustar un modelo de regresión para cada categoría
category_models = {}

for category, group in df.groupby('category'):
    X = group[['year', 'month']]
    y = group['score']
    model = LinearRegression()
    model.fit(X, y)
    category_models[category] = model

# Función para predecir los puntajes para los próximos 5 años
def predict_scores(category):
    model = category_models[category]
    future_years = np.arange(2022, 2027)
    future_months = np.arange(1, 13)
    predictions = []
    for year in future_years:
        for month in future_months:
            predictions.append([year, month, model.predict([[year, month]])[0]])
    return pd.DataFrame(predictions, columns=['year', 'month', 'predicted_score'])

# Crear la aplicación con Streamlit
st.title('Predicción de puntajes por categoría')
st.header("- Proyección a 5 años -")


category_list = df['category'].unique()
selected_category = st.selectbox('Selecciona una categoría', category_list)

if st.button('Predecir'):
    predictions_df = predict_scores(selected_category)
    st.write(predictions_df)