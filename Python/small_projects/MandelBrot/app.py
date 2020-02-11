import pygame
import colorsys
import threading
import math
import time


def Mandelbrot(surf,re_start,im_start,zoom, brot = True):
    limit = 150#50+math.log10(((4/abs((zoom)))))**5
    old_percent = -1
    for y in range(700):
        for x in range(700):

            if brot:
                #Mandelbrot
                cur_c = complex(re_start + x*(zoom/700), im_start - y*(zoom/700))
                z = complex(0, 0)
            else:
                #Julia
                cur_c = complex(re_start, im_start)
                z = complex(-2 + x * (zoom / 700), 1.5 - y * (zoom / 700))


            count, z = MandelCounter(limit,z,cur_c)

            if count == limit:
                pygame.draw.rect(surf, (0, 0, 0), pygame.Rect(x, y, 1, 1))
            else:
                smooth_count = count + 1 - math.log(math.log2(abs(z)))
                b_one_col = smooth_count/limit
                col = colorsys.hsv_to_rgb(b_one_col, 1, 1)
                pygame.draw.rect(surf,(col[0]*255,col[1]*255,col[2]*255), pygame.Rect(x, y, 1, 1))

        percent = math.floor(y/7)
        if old_percent != percent:
            print(str(percent) + "%")
            old_percent = percent

    print("done")


def MandelCounter(limit,z, c):
    n = 0

    while abs(z) < 2 and n < limit:
        z = z * z + c
        n += 1

    return n, z


# define a main function
def main():
    # initialize the pygame module
    pygame.init()


    # create a surface on screen that has the size of 240 x 180
    screen_width = 700
    screen_height = 700
    disp = pygame.display.set_mode((screen_width, screen_height),pygame.SRCALPHA)
    screen = pygame.Surface((700,700))

    # load image (it is in same directory)

    int_re_start = -2
    int_im_start = 1.5
    cur_zoom = 3
    t0 = time.time()
    Mandelbrot(screen,int_re_start, int_im_start, cur_zoom)
    print(time.time()-t0)
    rec_screen = pygame.Surface((87,87))
    pygame.draw.rect(rec_screen,pygame.Color(200,200,200,a=50),pygame.Rect(0,0,87,87))

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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_j:
                Mandelbrot(screen,int_re_start,int_im_start,3, brot=False)

        if pygame.mouse.get_pressed()[0]:
            screen.fill((0,0,0))
            int_re_start = int_re_start + pygame.mouse.get_pos()[0]*(cur_zoom/700)
            int_im_start = int_im_start - pygame.mouse.get_pos()[1]*(cur_zoom/700)
            cur_zoom = cur_zoom / 8
            print(str(pygame.mouse.get_pos()[0]) + ", " + str(pygame.mouse.get_pos()[1]))
            print(str(int_re_start) + ", " + str(int_im_start))
            Mandelbrot(screen, int_re_start , int_im_start , cur_zoom)


        disp.blit(screen, (0, 0))
        disp.blit(rec_screen,(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))


        pygame.display.flip()


        clock.tick(10)



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()


