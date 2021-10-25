
from PIL import Image


im = Image.open("cesarkinanew.png")   
c = 0
tc = 0
width, height = im.size
for x in range(width):
    for y in range(height):
        s = im.getpixel((x,y))
        r,g,b = s
        if r == 0 and b == 228 and g == 255:
            c += 1
        tc += 1

print("Count is: ", c)
print("Total", tc)
print("Ratio is:", c/tc)












