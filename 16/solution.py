import re

RULE_PATTERN = re.compile(r'\w+\s?\w+?: (\d+)-(\d+) or (\d+)-(\d+)')
RULES_STARTING_WITH_DEPARTURE = 0

def parse_rule(r):
    if r.startswith('departure'):
        global RULES_STARTING_WITH_DEPARTURE
        RULES_STARTING_WITH_DEPARTURE += 1
    a, b, c, d = re.match(RULE_PATTERN, r).groups()
    return int(a), int(b), int(c), int(d)

def parse_ticket(ticket):
    return [int(x) for x in ticket.split(',')]

def satisfies_rule(v, rule):
    return rule[0] <= v <= rule[1] or rule[2] <= v <= rule[3]


with open('input.txt', 'r') as f:
    data = f.read()
    rules, my_ticket, nearby_tickets = data.split('\n\n')

    my_ticket = my_ticket.lstrip('your ticket:\n')
    my_ticket = parse_ticket(my_ticket)

    nearby_tickets = nearby_tickets.lstrip('nearby tickets:\n')
    nearby_tickets = [parse_ticket(x) for x in nearby_tickets.split('\n')]

    rules = [parse_rule(r) for r in rules.split('\n')]



####################
#      PART 1      #
####################

valid_tickets = []
part_1_sum = 0
for ticket in nearby_tickets + [my_ticket]:
    t_sum = 0
    for v in ticket:
        if not any(satisfies_rule(v, r) for r in rules):
            t_sum += v
    if t_sum == 0:
        valid_tickets.append(ticket)
    part_1_sum += t_sum

print("Part 1:", part_1_sum) # 26869




####################
#      PART 2      #
####################

def find_next_pairs(indexes, used_ri, used_ti, rules, tickets):
    ri_to_possible_ti = {i:set() for i in indexes}
    for t_index in indexes:
        if t_index in used_ti:
            continue
        for r_index in indexes:
            if r_index in used_ri:
                continue
            if all(satisfies_rule(ticket[t_index], rules[r_index]) for ticket in tickets):
                ri_to_possible_ti[r_index].add(t_index)

    pairs = {}
    for r_i,t_set in ri_to_possible_ti.items():
        if len(t_set) == 1:
            t_i = next(iter(t_set))
            used_ri.add(r_i)
            used_ti.add(t_i)
            pairs |= {r_i:t_i}
    return pairs


ri_to_ti = {}
indexes = [i for i in range(len(my_ticket))]

used_ri = set()
used_ti = set()
for _ in indexes:
    ri_to_ti |= find_next_pairs(indexes, used_ri, used_ti, rules, valid_tickets)


product_sum = 1
for i in range(RULES_STARTING_WITH_DEPARTURE):
    index = ri_to_ti[i]
    product_sum *= my_ticket[index]

print("Part 2:", product_sum) # 855275529001
