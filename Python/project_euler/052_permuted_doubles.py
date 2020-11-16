import time 
def same(x, y):
    if len(str(x)) != len(str(y)): return False
    x_count = [0]*10
    y_count = [0]*10
    x_l = [int(p) for p in str(x)]
    y_l = [int(p) for p in str(y)]
    for i in range(len(str(x))):
        x_count[x_l[i]] += 1
        y_count[y_l[i]] += 1

    return x_count == y_count

def same1(x,y): #SNABBARE FUNKTION
    return sorted(str(x)) == sorted(str(y))

t0 = time.time()
i = 1
banned = set()
while True:
    if i in banned:
        i += 1 
        continue
    check = True
    mult = 2
    while check == True and mult < 7:
        if not same1(i, mult*i):
            if mult == 2 or mult == 3:
                banned.add(i*mult)
            check = False
        else:
            mult += 1


    if check == False:
        i += 1 
    else:
        print(i)
        break

print(time.time()-t0)

