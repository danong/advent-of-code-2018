with open('input/day05.txt', 'r') as f:
    inp = [l.strip() for l in f.readlines()]

polymer = inp[0]

# part 1
stack = []
for char in polymer:
    if not stack:
        stack.append(char)
    elif stack[-1].lower() == char.lower() and stack[-1] != char:
        stack.pop()
    else:
        stack.append(char)
print(len(stack))
# part 2
min_char = None
min_len = float('inf')
for n_char in set(polymer):
    stack = []
    new_poly = [x for x in polymer if x.lower() != n_char.lower()]
    for char in new_poly:
        if not stack:
            stack.append(char)
        elif stack[-1].lower() == char.lower() and stack[-1] != char:
            stack.pop()
        else:
            stack.append(char)
    if len(stack) < min_len:
        min_char = n_char
        min_len = len(stack)
print(min_char, min_len)
