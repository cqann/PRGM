ans_dic = {}
gcd_dic = {}
def gcd(a,b): 
    if b == 0:
        return a
    if (a,b) in gcd_dic:
        return gcd_dic[(a,b)]
    
    cur = gcd(b, a%b)
    gcd_dic[(a,b)] = cur
    gcd_dic[(b,a)] = cur
    return cur



t = int(input())
for i in range(t):
    n = int(input())
    if n in ans_dic:
        print(ans_dic[n])
    else:
        c = 0
        for tile in range(n+1):
            if gcd(tile,n) == 1:
                c += 1
        ans_dic[n] = c
        print(c)
        


    
