name = open("namn.txt", "r").readlines()
dic = {}
for i in name:
    dic[i] = 0

for i in name:
    dic[i] += 1 
    print(dic[i])