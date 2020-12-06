with open('input.txt','r') as f:
    groups = f.read().split('\n\n')

sum1 = sum2 = 0
for group in groups:
    sets = [set(x) for x in group.split('\n')]

    union = set.union(*sets)
    intersection = set.intersection(*sets)
    
    sum1 += len(union)
    sum2 += len(intersection)

print("Part 1: ", sum1)
print("Part 2: ", sum2)

#Part 1: 6437
#Part 2: 3229
