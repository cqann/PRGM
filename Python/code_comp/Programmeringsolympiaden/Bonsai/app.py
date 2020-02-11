import sys
from math import *
import pygame 

class Klump:
    def __init__(self, x, y, i, branch):
        self.x = x 
        self.y = y
        self.i = i
        self.n_buds = branch[0]
        self.buds = branch[1:]



N = int(sys.stdin.readline())
klumpar = []
for i in range(N):
    x = int(200*cos((2*i*pi)/N)+300)
    y = int(200*sin((2*i*pi)/N)+300)
    klumpar.append(Klump(x,y,i,[int(x) for x in sys.stdin.readline().split(" ")]))

nexions = []    
for klump in klumpar:
    for bud in klump.buds:
        
        nexions.append((klump.i,bud))

def grow(start):
    splits = [0]
    for bud in start.buds:
        if (start.i,bud) in nexions:
            nexions.remove((start.i,bud))
            nexions.remove((bud,start.i))
            splits[0] += 1
            if len(klumpar[bud].buds) > 1 :
                splits.append(grow(klumpar[bud]))
                
    return max(splits)

#time = grow(klumpar[0])
#print(time)


# define a main function
def main():
    # initialize the pygame module
    pygame.init()

    # create a surface on screen that has the size of 240 x 180
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height),pygame.SRCALPHA)

   
    screen.fill((0,0,0))

    for klump in klumpar:
        pygame.draw.circle(screen,(255,0,0),(klump.x,klump.y),20)

    for nex in nexions:
        k1 = klumpar[nex[0]]
        k2 = klumpar[nex[1]]
        pygame.draw.line(screen,(0,255,0),(k1.x,k1.y),(k2.x,k2.y))
    
    pygame.display.flip()

    clock = pygame.time.Clock()

    running = True
    # main loop
    while running:
        for event in pygame.event.get():
            # only do something if the event if of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # check for keypress and check if it was Esc
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        pygame.display.flip()


        clock.tick(100)



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()



