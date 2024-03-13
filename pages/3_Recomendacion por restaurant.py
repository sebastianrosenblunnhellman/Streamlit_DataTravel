# Importamos librerias
import streamlit as st
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import pickle

st.set_page_config(page_title="Restaurant", page_icon="🍽️", layout="wide")


# Importamos nuestra funcion de recomendación
from functions.item_item import restaurantes_similares

names = ["Bachata Rosa", "Esencias Cafe", "Le Bifteck Restaurant", "El Cubano Restaurant", "Salt & Sugar Cafe", "Mainstay Tavern", "Taco San Marcos", "Salty Bagel and Grill"]

# [codigo] RECOMENDACIONES POR restaurante ==========================>
# Título de la aplicación
st.title('Recomendaciones personalizadas por restaurantes similares')

# Separador
st.markdown("---")

# Ingresar name del restaurante
name = st.selectbox('**Selecciona un restaurante:**', names)

# Botón para generar recomendaciones
if st.button('Generar recomendaciones'):
    if name:
        st.balloons()
        top_n = 5
        recomendaciones = restaurantes_similares(name, n_restaurants=top_n)
        st.write(f'Recomendaciones para el restaurante {name}:')
        for i, recomendacion in enumerate(recomendaciones, start=1):
            st.write(f'{i}. {recomendacion}')
    else:
        st.write('Por favor, selecciona un nombre de restaurante.')

# Separador
st.markdown("---")