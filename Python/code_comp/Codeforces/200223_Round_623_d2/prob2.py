t = int(input())

for test in range(t):
    a, b, p = [int(x) for x in input().split()]
    lines = input()

    if a > p and b > p:
        print(len(lines))
        continue

    tot = 0
    last = lines[-1]
    ind = len(lines)-1
    changes = []

    for c in list(reversed(lines))[1:]:

        if last != c:
            if ind != len(lines)-1:
                off = b if c == "A" else a
                if tot + off <= p:
                    tot += off
                    changes.append(ind+1)
                else:
                    break
            else:
                off = a if c == "A" else b
                if tot + off > p:
                    changes.append(len(lines))
                    break
        if ind == 1:
            off = a if c == "A" else b
            if tot+off <= p:
                tot += off
                changes.append(1)
                break

        if tot >= p:
            break
        last = c
        ind -= 1

    if len(changes) == 0:
        if lines[0] == "A":
            if a > p:
                print(len(lines))
            else:
                print(1)
        else:
            if b > p:
                print(len(lines))
            else:
                print(1)

    else:
        print(changes[-1])
