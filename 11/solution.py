import copy
from collections import defaultdict
from pprint import pprint
import json

with open('input.txt', 'r') as f:
    data = f.read()
'''
data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
'''
seats = [list(row) for row in data.split('\n')]

height = len(seats)
width = len(seats[0])

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

seat_map = {}
for i in range(height):
    for j in range(width):
        seat_map[i,j] = {
            'value': seats[i][j],
            'neighbors': [],
            'nearest_seats': []
        }

for i, j in seat_map:
    for d_i, d_j in directions:
        k = i + d_i
        l = j + d_j
        if (k, l) in seat_map:
            seat_map[i,j]['neighbors'].append((k,l))
        while 1:
            if (k,l) not in seat_map:
                break
            if seat_map[k,l]['value'] != ".":
                seat_map[i,j]['nearest_seats'].append((k,l))
                break
            k += d_i
            l += d_j

def part1(seat_map):
    for _ in range(10):
        new = copy.deepcopy(seat_map)
        for (i,j), d in seat_map.items():
            count = 0
            for k,l in d['neighbors']:
                if seat_map[(k,l)]['value'] == '#':
                    count += 1
            if d['value'] == '#' and count >= 4:
                new[i,j]['value'] = 'L'
            elif d['value'] == 'L' and count == 0:
                new[i,j]['value'] = '#'
        if new == seat_map:
            count = 0
            for i,j in seat_map:
                if seat_map[i,j]['value'] == '#':
                    count += 1
            return count
        seat_map = new
    
print(part1(seat_map))

def occupied_in_direction(i, j, dx, dy, seats, radius):
    for _ in range(radius):
        i += dx
        j += dy
        if is_occupied(i, j, seats):
            return True
        if is_vacant(i, j, seats):
            return False
    return False

def count_occupied(i, j, seats, radius):
    count = 0
    for dx, dy in directions:
        if occupied_in_direction(i, j, dx, dy, seats, radius):
            count += 1
    return count

def is_vacant(i, j, seats):
    if not in_grid(i, j):
        return True
    if seats[i][j] == "L":
        return True
    return False

def is_occupied(i, j, seats):
    if not in_grid(i, j):
        return False
    if seats[i][j] == "#":
        return True
    return False

def in_grid(i, j):
    if i < 0:
        return False
    if i >= height:
        return False
    if j < 0:
        return False
    if j >= width:
        return False
    return True

def update_seats(seats, radius, tolerance):
    new_seats = copy.deepcopy(seats)
    for i in range(height):
        for j in range(width):
            if seats[i][j] == "L":
                if count_occupied(i, j, seats, radius) == 0:
                    new_seats[i][j] = "#"
            elif seats[i][j] == "#":
                if count_occupied(i, j, seats, radius) >= tolerance:
                    new_seats[i][j] = "L"
    return new_seats

def print_seats(seats):
    for row in seats:
        print("".join(row))

def part1(seats):
    while 1:
        prev = copy.deepcopy(seats)
        seats = update_seats(seats, 1, 4)
        print("")
        print_seats(seats)
        if prev == seats:
            break

    count = 0
    for i in range(height):
        for j in range(width):
            if seats[i][j] == "#":
                count += 1
                
    return count

def part2(seats):
    while 1:
        prev = copy.deepcopy(seats)
        seats = update_seats(seats, max(height,width), 5)
        print("")
        print_seats(seats)
        if prev == seats:
            break

    count = 0
    for i in range(height):
        for j in range(width):
            if seats[i][j] == "#":
                count += 1
                
    return count


#part_1 = part1(seats)
#part_2 = part2(seats)

#print("Part 1: ", part_1) #2281
#print("Part 2: ", part_2) #2085
