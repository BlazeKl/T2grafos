# X es el arreglo bidimensional (matriz)
# n es el largo del arreglo, matriz n*n cuadrada

def is_euleriano(x,n):
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

    contador=0
    for i in range(0,n):
        if arreglo_grados[i]%2== 0:
            contador+=1

    if contador==n:
        print("Es Euleriano")
        return True
    else:
        print("No es euleriano")
        return False