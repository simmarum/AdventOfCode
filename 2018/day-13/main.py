import numpy as np


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [[c for c in line.replace('\n', '')] for line in f.readlines()]


def print_board(b, c=None):
    if c is None:
        [print(''.join(row)) for row in b]
    else:
        tmp_board = np.copy(b)
        for one_c in c:
            tmp_board[one_c[0], one_c[1]] = one_c[2]
        [print(''.join(row)) for row in tmp_board]


def part_1(inp):

    dirs = {
        '>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0),
    }
    new_dir = {
        '>-': '>',
        '>\\': 'v',
        '>/': '^',

        '<-': '<',
        '<\\': '^',
        '</': 'v',

        'v|': 'v',
        'v\\': '>',
        'v/': '<',

        '^|': '^',
        '^\\': '<',
        '^/': '>',

    }
    turn_order_left = {
        '^': '<',
        '<': 'v',
        'v': '>',
        '>': '^',
    }
    turn_order_right = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^',
    }

    # prepare cleaned board - without carts
    board = np.array(inp)
    carts = []
    clean_board = np.copy(board)
    for iy, ix in np.ndindex(board.shape):
        if board[iy, ix] in '<>^v':
            if board[iy, ix-1] in '-+/\\' and board[iy, ix+1] in '-+/\\':
                clean_board[iy, ix] = '-'
                carts.append([iy, ix, board[iy, ix], 0])
            if board[iy-1, ix] in '|+/\\' and board[iy+1, ix] in '|+/\\':
                clean_board[iy, ix] = '|'
                carts.append([iy, ix, board[iy, ix], 0])
    carts.sort()

    # print(f"After tick {0}", carts)
    # print_board(clean_board, carts)
    for tick in range(1, 1+1000):
        for cart in carts:
            new_pos = (cart[0]+dirs[cart[2]][0], cart[1]+dirs[cart[2]][1])
            if cart[2]+clean_board[new_pos] in new_dir:
                cart[0] = new_pos[0]
                cart[1] = new_pos[1]
                cart[2] = new_dir[cart[2]+clean_board[new_pos]]
            elif clean_board[new_pos] == '+':
                cart[0] = new_pos[0]
                cart[1] = new_pos[1]
                if cart[3] == 0:
                    cart[2] = turn_order_left[cart[2]]
                elif cart[3] == 2:
                    cart[2] = turn_order_right[cart[2]]
                cart[3] = (cart[3]+1) % 3
        idx_carts = sorted([(c[0], c[1]) for c in carts])
        for n in range(1, len(idx_carts)):
            if idx_carts[n] == idx_carts[n-1]:
                return ','.join([str(c) for c in reversed(idx_carts[n])])

        # print(f"After tick {tick}", carts)
        # print_board(clean_board, carts)

    return None


def part_2(inp):

    dirs = {
        '>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0),
    }
    new_dir = {
        '>-': '>',
        '>\\': 'v',
        '>/': '^',

        '<-': '<',
        '<\\': '^',
        '</': 'v',

        'v|': 'v',
        'v\\': '>',
        'v/': '<',

        '^|': '^',
        '^\\': '<',
        '^/': '>',

    }
    turn_order_left = {
        '^': '<',
        '<': 'v',
        'v': '>',
        '>': '^',
    }
    turn_order_right = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^',
    }

    # prepare cleaned board - without carts
    board = np.array(inp)
    carts = []
    carts_removed = []
    clean_board = np.copy(board)
    for iy, ix in np.ndindex(board.shape):
        if board[iy, ix] in '<>^v':
            if board[iy, ix-1] in '-+/\\' and board[iy, ix+1] in '-+/\\':
                clean_board[iy, ix] = '-'
                carts.append([iy, ix, board[iy, ix], 0])
            if board[iy-1, ix] in '|+/\\' and board[iy+1, ix] in '|+/\\':
                clean_board[iy, ix] = '|'
                carts.append([iy, ix, board[iy, ix], 0])
    carts.sort()
    # print(f"After tick {0}", carts)
    # print_board(clean_board, carts)
    for tick in range(1, 1+100000):
        carts.sort()
        for cart in carts:
            new_pos = (cart[0]+dirs[cart[2]][0], cart[1]+dirs[cart[2]][1])
            if cart[2]+clean_board[new_pos] in new_dir:
                cart[0] = new_pos[0]
                cart[1] = new_pos[1]
                cart[2] = new_dir[cart[2]+clean_board[new_pos]]
            elif clean_board[new_pos] == '+':
                cart[0] = new_pos[0]
                cart[1] = new_pos[1]
                if cart[3] == 0:
                    cart[2] = turn_order_left[cart[2]]
                elif cart[3] == 2:
                    cart[2] = turn_order_right[cart[2]]
                cart[3] = (cart[3]+1) % 3
            idx_carts = sorted([(c[0], c[1]) for c in carts])
            for n in range(1, len(idx_carts)):
                if idx_carts[n] == idx_carts[n-1]:
                    carts = [c for c in carts if (c[0], c[1]) != idx_carts[n]]

        # print(f"After tick {tick}", len(carts))
        if len(carts) == 1:
            return f'{carts[0][1]},{carts[0][0]}'

    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
