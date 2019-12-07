''''
Readable version
def find_val(string):
    return sum( [ord(x)-96 for x in string.lower()] )


file = open("022.txt","r")

names = [x[1:-1] for x in file.readline().split(",")]
scores = []
names.sort()

for i in range(len(names)): 
    scores.append(find_val(names[i])*(i+1))

print(sum(scores))
'''

file = open("022.txt","r")
names = [x[1:-1] for x in file.readline().split(",")]
names.sort()
print(sum([sum([ord(x)-96 for x in names[i].lower()])*(i+1) for i in range(len(names))]))