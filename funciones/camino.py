# x es el arreglo bidimensional (matriz)
# n es el largo del arreglo, matriz n*n cuadrada
#n es la cantidad de vertices o nodos
from numpy.linalg import matrix_power

def m_camino(x,n):
    arrgl = [[0 for x in range(n)] for y in range(n)]
    matc=[[0 for x in range(n)] for y in range(n)]

    for i in range(0,n):
        for j in range(0,n):
            arrgl[i][j] = x[i][j]
    
    for i in range(0,n):
        matc += matrix_power(arrgl, i)
    
    return matc
