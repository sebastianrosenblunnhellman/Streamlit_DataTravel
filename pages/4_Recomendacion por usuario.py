# importamos librerias
import streamlit as st
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import ast
from surprise.dump import load

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

# [codigo] RECOMENDACIONES POR USUARIO ==========================>
# Título de la aplicación
st.title('Recomendaciones personalizadas para usuarios')

# Separador
st.markdown("---")

# Ingresar el ID del usuario
user_id = st.selectbox('**Selecciona un ID de usuario:**', [str(id) for id in user_ids])

# Botón para generar recomendaciones
if st.button('Generar recomendaciones'):
    if user_id:
        st.balloons()
        top_n = 5
        recomendaciones = recomendacion_usuario(user_id, top_n)
        st.write(f'Recomendaciones para el usuario {user_id}:')
        for i, recomendacion in enumerate(recomendaciones, start=1):
            st.write(f'{i}. {recomendacion}')
    else:
        st.write('Por favor, selecciona un ID de usuario.')

# Separador
st.markdown("---")