import itertools

'''
io = {"pos":(-15, 1, 4), "v":(0,0,0)}
europa = {"pos":(1, -10, -8), "v":(0,0,0)}
ganymede = {"pos":(-5, 4, 9), "v":(0,0,0)}
callisto = {"pos":(4, 6, -2), "v":(0,0,0)}
'''

moons = [{"pos":[-15, 1, 4], "v":[0,0,0]},
{"pos":[1, -10, -8], "v":[0,0,0]},
{"pos":[-5, 4, 9], "v":[0,0,0]},
{"pos":[4, 6, -2], "v":[0,0,0]}]

for i in range(1000):
    for combo in itertools.combinations(moons,2):
        for axis in range(3):
            if combo[0]["pos"][axis] > combo[1]["pos"][axis]:
                combo[0]["v"][axis] -= 1 
                combo[1]["v"][axis] += 1
            elif combo[0]["pos"][axis] < combo[1]["pos"][axis]:
                combo[0]["v"][axis] += 1 
                combo[1]["v"][axis] -= 1
    for moon in moons:
        moon["pos"][0] += moon["v"][0]
        moon["pos"][1] += moon["v"][1]
        moon["pos"][2] += moon["v"][2]

for moon in moons:
    print(moon)
energies = [ sum([abs(x) for x in moon["pos"]])*sum([abs(x) for x in moon["v"]]) for moon in moons]
print(sum(energies))

