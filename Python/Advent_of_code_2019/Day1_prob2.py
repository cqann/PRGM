def get_fuel(m, t):
    f = m//3 - 2 
    if f <= 0:
        return t
    return get_fuel(f,t+f)


file = open("Day1.txt","r")

masses = [int(line[:-1]) for line in file]
masses[-1] = 117809

fuels = [get_fuel(x,0) for x in masses]

print(sum(fuels))
#ans 3443395