
t = 110.01

def setup():
    size(1000,1000)
    
    '''
    noStroke()
    fill(255,255,0,255)
    circle(0,0,40)
    '''

def draw():
    global t
    background(0)
    translate(width/2,height/2)
    #fill(255)
    noFill()
    
    n = 7#6 - 6*cos(radians(t)/10)
    d = 180 - 180*sin(radians(t)/10)
    
    lastx = 0
    lasty = 0
    for i in range(361):
        stroke(255*abs(cos(i/100)),255*abs(sin(i/100)),255*abs(sin(i/100+0.97)))
        k = radians(i*d)
        r = sin(n*k)
        x = width/2 * r * cos(k)
        y = -height/2 * r * sin(k)
        line(x,y,lastx,lasty)
        lastx = x
        lasty = y
    
    
    t += 0.0001
