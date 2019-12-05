
def setup():
    size(1000,1000)
    background(0)
    colorMode(HSB,1000)
    noStroke()
    noFill()

count = 0 
def draw():
    global count
    if count == 1001:
        count = 0
    background(count,1000,1000)
    img = loadImage("filippa car.png")
    circle(500,500,700)
    
    t = "Grattis till"
    t2 = "brumm-brumm-bil-kortet!"
    fill(count,1000,1000)
    textSize(130)
    text(t,180,450)
    textSize(50)
    text(t2,170,600)

    translate(500,500)
    fill(1000)
    
    rotate(-count*PI/500)
    image(img,-100,-350-110+4,200,110)
    
    
    count += 1
