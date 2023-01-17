
#El tablero, no se, capaz lo querias cambiar por man.jpeg o alguna otra imagen
tablero = 'C:/Users/user/Desktop/Proyectos/Oca Battle Royale/tablero.jpeg'

#Color del fondo
colorFondo = 'Grey'

#Mostrar el numero de la esfera mas cercana
mostrarNumeroBola = True

#Tablero de tamaño 30 x 20 tiles mas el indice
board = [ [None]*31 for _ in range(21) ]


#lista de las casillas en las que no puede estar una entidad
invalidas = [[0, 0], [0, 2], [0, 4], [0, 6], [1, 0], [1, 4], [1, 2], [1, 6], [6, 7], [6, 6], [6, 4], [6, 1], [8, 5], [8, 1]
            , [13, 8], [13, 7], [13, 6], [13, 5], [12, 1], [11, 3], [12, 3], [10, 1], [13, 1], [13, 0], [19, 8], [16, 8]
            , [15, 8], [13, 11], [15, 11], [6, 11], [3, 15], [4, 15], [3, 21], [3, 22], [2, 22], [2, 21], [1, 22]
            , [1, 21], [0, 15], [9, 19], [11, 20], [11, 19], [10, 19], [10, 20], [12, 17], [13, 17], [13, 18], [19, 14]
            , [15, 15], [15, 17], [16, 20], [15, 20], [13, 20], [19, 20], [1, 24], [1, 28], [5, 22], [18, 28], [17, 28]
            , [17, 27], [18, 27], [18, 26], [17, 26], [17, 20], [11, 23], [11, 24], [12, 24], [13, 24], [13, 23], [13, 22]
            , [12, 22], [11, 22], [12, 23], [9, 11], [9, 7], [8, 7], [7, 15], [3, 24], [3, 26], [3, 28], [13, 29], [13, 28]
            , [5, 23], [8, 22], [8, 21], [5, 21], [12, 5], [10, 17], [8, 17], [8, 15],[10,23],[10,22],[10,24],[13,21], [8,11], [13, 3]]


#Las zonas estan hechas de esta forma para que sean faciles de modificar
oca = {
    'zona': [[11, 15], [12, 15], [14, 14], [13, 14], [14, 13], [13, 13], [13, 12], [14, 12]
    , [12, 12], [12, 13], [11, 13], [11, 14], [12, 14], [11, 12], [10, 12], [9, 12], [9, 13] #Se puede modificar las casillas de cada zona, pero si no sabes lo que estas haciendo no es recomendado.
    , [10, 13], [10, 14], [9, 14], [9, 15], [10, 15], [10, 16], [9, 16], [8, 16], [11, 16]
    , [12, 16], [13, 16], [14, 16], [14, 15], [13, 15]],
    'color': 'blue',
    'enemigos': ['gaturro'],
    'enemigosR': [],
    'promedio': 2,   
    'var': 1
}

sin_juanma = {
    'zona':[[19, 7], [19, 6], [19, 5], [19, 4], [19, 3], [19, 2], [19, 1], [19, 0]
    , [18, 0], [18, 1], [18, 2], [18, 3], [18, 4], [18, 5], [18, 6], [18, 7], [18, 8]
    , [17, 8], [17, 7], [16, 7], [15, 7], [14, 7], [14, 8], [14, 6], [15, 6], [16, 6]   #¡¡(promedio + var) =< #(zona)!! sino se muere por obvias razones
    , [17, 6], [16, 5], [17, 5], [15, 5], [14, 5], [14, 4], [13, 4], [13, 2], [14, 3]
    , [14, 2], [14, 1], [14, 0], [15, 0], [16, 0], [17, 0], [17, 1], [16, 1], [15, 1]
    , [15, 2], [17, 2], [16, 3], [16, 2], [17, 3], [15, 4], [16, 4], [17, 4], [15, 3]], #coordenadas donde la zona esta
    'color': 'purple',
    'enemigos': ['cavernicola'], #los enemigos que pueden spawnear dentro de la zona, cada enemigo que aparece ocupa una casilla.
    'enemigosR': ['juanma'],
    'promedio': 2, #el promedio de enemigos                 
    'var': 1 #la variacion que se puede tener del promedio      ¡¡var =< promedio!! 
}

breaking_bad = {
    'zona': [[1, 5], [0, 5], [2, 6], [2, 5], [3, 5], [3, 6], [4, 6], [5, 5]
    , [4, 5], [5, 6], [5, 4], [4, 4], [3, 4], [2, 4], [2, 3], [1, 3], [0, 3]
    , [3, 3], [4, 3], [5, 3], [4, 2], [5, 2], [3, 2], [2, 2], [2, 1], [1, 1]
    , [0, 1], [2, 0], [3, 0], [3, 1], [4, 0], [5, 0], [5, 1], [4, 1]
    ],
    'color': 'red',
    'enemigos': ['terrorista'],
    'enemigosR': ['tezcatlipoca'],
    'promedio': 2,
    'var': 1
}

