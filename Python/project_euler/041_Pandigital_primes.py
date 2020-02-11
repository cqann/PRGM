def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def is_pan(n):
    lngth = len(str(n))
    bool_list = [False for x in range(lngth)]
    for i in str(n):
        if int(i)>lngth:
            return False
        bool_list[int(i)-1] = True
    
    for i in bool_list:
        if i == False:
            return False
    
    return True

record = 0
for i in range(10000):
    if is_pan(i) and is_prime(i) and record < i:
        record = i
print(record)

