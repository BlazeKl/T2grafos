#librerias
import tkinter as tk
from funciones.clasegrafo import grafo

#variables
global pos_x, pos_y, click, vert, cant_v, cant_a, j, grafo_n,is_dirigido
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
    global vert, cant_v
    print("Insertando nodo")
    print("(",+event.x,",",+event.y,")")
    vert[cant_v] = lienzo.create_oval(event.x-10, event.y-10, event.x+10, event.y+10, fill='black', activeoutline='green', activewidth=3)
    lienzo.create_text(event.x-13, event.y-13, text=chr(97+cant_v))
    lienzo.tag_bind(vert[cant_v], '<Button-3>', lambda event, var1 = cant_v, var2 = event.x, var3 = event.y: add_arista(event,var1,var2,var3))
    cant_v += 1

def add_arista(event,i, x, y):
    global pos_x, pos_y, j, grafo_n, is_dirigido, cant_a
    global click
    if click:
        print("insertando arista end =", chr(97+i))
        lienzo.pack()
        if is_dirigido.get():
            if i == j:
                print("bucle")
                arista = lienzo.create_line(x, y, x-25, y, x-25, y+25, x, y+25, x, y, arrow=tk.LAST, arrowshape=(16,20,6), fill='black', width=2, smooth=1)
            else:
                arista = lienzo.create_line(pos_x, pos_y, x, y, arrow=tk.LAST, arrowshape=(16,20,6), fill='black', width=2)  
            grafo_n.sum_n(1,j,i)

        else:
            if i == j:
                print("bucle")
                arista = lienzo.create_line(x, y, x-25, y, x-25, y+25, x, y+25, x, y, fill='black', width=2, smooth=1)
                grafo_n.sum_n(1,i,j)
            else:
                arista = lienzo.create_line(pos_x, pos_y, x, y, fill='black', width=2)
                grafo_n.sum_n(1,i,j)
                grafo_n.sum_n(1,j,i)

        lienzo.tag_lower(arista)
        print("(",+x,",",+y,")")
        cant_a += 1
        click=0
    else:
        print("insertando arista start = ",chr(97+i))
        pos_x = x
        pos_y = y
        j = i
        print("(",+pos_x,",",+pos_y,")")
        click=1

def detalles():
    menu = tk.Tk()
    menu.geometry('300x300')
    menu.title('Detalles de grafo')
    frame1 = tk.Frame(menu) 
    frame1.pack(side="top", fill="both")
    text = tk.Label(frame1, text="Matriz de adyacencia")
    text.grid(row=0, column=0)
    frame2 = tk.Frame(menu)
    frame2.pack(side="top", fill="both") 
    for ii in range(0, cant_v+1):
        tabla = tk.Entry(frame2, width=5, bg='green', fg='white')
        tabla.grid(row=0, column=ii)
        tabla.insert(tk.END, chr(96+ii))
    for ii in range(0, cant_v+1):
        tabla = tk.Entry(frame2, width=5, bg='green', fg='white')
        tabla.grid(row=ii, column=0)
        tabla.insert(tk.END, chr(96+ii))
    for ii in range(0, cant_v):
        for jj in range(0, cant_v):
            if grafo_n.get_n(ii,jj) > 0:
                tabla = tk.Entry(frame2, width=5, bg='blue', fg='white')
            else:
                tabla = tk.Entry(frame2, width=5, bg='black', fg='white')
            tabla.grid(row=1+ii, column=1+jj)
            tabla.insert(tk.END, grafo_n.get_n(ii,jj))
    tabla = tk.Entry(frame2, width=5)
    tabla.grid(row=0, column=0)
    tabla.insert(tk.END, "M")
    frame3 = tk.Frame(menu)
    frame3.pack(side="top", fill="both")
    text = tk.Label(frame3, text="Cantidad de vertices: ")
    text.grid(row=0, column=0)
    tabla = tk.Entry(frame3, width=5, bg='black', fg='white')
    tabla.grid(row=0, column=1)
    tabla.insert(tk.END, cant_v)
    text = tk.Label(frame3, text="Cantidad de aristas: ")
    text.grid(row=1, column=0)
    tabla = tk.Entry(frame3, width=5, bg='black', fg='white')
    tabla.grid(row=1, column=1)
    tabla.insert(tk.END, cant_a)
    text = tk.Label(frame3, text="Grado del grafo: ")
    text.grid(row=2, column=0)
    tabla = tk.Entry(frame3, width=5, bg='black', fg='white')
    tabla.grid(row=2, column=1)
    tabla.insert(tk.END, grafo_n.get_grado(cant_v))
    text = tk.Label(frame3, text="Numero cromatico : ")
    text.grid(row=3, column=0)
    tabla = tk.Entry(frame3, width=5, bg='black', fg='white')
    tabla.grid(row=3, column=1)
    tabla.insert(tk.END, grafo_n.do_cromatico(cant_v))
    menu.mainloop
    grafo_n.print_mat(cant_v)
    print("grado del grafo: ", +grafo_n.get_grado(cant_v))
    print("Cantidad aristas: ", +cant_a) 
    print("Num cromatico: ", grafo_n.do_cromatico(cant_v))
    

def algoritmos():
    menu = tk.Tk()
    menu.geometry('300x300')
    menu.title('Algoritmos')
    btn = tk.Button(menu, text="Salir", command=menu.destroy)
    btn.pack()
    menu.mainloop
    print("menu de algoritmos")


def limpiar_canvas():
    print("limpiar canvas")
    global pos_x, pos_y, click, vert, cant_v, cant_a, grafo_n
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
frame_canv = tk.Frame(ventana)
frame_canv.pack(side="top", fill="both")
lienzo = tk.Canvas(frame_canv, width=640, height=480, background='light blue')
lienzo.grid(row=0, column=0)
lienzo.bind('<Button-1>', add_nodo)
frame_btn = tk.Frame(ventana)
frame_btn.pack(side="top", fill="both")
btn_1 = tk.Button(frame_btn, text="Detalles", command=detalles)
btn_1.grid(row=0, column=0)
btn_2 = tk.Button(frame_btn, text="Operaciones", command=algoritmos)
btn_2.grid(row=0, column=1)
btn_3 = tk.Button(frame_btn, text="Limpiar", command=limpiar_canvas)
btn_3.grid(row=0, column=2)
is_dirigido=tk.IntVar()
cbox_1 = tk.Checkbutton(frame_btn, text="Dirigido", variable=is_dirigido, onvalue=1, offvalue=0, command=limpiar_canvas, fg="green")
cbox_1.grid(row=0,column=3)
ventana.mainloop()