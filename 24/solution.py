with open('input.txt', 'r') as f:
    data = f.read()

def parse_instruction(row):
    instructions = []
    i = 0
    while i < len(row):
        if row[i] in ('s', 'n'):
            instructions.append(row[i:i+2])
            i += 2
        else:
            instructions.append(row[i])
            i += 1
    return instructions

direction_to_offset = {
    "e":  ( 0, 2),
    "se": ( 1, 1),
    "sw": ( 1,-1),
    "w":  ( 0,-2),
    "nw": (-1,-1),
    "ne": (-1, 1)
}

def instruction_to_offset(instruction):
    dy, dx = 0, 0
    for direction in instruction:
        offset = direction_to_offset[direction]
        dy += offset[0]
        dx += offset[1]
    return (dy,dx)

def count_black_neighbors(y,x,grid):
    count = 0
    for dy,dx in direction_to_offset.values():
        if grid[y+dy][x+dx] == 'B':
            count += 1
    return count

def compute_buffer(grid):
    buffer = {}
    for x in range(2,len(grid)-2):
        for y in range(2+x%2,len(grid)-2,2):
            color = grid[y][x]
            count = count_black_neighbors(y,x,grid)
            if color == 'B':
                if count == 0 or count > 2:
                    buffer[(y,x)] = 'W'
            else:
                if count == 2:
                    buffer[(y,x)] = 'B'
    return buffer

def update_grid(grid, buffer):
    for (y,x), v in buffer.items():
        grid[y][x] = v
    return grid

def main():
    instructions = [parse_instruction(row) for row in data.splitlines()]

    dim = 250
    grid = [['.' for _ in range(dim)] for _ in range(dim)]

    for x in range(dim):
        for y in range(x%2, dim, 2):
            grid[y][x] = 'W'

    y_0 = int(dim/2)
    x_0 = int(dim/2)

    for instruction in instructions:
        dy,dx = instruction_to_offset(instruction)
        y = y_0 + dy
        x = x_0 + dx
        if grid[y][x] == 'W':
            grid[y][x] = 'B'
        else:
            grid[y][x] = 'W'

    print("Part 1:", sum(row.count('B') for row in grid)) # 275

    for _ in range(100): # takes ~2s
        buffer = compute_buffer(grid)
        grid = update_grid(grid, buffer)

    print("Part 2:", sum(row.count('B') for row in grid)) # 3537

main()