naruto = {
    'zona': [[7, 6], [8, 6], [9, 6], [10, 6], [11, 6], [12, 6], [12, 4], [12, 2]
    , [12, 0], [11, 0], [11, 1], [11, 2], [11, 4], [11, 5], [10, 5], [9, 4], [10, 4]
    , [10, 3], [9, 3], [9, 5], [8, 4], [6, 5], [7, 5], [7, 4], [7, 3], [8, 3], [6, 3]
    , [6, 2], [7, 2], [8, 2], [7, 1], [7, 0], [6, 0], [8, 0], [9, 0], [9, 1], [10, 2]
    , [9, 2], [10, 0]],
    'color': 'orange',
    'enemigos': ['gokuto'],
    'enemigosR': ['otaku'],
    'promedio': 2,
    'var': 1
}

disney = {'zona': [[12, 10], [11, 10], [10, 10], [10, 9], [11, 8], [11, 9]
    , [10, 8], [12, 8], [9, 10], [9, 9], [10, 7], [11, 7], [10, 11], [11, 11]
    , [12, 11], [9, 8], [12, 7], [12, 9]],
    'color': 'green',
    'enemigos': ['ratón'],
    'enemigosR': ['el rey'],
    'promedio': 1,
    'var': 0
}

fortnite = {'zona': [[8, 10], [8, 9], [8, 8], [7, 8], [7, 7], [6, 8], [7, 9]
    , [6, 9], [6, 10], [7, 10], [7, 11]],
    'color': 'white',
    'enemigos': ['jonesy'],
    'enemigosR': ['la fundación'],
    'promedio': 1,
    'var': 0
}

loquendo = {'zona': [[0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13]
    , [0, 14], [1, 14], [1, 13], [1, 12], [1, 11], [1, 10], [1, 9], [1, 8]
    , [1, 7], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [2, 12], [2, 13]
    , [2, 14], [3, 14], [3, 13], [3, 12], [3, 11], [3, 10], [3, 9], [3, 8]
    , [3, 7], [4, 7], [4, 8], [5, 7], [5, 9], [4, 9], [5, 10], [4, 10], [5, 8]
    , [5, 11], [4, 11], [4, 12], [5, 13], [4, 13], [4, 14], [5, 14], [5, 12]],
    'color': 'purple',
    'enemigos': ['walfa'],
    'enemigosR': ['esqueleto'],
    'promedio': 2,
    'var': 1
}

gta = {'zona': [[1, 15], [0, 16], [1, 16], [2, 15], [2, 16], [3, 16]
    , [4, 16], [5, 16], [6, 16], [6, 15], [5, 15], [7, 16], [7, 17]
    , [6, 17], [5, 17], [3, 17], [2, 17], [1, 17], [0, 17], [0, 18]
    , [1, 18], [2, 18], [3, 18], [4, 18], [5, 18], [6, 18], [7, 18]
    , [7, 19], [6, 19], [6, 20], [7, 20], [7, 21], [6, 21], [4, 17]
    , [5, 19], [5, 20], [4, 20], [4, 19], [4, 21], [3, 20], [2, 20]
    , [3, 19], [2, 19], [1, 19], [1, 20], [0, 19], [0, 20], [0, 21]],
    'color': 'orange',
    'enemigos': ['un balla'],
    'enemigosR': ['tanque'],
    'promedio': 2,
    'var': 1
}

backrooms = {'zona': [[0, 23], [0, 22], [2, 23], [1, 23], [4, 23]
    , [4, 22], [4, 24], [3, 23], [2, 24], [2, 25], [3, 25], [4, 25]
    , [4, 26], [4, 27], [4, 28], [3, 29], [4, 29], [2, 27], [3, 27]
    , [2, 26], [2, 28], [2, 29], [1, 29], [1, 27], [1, 26], [1, 25]
    , [0, 24], [0, 25], [0, 26], [0, 27], [0, 28], [0, 29]],
    'color': 'light blue',
    'enemigos': ['medusa'],
    'enemigosR': ['obama trolcara'],
    'promedio': 2,
    'var': 1
}

minecraft ={'zona': [[6, 22], [9, 23], [8, 23], [7, 23], [6, 23]
    , [7, 22], [7, 24], [8, 24], [9, 24], [9, 25], [8, 25], [7, 25]
    , [5, 24], [5, 25], [6, 24], [6, 25], [6, 26], [5, 26], [5, 27]
    , [6, 27], [6, 28], [5, 28], [5, 29], [6, 29], [7, 29], [7, 28]
    , [7, 27], [7, 26], [8, 26], [8, 27], [9, 27], [9, 26], [9, 28]
    , [8, 28], [8, 29], [9, 29], [10, 29], [10, 28], [10, 27], [10, 26]
    , [10, 25], [11, 25], [11, 26], [11, 27], [11, 28], [11, 29]
    , [12, 29], [12, 28], [12, 27], [12, 25], [12, 26]],
    'color': 'red',
    'enemigos': ['niño rata', 'zombie'],
    'enemigosR': ['trotu'],
    'promedio': 2,
    'var': 1
}

