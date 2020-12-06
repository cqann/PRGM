import re

answers = []
letter_counts = []
counts = []

with open("day6_e.txt") as answer_file:
    file_string = answer_file.read()

    entries = re.split(r"^\s*$", file_string, flags=re.MULTILINE|re.IGNORECASE)

    # Parse each group into single line
    for entry in entries:
        answer = "".join(re.split(r"\s", entry, flags=re.MULTILINE|re.IGNORECASE))
        answers.append(answer)

# Count number of appearances per letter per group
for answer in answers:
    count = {}
    for letter in answer:
        if letter not in count:
            count[letter] = 0
        count[letter] = count[letter] + 1
    letter_counts.append(count)

# Count number of unique letters (keys) in each group
for count in letter_counts:
    counts.append(len(count.keys()))

# print sum of counts of unique letters
print(sum(counts))
