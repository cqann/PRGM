import pygame as pg
import random
import math
import os
import pygame

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path

screen_width = 400
screen_height = 400


class Boat:
    def __init__(self, x, y, prob):
        self.x = x
        self.y = y
        self.prob = prob

class Board:
    def __init__(self):
        self.point_A = (random.randint(1, screen_width+1), random.randint(1, screen_height+1))
        self.point_B = (random.randint(1, screen_width+1), random.randint(1, screen_height+1))
        self.point_C = (random.randint(1, screen_width+1), random.randint(1, screen_height+1))
        self.dis_AB = math.sqrt(math.pow(self.point_A[0] - self.point_B[0], 2) + math.pow(self.point_A[1] - self.point_B[1], 2))
        self.dis_AC = math.sqrt(math.pow(self.point_A[0] - self.point_C[0], 2) + math.pow(self.point_A[1] - self.point_C[1], 2))
        self.dis_BC = math.sqrt(math.pow(self.point_B[0] - self.point_C[0], 2) + math.pow(self.point_B[1] - self.point_C[1], 2))
    
        self.point_S = (0, random.randint(1, screen_height+1))
        self.point_E = (screen_width, random.randint(1, screen_height+1))

        self.y_steps = (self.point_E[1] - self.point_S[1]) / screen_width
    
        self.my_boat = Boat(self.point_S[0], self.point_S[1], 0)

# define a main function
def main():
    # initialize the pygame module
    pygame.init()

    # create a surface on screen that has the size of 240 x 180

    screen = pygame.display.set_mode((screen_width, screen_height))

    # load image (it is in same directory)
    image = pygame.image.load(os.path.join(resource_path, 'bb.png'))
    image.set_colorkey((255, 255, 255))

    my_board = Board()

    screen.fill((0,0,255))
    pygame.draw.polygon(screen, (255,0,0), [my_board.point_A,my_board.point_B,my_board.point_C])
    pygame.draw.circle(screen,(160,160,0),(my_board.my_boat.x,my_board.my_boat.y),5)

    pygame.display.flip()

    clock = pygame.time.Clock()
    survived = 0
    died = 0

    running = True
    # main loop
    while running:
        for event in pygame.event.get():
            # only do something if the event if of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                print(str(survived)+ ", " + str(died))
                running = False
            # check for keypress and check if it was Esc
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print(str(survived) + ", " + str(died))
                running = False

        my_board.my_boat.x += 1
        my_board.my_boat.y += my_board.y_steps

        dis_BoatA = math.sqrt(math.pow(my_board.point_A[0] - my_board.my_boat.x, 2) + math.pow(my_board.point_A[1] - my_board.my_boat.y, 2))
        dis_BoatB = math.sqrt(math.pow(my_board.point_B[0] - my_board.my_boat.x, 2) + math.pow(my_board.point_B[1] - my_board.my_boat.y, 2))
        dis_BoatC = math.sqrt(math.pow(my_board.point_C[0] - my_board.my_boat.x, 2) + math.pow(my_board.point_C[1] - my_board.my_boat.y, 2))


        pygame.display.flip()

        screen.fill((0,0,255))
        pygame.draw.polygon(screen, (255, 0, 0), [my_board.point_A, my_board.point_B, my_board.point_C])

        if screen.get_at((math.floor(my_board.my_boat.x),math.floor(my_board.my_boat.y))) == (255,0,0):
            my_board.my_boat.prob += 0.009
            if random.random() < my_board.my_boat.prob:
                died += 1
                my_board = Board()



        if my_board.my_boat.x == screen_width - 1:
            screen.fill((0, 255, 0))
            survived += 1
            my_board = Board()

        pygame.draw.circle(screen, (160, 160, 0), (math.floor(my_board.my_boat.x), math.floor(my_board.my_boat.y)), 5)

        clock.tick(1000)



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()


