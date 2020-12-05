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

print("Part 1: ", two_makes_2020(ints))
print("Part 2: ", three_makes_2020(ints))

#Part 1: 1005459
#Part 2: 92643264
