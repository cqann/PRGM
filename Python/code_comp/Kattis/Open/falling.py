

n = int(input())
sq_n = n**0.5
lf = 1
res = None
while lf < int(sq_n + 1):
    if n % lf == 0:
        hf = n // lf

        b = (hf - lf)/2

        if (b*2) % 2 == 1:
            lf += 1
            continue

        a = lf + b
        res = (b, a)

        break

    lf += 1

if res == None:
    print("impossible")
else:
    print(int(res[0]), int(res[1]))
