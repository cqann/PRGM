from math import * 


vals = [abs(3*sin(x)) for x in range(10000)]
avg = sum(vals)/len(vals)
print(avg)
print(3/sqrt(2))