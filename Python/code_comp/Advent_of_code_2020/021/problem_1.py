from os import path
import re

food_sets = []
all_allergens = set()
all_ingredients = set()

with open(path.join(__file__, "..", "input_c.txt")) as file:
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

allergen_ingredients = set()
for allergen in allergen_dic:
    allergen_ingredients = allergen_ingredients.union(allergen_dic[allergen])

# print(all_ingredients)
free = set([x for x in all_ingredients if x not in allergen_ingredients])

result = 0
for food in food_sets:
    food_ingredients = food[0]
    for ingredient in food_ingredients:
        if ingredient in free:
            result += 1

print(result)

'''
certain_ingredients = set()
certain_allergens = set()

free = set()
for _ in range(10):
    for food_index, food_1 in enumerate(food_sets):
        ingredients_1, allergens_1 = food_1

        for food_2 in food_sets:
            if food_1 == food_2: continue
            ingredients_2, allergens_2 = food_2

            ingredients_intersection = ingredients_1.intersection(ingredients_2)
            allergen_intersection = allergens_2#allergens_1.intersection(allergens_2)
            ingredients_intersection.difference_update(certain_ingredients)
            allergen_intersection.difference_update(certain_allergens)

            ingredients_intersection.difference_update(free)

            if len(ingredients_intersection) == len(allergen_intersection):
                certain_ingredients = certain_ingredients.union(ingredients_intersection)
                certain_allergens = certain_allergens.union(allergen_intersection)

                free = free.union(ingredients_2.difference(certain_ingredients))

            if len(allergen_intersection) == 0:
                free = free.union(ingredients_intersection)

print(free)
'''