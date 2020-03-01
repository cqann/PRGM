import math
import re
from decimal import *
record = 0
best = 0
for i in range(2, 1000):
    string = str(Decimal(1/i))[2:]
    string = re.sub("\A0*", "", string)
    first = ""
    cur = 0
    for c in string:
        if c not in first:
            first += c
            cur += 1
        else:
            break
    if cur > record:
        record = cur
        best = i

# print(Decimal(1/13))
print(Decimal(1/17))
print(1/17)
print(D)
# print(Decimal(1/19))
