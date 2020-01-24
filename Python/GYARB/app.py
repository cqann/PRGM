
from PIL import Image


im = Image.open("6.png")   
c = 0
tc = 0
width, height = im.size
for x in range(width):
    for y in range(height):
        s = im.getpixel((x,y))
        r,g,b = s
        if r == 255 and b == 0:
            if g == 0:
                c += 1
            tc += 1

print("Count is: ", c)
print("Ratio is:", c/tc)












