from tkinter import *


global click

def d_nodo(event):
    global x,y,nodos
    print("Insertando nodo N ",+nodos)
    x = event.x
    y = event.y
    print("(",+x,",",+y,")")
    vert = lienzo.create_oval(x-10,y-10,x+10,y+10,fill='black',activeoutline='green',activewidth=3,tags=nodos)
    lienzo.tag_bind(vert,'<Button-3>',d_arista)
    nodos += 1

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

nodos=0
click=0
ventana = Tk()
lienzo = Canvas(ventana,width=640,height=480,background='light blue')
lienzo.grid(row=0,column=0)
lienzo.bind('<Button-1>',d_nodo)
ventana.mainloop()