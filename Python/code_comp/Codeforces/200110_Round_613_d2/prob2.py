
t = int(input())

for test in range(t):

    n = int(input())
    cakes = [int(x) for x in input().split(" ")]

    tot_sum = 0
    max_sub_sum = 0
    cur_sum = 0
    start = 0

    for i in range(len(cakes)):
        if cakes[i] >= cur_sum + cakes[i]:
            cur_sum = cakes[i]
            start = i
        else:
            cur_sum = cur_sum + cakes[i]
        
        if cur_sum > max_sub_sum:
            if not (start == 0 and i == n-1):
                max_sub_sum = cur_sum
        tot_sum += cakes[i]

    if tot_sum > max_sub_sum:
        print("YES")
    else:
        print("NO")

    
