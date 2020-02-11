

file = open("Day8.txt","r")
inpt = file.readline()
#25*6 = 150

layers = [inpt[x*150:(x+1)*150] for x in range(len(inpt)//150)]

record = 150
best = None

for layer in layers:
    if layer.count("0") < record:
        record = layer.count("0")
        best = layer

print(best.count("1")*best.count("2"))
