import math
  

dim = 700
def setup():
  global dim
  size(dim, dim)
  background(0)
  noStroke()
  fill(102)

def draw():
  background(0)
  global dim
  re_start = -2
  im_start = 1.5
  screen_dis = 3
  
  for y in range(dim):
      print(y)
      for x in range(dim):
          
          c_re = map(x,0,dim,re_start,re_start + screen_dis)
          c_im = map(y,0,dim,im_start,im_start - screen_dis)
          count = brot(c_re,c_im)
          stroke(map(count,0,100,0,255))
          point(x,y)

  noLoop()        

          

def brot(re,im):
    z_re = 0
    z_im = 0
    n = 0 
    max_limit = 100
    while z_re**2 + z_im**2 < 4 and n < max_limit:
        z_re, z_im = z_re**2 - z_im**2 + re, 2*z_re*z_im + im
        n += 1
    
    return n
