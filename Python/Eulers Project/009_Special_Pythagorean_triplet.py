import math
def is_trip(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    return False

for a in range(1,999):
    for b in range(1,999):
        c = math.sqrt(a**2 + b**2)
        if c == round(c) and a+b+c == 1000:
            print(a*b*c)

print("done")