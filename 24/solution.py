from collections import defaultdict

def parse_instruction(row):
    instruction = []
    i = 0
    while i < len(row):
        if row[i] in ('s', 'n'):
            instruction.append(row[i:i+2])
            i += 2
        else:
            instruction.append(row[i])
            i += 1
    return instruction

direction_to_offset = {
    "e":  ( 0, 2),
    "se": ( 1, 1),
    "sw": ( 1,-1),
    "w":  ( 0,-2),
    "nw": (-1,-1),
    "ne": (-1, 1)
}

def instruction_to_coords(instruction):
    y, x = 0, 0
    for direction in instruction:
        offset = direction_to_offset[direction]
        y += offset[0]
        x += offset[1]
    return (y, x)

def main():
    with open('input.txt', 'r') as f:
        data = f.read()
        instructions = [parse_instruction(row) for row in data.splitlines()]

    black_tiles = set()
    for i in instructions:
        coords = instruction_to_coords(i)
        black_tiles.symmetric_difference_update([coords])
    print("Part 1:", len(black_tiles))

    for _ in range(100):
        nbr_black_neighbors = defaultdict(int)
        for y,x in black_tiles:
            for dy,dx in direction_to_offset.values():
                nbr_black_neighbors[(y+dy, x+dx)] += 1

        additions = set()
        for coords,v in nbr_black_neighbors.items():
            if coords not in black_tiles and v == 2:
                additions.add(coords)

        removals = set()
        for coords in black_tiles:
            n = nbr_black_neighbors[coords]
            if n == 0 or n > 2:
                removals.add(coords)

        black_tiles.update(additions)
        black_tiles.difference_update(removals)
    print("Part 2:", len(black_tiles))

main()
