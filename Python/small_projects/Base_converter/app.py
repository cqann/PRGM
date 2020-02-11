
# 37 to base 2 = 100111

def base_converter(x,b):
    highest_exp = 0
    chars = "0123456789ABCED"


    while b**highest_exp <= x:
        highest_exp += 1

    res = [0]*highest_exp

    for i in range(x):
        res[0] += 1
        for j in range(len(res)):
            if res[j] == b:
                res[j+1]+=1
                res[j] = 0



    return int("".join([str(x) for x in res[::-1]]))



fasf = open("3.txt","r")
fasf.close()