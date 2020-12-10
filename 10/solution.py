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
    diff1 = 0
    diff3 = 1
    if adapters[0] == 1:
        diff1 += 1
    for i in range(len(adapters) - 1):
        if adapters[i+1] - adapters[i] == 3:
            diff3 += 1
        elif adapters[i+1] - adapters[i] == 1:
            diff1 += 1
    return diff1 * diff3

with open('input.txt', 'r') as f:
    adapters = sorted([int(x) for x in f.read().split('\n')])

part1 = multiply_diffs(adapters)
part2 = valid_ways(max(adapters), 0, frozenset(adapters + [0]))

print("Part 1: ", part1) # 2312
print("Part 2: ", part2) # 12089663946752