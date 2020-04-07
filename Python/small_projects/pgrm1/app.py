
def f(x):
    return (4 * x**2)/(4 * x**2 - 1)


res = 1
for i in range(1,1000000):
    res *= f(i)

print(res*2)





