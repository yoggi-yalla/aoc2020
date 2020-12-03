with open('input.txt','r') as f:
    m = f.read().split('\n')

strategies = [(1,1),(3,1),(5,1),(7,1),(1,2)]

width = len(m[0])
product_sum = 1
for s in strategies:
    dx = s[0]
    dy = s[1]
    xpos = 0
    ypos = 0
    sum_trees = 0

    while ypos < len(m):
        row = m[ypos]
        if row[xpos] == '#':
            sum_trees += 1
        xpos = (xpos+dx) % width
        ypos += dy

    product_sum *= sum_trees
    
    if s == (3,1):
        print("Part 1: " + str(sum_trees))

print('Part 2: ' + str(product_sum))