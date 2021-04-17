import re
from itertools import product

MEM_PATTERN = re.compile(r'mem\[(\d+)\] = (\d+)')

def padded_bin(i):
    bin_string = bin(i)[2:]
    padding = 36-len(bin_string)
    return '0'*padding + bin_string

with open('input.txt', 'r') as f:
    data = f.read()

    mem_1 = {}
    mem_2 = {}    
    for line in data.splitlines():
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        else:
            address, value = re.match(MEM_PATTERN, line).groups()
            p_address = padded_bin(int(address))
            p_value = padded_bin(int(value))

            # Part 1
            masked_value = ''
            for i in range(36):
                if mask[i] == 'X':
                    masked_value += p_value[i]
                else:
                    masked_value += mask[i]
            mem_1[int(p_address, 2)] = int(masked_value, 2)

            # Part 2
            floating_bits = mask.count('X')
            configurations = product(('1','0'), repeat=floating_bits)
            
            mems = []
            for bits in configurations:
                new_mem = ''
                bits_counter = 0
                for i in range(36):
                    if mask[i] == 'X':
                        new_mem += bits[bits_counter]
                        bits_counter += 1
                    elif mask[i] == '1':
                        new_mem += '1'
                    else:
                        new_mem += p_address[i]
                mems.append(new_mem)

            for m in mems:
                mem_2[int(m,2)] = int(p_value,2)

print("Part 1:", sum(mem_1.values())) # 13865835758282
print("Part 2:", sum(mem_2.values())) # 4195339838136