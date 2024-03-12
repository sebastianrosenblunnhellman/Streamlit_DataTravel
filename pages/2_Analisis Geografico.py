import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import pyarrow.parquet as pq
import pyarrow as pa

st.set_page_config(page_title="Heatmap Interactivo", page_icon="🔥", layout="wide")

st.header("Visualización Geográfica Rápida")  # Agrega esta línea

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

# Agrega el encabezado y la línea divisoria para la sección "Búsqueda Detallada"
st.header("Búsqueda Detallada")
st.markdown("---")