import itertools

with open('input.txt','r') as f:
    ints = [int(x) for x in f.readlines()]

def two_makes_2020(ints):
    for i,j in itertools.combinations(ints, 2):
        if i+j == 2020:
            return i*j

def three_makes_2020(ints):
    for i,j,k in itertools.combinations(ints, 3):
        if i+j+k == 2020:
            return i*j*k

print("Part 1: " + str(two_makes_2020(ints)))
print("Part 2: " + str(three_makes_2020(ints)))
