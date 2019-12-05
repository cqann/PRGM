#((2*n)!)/((n!)**2)
import math
size = 3
count = 0
print(math.factorial(40)/(math.factorial(20)**2))

def go(x,y):
    global count
    x_check = x==size
    y_check = y==size
    if x_check and y_check:
        count += 1 
        return
    if not x_check:
        go(x+1,y)
        
    if not y_check:
        go(x,y+1)


go(0,0)
print(count)