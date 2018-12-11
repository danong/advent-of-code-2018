import timeit
from collections import namedtuple
from itertools import product

import numpy as np
from scipy.signal import convolve2d

Sum = namedtuple('Sum', ['sum', 'x', 'y', 'size'])
SERIAL = 8444
DIM = 300
SIZE = 300


def power(x, y):
    r = x + 11
    return (((r * y + r + SERIAL) * r) // 100) % 10 - 5


def brute_force(grid):
    best = Sum(float('-inf'), -1, -1, 3)
    for s in range(1, SIZE):
        c = convolve2d(grid, np.ones((s, s), dtype=np.int), mode='valid')
        x, y = np.unravel_index(c.argmax(), c.shape)
        if c[x, y] > best.sum:
            best = Sum(c[x, y], x, y, s)
    print(best)


def summed_area(grid):
    sum_grid = grid.cumsum(axis=0).cumsum(axis=1)
    best = Sum(float('-inf'), -1, -1, 3)
    for s in range(1, SIZE):
        for x, y in product(range(s, DIM), repeat=2):
            square_sum = sum_grid[x, y] + sum_grid[x - s, y - s] - sum_grid[x - s, y] - sum_grid[x, y - s]
            if square_sum > best.sum:
                best = Sum(square_sum, x - s + 1, y - s + 1, s)
    print(best)


if __name__ == '__main__':
    p_grid = np.fromfunction(power, (DIM, DIM), dtype=np.int8)
    t1 = timeit.default_timer()
    brute_force(p_grid)
    t2 = timeit.default_timer()
    summed_area(p_grid)
    t3 = timeit.default_timer()
    print('brute force: {}'.format(t2 - t1))
    print('summed area: {}'.format(t3 - t2))
