with open('input.txt', 'r') as f:
    data = f.read()

earliest_ts, schedule = data.split('\n')
earliest_ts = int(earliest_ts)
schedule = [(int(offset), int(bus)) for offset, bus in enumerate(schedule.split(',')) if bus != 'x']

shortest_wait = earliest_ts + max(schedule, key = lambda v: v[1])[1]
for offset, bus in schedule:
    wait = bus - earliest_ts % bus
    if wait < shortest_wait:
        shortest_wait, best_bus = wait, bus
part_1 = shortest_wait * best_bus

step_size = schedule[0][1]
ts = 0
for offset, bus in schedule[1:]:
    while (ts + offset) % bus != 0:
        ts += step_size
    step_size *= bus
part_2 = ts

print("Part 1:", part_1) # 296
print("Part 2:", part_2) # 535296695251210
