#El orden en el que funciona este programa es primero LEER el documento entero, luego CORRER TODO lo que esté afuera de setup() y draw(). Luego, correr setup(), y finalmente hacer un loop eterno en draw()

import random
import math

#ATACANTE: 1
#DEFENSOR: 0
class Jugador:
    plus= 40
    xpos = 0
    ypos = 0
    name = ""
    mode = 0
    v = 0 #Velocidad de movimiento de 1 pixel por PASO(Schritt)
   
    #Esta función sólo correrá una vez por jugador, durante el setup
    def __init__(self, n, m, v):
        self.name = n
        self.mode = m
        self.v = v
        self.xpos = random.randint(xlimit, width - xlimit) #El eje x no importa, no depende de nada

        #La variable FUNDAMENTAL que depende del modo es la posición en y
        #porque los defensores van abajo, y los atacantes arriba (ORDEN)
        if m == 1:
            self.ypos = random.randint(ylimit, height/3)
        if m == 0:    
            self.ypos = random.randint(height*2/3,height - ylimit)

    def identify (self):
        print self.name, self.mode, self.ypos, self.xpos

    def render(self): 
        if self.mode == 1:
            fill(255,0,0)
            ellipse(self.xpos, self.ypos, 40, 40)
            coordinates = str(int(self.xpos)) + "\n" + str(int(self.ypos))
        if self.mode == 0:
            fill(0,0,255)    
            triangle(self.xpos, self.ypos, self.xpos + self.plus*2/3, self.ypos - self.plus, self.xpos + self.plus*4/3, self.ypos)
            coordinates = str(int(self.xpos + self.plus*2/3)) + "\n" + str(int(self.ypos - self.plus/2))
    
    #Esta función sólo toma un OBJETIVO de la forma (X,Y) y hace que el jugador se mueva en esa dirección.        
    def move (self, xziel, yziel): 
        #CATETOS
        if self.mode == 0:
            varx = xziel - (self.xpos + self.plus*2/3) #PARA CENTRAR LAS COORDENADAS DEL TRIÁNGULO
            vary = yziel - (self.ypos - self.plus/2)
            stroke(0,0,255)
            strokeWeight(2)
            distance = math.sqrt(varx**2 + vary**2)
            #line(self.xpos + self.plus*2/3, self.ypos - self.plus/2, xziel, yziel) #Con esto sólo MUESTRO EL CAMINO A RECORRER.
            if distance < 35: #Se define el radio de interacción para los objetos.
                print "PERDISTE"
        if self.mode == 1:
            varx = mouseX - self.xpos  
            vary = mouseY - self.ypos 
            stroke(255,0,0)
            strokeWeight(2)
            #line(self.xpos, self.ypos, xziel, yziel) #Con esto sólo MUESTRO EL CAMINO A RECORRER.
            distance = math.sqrt(varx**2 + vary**2)
            if math.sqrt((xziel - self.xpos)**2 + (yziel - self.ypos)**2) < 12: #Se define el radio de interacción para los objetos. Para cada figura debe ser distinto
                print "GANASTE"
        noStroke()
        noFill()
        #HIPOTENUSA
        schrittn = distance/self.v        
        xschritt = varx/schrittn
        yschritt = vary/schrittn
        #MOVIMIENTO
        self.xpos = self.xpos + xschritt
        self.ypos = self.ypos + yschritt
                
    
#Esta clase renderiza automáticamente al ser llamada. Es un objeto inerte detro del juego
class goal:
    #Estas coordenadas en realidad sólo indican una esquina del cuadrado, mas no el centro. Cambiar en la version 3
    xpos = 0
    ypos = 0
    gross = 0  #El grosor del cuadrado (arco)
    def __init__(self, xlimit, ylimit, gross):
        self.gross = gross
        self.xpos = width/2
        self.ypos = height - self.gross

    def render(self):
        fill(75)
        square(self.xpos, self.ypos, self.gross) #Para hacer render en UNA SOLA POSICIÓN FIJA
    
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
    teambuilder(1, 1, 6) 
    #El DEFENSOR tiene como objetivo: EL ATACANTE
    teambuilder(0, 4, 1)
    
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
    
    jugadores[1][0].render()
    jugadores[1][0].move(zielx, ziely)
    
    for i in range(0, len(jugadores[0])):
        jugadores[0][i].render()
        jugadores[0][i].move(jugadores[1][0].xpos, jugadores[1][0].ypos)
    

def teambuilder(mode, total, v):
    for i in range(0,total):
        jugadores[mode].append(Jugador(str(i),mode, v))
