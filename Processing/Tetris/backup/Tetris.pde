ArrayList<Tetroid> tetroids = new ArrayList<Tetroid>();
int t = 0;

void setup(){
  size(600,800);
  frameRate(8);
  drawCourt();
   
  
  tetroids.add(new Tetroid(80,0,4,0));
 
}


void draw(){
  
  if(tetroids.get(tetroids.size()-1).stuck){
    int temp_rand_x = round(random(7))*40+40;
    int temp_rand_type = round(random(6));
    tetroids.add(new Tetroid(temp_rand_x,0,temp_rand_type,tetroids.size()));
  }
  
  drawCourt();
  for(int i = 0; i<tetroids.size();i++){
    tetroids.get(i).checkMovement(tetroids);
    tetroids.get(i).checkStuck(tetroids);
    if(t%2 == 0){
      tetroids.get(i).update(tetroids);
    }
    tetroids.get(i).show();
  }
  t++;
}




void drawCourt(){
  background(0);
  strokeWeight(2);
  stroke(50);
   for(int i = 0; i < 20; i++){
    float x_y_coord = i*20;
    line(0,x_y_coord*2,400,x_y_coord*2);
    if(i%2==0){
      line(x_y_coord,0,x_y_coord,800);
    }
  }
  
  noStroke();
  fill(155);
  rect(400,0,200,800);
  
  
}
