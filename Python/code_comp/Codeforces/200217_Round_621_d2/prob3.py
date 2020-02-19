
from math import factorial as fct
from itertools import product as pdt


def nCr(n, r):
    return fct(n)//(fct(r)*fct(n-r))


s = input()

cdic = {}
chars = ""
for c in s:
    if c in cdic:
        cdic[c] += 1
    else:
        cdic[c] = 1
        chars += c
record = 0

for i in range(1, 2**len(chars)):
    cur_subset = str(bin(i))[2:]
    cur_subset = "0"*(len(chars) - len(cur_subset)) + cur_subset
    cur_chars = ""
    for j in range(len(cur_subset)):
        if cur_subset[j] == "0":
            continue

        cur_chars += chars[j]
    pdt_list = []
    for c in cur_chars:
        pdt_list.append([x for x in range(1, cdic[c]+1)])

    for i in pdt(*pdt_list):
        cur = 1
        for j in range(len(i)):
            cur *= nCr(cdic[cur_chars[j]], i[j])

        if cur > record:
            record = cur

print(record)
