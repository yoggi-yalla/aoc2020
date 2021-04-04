from itertools import product

with open('input.txt', 'r') as f:
    data = f.read()
    rows = data.split('\n')



##################################
###           PART 1           ###
##################################

grid = [[[ch for ch in row] for row in rows]]
directions = [x for x in product([1,0,-1],repeat=3) if x != (0,0,0)] # [(1,1,1), (1,1,0), ...]

def get_size(grid):
    return (len(grid), len(grid[0]), len(grid[0][0]))

def show(grid):
    size = get_size(grid)
    for z in range(size[0]):
        print("\nz={}".format(z))
        for y in range(size[1]):
            print("".join(grid[z][y]))
    print('\n')

def expand_grid(grid):
    size = get_size(grid)
    new_z = size[0] + 2
    new_y = size[1] + 2
    new_x = size[2] + 2
    new_grid = [[['.' for _ in range(new_x)] for _ in range(new_y)] for _ in range(new_z)]
    for z in range(size[0]):
        for y in range(size[1]):
            for x in range(size[2]):
                if grid[z][y][x] == '#':
                    new_grid[z+1][y+1][x+1] = '#'
    return new_grid

def is_in_grid(z,y,x,grid):
    if z < 0 or y < 0 or x < 0:
        return False
    size = get_size(grid)
    if z >= size[0] or y >= size[1] or x >= size[2]:
        return False
    return True

def count_active(grid):
    size = get_size(grid)
    count = 0
    for z in range(size[0]):
        for y in range(size[1]):
            for x in range(size[2]):
                if grid[z][y][x] == '#':
                    count += 1
    return count

def count_neighbors(z,y,x,grid):
    count = 0
    for dz,dy,dx in directions:
        new_z = z + dz
        new_y = y + dy
        new_x = x + dx
        if is_in_grid(new_z, new_y, new_x, grid):
            if grid[new_z][new_y][new_x] == '#':
                count += 1
    return count

def compute_buffer(grid):
    buffer = {}
    size = get_size(grid)
    for z in range(size[0]):
        for y in range(size[1]):
            for x in range(size[2]):
                v = grid[z][y][x]
                count = count_neighbors(z,y,x,grid)
                if v == '#' and count not in [2,3]:
                    buffer[(z,y,x)] = '.'
                if v == '.' and count == 3:
                    buffer[(z,y,x)] = '#'
    return buffer

def update(grid, buffer):
    for (z,y,x),v in buffer.items():
        grid[z][y][x] = v
    return grid

def run(grid, iterations):
    for _ in range(iterations):
        new_grid = expand_grid(grid)
        buffer = compute_buffer(new_grid)
        grid = update(new_grid, buffer)
    return count_active(grid)

print("Part 1:", run(grid,6))



##################################
###           PART 2           ###
##################################

grid_4d = [[[[ch for ch in row] for row in rows]]]
directions_4d = [x for x in product([1,0,-1],repeat=4) if x != (0,0,0,0)] # [(1,1,1,1), (1,1,1,0), ...]

def get_size_4d(grid):
    return (len(grid), len(grid[0]), len(grid[0][0]), len(grid[0][0][0]))

def show_4d(grid):
    size = get_size_4d(grid)
    for w in range(size[0]):
        for z in range(size[1]):
            print("\nw={}".format(w), "z={}".format(z))
            for y in range(size[2]):
                print("".join(grid[w][z][y]))
    print('\n')

def expand_grid_4d(grid):
    size = get_size_4d(grid)
    new_w = size[0] + 2
    new_z = size[1] + 2
    new_y = size[2] + 2
    new_x = size[3] + 2
    new_grid = [[[['.' for _ in range(new_x)] for _ in range(new_y)] for _ in range(new_z)]for _ in range(new_w)]
    for w in range(size[0]):
        for z in range(size[1]):
            for y in range(size[2]):
                for x in range(size[3]):
                    if grid[w][z][y][x] == '#':
                        new_grid[w+1][z+1][y+1][x+1] = '#'
    return new_grid

def is_in_grid_4d(w,z,y,x,grid):
    if w < 0 or z < 0 or y < 0 or x < 0:
        return False
    size = get_size_4d(grid)
    if w >= size[0] or z >= size[1] or y >= size[2] or x >= size[3]:
        return False
    return True

def count_active_4d(grid):
    size = get_size_4d(grid)
    count = 0
    for w in range(size[0]):
        for z in range(size[1]):
            for y in range(size[2]):
                for x in range(size[3]):
                    if grid[w][z][y][x] == '#':
                        count += 1
    return count

def count_neighbors_4d(w,z,y,x,grid):
    count = 0
    for dw,dz,dy,dx in directions_4d:
        new_w = w + dw
        new_z = z + dz
        new_y = y + dy
        new_x = x + dx
        if is_in_grid_4d(new_w,new_z,new_y,new_x,grid):
            if grid[new_w][new_z][new_y][new_x] == '#':
                count += 1
    return count

def compute_buffer_4d(grid):
    buffer = {}
    size = get_size_4d(grid)
    for w in range(size[0]):
        for z in range(size[1]):
            for y in range(size[2]):
                for x in range(size[3]):
                    v = grid[w][z][y][x]
                    count = count_neighbors_4d(w,z,y,x,grid)
                    if v == '#' and count not in [2,3]:
                        buffer[(w,z,y,x)] = '.'
                    if v == '.' and count == 3:
                        buffer[(w,z,y,x)] = '#'
    return buffer

def update_4d(grid, buffer):
    for (w,z,y,x),v in buffer.items():
        grid[w][z][y][x] = v
    return grid

def run_4d(grid, iterations):
    for _ in range(iterations):
        new_grid = expand_grid_4d(grid)
        buffer = compute_buffer_4d(new_grid)
        grid = update_4d(new_grid, buffer)
    return count_active_4d(grid)

print("Part 2:", run_4d(grid,6))