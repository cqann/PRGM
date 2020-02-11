import pygame
import random
import math
import os





# define a main function
def main():
    # initialize the pygame module
    pygame.init()

    # create a surface on screen that has the size of 240 x 180
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # load image (it is in same directory)



    screen.fill((0,0,255))
    pygame.draw.circle(screen,(0,255,0),(300,300),300)

    dots_within = 0
    dots = 0


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
                print((dots_within/dots)*4)

        x = random.randint(1, 599)
        y = random.randint(1, 599)

        if math.sqrt((x-300)**2 + (y-300)**2) <= 300:
            dots_within += 1

        #print(str(x)+", " + str(y))


        dots += 1
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 3)

        pygame.display.flip()


        clock.tick(100)



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()