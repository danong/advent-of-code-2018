import numpy as np


def main():
    with open('input/day18.txt', 'r') as f_in:
        lines = [list(l.strip()) for l in f_in.readlines()]
    
    board = np.array(lines, dtype=str)
    print(board)

    minutes = 10
    order = ['.', '|', '#']
    
    for i in range(minutes):
        new_board = np.array(board)

        for idx, val in np.ndenumerate(board):
            char_idx = order.index(val)
            count = 0
            count_1 = 0
            count_2 = 0
            for offset in range(-1, 2, 2):
                for n_idx in ((idx[0] + offset, idx[1]), (idx[0], idx[1] + offset)):
                    if 0 <= n_idx[0] < board.shape[0] and 0 <= n_idx[1] < board.shape[1]:
                        if char_idx == 2:
                            count_1 += int(board[n_idx] == '|')
                            count_2 += int(board[n_idx] == '#')
                        else:
                            count += int(board[n_idx] == order[(char_idx + 1) % 3])

            if char_idx == 2:
                if not (count_1 and count_2):
                    new_board[idx] == '.'
            elif count >= 3:
                print('changing something')
                new_board[idx] = order[(char_idx + 1) % 3]

        board = new_board
        print(i)
        for row in board:
            print(''.join(row))
    print((board == '|').sum() * (board == '#').sum())



if __name__ == '__main__':
    main()
