
t = 0

def setup():
    size(600,600)
    
    '''
    noStroke()
    fill(255,255,0,255)
    circle(0,0,40)
    '''

def draw():
    global t
    background(0)
    translate(width/2,height/2)
    stroke(255)
    #fill(255)
    noFill()
    
    n = 7#6 - 6*cos(radians(t)/10)
    d = 180 - 180*sin(radians(t)/10)
    
    beginShape()
    for i in range(361):
        k = radians(i*d)
        r = sin(n*k)
        x = width/2 * r * cos(k)
        y = -height/2 * r * sin(k)
        vertex(x,y)
    endShape()
    
    
    t += 0.5
