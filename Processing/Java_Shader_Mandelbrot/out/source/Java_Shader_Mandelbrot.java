import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class Java_Shader_Mandelbrot extends PApplet {

PGraphics pg;
PShader shade;


public void setup(){
  
  shade = loadShader("brot.glsl");
  pg = createGraphics(800,800,OPENGL);
 
}


float theta = 1.123f;
float r = (1.0f - cos(theta))/2.0f;
float pre =  r*cos(theta)+0.25f;
float pim =  r*sin(theta);
float clock;

float k = 0.0f;
float lim;
float expk;
float xmin;
float xmax;
float ymin;
float ymax;




public void draw(){

  expk = pow(1.01f,k);
  xmin = pre-1.0f/expk;
  xmax = pre+1.0f/expk;
  ymin = pim-1.0f/expk;
  ymax = pim+1.0f/expk;
  lim = 30.0f*pow(1.003f,k);
  
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
  public void settings() {  size(800,800,P2D); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "Java_Shader_Mandelbrot" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
