from tkinter import *
from random import *
from tkinter import ttk
from PIL import ImageTk,Image
from posiciones import *
from math import *
import functools
from os import  *

def getZonaByMalo(m):
    for d in zonas:
        if (m in d['enemigos']) or (m in d['enemigosR']):
            return d

def getColorDeZona(i,j):
    for d in zonas:
        if [i,j] in d['zona']:
            return d['color']

def gerEnemigosDeZona(i,j):
    for d in zonas:
        if [i,j] in d['zona']:
            return d['enemigos']
for n in invalidas:
    n[0] += 1
    n[1] += 1

#originalmente, el indice aparecia abajo y a la izquierda, para cambiarlo a algo mas legible, tuve que hacer esto para no reescribir todas las zonas
for l in zonas:
    for i in l['zona']:
        i[0] += 1
        i[1] += 1

class Mapa(Frame):
    def __init__(self, tablero):
        super().__init__()#podria usar *args pero no los necesito
        
        self.board = [ [None]*31 for _ in range(21) ]

        self.imagen = Image.open(tablero).resize( (1050, 700), Image.Resampling.LANCZOS) #LANCZOS es antialias
        self.tablero = ImageTk.PhotoImage(self.imagen)
        Label(self, image = self.tablero).grid(row=1, column=1, columnspan=30,rowspan=20)

        self.casillas()
        self.indice()


    def casillas(self):
        for i,row in enumerate(self.board):
            for j,column in enumerate(row):
                if [i,j] not in invalidas:
                    self.board[i][j] = Label(self,text='    ', bg = getColorDeZona(i,j)) #le da un color a cada zona
                    self.board[i][j].grid(row=i,column=j)
                    #self.board[i][j].bind('<Enter>',lambda e,i=i,j=j: sortArr(bolasLE, i,j, e))#distanciaBola(i,j,e)

    def indice(self):
        for i in range(20 + 1):
            self.board[i][0].destroy()
            self.board[i][0] = Label(self, text = i, bg = 'white')
            self.board[i][0].grid(row=i, column=0)

        for j in range(30 + 1):                             
            self.board[0][j].destroy()
            self.board[0][j] = Label(self, text= j, bg = 'white')
            self.board[0][j].grid(row=0, column=j)

    def recuperar(self,i,j, event,lista):
        self.m = lista[i][j].cget('text')
        k = self.m.index(']')
        str = self.m[k+2:]
        event.widget.config(text = '    ')
        lista[i][j].destroy()
        z = getZonaByMalo(str) #ASUME QUE NO HAY MALOS QUE SE REPITEN ENTRE ZONAS
        z['zona'].append([i,j])

    def spawn(self,x,y,tipo,lista):
        L = Label(self, text = tipo, bg = getColorDeZona(y,x))
        L.bind('<Button-1>',lambda e,i=y,j=x,l=lista: self.recuperar(i,j,e,l))
        L.bind('<Enter>', lambda e, i=y,j=x,l=lista: self.mostrarS(i,j,e,l))
        L.grid(row = y,column = x)

class Malos(Frame):
    def __init__(self) -> None:
        super().__init__()

        self.counterMalos = 0
        self.columns = 0
        self.malosL = [ [None]*31 for _ in range(21) ]

class Seleccion(LabelFrame):
    def __init__(self):
        super().__init__()

        self.seleccionado = Label(self, text = '')

    def actualizar(self, texto):
        self.seleccionado.config(text = texto)

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Tablero Oca')
        self.config(bg = colorFondo)

        self.width= self.winfo_screenwidth()               
        self.height= self.winfo_screenheight() 

        self.geometry("%dx%d" % (self.width, self.height))

        self.widgets()
        
    
    def widgets(self):
        self.mapa = Mapa(tablero= path.normpath(tablero))
        self.mapa.grid(row=0, column=0,rowspan=25,columnspan=10)

        self.malos = Malos()
        self.malos.grid(row=0,column=1, rowspan= 25)

        self.seleccionado = Seleccion()
        self.seleccionado.grid(row=1,column=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()