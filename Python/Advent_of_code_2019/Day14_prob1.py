import re

file = open("Day14.txt","r")
rec_list = [line[:-1] for line in file]
rec = {}
for r in rec_list:
    cur = r.split(" => ")
    components = cur[0].split(", ")
    components = [(int(re.findall(r"\A\d+",x)[0]),re.findall(r"[A-Z]+\Z",x)[0]) for x in components]
    rec[re.findall(r"[A-Z]+\Z",cur[1])[0]] = re.findall(r"\A\d+",cur[1]) + components

storage = {k:0 for k in rec}
storage["ORE"] = 1000000000000

def trickle(key,amount):
    
    for comp in rec[key][1:]:
        comp_needed = comp[0]
        comp_name = comp[1]
        storage[comp_name] -= comp_needed
        while storage[comp_name] < 0: 
            storage[comp_name] += trickle(comp_name, abs(storage[comp_name]))
    return int(rec[key][0])

#elif filippa är en sockerdricka 
vals = [1000000000000]
diffs = []
for i in range(10000):
    trickle("FUEL",1)

print(vals[0]-storage["ORE"])



