from os import path
import re

food_sets = []
all_allergens = set()
all_ingredients = set()

with open(path.join(__file__, "..", "input_e.txt")) as file:
    file_string = file.read()
    finds = re.findall(r"^(.*)\ \(contains\ (.*)\)$", file_string, flags=re.MULTILINE)
    food_sets = [(set(a[0].split(" ")), set(a[1].split(", "))) for a in finds]

    for tup in food_sets:
        all_ingredients = all_ingredients.union(tup[0])
        all_allergens = all_allergens.union(tup[1])

allergen_dic = {}
for ingredients, allergens in food_sets:
    for allergen in allergens:
        if allergen not in allergen_dic:
            allergen_dic[allergen] = ingredients
            continue

        allergen_dic[allergen] = allergen_dic[allergen].intersection(ingredients)

        if len(allergen_dic[allergen]) == 1:
            for old_allergen in allergen_dic:
                if old_allergen == allergen: continue
                allergen_dic[old_allergen] = allergen_dic[old_allergen].difference(allergen_dic[allergen])

# print(allergen_dic)
danger_list = ""
allergen_names = sorted(allergen_dic.keys())

for allergen in allergen_names:
    ingredient = allergen_dic[allergen].pop()
    danger_list += ingredient + ","

print(danger_list[:-1])