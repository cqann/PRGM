int W = 800;
int H = 800;
float xmin = -5.0;
float xmax = 5.0;
float ymin = -5.0;
float ymax = 5.0;

float k = 1.0;
PGraphics pg;
PShader shade;

void setup(){
  size(800,800,P2D);
  //background(0);
  shade = loadShader("col.glsl");
  //shade.set("resolution", float(800), float(800));
  shade.set("xmin", xmin);
  shade.set("xmax", xmax);
  shade.set("ymin", ymin);
  shade.set("ymax", ymax);
  pg = createGraphics(800,800,OPENGL);
}


void draw(){
  
  float mx = mouseX/80.0;
  float my = mouseY/80.0;

  shade.set("mx", mx);
  shade.set("my", my);
  shade.set("k",k);
  pg.beginDraw();
  pg.shader(shade);
  pg.rect(0, 0, pg.width, pg.height);
  pg.endDraw();
  
  fill(0);
  //rect(0, 0, 800, height);
  image(pg, 0, 0); 
  
  resetShader();
  
  k += 0.01;
  
}
