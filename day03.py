import numpy as np

with open('input/day03.txt', 'r') as f:
    inp = [l.strip() for l in f.readlines()]

dim = 1024
arr = np.zeros((dim, dim))

# part 1
for claim in inp:
    id, _, pos, size = claim.split(' ')
    row, col = (int(x) for x in pos[:-1].split(','))
    side1, side2 = [int(x) for x in size.split('x')]

    arr[row:row + side1, col:col + side2] += 1
print((arr > 1).sum())

# part 2
for claim in inp:
    id, _, pos, size = claim.split(' ')
    row, col = (int(x) for x in pos[:-1].split(','))
    side1, side2 = [int(x) for x in size.split('x')]

    if arr[row:row + side1, col:col + side2].sum() == side1 * side2:
        print(id)
        break
