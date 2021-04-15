def cycle_to_list(cycle, start):
    out = []
    curr = cycle[start]
    while 1:
        if curr == start:
            break
        out.append(curr)
        curr = cycle[curr]
    return out

def move_cups(data, iterations, max_value):
    cycle = {}
    for i,v in enumerate(data[:-1]):
        cycle[v] = data[i+1]
    cycle[data[-1]] = data[0]

    current = data[0]
    for _ in range(iterations):
        n1 = cycle[current]
        n2 = cycle[n1]
        n3 = cycle[n2]
        n4 = cycle[n3]

        cycle[current] = n4

        destination = current - 1
        while 1:
            if destination in (n1,n2,n3):
                destination -= 1
            elif destination == 0:
                destination = max_value
            else:
                break
        
        cycle[n3] = cycle[destination]
        cycle[destination] = n1

        current = n4
    return cycle

data = [1,9,8,7,5,3,4,6,2]
extended_data = data + list(range(10,1_000_001))

cycle_1 = move_cups(data, 100, 9)
part_1 = "".join([str(x) for x in cycle_to_list(cycle_1, 1)])
print("Part 1:", part_1) # 62934785

cycle_2 = move_cups(extended_data, 10_000_000, 1_000_000)
part_2 = cycle_2[1] * cycle_2[cycle_2[1]]
print("Part 2:", part_2) # 693659135400
