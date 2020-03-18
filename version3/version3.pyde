#El orden en el que funciona este programa es primero LEER el documento entero, luego CORRER TODO lo que esté afuera de setup() y draw(). Luego, correr setup(), y finalmente hacer un loop eterno en draw()

import random
import math

#ATACANTE: 1
#DEFENSOR: 0
class Jugador:
    #Probablemente tenga que guardar la posición en una lista y no como datos separados
    plus= 40
    xpos = 0
    ypos = 0
    #counter = 0
    name = ""
    mode = 0
    v = 0 #Velocidad de movimiento de 1 pixel por PASO(Schritt)
   
    #Esta función sólo correrá una vez por jugador, durante el setup
    def __init__(self, n, m, v):
        self.name = n
        self.mode = m
        self.v = v
        #self.counter = self.counter + 1 
        self.xpos = random.randint(xlimit, width - xlimit) #El eje x no importa, no depende de nada

        #La variable FUNDAMENTAL que depende del modo es la posición en y
        #porque los defensores van abajo, y los atacantes arriba (ORDEN)
        if m == 1:
            self.ypos = random.randint(ylimit, height/3)
        if m == 0:    
            self.ypos = random.randint(height*2/3,height - ylimit)

    def identify (self):
        print self.name, self.mode, self.ypos, self.xpos

    #Por el momento se trabajará sólo con el atacante.
    def render(self): #Solo se encarga de renderizar la imagen del atacante (círculo rojo) en las coordenadas self.xpos, self.ypos
        if self.mode == 1:
            fill(255,0,0)
            ellipse(self.xpos, self.ypos, 40, 40)
        if self.mode == 0:
            fill(0,0,255)    
            triangle(self.xpos, self.ypos, self.xpos + self.plus*2/3, self.ypos - self.plus, self.xpos + self.plus*4/3, self.ypos)
    
    
    #Esta función sólo toma un OBJETIVO de la forma (X,Y) y hace que el jugador se mueva en esa dirección.        
    def move (self, xziel, yziel): 
        #Para trazar el camino desde EL CENTRO en caso del triángulo.
        if self.mode == 0:
            varx = xziel - (self.xpos + self.plus*2/3)
            vary = yziel - (self.ypos - self.plus/2)
            stroke(0,0,255)
            strokeWeight(2)
            #line(self.xpos + self.plus*2/3, self.ypos - self.plus/2, xziel, yziel) #Con esto sólo MUESTRO EL CAMINO A RECORRER.
        if self.mode == 1:
            varx = xziel - self.xpos
            vary = yziel - self.ypos
            stroke(255,0,0)
            strokeWeight(2)
            #line(self.xpos, self.ypos, xziel, yziel) #Con esto sólo MUESTRO EL CAMINO A RECORRER.
        noStroke()
        noFill()


        distance = math.sqrt(varx**2 + vary**2)

        schrittn = distance/self.v
        #print "Faltan" + str(schrittn) + "pasos para llegar" 
        
        xschritt = varx/schrittn
        yschritt = vary/schrittn
        
        self.xpos = self.xpos + xschritt
        self.ypos = self.ypos + yschritt
        #print schrittn, xschritt, yschritt
    
#Esta clase renderiza automáticamente al ser llamada. Es un objeto inerte detro del juego
class goal:
    #Estas coordenadas en realidad sólo indican una esquina del cuadrado, mas no el centro. Cambiar en la version 3
    xpos = 0
    ypos = 0
    gross = 0  #El grosor del cuadrado (arco)
    def __init__(self, xlimit, ylimit, gross):
        self.xpos = random.randint(2*xlimit, width - 2*xlimit)
        self.ypos = random.randint(2*ylimit,height - 2*ylimit)
        self.gross = gross

    def render(self):
        #strokeWeight(1)
        #stroke(75)
        fill(75)
        square(self.xpos, self.ypos, self.gross) #Para hacer render en UNA SOLA POSICIÓN FIJA
        
        self.xpos = mouseX
        self.ypos = mouseY

#Con esto pongo límites al área de la interacción
xlimit = 20
ylimit = 20

#Primera lista: DEFENSOR (0)
#Segunda lista: ATACANTE (1)
#Tercera lista: ARCO     (2)
jugadores = [[],[],[]] 

#Puedo crear a los jugadores en el setup del sistema, pero el problema es que después (fuera de la función setup) no hay manera de referirse a ellos. Y la idea es hacer el render en el draw, pero definirlos en el setup.
#La razón por la que deben crearse dentro del setup es por las variables WIDTH Y HEIGHT, que son accesibles solamente dentro de esta función.
def setup():
    size(1000,600)    
    
    #Se crean las instancias para los jugadores, pero no se renderizan.
    #El ATACANTE tiene como OBJETIVO: EL ARCO
    teambuilder(1, 5, 1) 
    #El DEFENSOR tiene como objetivo: EL ATACANTE
    teambuilder(0, 5, 1)
    
    arco = goal(xlimit, ylimit, 40)
    jugadores[2].append(arco)
    


#En este método es en el que va a ocurrir la INTERACCIÓN
def draw():
    background(255) #Al definir el FONDO (BACKGROUND) cada vez que corro, dejo atrás cualquier elemento que había creado antes.
    
    #Dibujar el campo
    stroke(155)
    strokeWeight(2)
    rect(xlimit, ylimit, width - 2*xlimit, height - 2*ylimit)
    noStroke()
    noFill()
    
    jugadores[2][0].render()
    zielx = jugadores[2][0].xpos + (jugadores[2][0].gross)/2
    ziely = jugadores[2][0].ypos + (jugadores[2][0].gross)/2
    
    #Aquí es donde se empareja al defensor con su atacante... se debe hacer por qué tan cerca está éste del otro.                        
    for j in [0,1]:
        for i in range(0,len(jugadores[j])):
            jugadores[j][i].render()
            if jugadores[j][i].mode == 0:
                #Con esta línea ASIGNO A CADA DEFENSOR UN PAR PARA DEFENDER.
                jugadores[j][i].move(jugadores[j+1][i].xpos, jugadores[j+1][i].ypos)
            if jugadores[j][i].mode == 1:
                jugadores[j][i].move(zielx, ziely)

       
"""
    #LÓGICA INDIVIDUAL de movimiento
    for x in range(0,len(jugadores)-1):
        if jugadores[x].mode == 0:
            jugadores[x].move(zielx, ziely)  #DEFENSA --- ATACANTE
        if jugadores[x].mode == 1:
            jugadores[x].move(zielx, ziely)  #ATACANTE --- ARCO
"""


def teambuilder(mode, total, v):
    for i in range(0,total):
        jugadores[mode].append(Jugador(str(i),mode, v))
