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

public class Java_Diff_test extends PApplet {

int W = 800;
int H = 800;
float xmin = -5.0f;
float xmax = 5.0f;
float ymin = -5.0f;
float ymax = 5.0f;

float k = 1.0f;
PGraphics pg;
PShader shade;

public void setup(){
  
  //background(0);
  shade = loadShader("col.glsl");
  //shade.set("resolution", float(800), float(800));
  shade.set("xmin", xmin);
  shade.set("xmax", xmax);
  shade.set("ymin", ymin);
  shade.set("ymax", ymax);
  pg = createGraphics(800,800,OPENGL);
}


public void draw(){
  
  float mx = mouseX/80.0f;
  float my = mouseY/80.0f;

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
  
  k += 0.01f;
  
}
  public void settings() {  size(800,800,P2D); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "Java_Diff_test" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
