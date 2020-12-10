def multiply_diffs(full_path):
    count = {1:0,2:0,3:0}
    for i in range(len(full_path) - 1):
        diff = full_path[i+1] - full_path[i]
        count[diff] += 1
    return count[1] * count[3]

def paths_to_target(current, target, full_path, memo={}):
    if current in memo:
        return memo[current]
    if current not in full_path:
        return 0
    if current == target:
        return 1
    memo[current] = (
        paths_to_target(current + 1, target, full_path, memo) + 
        paths_to_target(current + 2, target, full_path, memo) + 
        paths_to_target(current + 3, target, full_path, memo)
    )
    return memo[current]

with open('input.txt', 'r') as f:
    adapters = sorted([int(x) for x in f.read().split('\n')])

outlet = 0
device = adapters[-1] + 3
full_path = [outlet] + adapters + [device]

part1 = multiply_diffs(full_path)
part2 = paths_to_target(outlet, device, full_path)

print("Part 1: ", part1) # 2312
print("Part 2: ", part2) # 12089663946752