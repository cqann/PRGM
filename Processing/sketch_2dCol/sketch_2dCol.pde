

float sq2 = pow(2,0.5);


void setup(){
  size(800,800);
  colorMode(HSB);
  rectMode(CENTER);
  background(0);
}

int clamp(int num){
  if (num>799){
    return 799;
  } else if (num<0){
    return 0;
  } else {
    return num;
  }
}

void draw(){
  float hue;
  float hyp;
  float y;
  float x;
  float angle;
  
  ArrayList<float[]> colMap = new ArrayList<float[]>();
  
  
  for(int i = 0; i<height; i++){
    y = i - 400;
    for(int j = 0; j<width; j++){
      x = j - 400;
      hyp = pow(x*x + y*y,0.5);
      
      if(x<0){
        angle = atan(y/x);
      } else {
        angle = PI + atan(y/x);
      }
      
      hue = map(angle,-(PI/2),PI*1.5,0,255);
      fill(hue,255,255);
      //stroke(hue,map(hyp,sq2*200,sq2*400,255,125),map(sqrt(hyp),0,15,0,255));
      float[] toAppend = {hue,map(hyp,sq2*200,sq2*400,255,125),map(sqrt(hyp),0,15,0,255)};
      colMap.add(toAppend);
      //point(i,j);
    }
  }
  
  float a;
  float b;
  float opre;
  float opim;
  int index;
  float axmin = -3;
  float axmax = 3;
  
  
  for(int i = 0; i<height; i++){
    b = map(i,0,800,axmin,axmax);
    for(int j = 0; j<width; j++){
       a = map(j,0,800,axmin,axmax);
       opre =  b*cos(a);
       opim = -a*sin(b+a) ;
       index = clamp(round(map(opim,axmin,axmax,0,799)))*800 + clamp(round(map(opre,axmin,axmax,0,799)));
       stroke(colMap.get(index)[0],colMap.get(index)[1],colMap.get(index)[2]);
       point(i,j);
    }
    
  }
  
  
  
  noLoop();
}
