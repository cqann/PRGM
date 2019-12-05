


def collatz(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n+1

record = 0 

for i in range(1,1000000):
    cur_val = i
    count = 0
    while cur_val != 1:
        cur_val = collatz(cur_val)
        count += 1
    
    if count > record:
        print(i)
        bestn = i
        record = count