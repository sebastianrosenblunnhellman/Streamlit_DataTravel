# Importamos librerias
import streamlit as st
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import pickle
import pyperclip


# Importamos nuestra funcion de recomendación
from functions.item_item import restaurantes_similares


names = ["Bachata Rosa",
        "Esencias Cafe",
        "Le Bifteck Restaurant",
        "El Cubano Restaurant",
        "Salt & Sugar Cafe",
        "Mainstay Tavern",
        "Taco San Marcos",
        "Salty Bagel and Grill"]
# [codigo] RECOMENDACIONES POR restaurante =========================>

# Título de la aplicación
st.title('Recomendaciones personalizadas por restaurantes similares')

# Separador
st.markdown("---")

# Ingresar name del restaurante
name = st.text_input('## **Ingresa el nombre del restaurante:**')

# Botón para generar recomendaciones
if st.button('Generar recomendaciones'):
    if name and name in names:
        st.balloons()
        top_n = 5
        recomendaciones = restaurantes_similares(name, n_restaurants=top_n)
        st.write(f'Recomendaciones para el restaurante {name}:')
        for i, item_id in enumerate(recomendaciones, start=1):
            st.write(f'{i}. {item_id}')
    elif not name:
        st.write('Por favor, ingresa un nombre de restaurante.')
    elif name not in names:
        st.write('El nombre del restaurante ingresado no es válido. Por favor, ingresa un nombre de restaurante válido.')

# Separador
st.markdown("---")

# Mostrar los names de restaurantes disponibles en dos columnas
st.write('**Muestra de nombres de restaurantes:**')

col1, col2 = st.columns(2)

for idx, id in enumerate(names):
    if idx % 2 == 0:
        id_button = col1.button(f'{id}')
        if id_button:
            pyperclip.copy(str(id))
            st.info(f'Nombre de restaurante "{id}" copiado al portapapeles.')
    else:
        id_button = col2.button(f'{id}')
        if id_button:
            pyperclip.copy(str(id))
            st.info(f'Nombre de restaurante "{id}" copiado al portapapeles.')
