import re

def parse_line(line):
    parent = re.search(r'^(\w+ \w+)', line).group()
    children = re.findall(r'(\d+) (\w+ \w+)', line)
    rule = {}
    for nbr_of, child in children:
        rule[child] = int(nbr_of)
    return {parent:rule}

def may_contain(color, parent, rules):
    if color in rules[parent]:
        return True
    for child in rules[parent]:
        if may_contain(color, child, rules):
            return True
    return False

def nbr_of_bags_within(parent, rules):
    count = 0
    for child, nbr_of in rules[parent].items():
        count += nbr_of * (1 + nbr_of_bags_within(child, rules))
    return count

with open('input.txt', 'r') as f:
    data = f.read()

rules = {}
for line in data.split('\n'):
    rules |= parse_line(line)

sum1 = sum(may_contain('shiny gold', r, rules) for r in rules)
sum2 = nbr_of_bags_within('shiny gold', rules)

print("Part 1: ", sum1)
print("Part 2: ", sum2)

#Part 1: 238
#Part 2: 82930
