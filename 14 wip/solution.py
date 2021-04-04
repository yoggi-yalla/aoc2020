import re

def parse_line(line):
    op,v = line.split(' = ')
    if op != 'mask':
        op = int(re.search('\d+',op).group())
        v = int(v)
    return op, v

def apply_mask(mask, v):
    mask = [ch for ch in mask]
    v = [ch for ch in v]
    for i in range(len(v)):
        if mask[-(i+1)] == 'X':
            mask[-(i+1)] = v[-(i+1)]
    mask = "".join(mask).replace('X','0')
    return(int(mask,2))

def part_1(lines):
    mem = {}
    for i in range(64):
        print(bin(i))
    for line in lines:
        op, v = parse_line(line)
        if op == 'mask':
            mask = v
        else:
            store = apply_mask(mask, v)
            mem[op] = store
    return sum(mem.values())

def part_2(lines):
    mem = {}
    for line in lines:
        op, v = parse_line(line)
        if op == 'mask':
            mask = v
        else:
            write_to_mem(mem, mask, v)

def write_to_mem(mem, mask, v):
    count = mask.count('X')




with open('input.txt', 'r') as f:
    data = f.read()
'''
data = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""'''

lines = data.split('\n')

part1 = part_1(lines)
part2 = part_2(lines)


print("Part 1:", part1) # 13865835758282
print("Part 2:")

