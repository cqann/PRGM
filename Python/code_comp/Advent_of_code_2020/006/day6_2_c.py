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
    group_dic = {}
    n_persons = len(group)
    for person in group:
        for question in person:
            if question not in group_dic: group_dic[question] = 0
            group_dic[question] += 1

    for question in group_dic:
        if group_dic[question] == n_persons:
            count += 1

print(count)