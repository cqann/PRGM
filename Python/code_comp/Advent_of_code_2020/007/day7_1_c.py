
def get_bags(dictionary, bag, search_term):
    if not dictionary[bag]:
        return 0 
    
    count = 0
    for internal_bag in dictionary[bag]:
        if internal_bag[1] == search_term:
            count += 1
        else:
            count += get_bags(dictionary, internal_bag[1], search_term)

    if count > 0:
        return 1
    else:
        return 0 


file = open("day7_c.txt", "r")
bag_dic = {}

for line in file:
    line = line.strip()
    line_space_split = line.split(" ")
    bag_name = " ".join(line_space_split[:2])
    bag_dic[bag_name] = []
    
    bag_contains = line.split(" contain ")[1]
    if bag_contains == "no other bags.":
        continue
    contained_bags = bag_contains.split(", ")
    
    for contained_bag in contained_bags:
        internal_bag_split = contained_bag.split(" ")
        internal_bag_count = int(internal_bag_split[0])
        internal_bag_name = " ".join(internal_bag_split[1:3])

        bag_dic[bag_name].append((internal_bag_count, internal_bag_name))

file.close()

count = 0 
for bag in bag_dic:
    count += get_bags(bag_dic, bag, "shiny gold")

print(count)
