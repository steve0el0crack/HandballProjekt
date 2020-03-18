//Tanto el jugador que cumple el rol de defensa y ataque son ambos: JUGADORES
//Solo cumplen un ROL DISTINTO dentro del campo, dependiendo de ciertos factores:
//  ¿Quién tiene el balón? BASIC
//  ¿Dónde está posicionado? BASIC
//  ¿Color de vestimenta?  HARD - Image recongnition

int counter = 0;

class Jugador {
 
  //Pensar el uso de listas para estos datos
 //NOMBRE, ROL, NÚMERO (en su equipo - y en la cancha -counter-)
  String name, function;  
  int counter = 0;
  float xpos, ypos;
  Jugador (String n, String f) { //CONSTRUCTOR
    name = n;
    function = f;
    //print(counter);
    counter++;
    //print(counter);  
  }
  
  
  void identify() {  //DEBUGGING
    print(name, function, counter);
  }
 
  void create(int limit1, int limit2) {     //Círculo: Atack / Triángulo: Defense
    //Esta variable es usada en ambos casos
    xpos = random(limit1, width - limit1);
    int increment = 20;
    
    if (this.function == "ATTACK") {
      //print("ATACANTE\n");
      ypos = random(limit2, height/3);
      fill(255, 0, 0);
      ellipse(xpos, ypos, 20, 20);
    }
    
    if (this.function == "DEFENSE") { 
      //Ésta sólo aplica para el defensor(triángulo), porque está al otro lado de la cancha
      ypos = random(height*2/3, height - limit2);
      //print("DEFENSOR\n");
      //Así, el defensor puede quedar al límite de la cancha. Visualmente es horrible, pero técnicamente está correcto.
      fill(#2A41BF);
      triangle(xpos, ypos, xpos + increment*2/3, ypos + increment, xpos + increment*4/3, ypos);
    }  
    
    //Método automático de identificación VISUAL, después de CREAR al jugador
    PFont hi;
    hi = createFont("Arial",10);
    textFont(hi);
    fill(#02061C);
    text(name, xpos, ypos);
  }
  
  //En el balonmano, un ataque tiene un objetivo
  void Attack() {
      print(xpos + "\n", ypos+"\n");
  }
  
}
