
t = int(input())
groups = []

for i in range(t):
    longest = 0
    cur = 0
    started = False
    l = int(input())
    for k in input():   
        if k == "A":
            started = True
            longest = max(longest,cur)
            cur = 0
        else:
            if started:
                cur += 1
        
    
    longest = max(longest,cur)

    print(longest)

