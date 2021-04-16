import re
from itertools import product

MEM_PATTERN = re.compile(r'mem\[(\d+)\] = (\d+)')

def parse_line(line):
    if line.startswith('mem'):
        address, value = re.match(MEM_PATTERN, line).groups()
        return int(address), int(value)
    else:
        return line.split(' = ')[1]

def get_value(value, mask):
    value = bin(value)
    out = ''
    for i in range(1, len(mask)+1):
        if mask[-i] == '0':
            out += '0'
        elif mask[-i] == '1':
            out += '1'
        elif i < len(value) - 1:
            out += value[-i]
        else:
            out += '0'
    out += 'b0'
    return int(out[::-1], 2)

def get_memory_addresses(mem, mask):
    mem = bin(mem)

    floating_bits = mask.count('X')
    configurations = product(('0','1'), repeat=floating_bits)

    out = []
    for bits in configurations:
        bit_counter = 0
        new_mem = ''
        for i in range(1, len(mask)+1):
            if mask[-i] == 'X':
                new_mem += bits[bit_counter]
                bit_counter += 1
            elif mask[-i] == '1':
                new_mem += '1'
            else:
                if i < len(mem) - 1:
                    new_mem += mem[-i]
                else:
                    new_mem += '0'
        new_mem += 'b0'
        out.append(int(new_mem[::-1], 2))
    return out

def main():
    with open('input.txt', 'r') as f:
        data = f.read()
        instructions = [parse_line(line) for line in data.splitlines()]
    
    mem = {}
    for i in instructions:
        if type(i) == str:
            mask = i
        else:
            mem[i[0]] = get_value(i[1], mask)
    print("Part 1:", sum(mem.values())) # 13865835758282

    mem = {}
    for i in instructions:
        if type(i) == str:
            mask = i
        else:
            addresses = get_memory_addresses(i[0], mask)
            for a in addresses:
                mem[a] = i[1]
    print("Part 2:", sum(mem.values())) # 4195339838136

main()