gmod = {
    'zona': [[14, 21], [15, 21], [16, 21], [17, 21], [18, 21], [19, 21]
    , [18, 20], [18, 22], [19, 22], [19, 23], [18, 23], [18, 24], [17, 24]
    , [17, 23], [17, 22], [16, 22], [16, 23], [15, 23], [15, 22], [14, 22]
    , [14, 24], [14, 25], [13, 26], [13, 27], [13, 25], [14, 23], [14, 26]
    , [14, 27], [14, 28], [15, 29], [14, 29], [15, 28], [15, 27], [15, 26]
    , [15, 25], [15, 24], [16, 24], [16, 25], [17, 25], [18, 25], [19, 25]
    , [19, 24], [19, 26], [19, 27], [19, 28], [19, 29], [18, 29], [16, 29]
    , [17, 29], [16, 27], [16, 26], [16, 28], [14, 20]],
    'color': 'purple',
    'enemigos': ['bunger'],
    'enemigosR': ['traidor'],
    'promedio': 2,
    'var': 1
}

colosos = {
    'zona': [[15, 14], [15, 12], [15, 13], [16, 14], [16, 13], [17, 13], [17, 14]
    , [18, 14], [18, 13], [19, 12], [19, 13], [17, 12], [16, 12], [16, 11], [16, 10]
    , [17, 11], [18, 12], [18, 11], [17, 10], [18, 10], [19, 10], [19, 11], [19, 9]
    , [18, 9], [17, 9], [16, 9]],
    'color': 'orange',
    'enemigos': ['lagarto'],
    'enemigosR': ['trolcara'],
    'promedio': 2,
    'var': 1
}

kirby = {
    'zona': [[14, 11], [14, 10], [15, 10], [15, 9], [14, 9], [13, 9], [13, 10]],
    'color': 'light grey',
    'enemigos': ['daddle dee'],
    'enemigosR': ['dedede'],
    'promedio': 1,
    'var': 0
}

mario = {
    'zona':[[9, 21], [9, 22], [9, 20], [8, 20], [8, 19], [8, 18], [9, 18]
    , [9, 17], [10, 18], [11, 18], [11, 17], [12, 18], [12, 19], [13, 19]
    , [12, 20], [12, 21], [11, 21], [10, 21]],
    'color': 'green',
    'enemigos': ['goomba'],
    'enemigosR': ['bully'],
    'promedio': 2,
    'var': 1
}

sonic = {
    'zona': [[14, 19], [15, 19], [15, 18], [14, 18], [14, 17]],
    'color':'light grey',
    'enemigos': ['motobug'],
    'enemigosR': ['tails doll'],
    'promedio': 1, 
    'var': 0
}

medio_oriente = {
    'zona': [[16, 19], [17, 19], [19, 19], [19, 18], [18, 18]
    , [18, 19], [19, 17], [18, 17], [18, 16], [19, 16], [19, 15]
    , [18, 15], [17, 15], [16, 16], [17, 16], [16, 15], [16, 17]
    , [16, 18], [17, 18], [17, 17], [15, 16]],
    'color': 'cyan',
    'enemigos': ['rooey'],
    'enemigosR': ['chrome'],
    'promedio': 2,
    'var': 1
}

kingdom_hearts = {
    'zona': [[7, 14], [7, 13], [8, 12], [8, 13], [8, 14], [7, 12], [6, 12], [6, 13], [6, 14]],
    'color':'light grey',
    'enemigos': ['sincorazon'],
    'enemigosR': ['buzz'],
    'promedio': 1,
    'var': 0
}


zonas = [oca, sin_juanma, breaking_bad, naruto, disney, loquendo
    , fortnite, gta, backrooms, minecraft, gmod, colosos, kirby     #todas las zonas
    , mario, sonic, medio_oriente, kingdom_hearts]

zonasE = [sin_juanma, breaking_bad, naruto, disney, loquendo
    , fortnite, gta, backrooms, minecraft, gmod, colosos, kirby     #zonas donde malos pueden aparecer
    , mario, sonic, medio_oriente, kingdom_hearts]

zonasB = [sin_juanma, breaking_bad, naruto, disney, loquendo
    , fortnite, gta, backrooms, minecraft, gmod, colosos, kirby     #zonas donde bolas pueden aparecer
    , mario, sonic, medio_oriente, kingdom_hearts]