#cos(k*x+y)-sin(x-k*y) OUTZOOM SPIN SQUARE
#cos(sin(x)*k+sin(y*k)) MASH WAVE
#sin(k*sin(y-k)+k*cos(x+k)) GRAZING CIRCLES
#sin(k*cos(x+y))+cos(k*sin(x+y)) STRIPES OSCILATION
#cos(x+y+k)/(tan(x*y)+1) STAR WAVE
#sin(x*cos(y-k))/sin(x*cos(k)) SHIFT DUNNO
#cos(k+y+sin(x))-sin(k-x+cos(y)) HAMMER MORPH
#cos(k*sin(y-x))-sin(k*cos(x+y)) FRACTAL BLOBS
#cos(k*sin(y%x))-sin(k*cos(x%y)) SPINNING WINGS
#cos(k*(y%cos(x)))-sin(k*(x%sin(y))) BIG BAD WTF
#tan(k*cos(x))/cos(x-y) ROMBER OCH OVALER
#cos(y+k*x) + sin(x-y*k*sin(x*x-y-y*y))-cos(k*y) - sin(x-k*y*sin(x*x-y)) LONG BEADS
W = 800
H = 800
count = 400
save_count = count
x_intv = W/count 
y_intv =  H/count 
r = 0.5 * (W/count)

xmin = -5
xmax = 5
ymin = -5
ymax = 5

k = 1
stopped = False


def setup():
    global pg,sh
    size(W,H)
    colorMode(HSB)
    





class Tilt:
    def __init__(self,x,y,angle,col):
        self.x = x 
        self.y = y
        self.angle = angle 
        self.rev_angle = angle + PI
        self.col = col
    
    def show(self):
        stroke(self.col[0],self.col[1],self.col[2])
        fill(self.col[0],self.col[1],self.col[2])
        #line(self.x+r*cos(self.angle),self.y+r*sin(self.angle),self.x+r*cos(self.rev_angle),self.y+r*sin(self.rev_angle))
        #circle(self.x,self.y,r)
        rectMode(CENTER)
        rect(self.x,self.y,r*2,r*2)




    
def draw():
    global k, stopped, count, x_intv, y_intv, r, pg, sh
    
    if keyPressed:
        if key == "g":
            print(k)
            count = 400
            x_intv = W/count 
            y_intv =  H/count 
            r = 0.5 * (W/count)
            stopped = True
        if key == "p":
            count = 100
            x_intv = W/count 
            y_intv =  H/count 
            r = 0.5 * (W/count)
            stopped = False
    
    background(0)
    
    tilts = []
    
    
    for i in range(count):
        co_y = i * y_intv + (H/count)/2
        y = -float(map(co_y,0,H,ymin,ymax))
        for j in range(count):
            co_x = j * x_intv + (W/count)/2
            x = float(map(co_x,0,W,xmin,xmax))
            
            dy = cos(x) + y
                            
            angle = -atan(dy)
            rev_angle = angle + PI
            tilts.append(Tilt(co_x,co_y,angle,[map(angle+HALF_PI,0,PI,0,255),255,255]))
    
    
    for tilt in tilts:
        tilt.show()
    stroke(255)
    line(0,400,800,400)
    line(400,0,400,800)
    
    if not stopped:
        k += 0.05

        
