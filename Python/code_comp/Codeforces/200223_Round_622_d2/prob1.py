import itertools
t = int(input())


for test in range(t):
    meals = [int(x) for x in input().split()]

    res = 0

    for i in range(3):
        if meals[i] > 0:
            res += 1
            meals[i] -= 1

    new_meals = [i for i in meals if i > 0]

    if len(new_meals) == 2:
        res += 1
    elif len(new_meals) == 3:
        lowest = min(new_meals)
        low_ind = new_meals.index(lowest)
        if lowest >= 2:
            res += 3
        else:
            if new_meals.count(1) == 3:
                res += 1
            else:
                res += 2

    if len([i for i in new_meals if i > 2]) == 3:
        res += 1

    print(res)
