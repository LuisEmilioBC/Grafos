from MatrizAdyacenciaAleatoria import MatrizAdyacenciaAleatoria
from MatrizPesosAleatoria import MatrizPesosAleatoria
from AlgoritmoFloyd import AlgoritmoFloyd
import numpy as np
import pandas as pd

n = 4
vuelos = [f"Lugar{v}" for v in range(n)]
matriz_adyacencia = MatrizAdyacenciaAleatoria(n).mAdy
matriz_pesos = MatrizPesosAleatoria(matriz_adyacencia).mPesos

matriz_distancias, matriz_caminos = AlgoritmoFloyd(matriz_pesos).algoritmo_floyd()

df_pesos = pd.DataFrame(matriz_pesos, index=vuelos, columns=vuelos)
print("Dada una matriz de pesos, se puede calcular la ruta más barata mediante el algoritmo de Floyd-Warshall\n\nMatriz de Pesos\n",df_pesos)

for i in range(n):
    for j in range(n):
        if i != j:
            if ruta := matriz_caminos[i][j]:
                print(f"La ruta más barata del Lugar{i} al Lugar{j} es: {' -> '.join(map(str, ruta))} con un precio de {matriz_distancias[i][j]}")
            else:
                print(f"No hay ruta entre Lugar{i} y Lugar{j}")
