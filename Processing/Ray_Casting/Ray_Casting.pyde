
sx = 300
sy = 300
ray_count = 500
const_rays = []
midray = 10.0
fov = 0.15
incr = TWO_PI/ray_count

def calc_dis(x,y):
    #circle x=300 y=400 r=100
    #circle x=200 y=500 r=50
    dis1 = dist(x,y,300,400)-50
    dis2 = dist(x,y,300,300)-50
    #line x1,y1 = 300,50 x2,y2 = 550,300
    
    dis3 = dist_line(PVector(x,y),PVector(0,0),PVector(600,0))
    dis4 = dist_line(PVector(x,y),PVector(0,0),PVector(0,600))
    dis5 = dist_line(PVector(x,y),PVector(600,600),PVector(0,600))
    dis6 = dist_line(PVector(x,y),PVector(600,600),PVector(600,0))


    #print(str(dis1)+", " + str(dis2)+", " +str(dis3))
    return min(dis1,dis2,dis3,dis4,dis5,dis6)

def dist_line(p,a,b):
    pa = p.sub(a)
    ba = b.sub(a)
    h = clamp( pa.dot(ba)/ba.dot(ba), 0, 1 )
    finvec = pa.sub(ba.mult(h))
    return sqrt(finvec.x*finvec.x+finvec.y*finvec.y)


def clamp(x,MIN,MAX):
    if x<MIN:
        x = MIN
    elif x > MAX:
        x = MAX
    return x 

def smin( a, b):
    k = 0.0001
    h = max( k-abs(a-b), 0 )/k
    return min( a, b ) - h*h*k*(1/4)


class Ray:
    def __init__(self,x,y,dir):
        self.x = x 
        self.y = y
        self.dir = dir 
        self.dis = self.march()
        
    def march(self):
        scape_dis = 2000
        min_val = 0.5
        
        new_x = self.x
        new_y = self.y
        
        cur_dis = calc_dis(self.x,self.y)
        
        while cur_dis > min_val and cur_dis < scape_dis:
            new_x += cur_dis*cos(self.dir)
            new_y += cur_dis*sin(self.dir)
            cur_dis=calc_dis(new_x,new_y)
        
        #stroke(map(cur_dis,scape_dis,0,0,255))
        #circle(new_x,new_y,2)
        return dist(self.x,self.y,new_x,new_y)
    
    def update(self,x,y):
        self.x = x 
        self.y = y
        self.dis = self.march()
        self.show()
    
    def show(self):
        strokeWeight(1)
        stroke(255,70)
        line(self.x,self.y,self.dis*cos(self.dir)+self.x,self.dis*sin(self.dir)+self.y)
        
class Stripe:
    def __init__(self,index,brig,an,wid,dis):
        self.index = index
        self.brig = brig
        self.an = an 
        self.wid = wid 
        self.dis = dis
        self.hei = 80*(600/(cos(self.an)*self.dis+0.01)) 
    
    def show(self):
        fill(self.brig)
        strokeWeight(1)
        stroke(self.brig)
        rect(600+self.wid/2+self.index*self.wid,300,self.wid,self.hei)
        

for i in range(ray_count):
    cur_dir = incr * i
    const_rays.append(Ray(0,0,cur_dir))

def setup():
    size(1200,600)
    background(0)
    frameRate(120)
    noStroke()
    noFill()

def draw():
    background(0)
    stroke(255)
    rectMode(CENTER)
    global midray,sx,sy
    
    lookan = (midray/ray_count)*TWO_PI

    if keyPressed:
        if key == 'a' or key == 'A':
            midray -= 10
            if midray < 0:
                midray += ray_count 
            elif midray > ray_count:
                midray -= ray_count
        if key == 'd' or key == 'D':
            midray += 10
            if midray < 0:
                midray += ray_count 
            elif midray > ray_count:
                midray -= ray_count 
        if key == 'w' or key == 'W':
            sx += 10*cos(lookan)
            sy += 10*sin(lookan)
        if key == 's' or key == 'S':
            sx -= 10*cos(lookan)
            sy -= 10*sin(lookan) 
 
    rays= []
    spread = int(fov*ray_count)
    for i in range(spread):
        val = midray + spread/2-i
        if val < 0:
            val += ray_count
        elif val >= ray_count:
            val -= ray_count
        rays.append(const_rays[int(val)])

    
    
    stripes_dis = []

    for ray in rays:
        ray.update(sx,sy)
        stripes_dis.append(ray.dis)
    
  
    stripW = 600/len(stripes_dis)
    an_steps = TWO_PI/ray_count
    stripes_dis.reverse()
    stripes = []
    
    for i in range(len(stripes_dis)):
        sqstrip = stripes_dis[i]**2
        brig = map(sqstrip,0,850**2,255,0)
        an = -(fov*TWO_PI)/2 + i*an_steps
        stripes.append(Stripe(i,brig,an,stripW,stripes_dis[i]))
        stripes[i].show()

    
    
    strokeWeight(5)
    #line(300,50,550,300)
