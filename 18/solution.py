def parse_row(row):
    expression = []
    for ch in row:
        if ch != " ":
            if ch.isnumeric():
                expression.append(int(ch))
            else:
                expression.append(ch)
    return expression

with open('input.txt', 'r') as f:
    data = f.read()
    rows = data.split('\n')
    expressions = [parse_row(row) for row in rows]

def evaluate_brackets(expr, base_evaluator):
    bracket_start = 0
    i = 0
    while i < len(expr):
        if expr[i] == '(':
            bracket_start = i
        if expr[i] == ')':
            bracket_end = i
            left_side = expr[:bracket_start]
            bracket = expr[bracket_start+1:bracket_end]
            if i == len(expr):
                right_side = []
            else:
                right_side = expr[bracket_end+1:]
            value = base_evaluator(bracket)
            expr = left_side + [value] + right_side
            i = 0
            continue
        i += 1
    return base_evaluator(expr)

def left_to_right(expr):
    ret = expr[0]
    i = 1
    while i < len(expr):
        op = expr[i]
        v = expr[i+1]
        if op == '*':
            ret *= v
        else:
            ret += v
        i += 2
    return ret

def add_then_multiply(expr):
    i = 0
    while i < len(expr) - 1:
        left = expr[i]
        op = expr[i+1]
        right = expr[i+2]
        if op == '+':
            v = left + right
            expr = expr[:i] + [v] + expr[i+3:]
            i = 0
        else:
            i += 2
    ret = 1
    for x in expr:
        if isinstance(x, int):
            ret *= x
    return ret

sum_1 = sum(evaluate_brackets(e, left_to_right) for e in expressions)
sum_2 = sum(evaluate_brackets(e, add_then_multiply) for e in expressions)

print("Part 1:", sum_1) # 5374004645253
print("Part 2:", sum_2) # 88782789402798
