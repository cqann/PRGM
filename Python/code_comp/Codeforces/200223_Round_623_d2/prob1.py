t = int(input())


for test in range(t):
    a, b, x, y = [int(x) for x in input().split()]

    c_x = a - x - 1
    c_y = b - y - 1

    print(max(a*y, b*x, a*c_y, b*c_x))
