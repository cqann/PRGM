PGraphics pg;
PShader shade;

float axmin = -5;
float axmax =  5;
float k = 1;

void setup(){
  size(800,800,P2D);
  frameRate(60);
  //fullScreen(P2D);
  //background(0);
  shade = loadShader("dom.glsl");
  float resx = width;
  float resy = height;
  shade.set("min",axmin);
  shade.set("max",axmax);
  shade.set("resx",resx);
  shade.set("resy",resy);
  pg = createGraphics(width,height,OPENGL);
}


void draw(){
  
  shade.set("k", k);
  
  pg.beginDraw();
  pg.shader(shade);
  pg.rect(0, 0, pg.width, pg.height);
  pg.endDraw();
  
  fill(0);
  //rect(0, 0, 800, height);
  image(pg, 0, 0); 
  
  resetShader();
  
  k += 0.05;
}
