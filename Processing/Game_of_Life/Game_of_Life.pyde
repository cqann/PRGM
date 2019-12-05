add_library('pdf')
sizeX = 1000
sizeY = 1000
n = 200
cells = [None]*n
GOTIME = False
recording = False 

class Cell:
    def __init__(self,x,y,side,alive,nb):
        self.x = x
        self.y = y
        self.side = side
        self.alive = alive 
        self.nb = nb
    
    def show(self):
        if self.alive:
            circle(self.x+self.side/2,self.y+self.side/2,self.side*1)
            #rect(self.x+self.side/2,self.y+self.side/2,self.side*3,self.side*3)
            
    def flip(self):
        if self.alive:
            self.alive = False
        else: 
            self.alive = True



def setup():
    global cells
    size(sizeX,sizeY)
    frameRate(60)
    background(0)
    colorMode(HSB)
    noStroke()
    
    side = width/n
    for y in range(n):
        cells[y] = []
        for x in range(n):
            cells[y].append(Cell(x*side,y*side,side,False,0))
    

time = 1
def draw():
    global cells, GOTIME, time, recording
    if keyPressed: 
        if key == "g":
            GOTIME = True
        if key == "c":
            GOTIME = False
            for rows in cells:
                for cell in rows:
                    cell.alive = False
        if key == "r":
            recording = True
            beginRecord(PDF,"GOL.pdf")
            print("recording")
    
    background(0)
    noStroke()
    colorMode(HSB)
    rectMode(CENTER)
    mX = 0
    mY = 0
    time += 1 

   
    
    
    if mousePressed:
        print("press")
        mX = int(map(mouseX,0,sizeX,0,len(cells)))
        mY = int(map(mouseY,0,sizeY,0,len(cells)))
        rX = len(cells)-mX
        rY = len(cells)-mY
        
        cells[mY][mX].alive = True
        cells[mY][rX].alive = True 
        cells[rY][mX].alive = True
        cells[rY][rX].alive = True
    
    
    
                    
    if GOTIME:
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                neighbours = 0 
                for y in range(3):
                    for x in range(3):
                        if x==1 and y==1:
                            continue
                        try: 
                            t = cells[i-1+y][j-1+x]
                        except IndexError:
                            continue
                        if cells[i-1+y][j-1+x].alive:
                            neighbours += 1
                cells[i][j].nb = neighbours
    
    
    for y in range(len(cells)):
        for x in range(len(cells[y])):
            if GOTIME:
                if cells[y][x].alive:
                    if cells[y][x].nb < 2 or (cells[y][x].nb>3 and cells[y][x].nb<6) :
                        cells[y][x].flip()
                
                else: 
                    if cells[y][x].nb == 3:
                        cells[y][x].flip()
                if cells[y][x].alive:
                    hu = find_hu(cells,x,y)
                    fill(hu[0],hu[1],hu[2])
            cells[y][x].show()
    
    if recording:
        endRecord()
        recording = False
    

def find_hu(cells,x,y):
    curC = cells[y][x]
    fact = (255/8)
    bgfact = 255/30
    r = fact*curC.nb
    glist = 1
    blist = 1
    for i in range(3):
        for j in range(3):
            try:
                placeholder = cells[y-1+i][x-1+j]
            except IndexError:
                continue
            if i == 0:
                if j == 0:
                    blist += cells[y-1+i][x-1+j].nb
                elif j == 1:
                    glist += cells[y-1+i][x-1+j].nb
                else:
                    blist += cells[y-1+i][x-1+j].nb
            if i == 1:
                if j == 0:
                    glist += cells[y-1+i][x-1+j].nb
                elif j == 1:
                    continue
                else:
                    glist += cells[y-1+i][x-1+j].nb
            if i == 2:
                if j == 0:
                    blist += cells[y-1+i][x-1+j].nb
                elif j == 1:
                    glist += cells[y-1+i][x-1+j].nb
                else:
                    blist += cells[y-1+i][x-1+j].nb
       
   
    g = bgfact * glist 
    b = bgfact * blist
    
    return (r,g,b)
            
    
                
         
