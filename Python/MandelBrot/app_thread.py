import colorsys
import threading
import time
import pygame
import math


def MandelCounter(surf, limit,workers,index,re_start,im_start,zoom):
    chunk = int(700/workers)
    print(str(index)+ " is starting")
    for y in range(index*chunk,(index+1)*chunk):
        for x in range(700):
            c = complex(re_start + x * (zoom / 700), im_start - y * (zoom / 700))
            z = complex(0, 0)
            n = 0
            while abs(z) < 2 and n < limit:
                z = z * z + c
                n += 1

            if n == limit:
                pygame.draw.rect(surf, (0, 0, 0), pygame.Rect(x, y, 1, 1))
            else:
                smooth_count = n + 1 - math.log(math.log2(abs(z)))
                b_one_col = smooth_count / limit
                col = colorsys.hsv_to_rgb(b_one_col, 1, 1)
                pygame.draw.rect(surf, (col[0] * 255, col[1] * 255, col[2] * 255), pygame.Rect(x, y, 1, 1))
    print(str(index)+ " is finished")





def Mandelbrot(surf,re_start,im_start,zoom):
    limit = 50
    workers = 5
    threads = list()
    t0 = time.time()


    for i in range(workers):
        th = threading.Thread(target=MandelCounter,args=(surf,limit,workers,i,re_start,im_start,zoom))
        threads.append(th)
        th.start()
    for i in range(workers):
        threads[i].join()


    print(time.time()-t0)




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

    Mandelbrot(screen,int_re_start, int_im_start, cur_zoom)

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


