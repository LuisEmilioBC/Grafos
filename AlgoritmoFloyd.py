import numpy as np

class AlgoritmoFloyd:
    def __init__(self, mPesos) -> None:
        self.mPesos = mPesos
        
    def algoritmo_floyd(self):
        n = len(self.mPesos)
        
        mDist = np.array(self.mPesos, copy=True, dtype=float)
        mDist[mDist == 0] = float('inf')
        np.fill_diagonal(mDist, 0)
        
        mPredecesores = np.zeros((n, n), dtype=int)
        for i in range(n):
            for j in range(n):
                if self.mPesos[i][j] != 0 and i != j:
                    mPredecesores[i][j] = i
                else:
                    mPredecesores[i][j] = -1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if mDist[i][j] > mDist[i, k] + mDist[k, j]:
                        mDist[i][j] = mDist[i, k] + mDist[k, j]
                        mPredecesores[i][j] = mPredecesores[k, j]
        
        mCaminos = np.zeros((n, n), dtype=list)       
        for i in range(n):
            for j in range(n):
                mCaminos[i][j] = self.caminoR(mPredecesores, i, j)
        
        return mDist, mCaminos
    
    def caminoR(self, mCaminos, start, end):
        camino = []
        if mCaminos[start, end] == -1:
            return camino
                
        while end != start:
            camino.insert(0, end)
            end = mCaminos[start, end]
        
        camino.insert(0, start)
        return camino