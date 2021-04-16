with open('input.txt', 'r') as f:
    data = f.read()

c_pub, d_pub = [int(x) for x in data.splitlines()]

'''
c_loop_size = 0
c_subject = 7
for _ in range(10_000_000):
    if c_subject == c_pub:
        break
    c_subject *= 7
    c_subject %= 20201227
    c_loop_size += 1

d_loop_size = 0
d_subject = 7
for _ in range(10_000_000):
    if d_subject == d_pub:
        break
    d_subject *= 7
    d_subject %= 20201227
    d_loop_size += 1
'''


c_loop_size = 3974371
d_loop_size = 8623736

def transform_subject_number(subject, loops):
    value = subject
    for _ in range(loops):
        value *= subject
        value %= 20201227
    return value

encryption_key = transform_subject_number(c_pub, d_loop_size)

print(encryption_key)