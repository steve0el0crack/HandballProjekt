//El objetivo. Lo creo con el doble de margen para que no ocurra lo que pasa con los jugadores (estar al límite)

class Ziel {
  float xpos, ypos;
  void render (int xlimit, int ylimit){
    fill(150);
    xpos = random(2*xlimit, width - 2*xlimit);
    ypos = random(2*ylimit,height - 2*ylimit);
    square(xpos, ypos, 20);  
  }
}
