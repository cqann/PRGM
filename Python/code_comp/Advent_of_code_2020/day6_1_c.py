data = open("day6_c.txt", "r")
groups = []
current_group = []
for line in data:
    if line == "\n":
        groups.append(current_group)
        current_group = []
        continue
    current_group.append(line.strip())

count = 0
for group in groups:
    print(group)
    group_set = set()
    for person in group:
        for question in person:
            group_set.add(question)

    count += len(group_set)

print(count)