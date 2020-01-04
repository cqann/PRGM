import math

def is_prime(x):
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i == 0:
            return False

    return True

count = 0
for i in range(10,1000000):  
    if not is_prime(i):
        continue  
    cur = str(i)
    t = True
    for j in range(len(cur)):
        val1 = int(cur[0:len(cur)-j])
        #val2 = int(cur[j:len(cur)])
        if not is_prime(val1):
            t = False
        if not is_prime(val1):
            t = False
    
    if t:
        count += 1
        

print(count)