t = int(input())


for test in range(t):

    n, x, y = [int(x) for x in input().split()]

    niko_score = x + y

    min_to_beg = min(x-1, y-1)
    min_to_end = min(n-x, n-y)
    close_to_end = min_to_beg > min_to_end
    odd_off = 1 if abs(x-y) % 2 == 1 else 0
    if close_to_end:
        worst = abs(x-y) + n
    else:
        worst = 2*min_to_beg + abs(x-y) + 1

    diff = min_to_beg-min_to_end

    if diff < 0:
        best = 1
    else:
        best = 2 + diff
    best = n if best > n else best

    print(best, worst)
