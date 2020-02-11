import colorsys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
import threading
import time
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
                draw.point((x,y),fill=(0,0,0))
            else:
                smooth_count = n + 1 - math.log(math.log2(abs(z)))
                b_one_col = smooth_count / limit
                sqrcol = 180 + int(math.sqrt(180*b_one_col))
                draw.point((x,y),fill=(int(360*b_one_col),360,sqrcol))
    print(str(index)+ " is finished")





def Mandelbrot(surf,re_start,im_start,zoom):
    limit = 300
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

# initialize the pygame module


# create a surface on screen that has the size of 240 x 180
screen_width = 700
screen_height = 700

screen = Image.new("HSV",(700,700))
draw = ImageDraw.Draw(screen)

# load image (it is in same directory)

int_re_start = -2
int_im_start = 1.5
cur_zoom = 3

Mandelbrot(screen,int_re_start, int_im_start, cur_zoom)

screen.show()






