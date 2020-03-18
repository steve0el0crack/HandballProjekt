#Hay un gran problema, y es que las variables xpos, ypos deben referir siempre al CENTRO 
#del objeto en cuestión, lo cual es distinto en el caso del cuadrado y el triángulo.
#Por eso creo que debo crear más de un sólo objeto... cada vez se me hace más complicado
#manejar una sola clase JUGADOR con una sola diferencia, que hace que tenga que reescribir
# cada función, en caso sea el defensor o el atacante.

def setup():
    size(700, 900)
    background(255)

#def draw():
 #   for x in [circle, circle]:
  #      x(20, 20, 10, 10)
