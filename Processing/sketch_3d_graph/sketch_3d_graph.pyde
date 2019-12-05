add_library('peasycam')

scl = 10.0
start = -HALF_PI
finish = HALF_PI
xlist = []
ylist = []
t = 0
rotX = True  

def setup():
    global cam
    size(600,600,P3D)
    background(0)
    stroke(255)
    strokeWeight(3)
    
    cam = PeasyCam(this,300,300,0, 600)
    
    xfact = scl/width
    yfact = scl/height
    
    for i in range(width):
        xval = -scl/2+xfact*i
        x = xval/xfact
        if xval>start and xval<finish:
            d = sin(xval)
            
            for j in range(100):
                zval = d*cos(j*(PI/50))
                yval = d*sin(j*(PI/50))
                y = yval/yfact
                z = zval/yfact
                xlist.append((x,-y,z))
            
            for j in range(100):
                zval = xval*sin(j*(PI/50))
                nxval = xval*cos(j*(PI/50)) 
                nx = nxval/xfact
                y = d/yfact
                z = zval/xfact
                ylist.append((nx,-y,z))
               
    

def draw():
    global rotX,t
    background(0)
    line(0,300,600,300)
    line(width/2,0,width/2,height)
    
    if t%5 == 0:
        if keyPressed:
            if key == 'b':
                if rotX:
                    rotX = False
                else:
                    rotX = True
    
    
    translate(width/2,height/2,0)
    
    noFill()
    beginShape()
    if rotX:
        for p in xlist:
            vertex(p[0],p[1],p[2])
    else:
        for p in ylist:
            vertex(p[0],p[1],p[2]) 
    endShape()
    
    t += 1 
    
