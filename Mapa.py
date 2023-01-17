from tkinter import *
from random import *
from tkinter import ttk
from PIL import ImageTk,Image
from posiciones import *
from math import *
import functools

#file con datos y funciones relacionadas con el tablero

board = [ [None]*31 for _ in range(21) ]

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

#Arreglo
for n in invalidas:
    n[0] += 1
    n[1] += 1
#originalmente, el indice aparecia abajo y a la izquierda, para cambiarlo a algo mas legible, tuve que hacer esto para no reescribir todas las zonas
for l in zonas:
    for i in l['zona']:
        i[0] += 1
        i[1] += 1

#Crea la ventana, le pone un nombre y define su tamaño
root = Tk()
root.title('Tablero Oca')
root.config(bg = colorFondo)
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
root.geometry("%dx%d" % (width, height))

#señala en el frame de seleccion que se acaba de pasar por encima el mouse
def mostrarS(i,j,e):
    global m
    if malosL[i][j] != None:
        m.config(text = str(malosL[i][j].cget('text')))
        return 
    
    m.config(text = str([j,i]))




def sortFunction(a, b):  #es la sort default pero adaptado a listas
    if (a[0] == b[0]):
        return 0

    else :
        if (a[0] < b[0]):
            return -1
    return 1
#hice un desastre con esta funcion, funciona, pero que asco
def sortArr(arr, i, j, e):
    arr = bolasLE

    vp = [0 for _ in range(len(arr))]
    
    for m in range(len(arr)):
        if arr[m] != None:
            dist = abs((i - arr[m][0])) + abs((j - arr[m][1])); #distancia en casillas a moverse de forma rectilinea minimas hasta la esfera
            vp[m] = [dist, [arr[m][0], arr[m][1]]]       #[ [d, [y,x]],...]
        else:
            dist = 100
            vp[m] = [dist, [bolasL[m][0], bolasL[m][1]]]

    vp.sort(key=functools.cmp_to_key(sortFunction))

    b.config(text = str(vp[0][0]))                      #sortea las distancias de las bolas, y muetra la distancia mas baja
    
    if not mostrar:
        L.grid(row= vp[0][1][0], column = vp[0][1][1])

    if mostrarNumeroBola:
        L.config(text = str(bolasL.index(vp[0][1])+1))


#Summonea la imagen del tablero y le cambia el tamaño a 1050 x 700 (ratio 2/3)
imagen = Image.open(tablero).resize((1050, 700), Image.Resampling.LANCZOS) #LANCZOS es antialias
Tablero = ImageTk.PhotoImage(imagen)


#Crea un Frame para el mapa
frm = ttk.LabelFrame(root, padding=0, text='Mapa')
frm.place(x=10,y=1)


#Muestra la imagen de fondo como guia, le da 30 columnas y 20 filas para acomodar los tiles
Label(frm, image = Tablero).grid(row=1, column=1, columnspan=30,rowspan=20) 


#Crea casillas de colores para representar cada tile
for i,row in enumerate(board):
    for j,column in enumerate(row):
        if [i,j] not in invalidas:
            board[i][j] = Label(frm,text='    ', bg = getColorDeZona(i,j)) #le da un color a cada zona
            board[i][j].grid(row=i,column=j)
            board[i][j].bind('<Enter>',lambda e,i=i,j=j: [sortArr(bolasLE, i,j, e), mostrarS(i,j,e)] )



#Indice
for i in range(20 + 1):
    board[i][0].destroy()
    board[i][0] = Label(frm, text = i, bg = 'white')
    board[i][0].grid(row=i, column=0)

for j in range(30 + 1):                             
    board[0][j].destroy()
    board[0][j] = Label(frm, text= j, bg = 'white')
    board[0][j].grid(row=0, column=j)


def recuperar(i,j, event):
    m = malosL[i][j].cget('text')
    k = m.index(']')
    m = m[k+2:]
    event.widget.config(text = '    ')
    malosL[i][j].destroy()
    z = getZonaByMalo(m) #ASUME QUE NO HAY MALOS QUE SE REPITEN ENTRE ZONAS
    z['zona'].append([i,j])



#MALOS
counterMalos = 0
c = 0
malosL = [ [None]*31 for _ in range(21) ]

