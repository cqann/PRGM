import math
file = open("Day10.txt","r")

inpt = [line[:-1] for line in file]

asteroids = []

for y in range(len(inpt)):
    for x in range(len(inpt[y])):
        if inpt[y][x] == "#":
            asteroids.append((x,y))

record = 0
for asteroid in asteroids:
    cur_dic = {}
    for other in [x for x in asteroids if x != asteroid]:
        angle = math.atan2(other[1]-asteroid[1],other[0]-asteroid[0]) 
        if angle not in cur_dic:
            cur_dic[angle] = True
    
    if len(cur_dic) > record:
        record = len(cur_dic)

print(record)

