# Importar librerías
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
import json


# Crear página
st.set_page_config(page_title="Inicio", page_icon=":globe_with_meridians:")  # Establecer el título y un icono para la página web

# Agregar un encabezado y un subencabezado a la página web
st.title("Bienvenido a Data Travel!")
st.subheader("Explora las funcionalidades de nuestra app")

# Funcion para cargar animaciones de lottie
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# animaciones
map_anim = load_lottiefile("./assets/map_anim.json")
line_chart = load_lottiefile("./assets/line_chart.json")
data_search = load_lottiefile("./assets/data_search.json")
dashboard = load_lottiefile("./assets/dashboard.json")

# Usar columnas para organizar el texto
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    En esta sección, te presentamos las funcionalidades que puedes realizar en nuestra app. La pestaña **'Recomendación Geográfica'** presenta un heatmap interactivo de las zonas mejor y peor puntuadas para el emplazamiento de un negocio en un rubro específico.

    Nuestro mapa está pensado para realizar una selección rápida, visual e intuitiva, de los lugares preferentes para emplazar un nuevo negocio.

    Sumado a esto, ofrecemos una segunda sub-sección de **'Búsqueda Detallada'** que complementa la selección anterior con una profundidad y complejidad mayor sobre las especificaciones que relacionan la zona geográfica y el la categoría de negocio específica.
    
    """)

with col2:
# Incrustar animacion de lottie
    st_lottie(
        map_anim,
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        height=None,
        width=None,
        key=None,
    )

st.markdown("---")

col3, col4 = st.columns(2)


with col3:
# Incrustar animacion de lottie
    st_lottie(
        line_chart,
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        height=None,
        width=None,
        key=None,
    )

with col4:
    st.markdown("""
    La pestaña 'prediccion del mercado' por su parte, ...
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Sed eget risus porta, tincidunt turpis at, interdum ex. 
    Nam porta auctor ex, ac euismod magna interdum eget.
    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas
    """)

st.markdown("---") 

col5, col6 = st.columns(2)

with col5:
    st.markdown("""
    En las pestañas 'recomendacion por restaurant' y 'recomendacion por usuario' nos encontramos dos modelos de recomendacion de machine learning ...
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Sed eget risus porta, tincidunt turpis at, interdum ex. 
    Nam porta auctor ex, ac euismod magna interdum eget.
    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas
    """)

with col6:
# Incrustar animacion de lottie
    st_lottie(
        data_search,
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        height=None,
        width=None,
        key=None,
    )

st.markdown("---")

st.markdown("""
    Finalmente, la pestaña 'Dashboard' presenta ...    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Sed eget risus porta, tincidunt turpis at, interdum ex. 
    Nam porta auctor ex, ac euismod magna interdum eget.
    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas
    """
    )

st_lottie(
    dashboard,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    height=None,
    width=None,
    key=None,
)