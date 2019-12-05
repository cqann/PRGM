class Tetroid{
  float x;
  float y;
  int type;
  int index;
  int rot;
  Boolean stuck; 
  ArrayList<Piece> kids = new ArrayList<Piece>();
  float sq2 = sqrt(2);
  
  Tetroid(float tx, float ty,int ttype, int tindex){
    x = tx;
    y = ty;
    type = ttype;
    index = tindex;
    rot = 0;
    stuck = false;
    
    updateKids();
    
  }
  
  void update(ArrayList<Tetroid> tList){
    
    drop();
    updateKids();
    
    
  }
  
  void show(){
    stroke(255);
    
    for(int i = 0; i < 4; i++){
       kids.get(i).show();
    }
  }
  
  void checkStuck(ArrayList<Tetroid> tList){
    for(int i = 0; i< kids.size(); i++){
      if(kids.get(i).y >= 760){
        stuck = true;
      }
      
      
      for(int j = 0; j < tList.size(); j++){
        if(index != j){
          for(int k = 0; k < tList.get(j).kids.size(); k++){
            if(kids.get(i).y == tList.get(j).kids.get(k).y-40 && kids.get(i).x == tList.get(j).kids.get(k).x ){
              stuck = true;
            }
          }
        }
      }
    }
    
  }
  
  void drop(){
    if(!stuck){
      y += 40;
    }
  }
  
  void checkMovement(ArrayList<Tetroid> tList){
    if(index == tList.size()-1 && stuck == false && keyPressed){
      Boolean canSlideR = true;
      Boolean canSlideL = true;
      for(int i = 0; i<kids.size(); i++){
        if(kids.get(i).x >= 360){
          canSlideR = false;
        } else if (kids.get(i).x == 0){
          canSlideL = false;
        } 
        
        for(int j = 0; j < tList.size(); j++){
          if(index != j){
            for(int k = 0; k < tList.get(j).kids.size(); k++){
              if(kids.get(i).x + 40 == tList.get(j).kids.get(k).x && kids.get(i).y == tList.get(j).kids.get(k).y ){
                canSlideR = false;
              } else if (kids.get(i).x - 40 == tList.get(j).kids.get(k).x && kids.get(i).y == tList.get(j).kids.get(k).y){
                canSlideL = false;
              }
              
            }
          }
        }
      }
      
      if(keyCode == LEFT && canSlideL){
          x -= 40;
          updateKids();
      } else if (keyCode == RIGHT && canSlideR){
          x += 40;
          updateKids();
      } else if (keyCode == UP){
          rot++;
          updateKids();
      } else if (keyCode == DOWN){
          checkStuck(tList);
          if (stuck == false){
            y += 40;
            updateKids();
          }
          checkStuck(tList);
          if (stuck == false){
            y += 40;
            updateKids();
          }
        
      }
    }
    
  }
  
  void updateKids(){
    kids.clear();
    int coro = 40*round(cos(rot*(PI/2)));
    int siro = 40*round(sin(rot*(PI/2)));
    int Lcoro = 40*round( sq2*cos(rot*(PI/2)+PI/4) );
    int Lsiro = 40*round( sq2*sin(rot*(PI/2)+PI/4) );

    if(type == 0){
      kids.add(new Piece(x,y,this,255,0,255));
      kids.add(new Piece(x+coro,y+siro,this,255,0,255));
      kids.add(new Piece(x-coro,y-siro,this,255,0,255));
      kids.add(new Piece(x-siro,y-coro,this,255,0,255));
    } else if(type == 1){
      kids.add(new Piece(x,y,this,0,0,255));
      kids.add(new Piece(x-siro,y-coro,this,0,0,255));
      kids.add(new Piece(x+siro,y+coro,this,0,0,255));
      kids.add(new Piece(x-Lcoro,y+Lsiro,this,0,0,255));
    } else if(type == 2){
      kids.add(new Piece(x,y,this,205,105,0));
      kids.add(new Piece(x-siro,y-coro,this,205,105,0));
      kids.add(new Piece(x+siro,y+coro,this,205,105,0));
      kids.add(new Piece(x+Lcoro,y+Lsiro,this,205,105,0));   
    } else if(type == 3){
      kids.add(new Piece(x,y,this,52,204,255));
      kids.add(new Piece(x-coro,y-siro,this,52,204,255));
      kids.add(new Piece(x+coro,y+siro,this,52,204,255));
      kids.add(new Piece(x+2*coro,y+2*siro,this,52,204,255)); 
    } else if(type == 4){
      kids.add(new Piece(x,y,this,255,255,0));
      kids.add(new Piece(x,y+40,this,255,255,0));
      kids.add(new Piece(x+40,y+40,this,255,255,0));
      kids.add(new Piece(x+40,y,this,255,255,0)); 
    } else if(type == 5){
      kids.add(new Piece(x,y,this,0,255,0));
      kids.add(new Piece(x+siro,y-coro,this,0,255,0));
      kids.add(new Piece(x+coro,y+siro,this,0,255,0));
      kids.add(new Piece(x+Lcoro,y+Lsiro,this,0,255,0)); 
    } else if(type == 6){
      kids.add(new Piece(x,y,this,255,0,0));
      kids.add(new Piece(x-siro,y-coro,this,255,0,0));
      kids.add(new Piece(x-coro,y+siro,this,255,0,0));
      kids.add(new Piece(x-Lcoro,y+Lsiro,this,255,0,0));
    }
    
  }
  
}
