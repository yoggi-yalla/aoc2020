from collections import defaultdict

def parse_instruction(line):
    instruction = []
    i = 0
    while i < len(line):
        if line[i] in ('s', 'n'):
            instruction.append(line[i:i+2])
            i += 2
        else:
            instruction.append(line[i])
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
        instructions = [parse_instruction(line) for line in data.splitlines()]

    black_tiles = set()
    for i in instructions:
        coords = instruction_to_coords(i)
        black_tiles = black_tiles ^ set([coords])
    print("Part 1:", len(black_tiles)) # 275

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

        black_tiles = (black_tiles | additions) - removals

    print("Part 2:", len(black_tiles)) # 3537

main()
