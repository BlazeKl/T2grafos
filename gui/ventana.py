from tkinter import *

def d_nodo(event):
    print("click izquierdo")
    global x,y

def d_arista(event):
    print("click derecho")
    global x,y

ventana = Tk()
lienzo = Canvas(ventana,width=640,height=480,background='light blue')
lienzo.grid(row=0,column=0)
lienzo.bind('<Button-1>',d_nodo)
lienzo.bind('<Button-3>',d_arista)
ventana.mainloop()