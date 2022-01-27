import itertools
a = [[x for x in range(1,7)],[x for x in range(1,7)], [x for x in range(1,7)]]
prr = list(itertools.product(*a))
count = 0

for k in prr:
    k = list(k)
    if sum(k) <= 6:
        if (k[0] == 2):
            count += 1

print(count)