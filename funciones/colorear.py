# X es el arreglo bidimensional (matriz)
# n es el largo del arreglo, matriz n*n cuadrada
#n es la cantidad de vertices o nodos



def colorear(x,n,num_crom):
    arreglo_grados = [0 for x in range(n)]
    arreglo_aux = [0 for x in range(n)]
    for i in range(0,n):
        acum=0
        for j in range(0,n):
            acum+=x[i][j]
        arreglo_grados[i]=acum
    while True:
        acum=0
        pos=0
        for i in range(0,n):
            if arreglo_grados[i]>=acum:
                acum=arreglo_grados[i]
                pos=i
        # arreglo_grados[pos]=0

        # for i in range(0,n):
        #     for j in range(0,n):
        #         for k in range(0,n):

        break
    return  pos
