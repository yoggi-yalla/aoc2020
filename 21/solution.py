with open('input.txt', 'r') as f:
    data = f.read()

def parse_food(row):
    ingredients = set(row.split(" (contains ")[0].split(" "))
    allergens = set(row.split(" (contains ")[1][:-1].split(", "))
    return {"ingredients":ingredients, "allergens":allergens}

food_list = [parse_food(row) for row in data.splitlines()]

all_ingredients = set.union(*[f['ingredients'] for f in food_list])
all_allergens = set.union(*[f['allergens'] for f in food_list])

allergen_to_possible_ingredient = {k:all_ingredients.copy() for k in all_allergens}

for f in food_list:
    for a in f['allergens']:
        allergen_to_possible_ingredient[a].intersection_update(f['ingredients'])


suspected_ingredients = set.union(*allergen_to_possible_ingredient.values())
safe_ingredients = all_ingredients - suspected_ingredients

part_1 = 0
for f in food_list:
    for i in f['ingredients']:
        if i in safe_ingredients:
            part_1 += 1
print("Part 1:", part_1) # 2170


allergen_to_ingredient = {}
unmatched_allergens = list(all_allergens)

while unmatched_allergens:
    this_allergen = unmatched_allergens.pop()
    possible_ingredients = allergen_to_possible_ingredient[this_allergen]

    if len(possible_ingredients) == 1:
        ingredient = next(iter(possible_ingredients))
        allergen_to_ingredient[this_allergen] = ingredient
        for k,v in allergen_to_possible_ingredient.items():
            v.discard(ingredient)

    else:
        unmatched_allergens.insert(0,this_allergen)


out = [(k,v) for k,v in allergen_to_ingredient.items()]
out_sorted = sorted(out, key=lambda x: x[0])
part_2 = ",".join([x[1] for x in out_sorted])

print("Part 2:", part_2)