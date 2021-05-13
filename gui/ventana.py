from tkinter import *


global click

def d_nodo(event):
    global x,y
    print("click izquierdo")
    x = event.x
    y = event.y
    print("(",+x,",",+y,")")
    lienzo.create_oval(x-10,y-10,x+10,y+10,fill='black')

def d_arista(event):
    global x,y
    global click
    print("click derecho")
    if click:
        lienzo.create_line(x,y,event.x,event.y,fill='black',width=2)
        print("(",+event.x,",",+event.y,")")
        click=0
    else:
        x = event.x
        y = event.y
        print("(",+x,",",+y,")")
        click=1


click=0
ventana = Tk()
lienzo = Canvas(ventana,width=640,height=480,background='light blue')
lienzo.grid(row=0,column=0)
lienzo.bind('<Button-1>',d_nodo)
lienzo.bind('<Button-3>',d_arista)
ventana.mainloop()