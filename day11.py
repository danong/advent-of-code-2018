from itertools import product
import numpy as np


def rc_to_xy(row, col):
    return col + 1, row + 1


def xy_to_rc(x, y):
    return y - 1, x - 1


def cell_power(x, y, serial):
    id = x + 10
    p_lvl = id * y
    p_lvl += serial
    p_lvl *= id
    if p_lvl < 100:
        p_lvl = 0
    else:
        p_lvl = int(str(p_lvl)[-3])
    p_lvl -= 5
    return p_lvl


def conv3x3(cells, row, col, conv_size):
    return np.sum(cells[row:row + conv_size, col:col + conv_size])


def main():
    serial = 8444
    dim = 300
    cells = np.zeros((dim, dim), dtype=np.int8)
    for row, col in product(range(dim), repeat=2):
        x, y = rc_to_xy(row, col)
        cells[row][col] = cell_power(x, y, serial)
    conv = np.zeros((dim, dim))
    sizes = np.zeros((dim, dim))
    for conv_size in range(1, 25):
        print(conv_size)
        for row, col in product(range(dim), repeat=2):
            temp = conv3x3(cells, row, col, conv_size)
            if temp > conv[row][col]:
                conv[row][col] = temp
                sizes[row][col] = conv_size
    max_val = conv.max()
    max_loc = np.where(conv == max_val)
    return rc_to_xy(max_loc[0][0], max_loc[1][0]), sizes[max_loc[0][0]][max_loc[1][0]]
    # row, col = np.unravel_index(cells.argmax(), cells.shape)
    #
    # return rc_to_xy(row, col)


if __name__ == '__main__':
    print(main())
    # print(cell_power(122,79,57))
    # print(cell_power(217,196, 39))
    # print(cell_power(101,153, 71))
    # print(xy_to_rc(300, 1))
    # scipy.signal.convolve2d(np.ones((3, 3)), cells, mode='valid')