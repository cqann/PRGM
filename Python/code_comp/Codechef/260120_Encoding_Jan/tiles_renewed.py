ans_dic = {}
prime_dic = {1:False}
def is_prime(x):
    if x in prime_dic:
        return prime_dic[x]
    
    i = 2
    cur = True
    while i*i <= x:
        if x%i == 0:
            cur = False
            break
        i += 1
    
    prime_dic[x] = cur
    return cur
     

def get(x):
    
    cur = x
    p = 2
    while p*p <= x:
        if is_prime(p):
            if x%p == 0:
                while x%p == 0:
                    x //= p
                cur *= (1-1.0/p)

        p += 1
    if x > 1:
        cur *=  (1 - 1.0 / x)

    return int(cur)


t = int(input())
for i in range(t):
    n = int(input())
    if n in ans_dic:
        print(ans_dic[n])
    else:
        c = get(n)
        
        ans_dic[n] = c
        print(c)
        


    
