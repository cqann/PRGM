import math
def s_min(a,b):
    if (a,b) in dic:
        return dic[(a,b)]
    w = (b-a+1)/2

    dic[(a,b)] = min(s_min(a,a+w-1),s_minh(a+w,b))
    return dic[(a,b)]

def quer(a,b):
    k = 2**math.floor(math.log2(b-a+1))
    return 

arr = [int(x) for i in input().split(" ")]
dic = {}

for i in range(len(arr)):
    for j in range(len(arr)):
        if math.log(i-j+1, 2).is_integer():
            s_min(j,i)













