import pandas as pd
import numpy as np
from collections import deque
import pyarrow.parquet as pq
import pyarrow as pa
import pickle

def restaurantes_similares(restaurant_name, n_restaurants=5):
    # Cargar el modelo desde el archivo .pkl
    path = r'models/modelo_item_item.pkl'
    with open(path, 'rb') as file:
        model = pickle.load(file)

    # Cargar los datos desde el archivo Parquet
    file_path = 'data/data_item_item.parquet'
    table = pq.read_table(file_path)
    restaurantes = table.to_pandas()

    # Crear un nuevo DataFrame con las columnas 'avg_rating' y 'num_of_reviews'
    restaurantes = restaurantes[['name', 'avg_rating', 'num_of_reviews']]

    # Obtener el índice del restaurante de entrada
    restaurant_index = restaurantes[restaurantes['name'] == restaurant_name].index[0]

    # Obtener las características del restaurante de entrada
    X = restaurantes.drop(columns=['name'])
    restaurant_features = X.iloc[restaurant_index].values.reshape(1, -1)

    # Encontrar los índices de los restaurantes más cercanos
    distances, indices = model.kneighbors(restaurant_features, n_neighbors=len(X))

    # Eliminar el índice del propio restaurante de la lista de índices similares
    similar_indices = np.delete(indices[0], 0)

    # Crear una cola con los índices similares
    queue = deque(similar_indices)

    # Seleccionar los primeros n_restaurants índices no repetidos
    selected_indices = []
    while len(selected_indices) < n_restaurants:
        index = queue.popleft()
        if index not in selected_indices:
            selected_indices.append(index)
        else:
            queue.append(index)

    # Obtener los nombres de los restaurantes similares
    similar_restaurants = restaurantes.iloc[selected_indices]['name'].tolist()

    return similar_restaurants
