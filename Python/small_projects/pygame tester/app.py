import pygame
import os

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path



# define a main function
def main():
    # initialize the pygame module
    pygame.init()

    # create a surface on screen that has the size of 240 x 180
    screen_width = 454
    screen_height = 240
    screen = pygame.display.set_mode((screen_width, screen_height))

    # load image (it is in same directory)
    bgd = pygame.image.load(os.path.join(resource_path, "bgrnd.png"))
    image = pygame.image.load(os.path.join(resource_path, 'bb.png'))
    caption_str = os.path.split(__file__)[1]+"  keys: a/q: change fps, space: pause/resume, r: start/stop "
    pygame.display.set_caption(caption_str)
    
    image.set_colorkey((255, 0, 255))

    screen.blit(bgd,(0,0))

    xpos = 50
    ypos = 50

    x_step = 5
    y_step = 5

    screen.blit(image, (xpos, ypos))

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

        if xpos>screen_width-64 or xpos<0:
            x_step = -x_step
        if ypos>screen_height-64 or ypos<0:
            y_step = -y_step

        xpos += x_step
        ypos += y_step

        pygame.display.flip()

        screen.blit(bgd,(0,0))
        screen.blit(image,(xpos,ypos))

        clock.tick(30)



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()