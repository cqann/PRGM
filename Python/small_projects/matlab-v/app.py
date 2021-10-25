data = open("data.txt", "r").readlines()
data_split = []
for i in data:
    data_split.append([float(i.strip().split("  ")[0]), float(i.strip().split("  ")[-1])])

avg = sum([x[0] for x in data_split]) / len(data_split)

running = 0 
for i in data_split:
    running += (i[0] - avg)**2

varians = running / (len(data_split)-1)
print(varians)
print(varians**0.5)

