import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
from surprise.dump import load

def recomendacion_usuario(user_id, top_n=5):
    # Cargar el modelo entrenado desde el archivo guardado
    modelo_guardado = "models/modelo_user_item.pkl"
    loaded_model = load(modelo_guardado)[1]

    # Cargar los datos desde el archivo Parquet
    file_path = 'data/data_user_item.parquet'
    table = pq.read_table(file_path)
    reviews = table.to_pandas()

    # Crear una lista vacía para almacenar las recomendaciones
    recomendaciones = []

    # Obtener todos los ítems que el usuario aún no ha calificado
    items_no_vistos = reviews[~reviews['business_id'].isin(reviews[reviews['user_id'] == user_id]['business_id'])]['business_id'].unique()

    # Realizar predicciones para cada ítem no visto
    for item_id in items_no_vistos:
        pred = loaded_model.predict(user_id, item_id)
        recomendaciones.append(item_id)

    # Ordenar las recomendaciones en orden descendente según la calificación estimada
    recomendaciones.sort(key=lambda x: loaded_model.predict(user_id, x).est, reverse=True)

    # Devolver los top N elementos recomendados
    return recomendaciones[:top_n]