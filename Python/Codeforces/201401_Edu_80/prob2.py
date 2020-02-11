import sys


def calc(a,b):
    if a == 0 or b == 0:
        return 0
    #print(a,b)
    if (a,b) in ab_dic:
        return ab_dic[(a,b)]
    to_add = 0
    if a*b + a + b == int(str(a)+str(b)):
        to_add += 1

    ab_dic[(a,b)] = max(calc(a-1,b),calc(a,b-1),calc(a-1,b-1)) + to_add
    return ab_dic[(a,b)]




n_test = int(input())
to_check = []
ab_dic = {}
max_a = 0
max_b = 0

for t in range(n_test):
    cur = [int(x) for x in input().split(" ")]
    max_a = max(max_a,cur[0])
    max_b = max(max_b,cur[1])
    to_check.append(cur)

fmax = max(max_a, max_b)
result = []
s = 0
for i in range((fmax//9)):
    s += 9*i
    result.appned(s)

for i in to_check:
    print(result[max(i[0],i[1])-1])






