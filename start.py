#librerias
from tkinter import *
from funciones.grafo import grafo

#funciones para canvas
def d_nodo(event):
    global x,y,nodos
    print("Insertando nodo N ",+nodos)
    x = event.x
    y = event.y
    print("(",+x,",",+y,")")
    nodos += 1
    vert = lienzo.create_oval(x-10,y-10,x+10,y+10,fill='black',activeoutline='green',activewidth=3,tags=nodos)
    lienzo.tag_bind(vert,'<Button-3>',d_arista)

def d_arista(event):
    global x,y
    global click
    if click:
        print("insertando arista (end)")
        arist = lienzo.create_line(x,y,event.x,event.y,fill='black',width=2)
        lienzo.tag_lower(arist)
        print("(",+event.x,",",+event.y,")")
        click=0
    else:
        print("insertando arista (start)")
        x = event.x
        y = event.y
        print("(",+x,",",+y,")")
        click=1

def matriz_ady():
    print("funcion para mostrar matriz de adyacencia")

def menu_algoritmos():
    print("funcion para mostrar menu de algoritmos")

#area de pruebas
global graf1
graf1 = grafo(2)
graf1.add_n(6,0,0)
graf1.add_n(3,0,1)
graf1.add_n(4,1,0)
graf1.add_n(5,1,1)
graf1.print_mat()

#inicio ventana
nodos=0
click=0
ventana = Tk()
ventana.geometry('640x510')
ventana.title('Editor de grafos')
lienzo = Canvas(ventana,width=640,height=480,background='light blue')
lienzo.place(x=0,y=0)
lienzo.bind('<Button-1>',d_nodo)
btn_1 = Button(ventana,text="Adyacencia",command=matriz_ady)
btn_1.place(x=0,y=482)
btn_2 = Button(ventana,text="Operaciones",command=menu_algoritmos)
btn_2.place(x=93,y=482)
ventana.mainloop()