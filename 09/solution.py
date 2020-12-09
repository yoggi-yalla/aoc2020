from itertools import combinations

def two_sums_to_k(k, cache):
    for a, b in combinations(cache, 2):
        if a + b == k:
            return True
    return False

def find_first_invalid(ints, cache_size):
    for i in range(cache_size, len(ints)):
        cache = ints[i - cache_size : i]
        if not two_sums_to_k(ints[i], cache):
            return ints[i]

def find_encryption_weakness(ints, target):
    i, j = 0, 1
    count = ints[0]
    while j < len(ints):
        if count == target:
            return max(ints[i:j]) + min(ints[i:j])
        elif count < target:
            count += ints[j]
            j += 1
        elif count > target:
            count -= ints[i]
            i += 1

with open('input.txt', 'r') as f:
    ints = [int(x) for x in f.read().split('\n')]

part1 = find_first_invalid(ints, 25)
part2 = find_encryption_weakness(ints, part1)

print("Part 1: ", part1) #1492208709
print("Part 2: ", part2) #238243506