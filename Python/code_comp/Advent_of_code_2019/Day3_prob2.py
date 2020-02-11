file = open("Day3.txt","r")

inpt1 = file.readline()
inpt1 = [x for x in inpt1.split(",")]
inpt2 = file.readline()
inpt2 = [x for x in inpt2.split(",")]

inpt1_order = {}

x = 0
y = 0
count = 1
for i in inpt1:
    if i[0] == "R":
        for j in range(int(i[1:])):
            x += 1
            if (x,y) not in inpt1_order:
                inpt1_order[(x,y)] = count
            count += 1

    elif i[0] == "L":
        for j in range(int(i[1:])):
            x -= 1
            if (x,y) not in inpt1_order:
                inpt1_order[(x,y)] = count
            count += 1

    elif i[0] == "U":
        for j in range(int(i[1:])):
            y += 1
            if (x,y) not in inpt1_order:
                inpt1_order[(x,y)] = count
            count += 1

    elif i[0] == "D":
        for j in range(int(i[1:])):
            y -= 1
            if (x,y) not in inpt1_order:
                inpt1_order[(x,y)] = count
            count += 1

inpt2_order = {}
x = 0
y = 0 
count = 1
intersections = []

for i in inpt2:
    if i[0] == "R":
        for j in range(int(i[1:])):
            x += 1
            if (x,y) in inpt1_order:
                intersections.append((x,y))
            if (x,y) not in inpt2_order:
                inpt2_order[(x,y)] = count
            count += 1
                
    elif i[0] == "L":
        for j in range(int(i[1:])):
            x -= 1
            if (x,y) in inpt1_order:
                intersections.append((x,y))
            if (x,y) not in inpt2_order:
                inpt2_order[(x,y)] = count
            count += 1

    elif i[0] == "U":
        for j in range(int(i[1:])):
            y += 1
            if (x,y) in inpt1_order:
                intersections.append((x,y))
            if (x,y) not in inpt2_order:
                inpt2_order[(x,y)] = count
            count += 1

    elif i[0] == "D":
        for j in range(int(i[1:])):
            y -= 1
            if (x,y) in inpt1_order:
                intersections.append((x,y))
            if (x,y) not in inpt2_order:
                inpt2_order[(x,y)] = count
            count += 1

record = 99999999999999

for intersect in intersections:
    if  inpt1_order[intersect] + inpt2_order[intersect] < record:
        record = inpt1_order[intersect] + inpt2_order[intersect]

print(record)
