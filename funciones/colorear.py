# x es el arreglo bidimensional (matriz)
# n es el largo del arreglo, matriz n*n cuadrada
#n es la cantidad de vertices o nodos



def l_colorear(x,n):

    mayor=0
    for i in range(0,n):
        acum=0
        for j in range(0,n):
            acum+=x[i][j]
        if acum>=mayor:
            mayor=acum    
    mayor+=1

    arreglo_grados = [0 for x in range(n)]
    arreglo_colores = [0 for x in range(mayor)]
    arreglo_final = [0 for x in range(n)]
    for i in range(0,mayor):
        arreglo_colores[i]=chr(97+i)
    for i in range(0,n):
        acum=0
        for j in range(0,n):
            acum+=x[i][j]
        arreglo_grados[i]=acum

    arreglo_final[0]='a'
    for i in range(1,n):
        cont=0
        for j in range(0,i):
            if x[i][j]==1:
                if arreglo_final[j]==arreglo_colores[cont]:
                    cont+=1
            arreglo_final[i]=arreglo_colores[cont]

    return arreglo_final
