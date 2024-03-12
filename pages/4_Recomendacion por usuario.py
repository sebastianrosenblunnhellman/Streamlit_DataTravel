# importamos librerias
import streamlit as st
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import ast
from surprise.dump import load
import pyperclip

# Importamos nuestra funcion de recomendación
from functions.user_item import recomendacion_usuario

# Lista predeterminada de ID de usuarios a recomendar
user_ids = [
    1.1555531733618288e+20,
    1.168683985741959e+20,
    1.0898020753291964e+20,
    1.047022032410506e+20,
    1.0177046793955536e+20,
    1.123271807547656e+20,
    1.0162375103734276e+20,
    1.0910776748367553e+20
]

# [codigo] RECOMENDACIONES POR USUARIO =========================>

# Título de la aplicación
st.title('Recomendaciones personalizadas para usuarios')

# Separador
st.markdown("---")

# Ingresar el ID del usuario
user_id = st.text_input('## **Ingresa el ID del usuario:**')

# Botón para generar recomendaciones
if st.button('Generar recomendaciones'):
    if user_id and float(user_id) in user_ids:
        st.balloons()
        top_n = 5
        recomendaciones = recomendacion_usuario(user_id, top_n)
        st.write(f'Recomendaciones para el usuario {user_id}:')
        for i, item_id in enumerate(recomendaciones, start=1):
            st.write(f'{i}. {item_id}')
    elif not user_id:
        st.write('Por favor, ingresa un ID de usuario.')
    elif float(user_id) not in user_ids:
        st.write('El ID de usuario ingresado no es válido. Por favor, ingresa un ID de usuario válido.')

# Separador
st.markdown("---")

# Mostrar los IDs de usuario disponibles en dos columnas
st.write('**Muestra de IDs de usuario:**')

col1, col2 = st.columns(2)

for idx, id in enumerate(user_ids):
    if idx % 2 == 0:
        id_button = col1.button(f'{id}')
        if id_button:
            pyperclip.copy(str(id))
            st.info(f'ID "{id}" copiado al portapapeles.')
    else:
        id_button = col2.button(f'{id}')
        if id_button:
            pyperclip.copy(str(id))
            st.info(f'ID "{id}" copiado al portapapeles.')

