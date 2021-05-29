# X es el arreglo bidimensional (matriz)
# n es el largo del arreglo, matriz n*n cuadrada
#n es la cantidad de vertices o nodos



def num_cromatico(x,n):
    mayor=0
    for i in range(0,n):
        acum=0
        for j in range(0,n):
            acum+=x[i][j]
        if acum>=mayor:
            mayor=acum    
    return (mayor+1)


