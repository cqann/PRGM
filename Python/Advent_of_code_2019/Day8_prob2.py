

file = open("Day8.txt","r")
inpt = file.readline()
#25*6 = 150

layers = [inpt[x*150:(x+1)*150] for x in range(len(inpt)//150)]

final_image=[["2" for j in range(25)] for i in range(6)]

for layer in layers:
    for y in range(6):
        for x in range(25):
            if final_image[y][x] == "2":
                final_image[y][x] = layer[25*y+x]

for line in final_image:
    print("".join(line).replace("0","-"))






