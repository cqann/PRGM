

def drone_problem_solver(n_people, k_to_share,days_in_year,days_within):
    compliment = 1
    decrement_when = k_to_share-1
    denominator = days_in_year + 1
    for i in range(n_people):
        if i % decrement_when == 0:
            denominator -= days_within
        compliment *= denominator/days_in_year
    probability = 1-compliment
    return probability

print(drone_problem_solver(5,3,10,1))