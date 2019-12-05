import pygame
import numpy as np
import colorsys
import random
import math
import os

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path


def selection_sort(arr,compare):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Select the smallest value
            arr_sum = compare[j]
            min_sum = compare[minimum]
            if arr_sum < min_sum:
                minimum = j

        # Place it at the front of the
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr




# define a main function
def main():
    # initialize the pygame module
    pygame.init()

    # create a surface on screen that has the size of 240 x 180
    screen_width = 256*2
    screen_height = 256
    screen = pygame.display.set_mode((screen_width, screen_height))

    # load image (it is in same directory)

    image = pygame.image.load(os.path.join(resource_path, 'photo.jpg'))


    screen.blit(image, (0, 0))


    image_surf = pygame.surfarray.array3d(image)
    image_surf = image_surf[::2,::2]
    image_list = []


    for row in image_surf:
        for column in row:
            image_list.append(column)

    color_list = [colorsys.rgb_to_hsv(int(x[0]),int(x[1]),int(x[2]))[2] for x in image_list]

    print(len(image_list))

    image_list = selection_sort(image_list,color_list)

    for i in range(len(image_surf)):
        for j in range(len(image_surf[i])):
            image_surf[i,j] = image_list[i*len(image_surf[0])+j]




    screen.blit(pygame.surfarray.make_surface(image_surf), (256,0))





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