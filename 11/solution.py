import copy
import time

def part1(grid, seats, seat_to_neighbors):
    while 1:
        new_grid = copy.deepcopy(grid)
        for i,j in seats:
            count = 0
            for k,l in seat_to_neighbors[i,j]:
                if grid[k][l] == "#":
                    count += 1
            if grid[i][j] == "#" and count >=4:
                new_grid[i][j] = "L"
            elif grid[i][j] == "L" and count == 0:
                new_grid[i][j] = "#"
        if new_grid == grid:
            break
        grid = new_grid

    count = 0
    for i,j in seats:
        if grid[i][j] == "#":
            count += 1
    return count

def part2(grid, seats, seat_to_visible):
    while 1:
        new_grid = copy.deepcopy(grid)
        for i,j in seats:
            count = 0
            for k,l in seat_to_visible[i,j]:
                if grid[k][l] == "#":
                    count += 1
            if grid[i][j] == "#" and count >=5:
                new_grid[i][j] = "L"
            elif grid[i][j] == "L" and count == 0:
                new_grid[i][j] = "#"
        if new_grid == grid:
            break
        grid = new_grid

    count = 0
    for i,j in seats:
        if grid[i][j] == "#":
            count += 1
    return count
    

#Main:
with open('input.txt', 'r') as f:
    data = f.read()

start = time.time()

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


coords = set()
seats = set()
seat_to_neighbors = {}
seat_to_visible = {}

for i in range(height):
    for j in range(width):
        coords.add((i,j))
        if grid[i][j] != ".":
            seats.add((i,j))
            seat_to_neighbors[i,j] = set()
            seat_to_visible[i,j] = set()

for i, j in seats:
    for d_i, d_j in directions:
        k = i + d_i
        l = j + d_j
        if (k,l) in seats:
            seat_to_neighbors[i,j].add((k,l))
        while 1:
            if (k,l) not in coords:
                break
            if grid[k][l] != ".":
                seat_to_visible[i,j].add((k,l))
                break
            k += d_i
            l += d_j

part_1 = part1(grid,seats,seat_to_neighbors)
part_2 = part2(grid,seats,seat_to_visible)

print("Part 1: ", part_1) #2281
print("Part 2: ", part_2) #2085
