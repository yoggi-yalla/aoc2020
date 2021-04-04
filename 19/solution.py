import re

def parse_rule(r):
    """
    example input:    "50: 15 65 | 60 74"
    example output:   {'50':[('15','65'),('60','74')]}
    """
    rule = {}
    k,v = r.split(':')
    v = v.replace('\"','')
    value = [tuple(alt.split()) for alt in v.split('|')]
    rule[k] = value
    return rule

def get_regex_for_rule(r, rules):
    if r not in rules:
        return r
    regex = ""
    for alternative in rules[r]:
        for v in alternative:
            regex += "(" + get_regex_for_rule(v, rules) + ")"
        regex += "|"
    return regex[:-1]

def count_valid_messages(messages, rules):
    pattern = re.compile("^" + get_regex_for_rule('0', rules) + "$")
    return sum(1 for m in messages if re.match(pattern,m))

with open('input.txt', 'r') as f:
    data = f.read()
    rules_,messages_ = data.split('\n\n')

    rules = {}
    for r in rules_.split('\n'):
        rules |= parse_rule(r)

    messages = messages_.split('\n')


new_rule_8 = "8: 42"
for i in range(2,6):
    new_rule_8 += " |" + " 42"*i

new_rule_11 = "11: 42 31"
for i in range(2,6):
    new_rule_11 += " |" + " 42"*i + " 31"*i

updated_rules = rules.copy()
updated_rules |= parse_rule(new_rule_8)
updated_rules |= parse_rule(new_rule_11)

print("Part 1:", count_valid_messages(messages, rules)) # 171
print("Part 2:", count_valid_messages(messages, updated_rules)) # 369
