import math
file = open("Day10.txt","r")

inpt = [line[:-1] for line in file]

asteroids = []

for y in range(len(inpt)):
    for x in range(len(inpt[y])):
        if inpt[y][x] == "#":
            asteroids.append((x,y))

record = 0
best = None
dic_save = None
ast_200 = []
for asteroid in asteroids:
    cur_dic = {}
    for other in [x for x in asteroids if x != asteroid]:
        angle = math.atan2(other[1]-asteroid[1],other[0]-asteroid[0]) 
        if angle not in cur_dic:
            cur_dic[angle] = [other]
        else:
            cur_dic[angle].append(other)
        
    
    if len(cur_dic) > record:
        record = len(cur_dic)
        best = asteroid
        dic_save = cur_dic

angle_list = [(-k,v) for k,v in dic_save.items()]
angle_list = sorted(angle_list, key= lambda tup: tup[0]+math.pi/2 if tup[0] <= math.pi/2 else -1.5*math.pi+tup[0],reverse=True)

print(angle_list[199])