#funcion para facilitar lectura, muestra la posicion de un malo y su tipo en el mapa, y el nombre y coordenadas en la lista, ahora bindea eventos tambien
def spawn(tipo, list, x, y):
    L = Label(frm, text = tipo, bg = getColorDeZona(y,x))
    L.bind('<Button-1>',lambda e,i=y,j=x: recuperar(i,j,e))
    L.grid(row = y,column = x)

    l = Label(frmM, text = '[' + str(x) + ', ' + str(y) + ']'  + ' ' + str(choice(z[list])), justify=LEFT, anchor="w")  #[x, y] nombre_malo
    malosL[y][x] = l
    l.grid(sticky = W, column = c, row = counterMalos)
    



def massSpawn(e):
    global c, counterMalos, pos, _, z

    zones = []
    for _ in zonas:
        if len(['zona']) > 0:
            zones.append(_)


    for n in range(10):
        z = choice(zones)
        #Corregido luego del cumple del agu, antes spawneaba una cantidad random de bichos entre 10 y m (ni idea podria ser infinito xd)
        pos = choice(z['zona'])

        y = pos[0]
        x = pos[1]

        #dicta si spawnea un raro, oca no tiene raros
        if randint(0,100) < 33 and len(z['enemigosR']) > 0: 
            spawn('X', 'enemigosR',x,y) #RARO con 33% chance de spawnear
        else:
            spawn('x','enemigos',x,y)

        #se remueve la coordenada usada para evitar superposicion, y se chequea que la lista sea legible
        z['zona'].remove([y,x])
        counterMalos += 1
        if counterMalos == 30: 
            c += 1
            counterMalos = 0

#Crea un frame manejado por grid para mostrar posiciones de malos
frmM = LabelFrame(root, text = 'Malos')
frmM.place(x=1100, y=1)

frmL = LabelFrame(root, text = 'Seleccionado')
frmL.place(x = 1100, y = 650) 

m = Label(frmL, text = 'A seleccionar')
m.pack()

frmS = LabelFrame(root)
frmS.place(x = 1250, y = 662) 

boton = Label(frmS, text= 'Spawnear mas bichos')
boton.bind('<Button-1>',lambda e: massSpawn(e))
boton.pack()

#iteración que spawnea los malos
for z in zonasE:    
    pos = sample(z['zona'], z['promedio'] + z['var'])  #saca n cantidad de casillas de una zona; n siendo dictado por el maximo de bichos que puede tener
    for _ in range(randint(z['promedio'] - z['var'], z['promedio'] + z['var'])):
        y = pos[_][0]
        x = pos[_][1]
        
        #dicta si spawnea un raro, oca no tiene raros
        if randint(0,100) < 33: 
            spawn('X', 'enemigosR',x,y) #RARO con 33% chance de spawnear
        else:
            spawn('x','enemigos',x,y)
        
        #se remueve la coordenada usada para evitar superposicion, y se chequea que la lista sea legible
        z['zona'].remove([y,x])
        counterMalos += 1
        if counterMalos == 30: 
            c += 1
            counterMalos = 0

#La cantidad de malos al final del loop seria = 30*c + counterMalos

def oscuro(e):
    if ls[0].cget('bg') != 'Black':
        for i in ls:
            i.config(bg= 'Black')
    else:
        for i in ls:
            i.config(bg= 'white')


def redist1(event,i,j,_):
    global perdidos, bolasL, bolasLE

    P = B = zona = None
    n = 0
    
    j = bolasL[_][0]
    i = bolasL[_][1]

    for p in perdidos:
        if p[1] == [j,i]:           
            P = p
            
    for b in bolasL:
        n += 1
        if b == [j,i]:
            B = b
    
    print(B)

    #recupera la posicion previamente ocupada por una esfera
    P[0]['zona'].append(P[1])
    print(P)
    print(bolasL)
    #posicion aleatoria diponible en una zona aleatoria
    while zona == None or len(zona['zona']) == 0:
        zona = choice(zonasB)
    Pos =  choice(zona['zona'])

    #remplaza la posicion anterior de la esfera por la nueva
    bolasL[_] = Pos
    bolasLE[_] = Pos
    perdidos[perdidos.index(P)] = [zona,Pos]
    event.widget.config(text = str(Pos[::-1]))
    
    #saca la casilla de la pool de casillas disponibles para entidades
    zona['zona'].remove(Pos)


