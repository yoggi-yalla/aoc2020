def compute_shifts(grid, tolerance, surroundings_map):
    buffer = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])): 
            if grid[i][j] == ".":
                continue
            count = count_surroundings(i, j, grid, surroundings_map)
            if grid[i][j] == "#" and count >= tolerance:
                buffer[i,j] = "L"
            elif grid[i][j] == "L" and count == 0:
                buffer[i,j] = "#"
    return buffer

def count_surroundings(i, j, grid, surroundings_map):
    count = 0
    for i_n, j_n in surroundings_map[i,j]:
        if grid[i_n][j_n] == "#":
            count += 1
    return count

def update_grid(grid, buffer):
    for (i,j), v in buffer.items():
        grid[i][j] = v

def count_seated(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                count += 1
    return count

def run(grid, tolerance, surroundings):
    while 1:
        buffer = compute_shifts(grid, tolerance, surroundings)
        update_grid(grid, buffer)
        if not buffer:
            break
    return count_seated(grid)
    
def main():
    with open('input.txt', 'r') as f:
        data = f.read()

    grid = [list(row) for row in data.split('\n')]
    
    height = len(grid)
    width = len(grid[0])

    directions = (
        (-1,-1), 
        (-1, 0), 
        (-1, 1), 
        ( 0, 1), 
        ( 0,-1), 
        ( 1,-1), 
        ( 1, 0), 
        ( 1, 1)
    )

    seats = set()
    seat_to_neighbors = {}
    seat_to_visible = {}

    for i in range(height):
        for j in range(width):
            if grid[i][j] != ".":
                seats.add((i,j))
                seat_to_neighbors[i,j] = set()
                seat_to_visible[i,j] = set()

    for i, j in seats:
        for d_i, d_j in directions:
            i_n = i + d_i
            j_n = j + d_j
            if (i_n, j_n) in seats:
                seat_to_neighbors[i,j].add((i_n,j_n))
            while 1:
                if not ((0 <= i_n < height) and (0 <= j_n < width)):
                    break
                if (i_n, j_n) in seats:
                    seat_to_visible[i,j].add((i_n,j_n))
                    break
                i_n += d_i
                j_n += d_j

    grid2 = [list(x) for x in grid]

    part_1 = run(grid, 4, seat_to_neighbors)
    part_2 = run(grid2, 5, seat_to_visible)

    print("Part 1: ", part_1) #2281
    print("Part 2: ", part_2) #2085

main()