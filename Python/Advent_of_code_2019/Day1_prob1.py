import re
file = open("Day1_prob1.txt","r")

masses = [int(line[:-1]) for line in file]
masses[-1] = 117809

fuels = [x//3 - 2 for x in masses]

print(sum(fuels))
#ans 3443395