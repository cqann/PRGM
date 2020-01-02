

combos = set()
fc = (0,0,0,0,0,0,0,0)
result = 0

def create(carry,c):
    if carry >= 200:
        if carry == 200:
            if c in combos:
                combos.insert(c)
                result += 1
        return
    else:
        c = list(c)

        if carry + 1 <= 200:
            c[0] += 1
            create(carry+1,tuple(c))
            c[0] -= 1
        if carry + 2 <= 200:
            c[1] += 1
            create(carry+2,tuple(c))
            c[1] -= 1
        if carry + 5 <= 200:
            c[2] += 1
            create(carry+5,tuple(c))
            c[2] -= 1
        if carry + 10 <= 200:
            c[3] += 1
            create(carry+10,tuple(c))
            c[3] -= 1
        if carry + 20 <= 200:
            c[4] += 1
            create(carry+20,tuple(c))
            c[4] -= 1
        if carry + 50 <= 200:
            c[5] += 1
            create(carry+50,tuple(c))
            c[5] -= 1
        if carry + 100 <= 200:
            c[6] += 1
            create(carry +100,tuple(c))
            c[6] -= 1
        if carry + 200 <= 200:
            c[7] += 1
            create(carry+200,tuple(c))
            c[7] -= 1
        return



nextCoin = {1:2, 2:5, 5:10, 10:20,20:50,50:100,100:200};

def genNums(carry, curCoin):
    global result
    if carry == 200:
        result += 1
    elif carry < 200:
        
        limit = int(200/(curCoin)) + 1
        for i in range(limit):
            try:
                genNums(carry + curCoin*i, nextCoin[curCoin])
            except KeyError:
                pass
    return 
        

     

#73674
genNums(0,1)

print(result)







