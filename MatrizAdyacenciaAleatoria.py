import numpy as np

class MatrizAdyacenciaAleatoria:
    def __init__(self, n_nodos):
        self.mAdy = np.random.randint(2, size=(n_nodos, n_nodos))
        np.fill_diagonal(self.mAdy, 0)
        self.mAdy = np.maximum(self.mAdy, self.mAdy.T)
        
    