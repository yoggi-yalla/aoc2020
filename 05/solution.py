def get_row(s):
    row = 0
    step = 64
    for ch in s[:7]:
        if ch == 'B':
            row += step
        step /= 2
    return int(row)

def get_col(s):
    col = 0
    step = 4
    for ch in s[-3:]:
        if ch == 'R':
            col += step
        step /= 2
    return int(col)

def get_seat_id(s):
    return get_row(s) * 8 + get_col(s)

def is_valid(id, seat_ids):
    if id in seat_ids:
        return False
    if id+1 in seat_ids and id-1 in seat_ids:
        return True
    return False

with open('input.txt','r') as f:
    seats = [s.strip() for s in f.readlines()]

seat_ids = [get_seat_id(x) for x in seats]

max_seat_id = max(seat_ids)
print("Part 1: ", max_seat_id)

for x in range(max_seat_id):
    if is_valid(x, seat_ids):
        print("Part 2: ", x)
