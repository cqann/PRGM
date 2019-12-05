add_library('peasycam')

x = 1
y = 0
z = 0

p = 0.2
o = 0.2
B = 5.7

plist =  []
time = 0 

def setup():
    global cam
    size(600,600,P3D)
    background(0)
    colorMode(HSB)
    frameRate(120)

    cam = PeasyCam(this,230,370,0, 600)
    #cam.setMinimumDistance(50)
    #cam.setMaximumDistance(500)

    
def draw():
    global x,y,z,p,o,B,time
    translate(width/2,height/2)
    background(0)
    
    scl = 15
    rotateX(-.5)
    rotateY(-.5)
    
    dt = 0.05
    dx = (-y-z)*dt
    dy = (x+p*y)*dt
    dz = (o+z*(x-B))*dt
    
    x += dx
    y += dy
    z += dz
    
    plist.append(PVector(x,y,z).mult(scl))

    hu = 0 
    for i in range(len(plist)):
        if hu == 255:
            hu = 0
        if i != 0:
            stroke(hu,255,255)
            line(plist[i].x,plist[i].y,plist[i].z,plist[i-1].x,plist[i-1].y,plist[i-1].z)
            hu += 1
    
    time += 1 
