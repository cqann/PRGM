
top = 0
for a in range(1,100):
    for b in range(1,100):
        current = a**b
        cur_sum = sum([int(x) for x in list(str(current))])
        if cur_sum > top:
            top = cur_sum


print(top)