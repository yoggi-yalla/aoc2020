with open('input.txt', 'r') as f:
    data = f.read()

def transform_subject_number(subject, loops):
    value = subject
    for _ in range(loops):
        value *= subject
        value %= 20201227
    return value

c_pub, d_pub = [int(x) for x in data.splitlines()]

c_loop_size = 0
c_subject = 7
while 1:
    if c_subject == c_pub:
        break
    c_subject *= 7
    c_subject %= 20201227
    c_loop_size += 1

encryption_key = transform_subject_number(d_pub, c_loop_size)

print("Part 1:", encryption_key)

# No Part 2 on 25th, all done!