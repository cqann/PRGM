





trump_count = int(input("Votes on Trump: "))
biden_count = int(input("Votes on Biden: "))
votes_recorded = int(input("Percentage of votes recorded: "))/100

votes_left = (trump_count+biden_count)*((1-votes_recorded)/votes_recorded)

percentage_votes_needed = round(((trump_count-biden_count)/votes_left + 1) * 50,2)

print("Biden needs ", percentage_votes_needed, " of remaining votes to win this state!")



