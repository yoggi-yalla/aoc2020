import copy
import re

def run_program(instructions):
    pos = 0
    accumulator = 0
    visited = set()
    while pos < len(instructions):
        if pos in visited:
            return pos, accumulator
        visited.add(pos)
        op, v = instructions[pos]
        if op == 'nop':
            pos += 1
        elif op == 'jmp':
            pos += v
        elif op == 'acc':
            accumulator += v
            pos += 1
    return pos, accumulator

def fix_and_run_program(instructions):
    for i in range(len(instructions)):
        new_instructions = copy.copy(instructions)
        op, v = instructions[i]
        if op == 'nop':
            new_instructions[i] = ('jmp', v)
        elif op == 'jmp':
            new_instructions[i] = ('nop', v)
        pos, accumulator = run_program(new_instructions)
        if pos == len(instructions):
            return pos, accumulator

def parse_line(line):
    op, v = re.match(r'(\w+) ([+-]?\w+)', line).groups()
    return op, int(v)

with open('input.txt','r') as f:
    data = f.read()

instructions = [parse_line(l) for l in data.split('\n')]

_, part1 = run_program(instructions)
_, part2 = fix_and_run_program(instructions)

print("Part 1: ", part1)
print("Part 2: ", part2)
    
#Part 1: 1521
#Part 2: 1016
