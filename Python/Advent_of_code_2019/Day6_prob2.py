

file = open("Day6.txt","r")

orbits = [x[:-1] for x in file]

objects = set()

for orbit in orbits:
    objects.add(orbit[:3])
    objects.add(orbit[-3:])

tree = {k:[] for k in objects}
counter = {k:0 for k in objects}


for orbit in orbits: 
    tree[orbit[:3]].append(orbit[-3:])

tot = 0

def dive(key,carry):
    global tot
    tot += carry
    counter[key] = carry
    for sat in tree[key]:
        dive(sat,carry+1)
    return

dive("COM",0)


def burrow(key,l):
    if key == "COM":
        return l
    for orbit in orbits:
        if orbit[-3:] == key:
            l.append(orbit[:3])
            return burrow(orbit[:3],l)

you_com = burrow("YOU",[])
san_com = burrow("SAN",[])
# first similar = 6C4

print(counter[you_com[0]]+counter[san_com[0]]-2*counter["6C4"])
            
    









