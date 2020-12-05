with open('input.txt','r') as f:
    m = f.read().split('\n')

strategies = [(1,1),(3,1),(5,1),(7,1),(1,2)]

width = len(m[0])
product_sum = 1

for dx, dy in strategies:
    x = y = sum_trees = 0
    while y < len(m):
        row = m[y]
        if row[x] == '#':
            sum_trees += 1
        x = (x+dx) % width
        y += dy

    product_sum *= sum_trees
    
    if (dx,dy) == (3,1):
        part_1 = sum_trees

print('Part 1: ', part_1)
print('Part 2: ', product_sum)

#Part 1: 272
#Part 2: 3898725600
