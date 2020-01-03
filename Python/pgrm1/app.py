import math

def base_converter(x):
    highest_exp = 0
    

    while 2**highest_exp <= x:
        highest_exp += 1

    res = ""

    while highest_exp>= 0:
        if (x - pow(2,highest_exp) >= 0):
            res += "1"
            x -= pow(2,highest_exp)
        else:
            res += "0"
        
        highest_exp -= 1
    

    return int(res[1:])



def is_pal(n):
    nlist = list(str(n))
    for i in range(math.ceil(len(nlist))):
        if nlist[i] != nlist[len(nlist)-1-i]:
            return False
    return True


result = 0
for i in range(1,1000000):
    if is_pal(i) and is_pal(base_converter(i)):
        result += i
        print(i)

print(result)


