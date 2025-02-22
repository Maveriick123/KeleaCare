import faiss
import numpy as np
"""
class FaissIndex:
    
    # dimension -> numero de elementos de cada vector manejado por el mismo índice
    def __init__(self, dimension, nlist):
        self.dimension = dimension
        # Crear un índice FAISS con búsqueda aproximada IVFFlat (Inverted File with Flat quantization)
        # Flat: los vectores dentro de cada celda se almacenan sin compresión o reducción
        # IVF: (inverted file) división de los vectores en celdas
        # nlist -> numero de particiones / celdas; más celdas -> mayor precisión
        # faiss.IndexFlatL2(dimension) ->  calcula las distancias L2 (euclidianas)
        # faiss.METRIC_L2 -> cte que indica que se usará distancias para búsqueda dentro de las celdas del índice
        self.index = faiss.IndexIVFFlat(faiss.IndexFlatL2(dimension), nlist, faiss.METRIC_L2)
    # Verificar si el índice necesita ser entrenado antes de usarlo
        if not self.index.is_trained:
            # Con el entrenamiento se crean los clusters
            print("Entrenando el índice...")
            # Para entrenar, utilizamos un conjunto de datos representativo
            # Tomaremos 1000 vectores aleatorios para el entrenamiento
            train_data = np.random.random((1000, dimension)).astype('float32')
            # Preparamos el índice para que se puedan agregar vectores y realizar búsquedas
            self.index.train(train_data) 
            print("Índice entrenado.")"""

class FaissIndex:
    def __init__(self, dimension):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)

    def add_vectors(self, vectors: np.ndarray):
        """Añadir vectores al índice"""
        if not isinstance(vectors, np.ndarray):
            raise ValueError("Los vectores deben ser un arreglo numpy")
        if vectors.shape[1] != self.dimension:
            raise ValueError(f"El tamaño del vector debe ser {self.dimension}")
        self.index.add(vectors)

    def search_vectors(self, query: np.ndarray, k: int):
        """Buscar los vectores más cercanos en el índice"""
        if query.shape[1] != self.dimension:
            raise ValueError(f"El tamaño del vector de consulta debe ser {self.dimension}")
        distances, indices = self.index.search(query, k)
        return distances, indices
