import numpy as np

class MatrizPesosAleatoria:
    def __init__(self, mAdy) -> None:
        n = len(mAdy)
        self.mPesos = np.random.randint(1, 11, size=(n, n))
        self.mPesos = self.mPesos * mAdy
        self.mPesos = np.maximum(self.mPesos, self.mPesos.T)