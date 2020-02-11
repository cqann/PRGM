
sum_sq = 0

for i in range(1,101):
    sum_sq += i**2

sum_then_sq = ((100*101)/2)**2

print(sum_then_sq-sum_sq)