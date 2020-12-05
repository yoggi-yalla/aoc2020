def get_row(s):
    row = 0
    step = 64
    for ch in s[:7]:
        if ch == 'B':
            row += step
        step //= 2
    return row

def get_col(s):
    col = 0
    step = 4
    for ch in s[-3:]:
        if ch == 'R':
            col += step
        step //= 2
    return col

def get_seat_id(s):
    return get_row(s) * 8 + get_col(s)

def is_valid(i, seat_ids):
    return (
        i not in seat_ids and 
        i+1 in seat_ids and 
        i-1 in seat_ids
    )

with open('input.txt','r') as f:
    seat_ids = [get_seat_id(s.strip()) for s in f.readlines()]

max_id = max(seat_ids)

for i in range(max_id):
    if is_valid(i, seat_ids):
        my_id = i


print("Part 1: ", max_id)
print("Part 2: ", my_id)

#Part 1: 871
#Part 2: 640
