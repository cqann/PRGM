import itertools
import time

'''
io = {"pos":(-15, 1, 4), "v":(0,0,0)}
europa = {"pos":(1, -10, -8), "v":(0,0,0)}
ganymede = {"pos":(-5, 4, 9), "v":(0,0,0)}
callisto = {"pos":(4, 6, -2), "v":(0,0,0)}

'''
#actual
moons = [{"pos":[-15, 1, 4], "v":[0,0,0]},
{"pos":[1, -10, -8], "v":[0,0,0]},
{"pos":[-5, 4, 9], "v":[0,0,0]},
{"pos":[4, 6, -2], "v":[0,0,0]}]
#x=286332 = 2 × 2 × 3 × 107 × 223
#y=96236 = 2 × 2 × 7 × 7 × 491
#z=193052 = 2 × 2 × 17 × 17 × 167
# smallest common multiple = 2*2*3*7*7*17*17*107*223*491*167
'''
#test
moons = [{"pos":[-1, 0, 2], "v":[0,0,0]},
{"pos":[2, -10, -7], "v":[0,0,0]},
{"pos":[4, -8, 8], "v":[0,0,0]},
{"pos":[3, 5, -1], "v":[0,0,0]}]
'''
combos = [x for x in itertools.combinations(moons,2)]
original = "".join(["".join([str(x) for x in moon["pos"]+moon["v"]]) for moon in moons])
cur = "0"
i = 0
print(2*2*3*7*7*17*17*107*223*491*167)
while cur != original:
    for combo in combos:
        for axis in range(3):
            combo[0]["v"][axis] += 0 if combo[0]["pos"][axis] == combo[1]["pos"][axis] else (1 if combo[0]["pos"][axis] < combo[1]["pos"][axis] else -1)
            combo[1]["v"][axis] += 0 if combo[0]["pos"][axis] == combo[1]["pos"][axis] else (1 if combo[0]["pos"][axis] > combo[1]["pos"][axis] else -1)

    for moon in moons:
        moon["pos"][0] += moon["v"][0]
        moon["pos"][1] += moon["v"][1]
        moon["pos"][2] += moon["v"][2]
    
    i += 1
    cur = "".join(["".join([str(x) for x in moon["pos"]+moon["v"]]) for moon in moons])
    

print(i)



