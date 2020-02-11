
T = int(input())

for t in range(T):

    n = int(input())
    res = ["1"] * (n//2)
    if n%2 == 1:
        res[0] = "7"

    print(int("".join(res)))









