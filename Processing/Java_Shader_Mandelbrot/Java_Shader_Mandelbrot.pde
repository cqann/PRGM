PGraphics pg;
PShader shade;


void setup(){
  size(800,800,P2D);
  shade = loadShader("brot.glsl");
  pg = createGraphics(800,800,OPENGL);
 
}


float theta = 1.123;
float r = (1.0 - cos(theta))/2.0;
float pre =  r*cos(theta)+0.25;
float pim =  r*sin(theta);
float clock;

float k = 0.0;
float lim;
float expk;
float xmin;
float xmax;
float ymin;
float ymax;




void draw(){

  expk = pow(1.01,k);
  xmin = pre-1.0/expk;
  xmax = pre+1.0/expk;
  ymin = pim-1.0/expk;
  ymax = pim+1.0/expk;
  lim = 30.0*pow(1.003,k);
  
  shade.set("xmin",xmin);
  shade.set("xmax",xmax);
  shade.set("ymin",ymin);
  shade.set("ymax",ymax);
  shade.set("limit", lim);
  
  if (mousePressed && clock > 10){
    pre = map(mouseX,0,800,xmin,xmax);
    pim = map(mouseY,0,800,ymax,ymin);
    println(pre);
    clock = 0;
  } else {
    clock += 1;
  }

  
  pg.beginDraw();
  pg.shader(shade);
  pg.rect(0, 0, pg.width, pg.height);
  pg.endDraw();
  
  fill(0);
  image(pg, 0, 0); 
  
  resetShader();
  
  k += 1;


}
