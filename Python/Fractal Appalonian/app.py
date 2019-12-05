import pygame
import numpy as np
from scipy import optimize
import itertools
import random
import math
import os

class C:
    def __init__(self,x,y,rad,col):
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col
        self.tup = (x,y,rad)

def tate(point,center,angle):
    dis = math.sqrt((point[0]-center[0])**2+(point[1]-center[1])**2)
    beta_angle= (180-angle)/2
    O = math.cos(beta_angle)*dis
    x = math.cos(angle)*dis + (point[0]-center[0])
    y = math.sin(angle)*dis - (point[1]-center[1])
    return (point[0]-x,point[1]+y)


def func_solve(nums,c1,c2,c3):
    x = nums[0]
    y = nums[1]
    r = nums[2]

    F = [None]*3
    F[0] = (x - c1[0]) ** 2 + (y - c1[1]) ** 2 - (r - c1[2]) ** 2
    F[1] = (x - c2[0]) ** 2 + (y - c2[1]) ** 2 - (r - c2[2]) ** 2
    F[2] = (x - c3[0]) ** 2 + (y - c3[1]) ** 2 - (r - c3[2]) ** 2
    return F

def find_create_circle(circ_list,num_str):
    range_list = num_str
    iter_list = list(itertools.combinations(range_list, 2))

    for h in range(len(range_list)):
        comb_index1 = int(iter_list[h][0])
        comb_index2 = int(iter_list[h][1])

        numsGuess = (350, 350, 1)
        for i in range(500):
            point_test = (350 * math.cos(0.002 * i * 2 * math.pi) + 350, -350 * math.sin(0.002 * i * 2 * math.pi) + 350, 1)
            res = optimize.fsolve(func_solve, numsGuess, args=(circ_list[comb_index1].tup, point_test, circ_list[comb_index2].tup))
            while round(res[2] / 10) * 10 == 350:
                numsGuess = (random.randint(1, 700), random.randint(1, 700), 1)
                res = optimize.fsolve(func_solve, numsGuess, args=(circ_list[comb_index1].tup, point_test, circ_list[comb_index2].tup))
            if abs(math.sqrt((point_test[0] - circ_list[comb_index1].x) ** 2 + (point_test[1] - circ_list[comb_index1].y) ** 2) - math.sqrt((point_test[0] - circ_list[comb_index2].x) ** 2 + (point_test[1] - circ_list[comb_index2].y) ** 2)) < 0.28:
                to_draw = res
                # circs.append(C(point_test[0],point_test[1],5,(0,0,255)))
                if abs(to_draw[2])<160:
                    circ_list.append(C(to_draw[0], to_draw[1], to_draw[2], (0, 0, 0)))
                    print(to_draw)
                    break

def cr_cr(radius,circs):
    for y in screen_height:
        for x in screen_width:
            d_big = math.sqrt((x-350)**2+(y-350)**2)
            if 350 > (d_big+radius):

                for c in circs:
                    d = math.sqrt((x-c.x)**2+(y-c.y)**2)
                    if (radius + c.r) < d:
                        return C(x,y,radius,(0,0,0))
    return None






# define a main function
def main():
    # initialize the pygame module
    pygame.init()


    # create a surface on screen that has the size of 240 x 180
    screen_width = 700
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height),pygame.SRCALPHA)

    # load image (it is in same directory)
    surface = pygame.Surface((screen_width , screen_height), pygame.SRCALPHA)
    rotated_surf = surface
    rect = surface.get_rect()
    angle = 0

    surface.fill((0,0,0))

    pygame.draw.circle(surface,(255,0,0),(350,350),350)

    big_circle = (350,350,350)
    circs = [C(350, 350 - 187, 163,(0,0,0)), C(350 + 163, 350 + 92, 163,(0,0,0)), C(350 - 163, 350 + 92, 163,(0,0,0))]


    for i in range(78):
        current_r = 79-i

        for y in range(screen_height):
            for x in range(screen_width):
                if (x-350)**2+(y-350)**2 <= 350**2:
                    d_big = math.sqrt((x - 350) ** 2 + (y - 350) ** 2)
                    if 350 > (d_big + current_r):
                        intersect = False
                        for c in circs:
                            d = (x - c.x) ** 2 + (y - c.y) ** 2
                            if (current_r + c.rad)**2 > d:
                                intersect = True
                        if not intersect:
                            circs.append(C(x, y, current_r, (0, 0, 0)))





    #find_create_circle(circs,"012")
    #find_create_circle(circs,"0123")






    for circle in circs:
        pygame.draw.circle(surface,circle.col,(int(circle.x),int(circle.y)),abs(int(circle.rad)))










    screen.blit(surface,(0,0))
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



