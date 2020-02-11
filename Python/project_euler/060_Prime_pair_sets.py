def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def test3(a,b,c):
    alist = [b,c]
    blist = [a,c]
    clist = [b,a]


    for i in range(2):
        if not is_prime(int(str(a)+str(alist[i]))):
            return False
        if not is_prime(int(str(b)+str(blist[i]))):
            return False
        if not is_prime(int(str(c)+str(clist[i]))):
            return False


    return True
def test4(a,b,c,d):
    alist = [b,c,d]
    blist = [a,c,d]
    clist = [b,a,d]
    dlist = [b,c,a]

    for i in range(3):
        if not is_prime(int(str(a)+str(alist[i]))):
            return False
        if not is_prime(int(str(b)+str(blist[i]))):
            return False
        if not is_prime(int(str(c)+str(clist[i]))):
            return False
        if not is_prime(int(str(d)+str(dlist[i]))):
            return False


    return True

def test5(a,b,c,d,e):
    alist = [b,c,d,e]
    blist = [a,c,d,e]
    clist = [b,a,d,e]
    dlist = [b,c,a,e]
    elist = [b,c,d,a]

    for i in range(4):
        if not is_prime(int(str(a)+str(alist[i]))):
            return False
        if not is_prime(int(str(b)+str(blist[i]))):
            return False
        if not is_prime(int(str(c)+str(clist[i]))):
            return False
        if not is_prime(int(str(d)+str(dlist[i]))):
            return False
        if not is_prime(int(str(e)+str(elist[i]))):
            return False

    return True


prime_list = []
ban_list = {}
Bban_list = {}
a = 2


while True:
    if is_prime(a):
        prime_list.append(a)
        ban_list[a] = []
        print(a)
        for b in prime_list:
            if is_prime(int(str(a)+str(b))) and is_prime(int(str(b)+str(a))) and b not in ban_list[a]:
                for c in [x for x in prime_list if x < b and x not in ban_list[a]]:
                    if  is_prime(int(str(a)+str(c))) and is_prime(int(str(c)+str(a))) and is_prime(int(str(c)+str(b))) and is_prime(int(str(b)+str(c))):
                        for d in [x for x in prime_list if x < c and x not in ban_list[a]]:
                            if test4(a,b,c,d):
                                for e in [x for x in prime_list if x < d and x not in ban_list[a]]:
                                    if test5(a,b,c,d,e):
                                        print(a,b,c,d,e)
                                        break
                    else:
                        
            else:
                ban_list[a].append(b)



    a += 1