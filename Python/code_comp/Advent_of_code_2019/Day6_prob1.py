

file = open("Day6.txt","r")

orbits = [x[:-1] for x in file]

objects = set()

for orbit in orbits:
    objects.add(orbit[:3])
    objects.add(orbit[-3:])

counter = {k:[] for k in objects}

for orbit in orbits: 
    counter[orbit[:3]].append(orbit[-3:])

tot = 0
def dive(key,carry):
    global tot
    tot += carry
    for sat in counter[key]:
        dive(sat,carry+1)
    return

dive("COM",0)
print(tot)







