//Se va a hacer el intento de crear el ambiente VISUAL (UI) de central mind con Processing
//Esto quiere decir el campo y los jugadores (atacantes, defensores; tanto como su lógica) -objetos-.
//Además de ciertas reglas muy específicas, como: 
//  No pisar la zona de 6 metros

//Me es un poco complicado reconcer el correcto uso de declarar variables de manera GLOBAL y/o LOCAL.
int xlimit = 20;
int ylimit = 20;
ArrayList<Jugador> jugadores = new ArrayList<Jugador>();
//ArrayList<String> IDs = new ArrayList<String>();

String[] atacantes = {"guillermo", "javier"};
String[] defensores = {"tanque", "piero"};


void setup() {
  
  background(255);
  size(600,400);
  rect(xlimit, ylimit, width - 2*xlimit, height - 2*ylimit);
  
  //j.identify();
  
  teambuilder("DEFENSE", defensores); //Funciona de manera individual, pero no ambos al mismo tiempo.  
  teambuilder("ATTACK", atacantes);
  
  Ziel z = new Ziel();
  z.render(xlimit, ylimit);

}

//En esta función debe definir2se el MOVIMIENTO/INTERACCIÓN tanto del defensa, como del atacante.
void draw () {
  
}


//players puede ser int[] o int
void teambuilder(String mode, String[] players) {
  for (int i = 0; i < 2; i++) {
   
    Jugador jugador = new Jugador(players[i],mode);
    jugador.create(xlimit, ylimit);
    print(jugador.counter);
    
    //Agregar el concepto de que TODOS los jugadores entren en una lista hace del programa algo mucho más complejo.
    /*
    String id = mode + str(i+1);             //Para este tipo de cosas requería el algoritmo de COMBINATORIA, para generar IDs 
    
    jugadores.add(new Jugador(players[i],mode));
    jugadores.get(i).create(xlimit, ylimit);
    
    print(jugadores.get(i).name + "\n");  
    **/  
  }
}
