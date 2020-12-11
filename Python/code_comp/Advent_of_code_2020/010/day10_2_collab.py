
ratings = []

with open("day10_example.txt") as joltage_file:
    ratings = sorted([int(line) for line in joltage_file])
    ratings.append(ratings[-1] + 3)

diffs = {1: 0, 2: 0, 3: 0}

current_rating = 0
for rating in ratings:
    diff = rating - current_rating
    diffs[diff] += 1
    current_rating = rating


print(diffs[1] * diffs[3])
