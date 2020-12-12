with open('input.txt', 'r') as f:
    data = f.read()

instructions = [(x[:1], int(x[1:])) for x in data.split('\n')]

x = 0
y = 0
dx = 1
dy = 0
for op, v in instructions:
    if op == "F":
        x += dx * v
        y += dy * v
    elif op == "E":
        x += v
    elif op == "W":
        x -= v
    elif op == "N":
        y += v
    elif op == "S":
        y -= v
    elif op == "R":
        for _ in range(v//90):
            dx, dy = dy, -dx
    elif op == "L":
        for _ in range(v//90):
            dx, dy = -dy, dx

part1 = abs(x) + abs(y)

x = 0
y = 0
dx = 10
dy = 1
for op, v in instructions:
    if op == "F":
        x += dx * v
        y += dy * v
    elif op == "N":
        dy += v
    elif op == "S":
        dy -= v
    elif op == "E":
        dx += v
    elif op == "W":
        dx -= v
    elif op == "R":
        for _ in range(v//90):
            dx, dy = dy, -dx
    elif op == "L":
        for _ in range(v//90):
            dx, dy = -dy, dx

part2 = abs(x) + abs(y)

print("Part 1:", part1) # 364
print("Part 2:", part2) # 39518
