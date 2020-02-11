import math
n = int(input())
garland = []
gar_pairs = 0
flip = False

nU = math.ceil(n/2.0 - 0.1)
nE = math.floor(n/2.0 + 0.1) 

holes = []
inpt = [int(x) for x in input().split(" ")]
for c in range(len(inpt)):
    cur = inpt[c]%2==0 if inpt[c]!= 0 else None
    after = (inpt[c+1]%2==0 if inpt[c+1]!=0 else None) if c!=n-1 else None
   
    garland.append(inpt[c])
    if cur != None:     
        if cur:
            nE -= 1
        else:
            nU -= 1

coming = 1
for s in range(len(garland)):
    if garland[s] != 0:
        coming = 0 if  garland[s]%2 == 0 else 1
        break
pairs = 0
for s in range(len(garland)):
    if garland[s] == 0:
        if coming == 0:
            if nE != 0:
                garland[s] = 0
                nE -= 1
                coming = 0
            elif nU != 0:
                garland[s] = 1                
                nU -= 1
                coming = 1
        else:
            if nU != 0:
                garland[s] = 1
                nU -= 1
                coming = 1
            elif nE != 0:
                garland[s] = 0
                nE -= 1
                coming = 0
    else:
        coming = 0 if  garland[s]%2 == 0 else 1


for c in range(len(garland)-1):
    cur = garland[c]%2==0
    after = garland[c+1]%2==0
    
    if cur != after:

        pairs += 1

print(pairs)