def redist(e):
    global counterBolas, bolasL, zonasB, perdidos, bolasLE
    for p in perdidos:
        p[0]['zona'].append(p[1])

    for i in estados:
        i.config(bg = 'White')

    zonasB = zonasE
    bolasL = []
    bolasLE = []

    for l in ls:
        l.destroy()
    
    counterBolas = 0
    bolas(e)
    mostrarTodo('e')

def ocultar(e,n):
    global bolasLE, bolasL, estados

    if bolasL[n] in bolasLE:
        bolasLE[n] = None
        e.widget.config(bg = 'Grey')
        
    else:
        bolasLE[n] = (bolasL[n])
        e.widget.config(bg = 'White')

def mostrarTodo(e):
    global mostrar

    mostrar = not mostrar
    
    if mostrar:
        n = 0
        for b in bolasLE:
            n+=1
            bolasMostrar[n-1] = Label(frm, bg= 'yellow', text = ' '+str(n)+' ')
            bolasMostrar[n-1].grid(row=b[0],column=b[1])
    else:
        for b in bolasMostrar:
            b.destroy()
            b = None


#BOLAS
counterBolas = 0
#se nota que cree cada array en distintos dias
bolasL = []
ls = [None for i in range(7)]
perdidos = []
estados = [None for i in range(7)]
bolasLE = []
bolasMostrar = [None for i in range(7)]
mostrar = False

#frame con las coordenadas de las esferas
frmB = LabelFrame(root, text = 'Bolas')
frmB.place(x= 10, y = 750)

#frame para mostrar la distancia de la casilla seleccionada a la esfera mas cercana
frmD = LabelFrame(root, text= 'Dist. a bola')
frmD.place(x = 360, y = 750, in_ = root)


# 'boton' para censurar las coordenadas de las esferas
frmT = LabelFrame(root)
frmT.place(x = 310, y = 763, in_ = root)

t = Label(frmT, text = 'Toggle')
t.bind('<Button-1>',lambda e: oscuro(e))
t.pack()

#failsave para frmD
b = Label(frmD)
b.pack()
# 'boton' para redistribuir las esferas
frmDI = LabelFrame(root)
frmDI.place(x = 435, y = 763, in_ = root)

d = Label(frmDI, text = 'Redistribuir')
d.bind('<Button-1>',lambda e: redist(e))
d.pack()

# lista de bolas con sus estados
frmE = LabelFrame(root)
frmE.place(x=510, y = 763, in_ = root)

# boton para mostrar todas las esferas a la vez
frmMb = LabelFrame(root)
frmMb.place(x = 800, y = 763, in_ = root)

d = Label(frmMb, text = 'Mostrar Esferas')
d.bind('<Button-1>', mostrarTodo)
d.pack()


for i in range(7):
    estados[i] = Label(frmE, text = i+1,padx=15, bg= 'white')
    estados[i].bind('<Button-1>', lambda e, n=i: ocultar(e,n))
    estados[i].grid(row=0,column=i)


# el 'diseño' base de una esfera
L = Label(frm, text = 'O', bg = 'Yellow', padx=2)


def bolas(e):
    global ls, bolasL, counterBolas, perdidos
    zonaB = zonasB.copy()
    zona = None


    for _ in range(7):
        #while zona == None or len(zona['zona']) == 0:
        zona = choice(zonaB)
        pos = choice(zona['zona']) #seleccionar una casilla aleatoria de una zona aleatoria no ocupada por otra esfera
        zonaB.remove(zona)

        #facilidad de lectura
        y = pos[0]
        x = pos[1]

        #L.grid(row = y,column = x) #VUELA, PEGA Y ESQUIVA!!! son las 3AM.
        
        ls[_] = Label(frmB, text = str(pos[::-1]), bg= 'Black') #[::-1] da vuelta  el array
        ls[_].bind('<Button-1>', lambda e,i=x,j=y,_=_: redist1(e,i,j,_))
        ls[_].grid(column = counterBolas, row = 0)
        
        bolasL.append([y,x]) #Lista con la que se chequea, inamobilble excepto por redistribucion
        print(y,x);print(_)
        bolasLE.append([y,x]) #Lista que se va a usar, la modifica cualquier cosa
        counterBolas += 1
        perdidos.append([zona, [y, x]])  
        zona['zona'].remove([y,x])
    #print(list(enumerate(bolasL)))
