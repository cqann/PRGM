import math

gr = 1.61803398874989484820458
width = 800
height = 800 
time = 0

class Spinner:
    def __init__(self, x,y,rad,v):
        self.x = x
        self.y = y 
        self.rad = rad 
        self.v = v
    
    def show(self,time):
        self.px = self.rad*math.cos(self.v*time)+self.x
        self.py = self.rad*math.sin(self.v*time)+self.y
        
        noFill()
        stroke(255)
        strokeWeight(1)
        ellipse(self.x,self.y,self.rad*2,self.rad*2)
        fill(255)
        strokeWeight(3)
        ellipse(self.px,self.py,3,3)

class Pattern:
    def __init__(self,loc):
        self.pnt = []
        self.loc = loc 
    
    def show(self):
        strokeWeight(1)
        point(self.pnt[0],self.pnt[1])

def setup(): 
  global width, height
  size(width, height )
  background(0)
  noStroke()
  fill(102)

v = 0.005
count = 4
xSpinners = []
ySpinners = []

for i in range(1,count):
    xSpinners.append(Spinner(50+i*width/count,0.4*width/count,0.4*width/count,v*(i+1)))
    ySpinners.append(Spinner(0.4*height/count,50+i*height/count,0.4*height/count,v*(i+1)))

pats = []
for i in range(len(ySpinners)):
    for j in range(len(xSpinners)):
        pats.append(Pattern((j,i)))
    

def draw():
    global time,xSpinners,ySpinners,pat,count
    fill(0)
    rect(0,0,width,0.8*width/count)
    rect(0,0,0.8*height/count,height)
    
    for spinner in xSpinners:
        spinner.show(time)
    
    for spinner in ySpinners:
        spinner.show(time)
    
    for pat in pats:
        pat.pnt =  ( xSpinners[pat.loc[0]].px,ySpinners[pat.loc[1]].py ) 
        pat.show()

    time += 1

    
