
ratings = [0]

with open("day10_e.txt") as joltage_file:
    ratings += sorted([int(line) for line in joltage_file])
    ratings.append(ratings[-1] + 3)

ratings_dict = {rating: i for i, rating in enumerate(ratings)}
distinct_count = 1

count_array = [-1] * len(ratings)
count_array[-1] = 1

def paths_under(index):
    global ratings

    if count_array[index] != -1:
        return count_array[index]

    current_rating = ratings[index]

    potential_under = [current_rating + x for x in range(1, 4)]
    indicies_under = []
    for n in potential_under:
        if n in ratings_dict:
            indicies_under.append(ratings_dict[n])

    counter = 0
    for i in indicies_under:
        counter += paths_under(i)

    count_array[index] = counter
    return counter

print(paths_under(0))
