t = int(input())


for test in range(t):
    n, d = [int(x) for x in input().split()]

    bales = [int(x) for x in input().split()]

    for i in range(1, n):
        if d == 0:
            break
        if d - i*bales[i] >= 0:
            d -= i*bales[i]
            bales[0] += bales[i]
        else:
            c = d // i
            bales[0] += c
            break

    print(bales[0])
