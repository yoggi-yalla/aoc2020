from collections import defaultdict
from functools import cache

@cache
def valid_ways(target, current, adapters):
    if current not in adapters:
        return 0
    if current > target:
        return 0
    if current == target:
        return 1
    return (
        valid_ways(target, current + 1, adapters) + 
        valid_ways(target, current + 2, adapters) + 
        valid_ways(target, current + 3, adapters)
    )

def multiply_diffs(adapters):
    count = defaultdict(lambda: 0)
    for i in range(len(adapters) - 1):
        diff = adapters[i+1] - adapters[i]
        count[diff] += 1
    return count[1] * count[3]

with open('input.txt', 'r') as f:
    adapters = sorted([int(x) for x in f.read().split('\n')])

adapters = [0] + adapters + [adapters[-1] + 3] # Adds outlet and device

part1 = multiply_diffs(adapters)
part2 = valid_ways(adapters[-1], 0, frozenset(adapters))

print("Part 1: ", part1) # 2312
print("Part 2: ", part2) # 12089663946752