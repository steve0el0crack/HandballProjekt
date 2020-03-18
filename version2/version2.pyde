#El orden en el que funciona este programa es primero LEER el documento entero, luego CORRER TODO lo que esté afuera de setup() y draw(). Luego, correr setup(), y finalmente hacer un loop eterno en draw()

import random
import math

class Jugador:
    #Probablemente tenga que guardar la posición en una lista y no como datos separados
    xpos = 0
    ypos = 0
    #counter = 0
    name = ""
    mode = ""
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
        if m == "ATTACK":
            self.ypos = self.ypos + random.randint(ylimit, height/3)
        if m == "DEFENSE":    
            self.ypos = random(height*2/3,height - limit2)

    def identify (self):
        print self.name, self.mode, self.ypos, self.xpos

    #Por el momento se trabajará sólo con el atacante.
    def render(self): #Solo se encarga de renderizar la imagen del atacante (círculo rojo) en las coordenadas self.xpos, self.ypos
        if self.mode == "ATTACK":
            fill(255,0,0)
            ellipse(self.xpos, self.ypos, 20, 20)       
               
    def defineweg (self, xziel, yziel): #Las coordenadas del objetivo se introducirán de manera manual
        varx = xziel - self.xpos
        vary = yziel - self.ypos
        distance = math.sqrt(varx**2 + vary**2)
        #line(self.xpos, self.ypos, xziel, yziel) #Con esto sólo MUESTRO el camino que va a seguir el atacante hasta su meta
        return  varx, vary, distance #Retorna la distancia real a modo de TUPLA 
    
    def action(self, vector):        
        schrittn = vector[2]/self.v
        #print "Faltan" + str(schrittn) + "pasos para llegar" 
        
        xschritt = vector[0]/schrittn
        yschritt = vector[1]/schrittn
        
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
        fill(150)
        """        
        #Para que el objetivo en realidad sea el mouse
        self.xpos = mouseX
        self.ypos = mouseY
        """
        square(self.xpos, self.ypos, self.gross) #Para hacer render en UNA SOLA POSICIÓN FIJA
    

#Con esto pongo límites al área de la interacción
xlimit = 20
ylimit = 20

#En esta lista deben estar TODAS las intancias para los jugadores
jugadores = [] #El último elemento es el OBJETO ARCO (Esta implementación debe cambiar)

#Puedo crear a los jugadores en el setup del sistema, pero el problema es que después (fuera de la función setup) no hay manera de referirse a ellos. Y la idea es hacer el render en el draw, pero definirlos en el setup.
#La razón por la que deben crearse dentro del setup es por las variables WIDTH Y HEIGHT, que son accesibles solamente dentro de esta función.
def setup():
    print "Starting setup"
    size(600,400)
    rect(xlimit, ylimit, width - 2*xlimit, height - 2*ylimit)
    
    teambuilder("ATTACK", 5) #Se crean las instancias para los jugadores, pero no se renderizan.
    
    arco = goal(xlimit, ylimit, 20)
    jugadores.append(arco)
    
    #print len(jugadores)
    print "Finishing setup"
    

#En este método es en el que va a ocurrir la INTERACCIÓN
def draw():
    background(255) #Al definir el FONDO (BACKGROUND) cada vez que corro, dejo atrás cualquier elemento que había creado antes.
    
    jugadores[-1].render()
    #Coordenadas del OBJETIVO, al que TODOS LOS JUGADORES tienen que dirigirse
    zielx = jugadores[-1].xpos + (jugadores[-1].gross)/2
    ziely = jugadores[-1].ypos + (jugadores[-1].gross)/2
    
    for i in range(0,len(jugadores)-1):
        jugadores[i].render()

    for x in range(0,len(jugadores)-1):
        tuplaziel = jugadores[x].defineweg(zielx, ziely) #El camnio es distinto para cada jugador, lo puedo marcar dibujando una línea -opción dentro de la clase Jugador.
        jugadores[x].action(tuplaziel)


def teambuilder(mode, total):
    for i in range(0,total):
        jugadores.append(Jugador(str(i),mode, 1))

    
