import streamlit as st
import streamlit.components.v1 as components

# Make page
st.set_page_config(page_title="Dashboard 📊", page_icon="📊", layout="wide")

# Agrega un encabezado personalizado con CSS
st.markdown("""
<style>
.reportViewContainer .main .page {
    background-color: #F5F8FF;
}
</style>
""", unsafe_allow_html=True)

st.subheader(":bar_chart: Dashboard")
st.markdown("Explore los datos de forma interactiva con nuestro dashboard para entender las relaciones entre las variables. ")

# Código HTML de incrustación
looker_html = """
<iframe width="800" height="600" src="https://lookerstudio.google.com/embed/reporting/bc3ded4c-b5f9-4a5c-91cd-57743a9f63a1/page/p_m9yu4vd8ed" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>
"""
# Incrustar el código HTML en Streamlit
components.html(looker_html, height=600, width=800)
