#from .euleriano import is_euleriano
#from .hamiltoniano import is_hamiltoniano

class grafo:
    def __init__(self,N):
        self.N = N
        self.g_matr = [[0 for x in range(N)] for y in range(N)]

    def add_n(self,x,i,j):
        self.g_matr[i][j] = x

    def sum_n(self,x,i,j):
        self.g_matr[i][j] += x

    def get_n(self,i,j):
        return self.g_matr[i][j]

    def print_mat(self,limit):
        for i in range (0,limit):
            for j in range (0,limit):
                print(" ",+self.g_matr[i][j], end = " "),
            print("\n")
