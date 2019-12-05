import time
import random
import sys

inpt = ""
for i in range(1000000):
    if random.random() > 0.5:
        inpt += "B"
    else:
        inpt += "V"

t0 = time.time()

inpt = list(inpt)
lngth = len(inpt)
half = int(lngth/2)
n_b = inpt.count("B")


record = 0


for i in range(half):

    if i == 0:
        sub_b = inpt[i:half].count("B")
    else:
        if inpt[i+half-1] == "B":
            sub_b += 1

    ant_b = n_b-sub_b



    if sub_b > record:
        record = sub_b
    if ant_b > record:
        record = ant_b

    if inpt[i] == "B":
        sub_b -= 1

print(time.time()-t0)
print(record)