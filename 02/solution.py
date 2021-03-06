import re

pattern = re.compile(r'(\d+)-(\d+) (\w): (\w+)')

def parse_line(line):
    a, b, char, pw = re.match(pattern,line).groups()
    return int(a), int(b), char, pw

with open('input.txt', 'r') as f:
    passwords = [parse_line(x) for x in f.readlines()]

sum1 = sum2 = 0
for a, b, char, pw in passwords:
    if a <= pw.count(char) <= b:
        sum1 += 1
    if (pw[a-1] == char) ^ (pw[b-1] == char):
        sum2 += 1

print("Part 1: ", sum1)
print("Part 2: ", sum2)

#Part 1: 666
#Part 2: 670
