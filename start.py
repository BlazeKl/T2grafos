#librerias
from tkinter import *
from funciones.clasegrafo import grafo

#variables
global x,y,click,vert,i,grafo_n
x=0
y=0
z=0
click = 0
vert = [0 for x in range(999)]
i = 0
grafo_n = grafo(1000)

#funciones para canvas
def add_nodo(event):
    global vert,i
    print("Insertando nodo")
    print("(",+event.x,",",+event.y,")")
    vert[i] = lienzo.create_oval(event.x-10,event.y-10,event.x+10,event.y+10,fill='black',activeoutline='green',activewidth=3)
    lienzo.create_text(event.x-13,event.y-13,text=i)
    lienzo.tag_bind(vert[i],'<Button-3>',lambda event,x=i: add_arista(event,x))
    i += 1

def add_arista(event,i):
    global x,y,z,grafo_n
    global click
    if click:
        print("insertando arista end =",+i)
        arista = lienzo.create_line(x,y,event.x,event.y,fill='black',width=2)
        lienzo.tag_lower(arista)
        print("(",+event.x,",",+event.y,")")
        grafo_n.sum_n(1,i,z)
        grafo_n.sum_n(1,z,i)
        click=0
    else:
        print("insertando arista start = ",+i)
        x = event.x
        y = event.y
        z = i
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
    grafo_n.print_mat(i)

def algoritmos():
    menu = Tk()
    menu.geometry('300x300')
    menu.title('Algoritmos')
    btn = Button(menu,text="Salir",command=menu.destroy)
    btn.pack()
    menu.mainloop
    print("funcion para mostrar menu de algoritmos")


def limpiar_canvas(event):
    print("limpiar canvas")
    global x,y,click,vert,i,grafo_n
    lienzo.delete("all")
    x=0
    y=0
    z=0
    click = 0
    vert = [0 for x in range(999)]
    i = 0
    grafo_n = grafo(1000)


#area de pruebas
#def num_reg(x):

#inicio ventana
ventana = Tk()
ventana.geometry('640x510')
ventana.title('Editor de grafos')
lienzo = Canvas(ventana,width=640,height=480,background='light blue')
lienzo.place(x=0,y=0)
lienzo.bind('<Button-1>',add_nodo)
lienzo.bind('<Button-2>',limpiar_canvas)
btn_1 = Button(ventana,text="Adyacencia",command=detalles)
btn_1.pack()
btn_1.place(x=0,y=482)
btn_2 = Button(ventana,text="Operaciones",command=algoritmos)
btn_2.pack()
btn_2.place(x=93,y=482)
ventana.mainloop()