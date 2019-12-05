class Piece{
  Tetroid parent;
  float x;
  float y;
  float r;
  float g;
  float b;
  
  Piece(float tx , float ty, Tetroid tparent, float tr, float tg, float tb){
    x = tx;
    y = ty;
    parent = tparent;
    r = tr;
    g = tg;
    b = tb;
  }
  
  void show(){
    fill(r,g,b);
    rect(x,y,40,40);
  }
  
}
