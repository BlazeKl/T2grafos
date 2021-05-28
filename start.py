#librerias
from tkinter import *
from funciones.grafo import grafo

#variables
global x,y,click,vert,vert_n,aux
click = 0
vert = [0 for x in range(999)]
vert_n = 0

#funciones para canvas
def add_nodo(event):
    global x,y,vert,vert_n
    print("Insertando nodo")
    print("(",+event.x,",",+event.y,")")
    vert[vert_n] = lienzo.create_oval(event.x-10,event.y-10,event.x+10,event.y+10,fill='black',activeoutline='green',activewidth=3)
    lienzo.tag_bind(vert[vert_n],'<Button-3>',lambda event,i=vert_n: add_arista(event,i))
    vert_n += 1

def add_arista(event,i):
    global x,y
    global click
    print(i)
    if click:
        print("insertando arista (end)")
        arista = lienzo.create_line(x,y,event.x,event.y,fill='black',width=2)
        lienzo.tag_lower(arista)
        print("(",+event.x,",",+event.y,")")
        click=0
    else:
        print("insertando arista (start)")
        x = event.x
        y = event.y
        print("(",+x,",",+y,")")
        click=1

def detalles():
    menu = Tk()
    menu.geometry('300x300')
    menu.title('Matriz de adyacencia')
    btn = Button(menu,text="Salir",command=menu.destroy)
    btn.pack()
    menu.mainloop
    print("funcion para mostrar matriz de adyacencia")

def algoritmos():
    menu = Tk()
    menu.geometry('300x300')
    menu.title('Algoritmos')
    btn = Button(menu,text="Salir",command=menu.destroy)
    btn.pack()
    menu.mainloop
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
ventana = Tk()
ventana.geometry('640x510')
ventana.title('Editor de grafos')
lienzo = Canvas(ventana,width=640,height=480,background='light blue')
lienzo.place(x=0,y=0)
lienzo.bind('<Button-1>',add_nodo)
lienzo.bind('<Button-2>',lambda x="all":print(x))
btn_1 = Button(ventana,text="Adyacencia",command=detalles)
btn_1.pack()
btn_1.place(x=0,y=482)
btn_2 = Button(ventana,text="Operaciones",command=algoritmos)
btn_2.pack()
btn_2.place(x=93,y=482)
ventana.mainloop()