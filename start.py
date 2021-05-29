#librerias
import tkinter as tk
from funciones.clasegrafo import grafo

#variables
global pos_x,pos_y,click,vert,cant_v,cant_a,j,grafo_n,is_dirigido
pos_x = 0
pos_y = 0
click = 0
vert = [0 for x in range(999)]
cant_v = 0
cant_a = 0
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
    global pos_x,pos_y,j,grafo_n,is_dirigido,cant_a
    global click
    if click:
        print("insertando arista end =",+i)
        lienzo.pack()
        if is_dirigido.get():
            if i == j:
                print("bucle")
                arista = lienzo.create_line(x,y,x-25,y,x-25,y+25,x,y+25,x,y,arrow=tk.LAST,arrowshape=(16,20,6),fill='black',width=2,smooth=1)
            else:
                arista = lienzo.create_line(pos_x,pos_y,x,y,arrow=tk.LAST,arrowshape=(16,20,6),fill='black',width=2)  
            grafo_n.sum_n(1,j,i)

        else:
            if i == j:
                print("bucle")
                arista = lienzo.create_line(x,y,x-25,y,x-25,y+25,x,y+25,x,y,fill='black',width=2,smooth=1)
                grafo_n.sum_n(1,i,j)
            else:
                arista = lienzo.create_line(pos_x,pos_y,x,y,fill='black',width=2)
                grafo_n.sum_n(1,i,j)
                grafo_n.sum_n(1,j,i)

        lienzo.tag_lower(arista)
        print("(",+x,",",+y,")")
        cant_a += 1
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
    menu.title('Detalles de grafo')
    btn = tk.Button(menu,text="Salir",command=menu.destroy)
    btn.pack()
    menu.mainloop
    print("matriz de adyacencia")
    grafo_n.print_mat(cant_v)
    print("grado del grafo: ",+grafo_n.get_grado(cant_v))
    #grafo_n.get_grado(cant_v) obtiene la cantidad total grado del grafo 
    #cant_aristas = (grafo_n.get_grado(cant_v) // 2)
    print("Cantidad aristas: ",+cant_a) 
    
    

def algoritmos():
    menu = tk.Tk()
    menu.geometry('300x300')
    menu.title('Algoritmos')
    btn = tk.Button(menu,text="Salir",command=menu.destroy)
    btn.pack()
    menu.mainloop
    print("menu de algoritmos")


def limpiar_canvas():
    print("limpiar canvas")
    global pos_x,pos_y,click,vert,cant_v,cant_a,grafo_n
    lienzo.delete("all")
    pos_x=0
    pos_y=0
    z=0
    click = 0
    vert = [0 for x in range(999)]
    cant_v = 0
    cant_a = 0
    grafo_n = grafo(1000)

#inicio ventana
ventana = tk.Tk()
ventana.geometry('640x510')
ventana.title('Editor de grafos')
lienzo = tk.Canvas(ventana,width=640,height=480,background='light blue')
lienzo.place(x=0,y=0)
lienzo.bind('<Button-1>',add_nodo)
btn_1 = tk.Button(ventana,text="Detalles",command=detalles)
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