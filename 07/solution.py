import re

def parse_line(l):
    l = l.replace('.','').replace(',','').replace('bags','').replace('contain ','').replace('bag','')
    colors = re.findall(r'([a-z]+ [a-z]+)',l)
    numbers = re.findall(r'(\d+)',l) or [0]
    key = colors.pop(0)
    return key, colors, numbers

def may_contain(x, y, rules):
    if not y in rules:
        return False
    if x in rules[y]:
        return True
    else:
        for color in rules[y]:
            if may_contain(x, color, rules):
                return True
    return False

def nbr_of_bags_within(x, rules):
    if 'no other' in rules[x]:
        return 0
    tally = 0
    for sub,nbr in rules[x].items():
        tally += int(nbr) * (1+nbr_of_bags_within(sub, rules))
    return tally


with open('input.txt', 'r') as f:
    data = f.read()

rules = {}
for l in data.split('\n'):
    key, colors, numbers = parse_line(l)
    rules[key] = {}
    for color, nbr in zip(colors, numbers):
        rules[key][color] = nbr


sum1 = sum(may_contain('shiny gold',r,rules) for r in rules)
sum2 = nbr_of_bags_within('shiny gold', rules)

print("Part 1: ", sum1)
print("Part 2: ", sum2)


#Part 1: 238
#Part 2: 82930
