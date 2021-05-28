#librerias
import tkinter as tk
from funciones.clasegrafo import grafo

#variables
global pos_x,pos_y,click,vert,cant_v,j,grafo_n,is_dirigido
pos_x = 0
pos_y = 0
click = 0
vert = [0 for x in range(999)]
cant_v = 0
j = 0
grafo_n = grafo(1000)

#funciones para canvas
def add_nodo(event):
    global vert,cant_v
    print("Insertando nodo")
    print("(",+event.x,",",+event.y,")")
    vert[cant_v] = lienzo.create_oval(event.x-10,event.y-10,event.x+10,event.y+10,fill='black',activeoutline='green',activewidth=3)
    lienzo.create_text(event.x-13,event.y-13,text=cant_v)
    lienzo.tag_bind(vert[cant_v],'<Button-3>',lambda event,var1 = cant_v,var2 = event.x,var3 = event.y: add_arista(event,var1,var2,var3))
    cant_v += 1

def add_arista(event,i,x,y):
    global pos_x,pos_y,j,grafo_n,is_dirigido
    global click
    if click:
        print("insertando arista end =",+i)
        lienzo.pack()
        if is_dirigido.get():
            arista = lienzo.create_line(pos_x,pos_y,x,y,arrow=tk.LAST,arrowshape=(16,20,6),fill='black',width=2)
            grafo_n.sum_n(1,j,i)
        else:
            arista = lienzo.create_line(pos_x,pos_y,x,y,fill='black',width=2)
            grafo_n.sum_n(1,i,j)
            grafo_n.sum_n(1,j,i)
        lienzo.tag_lower(arista)
        print("(",+x,",",+y,")")
        click=0
    else:
        print("insertando arista start = ",+i)
        pos_x = x
        pos_y = y
        j = i
        print("(",+pos_x,",",+pos_y,")")
        click=1

def detalles():
    menu = tk.Tk()
    menu.geometry('300x300')
    menu.title('Matriz de adyacencia')
    btn = tk.Button(menu,text="Salir",command=menu.destroy)
    btn.pack()
    menu.mainloop
    print("funcion para mostrar matriz de adyacencia")
    grafo_n.print_mat(cant_v)

def algoritmos():
    menu = tk.Tk()
    menu.geometry('300x300')
    menu.title('Algoritmos')
    btn = tk.Button(menu,text="Salir",command=menu.destroy)
    btn.pack()
    menu.mainloop
    print("funcion para mostrar menu de algoritmos")


def limpiar_canvas():
    print("limpiar canvas")
    global pos_x,pos_y,click,vert,cant_v,grafo_n
    lienzo.delete("all")
    pos_x=0
    pos_y=0
    z=0
    click = 0
    vert = [0 for x in range(999)]
    cant_v = 0
    grafo_n = grafo(1000)


#area de pruebas
#def num_reg(x):

#inicio ventana
ventana = tk.Tk()
ventana.geometry('640x510')
ventana.title('Editor de grafos')
lienzo = tk.Canvas(ventana,width=640,height=480,background='light blue')
lienzo.place(x=0,y=0)
lienzo.bind('<Button-1>',add_nodo)
#lienzo.bind('<Button-2>',limpiar_canvas)
btn_1 = tk.Button(ventana,text="Adyacencia",command=detalles)
btn_1.pack()
btn_1.place(x=0,y=482)
btn_2 = tk.Button(ventana,text="Operaciones",command=algoritmos)
btn_2.pack()
btn_2.place(x=93,y=482)
is_dirigido=tk.IntVar()
cbox_1 = tk.Checkbutton(ventana,text="Dirigido",variable=is_dirigido,onvalue=1,offvalue=0,command=limpiar_canvas,fg="green")
cbox_1.pack()
cbox_1.place(x=193,y=485)
ventana.mainloop()