import random
#d=4;
#r1=1;
#r2=4;
#a=[[0 for x in range(d)] for y in range(d)]
#
#for i in range (0,d):
#    for j in range (0,d):
#        print("Ingrese el valor",chr(97+i),",",chr(97+j))
#        a[i][j]=int(input())
#        a[i][j]=int(random.randint(r1,r2))
#                
#print("Matriz A= ",a)

class grafo:
    def __init__(self,N):
        self.N = N
        self.g_matr = [[0 for x in range(N)] for y in range(N)]

    def add_n(self,x,i,j):
        self.g_matr[i][j] = x

    def get_n(self,i,j):
        return self.g_matr[i][j]
