import pygame
import random
import math
import os

def fractal(surf,x,y,rad,size):
    color = (-(size - 255), 100, size)
    side = rad/math.sqrt(2)

    pygame.draw.circle(surf,color,(x,y),rad)
    pygame.draw.rect(surf,(0,0,0),pygame.Rect(x-side,y-side,2*side,2*side))

    if size < 0.05*255:
        return

    fractal(surf,x,y,round(side),size*0.8)



def tate(point,center,angle):
    dis = math.sqrt((point[0]-center[0])**2+(point[1]-center[1])**2)
    beta_angle= (180-angle)/2
    O = math.cos(beta_angle)*dis
    x = math.cos(angle)*dis + (point[0]-center[0])
    y = math.sin(angle)*dis - (point[1]-center[1])
    return (point[0]-x,point[1]+y)






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

    fractal(surface,350,350,350,255)

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