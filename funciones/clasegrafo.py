from .euleriano import is_euleriano
from .hamiltoniano import is_hamiltoniano
from .gradosaristas import gradosgrafo
from .numcromatico import num_cromatico
from .colorear import l_colorear

class grafo:
    def __init__(self,N):
        self.N = N
        self.g_matr = [[0 for x in range(N)] for y in range(N)]

    def set_n(self,x,i,j):
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

    def get_grado(self,limit):
        res = gradosgrafo(self.g_matr,limit)
        return res

    def do_cromatico(self,limit):
        res = num_cromatico(self.g_matr,limit)
        return res

    def do_colorear(self,limit):
        res = l_colorear(self.g_matr,limit)
        return res

