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
En esta sección, te presentamos las funcionalidades que puedes realizar en nuestra app.

La pestaña **'Análisis Geográfico'** presenta un heatmap interactivo de las zonas con mejor y peor 'score' por categoría de negocio.

Una vez visualizados los mejores lugares para determinada categoría, se puede realizar una comparativa entre condados.

Dicha comparativa añade indicadores demográficos al análisis.
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

La pestaña **'Análisis Temporal'**, por su parte, permite visualizar las tendencias por categoría de negocio a lo largo de los años y los meses.

Estos datos se disponibilizan a través de un gráfico de líneas interactivo que añade la media móvil exponencial para evidenciar la tendencia del mercado.

Posteriormente se pueden realizar predicciones del puntaje por categoría con una proyección a 5 años, mes a mes, utilizando regresión lineal.
    """)

st.markdown("---") 

col5, col6 = st.columns(2)

with col5:
    st.markdown("""
    En las pestañas 'recomendacion por restaurant' y 'recomendacion por usuario' nos encontramos dos modelos de recomendacion de machine learning.

    El primero pondera caractiristicas intrinsecas de restaurantes de florida para recomendar 5 restaurantes similares al ingresado como argumento.

    Por otro lado, el segundo modelo se encarga de recomendar restaurantes en base a las preferencias de los usuarios.
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
    Finalmente, la pestaña 'Dashboard' presenta una visualizacion de los datos de completamente interantiva.

    Esto permite comprender mejor las relaciones entre las variables, entre las partes y el todo, aportar una mejor comprensión de los datos.
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

st.markdown("---")

st.markdown("""
    Para observar la estructura del proyecto en su conjunto, puede usted acceder al [repositorio de GitHub](https://github.com/Nazario3482/Proyecto-Grupal-Google-yelp) del mismo.
    """
    )


