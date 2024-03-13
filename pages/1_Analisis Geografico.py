import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import pyarrow.parquet as pq
import pyarrow as pa

st.set_page_config(page_title="Heatmap Interactivo", page_icon="🔥", layout="wide")

st.header("Visualización Geográfica Rápida")  # Agrega esta línea

# Línea divisoria
st.markdown("---")

# Cargar los datos desde el archivo Parquet
file_path = 'data/heatmap.parquet'
table = pq.read_table(file_path)
reseñas = table.to_pandas()

# Group the data by category
categorias = reseñas['category'].unique()
trazas = {}

for categoria in categorias:
    # Filter the data for the current category
    data_filtrada = reseñas[reseñas['category'] == categoria]

    # Create a heatmap trace for the current category
    traza = go.Densitymapbox(
        lat=data_filtrada['latitude'],
        lon=data_filtrada['longitude'],
        z=data_filtrada['score'],
        radius=15,  # Ajusta el radio según tus necesidades
        opacity=0.6,  # Ajusta la opacidad según tus necesidades
        name=categoria
    )

    # Add the trace to the dictionary
    trazas[categoria] = traza

# Crear el mapa de calor base
fig = go.Figure()

# Agregar todas las trazas de mapa de calor al mapa
for traza in trazas.values():
    fig.add_trace(traza)

# Configurar el diseño del mapa con el mapa base de Plotly
fig.update_layout(
    mapbox_style="carto-positron",  # utilizar el mapa base de OpenStreetMap
    mapbox_center_lat=28.6305,  # centro del mapa en latitud
    mapbox_center_lon=-82.8094,  # centro del mapa en longitud
    mapbox_zoom=4,  # nivel de zoom del mapa
    coloraxis_colorbar_title="Rating",

    updatemenus=[
        dict(
            type="dropdown",
            active=0,
            buttons=[dict(label="Todas",
                          method="update",
                          args=[{"visible": [True for _ in trazas]}]),
                      *[dict(label=categoria,
                             method="update",
                             args=[{"visible": [True if traza.name == categoria else False for traza in trazas.values()]}])
                        for categoria in categorias]
                      ]
        )
    ])

# Mostrar el mapa interactivo usando Streamlit
st.plotly_chart(fig)

# Línea divisoria
st.markdown("---")


# Carga de datos
demograficos_path = r'data\data_demograficos.parquet'

table = pq.read_table(demograficos_path)
merged_data = table.to_pandas()

# Crear la aplicación de Streamlit
st.title("Comparación por categoría y condado")

# Selector de categoría
categoria_seleccionada = st.selectbox("Selecciona una categoría:", merged_data['category'].unique())

# Filtrar los condados que tienen datos disponibles para la categoría seleccionada
condados_disponibles = merged_data[merged_data['category'] == categoria_seleccionada]['county'].unique()

# Si no hay condados disponibles, mostrar un mensaje y salir del script
if len(condados_disponibles) == 0:
    st.write("No hay datos disponibles para la categoría seleccionada.")
    st.stop()

# Selector de condado 1
condado1_seleccionado = st.selectbox("Selecciona el primer condado:", condados_disponibles)

# Selector de condado 2
condado2_seleccionado = st.selectbox("Selecciona el segundo condado:", condados_disponibles)

# Filtrar datos para el primer condado
datos_condado1 = merged_data[(merged_data['category'] == categoria_seleccionada) & (merged_data['county'] == condado1_seleccionado)].iloc[0]

# Filtrar datos para el segundo condado
datos_condado2 = merged_data[(merged_data['category'] == categoria_seleccionada) & (merged_data['county'] == condado2_seleccionado)].iloc[0]

# Convertir ingreso y población a enteros
datos_condado1['income'] = int(datos_condado1['income'])
datos_condado1['population'] = int(datos_condado1['population'])
datos_condado2['income'] = int(datos_condado2['income'])
datos_condado2['population'] = int(datos_condado2['population'])

# Mostrar los resultados
st.write("Comparación para", categoria_seleccionada)
st.write("")

# Crear columnas para mostrar los datos y el gráfico
col1, col2 = st.columns(2, gap="small")

# Mostrar datos en la primera columna
with col1:
    st.header(condado1_seleccionado)
    st.write("Puntaje:", f"{datos_condado1['score']}/5")
    st.write("Ingreso:", f"{datos_condado1['income']}/5")
    st.write("Población:", f"{datos_condado1['population']}/5")

    st.header(condado2_seleccionado)
    st.write("Puntaje:", f"{datos_condado2['score']}/5")
    st.write("Ingreso:", f"{datos_condado2['income']}/5")
    st.write("Población:", f"{datos_condado2['population']}/5")

# Crear un DataFrame con los datos de los dos condados seleccionados
df = pd.DataFrame({
    'Condado': [condado1_seleccionado, condado2_seleccionado],
    'Puntaje': [datos_condado1['score'], datos_condado2['score']],
    'Ingreso': [datos_condado1['income'], datos_condado2['income']],
    'Población': [datos_condado1['population'], datos_condado2['population']]
})

# Define los colores personalizados para cada condado
colores_condados = ['#1f77b4', '#ff7f0e']

# Crear el Spider Plot con Plotly en la segunda columna
with col2:
    fig = go.Figure()

    # Agregar el primer condado con su color personalizado
    fig.add_trace(go.Scatterpolar(
        r=df.iloc[0, 1:],
        theta=df.columns[1:],
        fill='toself',
        name=condado1_seleccionado,
        line=dict(color=colores_condados[0])
    ))

    # Agregar el segundo condado con su color personalizado
    fig.add_trace(go.Scatterpolar(
        r=df.iloc[1, 1:],
        theta=df.columns[1:],
        fill='toself',
        name=condado2_seleccionado,
        line=dict(color=colores_condados[1])
    ))

    # Ajustar diseño y etiquetas
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(df.iloc[:, 1:].values.max(), df.iloc[:, 1:].values.max()) * 1.1]
            )),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="top",
            y=1.3,
            xanchor="center",
            x=0.5
        )
    )

    # Mostrar el gráfico
    st.plotly_chart(fig)