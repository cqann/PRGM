import re

answers = []
letter_counts = []
counts = []

with open("day6_e.txt") as answer_file:
    file_string = answer_file.read()

    entries = re.split(r"^\s*$", file_string, flags=re.MULTILINE|re.IGNORECASE)

    # Parse each group into single line
    for entry in entries:
        entry = entry.strip()
        answers.append((entry, len(entry.split("\n"))))

# Count number of appearances per letter per group
for answer, group_size in answers:
    count = {}
    for letter in answer.replace("\n", ""):
        if letter not in count:
            count[letter] = 0
        count[letter] = count[letter] + 1

    letter_counts.append((count, group_size))

# Count number of letters whose length is that of the group
for count, group_size in letter_counts:
    n = 0
    for value in count.values():
        if value == group_size:
            n += 1
    counts.append(n)

# print sum of counts of unique letters
print(sum(counts))