'''
    -----------------------------------------------------------------------------------------------------------------------------------------------------
    CIRCLES WITHIN
    def fractal(surf,rad, size):
        color = (-(size-255),100,size)
        pygame.draw.circle(surf,color,(300,300),int(rad))
        pygame.draw.circle(surf,(0,0,0),(300,300),int(rad*0.95))



    if (size < 0.01*255):
        return

    fractal(surf, rad*0.85, size*0.8)
    -----------------------------------------------------------------------------------------------------------------------------------------------------
    SIERPINSKI TRIANGLE
    def fractal(surf,x,y,height,base, size):
        color = (-(size-255),100,size)
    
        pygame.draw.polygon(surf,color,[(x,y),(x-base/2,y+height),(x+base/2,y+height)])
        pygame.draw.polygon(surf,(0,0,0),[(x,y+height),(x-math.tan(math.pi/6)*(height/2),y+height/2),(x+math.tan(math.pi/6)*(height/2),y+height/2)])
    
    
        if (size < 0.3*255):
            return
    
        fractal(surf, x, y,int(height/2), int(base/2), size*0.8)
        fractal(surf, int(x-math.tan(math.pi/6)*(height/2)), int(y+height/2), int(height/2), int(base/2), size*0.8)
        fractal(surf, int(x+math.tan(math.pi/6)*(height/2)), int(y+height/2), int(height/2), int(base/2), size*0.8)
    -----------------------------------------------------------------------------------------------------------------------------------------------------
    CIRCELINSKI TRIANGLE
    def fractal(surf,x,y,height,base, size):
        color = (-(size-255),100,size)
    
        pygame.draw.polygon(surf,color,[(x,y+height),(x-math.tan(math.pi/6)*(height/2),y+height/2),(x+math.tan(math.pi/6)*(height/2),y+height/2)])
        circle_y = int( y + height - base / ( 2 * math.sqrt(3) ) )
        pygame.draw.circle( surf,(0,0,0),(x,circle_y),int(base / ( 4 * math.sqrt(3) )))
    
        if (size < 0.3*255):
            return
    
        fractal(surf, x, y,int(height/2), int(base/2), size*0.8)
        fractal(surf, int(x-math.tan(math.pi/6)*(height/2)), int(y+height/2), int(height/2), int(base/2), size*0.8)
        fractal(surf, int(x+math.tan(math.pi/6)*(height/2)), int(y+height/2), int(height/2), int(base/2), size*0.8)
    -----------------------------------------------------------------------------------------------------------------------------------------------------
    SIERPINSKI CARPET
    def fractal(surf,x,y,side, size):
    color = (-(size-255),100,size)

    pygame.draw.rect(surf, color, pygame.Rect(int(x),int(y),int(side),int(side)))
    pygame.draw.rect(surf, (0, 0, 0), pygame.Rect(int(x+side/3),int(y+side/3), int(side/3), int(side/3)))

    if (size < 0.4*255):
        return

    fractal(surf, x, y, side / 3, size * 0.8)
    fractal(surf, x + side / 3, y, side / 3, size * 0.8)
    fractal(surf, x + 2 * side / 3, y, side / 3, size * 0.8)
    fractal(surf, x + 2 * side / 3, y + side / 3, side / 3, size * 0.8)
    fractal(surf, x, y + side / 3, side / 3, size * 0.8)
    fractal(surf, x, y + 2 * side / 3, side / 3, size * 0.8)
    fractal(surf, x + side / 3, y + 2 * side / 3, side / 3, size * 0.8)
    fractal(surf, x + 2 * side / 3, y + 2 * side / 3, side / 3, size * 0.8)
    -----------------------------------------------------------------------------------------------------------------------------------------------------
    CIRCLES ROUND CIRCLES 
    def fractal(surf,x,y,rad, size):
        color = (-(size-255),100,size)
    
        pygame.draw.circle(surf,color,(int(x),int(y)),int(rad))
    
        if (size < 0.3*256):
            return
    
        for i in range(8):
    
            x_coord = int(1.5*rad*math.cos(((2*math.pi)/8)*i)+x)
            y_coord = int(1.5*rad*math.sin(((2*math.pi)/8)*i)+y)
    
            if surf.get_at((x_coord,y_coord)) == (0,0,0):
                fractal(surf,x_coord,y_coord,rad*0.4,size*0.8)
                

'''