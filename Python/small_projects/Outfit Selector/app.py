import pygame
from PIL import Image



class Article:

    def __init__(self, surf, type, name, img_dir, color ):
        self.surf = surf
        self.type = type
        self.name = name
        self.img_dir = img_dir
        self.color = color

    def show(self):
        if self.type == "TOP":
            x = 100
            y = 50
        elif self.type == "BOT":
            x = 100
            y = 250
        else:
            x = 100
            y = 600

        self.image = pygame.image.load(self.img_dir)
        self.surf.blit(self.image, (x,y))



def main():
    # initialize the pygame module
    pygame.init()

    # create a surface on screen that has the size of 240 x 180

    width = 500
    height = 700
    screen = pygame.display.set_mode((width, height))

    test = Article(screen,"TOP","test","sam.jpeg","white")
    test.show()

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



        clock.tick(10)



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
