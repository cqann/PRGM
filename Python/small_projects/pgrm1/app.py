


account = 0
p_change = 1.04**(1/12)
f_acc = 0

for i in range(300):
    account *= p_change
    account += 50000

    f_acc += 50000 * (p_change**i)


print(account)
print(f_acc)






