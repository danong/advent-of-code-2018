import numpy as np
from collections import deque
import heapq

DIM = 1000

def neighbors(x, y):
    potentials = ((x+1, y), (x, y-1), (x, y+1), (x-1, y))
    for potential in potentials:
        if 0 <= potential[0] < DIM and 0 <= potentials[1] < DIM:
            yield potential


def main():
    with open('input/day17.txt', 'r') as f_in:
        inp = [l.strip() for l in f_in.readlines()]
    lines = []
    board = np.zeros((DIM, DIM), dtype=str)
    for line in inp:
        first = line[0]
        first_num = int(line[2:line.find(',')])
        second_start, second_end = map(int, line.split('=')[-1].split('..'))
        if first !=  'x':
            board[first_num, second_start:second_end + 1] = '#'
        else:
            board[second_start:second_end + 1, first_num] = '#'
    board[0,500] = '+'
    p_queue = []
    heapq.heappush(p_queue, (-1, 500))

    while queue:
        x, y = heapq.heappop(p_queue)
        x = -x
        if not board[n_x + 1, n_y] and (-(n_x + 1), n_y) not in p_queue:
            
       for n_x, n_y in neighbors(x, y):
                heapq.heappush(p_queue, (-n_x, n_y))
        
        board[x, y] = '~'
        

if __name__ == '__main__':
    main()
