import re

def parse_line(line):
    parent = re.search(r'^(\w+ \w+)', line).group()
    children = re.findall(r'(\d+) (\w+ \w+)', line)
    return parent, children

def may_contain(color, parent, rules):
    if color in rules[parent]:
        return True
    else:
        for child in rules[parent]:
            if may_contain(color, child, rules):
                return True
    return False

def nbr_of_bags_within(parent, rules):
    nbr_of_bags = 0
    for child, nbr in rules[parent].items():
        nbr_of_bags += nbr * (1 + nbr_of_bags_within(child, rules))
    return nbr_of_bags

with open('input.txt', 'r') as f:
    data = f.read()

rules = {}
for line in data.split('\n'):
    parent, children = parse_line(line)
    rules[parent] = {}
    for nbr_of, child in children:
        rules[parent][child] = int(nbr_of)

sum1 = sum(may_contain('shiny gold', r, rules) for r in rules)
sum2 = nbr_of_bags_within('shiny gold', rules)

print("Part 1: ", sum1)
print("Part 2: ", sum2)

#Part 1: 238
#Part 2: 82930
