import math
t = int(input())

for test in range(t):
    m = int(input())
    an = 90
    x = 0
    y = 0
    for s in range(m):
        inpt = [float(c) for c in input().split(" ")]
        an += inpt[0]
        d = inpt[1]

        x += math.cos(math.radians(an)) * d
        y += math.sin(math.radians(an)) * d

    x = str(round(x, 6))
    y = str(round(y, 6))

    lx = len(x[x.find(".")+1:])
    ly = len(y[y.find(".")+1:])
    if lx < 6:
        x += "0" * (6-lx)
    if ly < 6:
        y += "0" * (6-ly)
    print(x, y)
