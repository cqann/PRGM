
import time 

t0 = time.time()
inpt = 800123123
temp = inpt
level = 0
i = 1

while True:
    i_sq = i**2
    if temp > i_sq:
        temp -= i_sq
        level += 1
    else: 
        break
    i += 2 

print(level)
print(time.time()-t0)
