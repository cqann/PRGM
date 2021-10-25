from random import shuffle

namn = open("namn.txt", "r").readlines()
tema = open("tema.txt", "r").readlines()
uppdrag = open("uppdrag.txt", "r").readlines()
fest = open("låda.txt", "r").readlines()

blocks = []
for i in range(len(namn)):
    blocks.append([namn[i].strip(),tema[i].strip(), uppdrag[i].strip(), fest[i].strip()])

can_hold = [x for x in blocks if "Ja" in x[3]]
can_hold[4], can_hold[-3] = can_hold[-3], can_hold[4]
can_hold[1], can_hold[-1] = can_hold[-1], can_hold[1]

best_group = None
best_score = 100000

new_blocks = []
for i in blocks:
    if i in can_hold: continue 
    new_blocks.append(i)
blocks = list(new_blocks)

for i in range(100000):
    groups = [[x] for x in can_hold]
    numbers = [x for x in range(len(blocks))]
    shuffle(numbers)
    group_index = 0 
    for j in numbers:
        groups[group_index].append(blocks[j])
        group_index += 1
        group_index %= len(can_hold)

    score = 0
    for group in groups:
        grupper = [x[1] for x in group] + [x[2] for x in group]
        score += len(grupper) - len(set(grupper))
    
    if score < best_score:
        best_score = score
        best_group = group
        print(best_score)

for i in groups:
    for j in i:
        print(j[0])
    print("================================")

print(len(can_hold))