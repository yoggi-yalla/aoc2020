import re

def parse_rule(r):
    rule = {}
    k,v = r.split(':')
    v = v.replace('\"','')
    value = []
    alternatives = v.split('|')
    for alt in alternatives:
        value.append(tuple(alt.split()))
    rule[k] = value
    return rule

def get_regex_for_rule(r, rules):
    if r not in rules:
        return r
    regex = ""
    for i in range(len(rules[r])):
        for k in rules[r][i]:
            regex += "(" + get_regex_for_rule(k, rules) + ")"
        regex += "|"
    return regex[:-1]

def count_valid_messages(messages, rules):
    pattern = re.compile("^" + get_regex_for_rule('0', rules) + "$")
    count = 0
    for m in messages:
        if re.match(pattern, m):
            count += 1
    return count

with open('input.txt', 'r') as f:
    data = f.read()
    rules_,messages_ = data.split('\n\n')

    rules = {}
    for r in rules_.split('\n'):
        rules |= parse_rule(r)

    messages = messages_.split('\n')


updated_rules = rules.copy()

rule_8 = "8: 42"
for i in range(2,6):
    rule_8 += " |" + " 42"*i

rule_11 = "11: 42 31"
for i in range(2,6):
    rule_11 += " |" + " 42"*i + " 31"*i

updated_rules |= parse_rule(rule_8)
updated_rules |= parse_rule(rule_11)

print("Part 1:", count_valid_messages(messages, rules)) # 171
print("Part 2:", count_valid_messages(messages, updated_rules)) # 369
