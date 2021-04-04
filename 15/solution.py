from numba import jit

@jit(nopython=True) # 65% faster ¯\_(ツ)_/¯
def play_game(iterations):

    nums = [2,1,10,11,0,6] # puzzle input
    index = len(nums)
    last = nums[-1]

    spoken = {}
    for i,num in enumerate(nums):
        spoken[num] = i

    while index < iterations:
        if last in spoken:
            new_last = index - spoken[last] - 1
            spoken[last] = index - 1
            last = new_last
        else:
            spoken[last] = index - 1
            last = 0
        index += 1

    return last

print("Part 1:", play_game(2020)) # 232
print("Part 1:", play_game(30_000_000)) # 18929178