bolas('e')


#inicia el programa
root.mainloop()

#horas: ya perdi la cuenta..
#me aprendi tkinter para esto, bien fachero, 9/10.

"""
                                                                                                                                 
                                                                                                                                                      
      .::::::.     .::::::.     .:::::::.                                                          
    #@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@                                                           
   %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@            @%.                      :%@@@+    %          
   @@=          @@*          @@%          #@@#          @@@@@%.#                 @@@@@@@@+:@           
  =@@           -@            @            @@@         @@#@@@@@%               .@@+..-@@@@@+           
  *@@           :@            @            @@@        @-    #@@                @@      @@@@+           
  *@@           :@            @            @@@       -@      .#               *@   @@@@:*@@+           
  *@@     @:    :@     @+     @     *%     @@@       @@-     @                @.  @+*@% -@@+           
  *@@     @:    :@     @+     @     *%     @@@      .@@@@##@@@@@@@:           @      @  -@@+           
  *@@     @:    :@     @+     @            @@@     :@ @@@@@@@@@@@@@@          @     @.  -@@+           
  *@@     @:    :@     @@@@@@@@            @@@     @%  %@@@@#=--#@@@@         %    -%   -@@+           
  *@@     @:    :@     @#=====@            @@@     @@.     @      -@@*        .+   @    -@@+           
  *@@     @:    :@     @+     @            @@@     @@@@*=*@@@@@@@  *@@         #  @     -@@+           
  *@@     @:    :@     @+     @     *%     @@@      @@@@@@@@@@@@@@  @@          ##@@@@@@@@@+           
  *@@     @:    :@     @+     @     *%     @@@       -#@@@@*===%@@. @@           @%%%%%%@@@+           
  *@@           :@            @     *%     @@@           %      @@ :@           @       =@@+           
  *@@           :@            @     *%     @@@     *@@@@@@*.   @@  @%    -     #@#      =@@*     =     
  *@@           :@            @     *%     @@@    #@@@@@@@@@@@@-  *@    .@%   .@@@@@    @@@@ +  *@-    
  :@@           *@           =@     *%     @@@    @+   =#@@@@@@@#*@    =@@@#  @ +@@@@@=* @@@@  %@@@-   
   @@@%########@@@@%########%@@#####@@#####@@@    @      .@@@@@@@%      @@@  .%   %@@@:  %@@    @@#    
   =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @.  :@:   %@@.        @   .@    .@     @     .#     
    :@@@@@@@@@@@@:@@@@@@@@@@@@@@@@@@@@@@@@@@@       .-:                                                


  .oooooo.                                                                  .o8              .oooooo.   oooo                                        
 d8P'  `Y8b                                                                "888             d8P'  `Y8b  `888                                        
888           .oooo.   ooo. .oo.  .oo.    .oooo.   oooo d8b  .oooo.    .oooo888   .oooo.   888           888 .oo.    .oooo.   oooo    ooo  .ooooo.  
888          `P  )88b  `888P"Y88bP"Y88b  `P  )88b  `888""8P `P  )88b  d88' `888  `P  )88b  888           888P"Y88b  `P  )88b   `88.  .8'  d88' `88b 
888           .oP"888   888   888   888   .oP"888   888      .oP"888  888   888   .oP"888  888           888   888   .oP"888    `88..8'   888   888    software
`88b    ooo  d8(  888   888   888   888  d8(  888   888     d8(  888  888   888  d8(  888  `88b    ooo   888   888  d8(  888     `888'    888   888 
 `Y8bood8P'  `Y888""8o o888o o888o o888o `Y888""8o d888b    `Y888""8o `Y8bod88P" `Y888""8o  `Y8bood8P'  o888o o888o `Y888""8o     `8'     `Y8bod8P'      
                                                                                                                                                
                                                                                                                                                                             
"""


#cuantas veces dijeron 'nerd' mientras leian esto?