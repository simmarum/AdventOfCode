import numpy as np

np.set_printoptions(threshold=np.inf)


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [line for line in f.read().splitlines()]


def _get_init_board(first_board, ss):
    lf = len(first_board)
    lff = lf + 2 * ss
    board = np.zeros((lff, lff, lff))
    cen = lff // 2
    fb = np.array([first_board])
    x = cen - lf // 2
    if lf % 2 == 0:
        y = cen + lf // 2
    else:
        y = cen + lf // 2 + 1

    board[cen, x:y, x:y] = fb
    return board


def _one_turn(board):
    new_board = np.copy(board)
    ind = np.argwhere(board == 1)
    for i, j, k in ind:
        s_board = board[
            max(0, i - 1):i + 2,
            max(0, j - 1):j + 2,
            max(0, k - 1):k + 2
        ]
        neigh = np.count_nonzero(s_board)
        if neigh not in [3, 4]:
            new_board[i, j, k] = 0
    ind_0 = np.argwhere(board == 0)
    for i, j, k in ind_0:
        s_board = board[
            max(0, i - 1):i + 2,
            max(0, j - 1):j + 2,
            max(0, k - 1):k + 2
        ]
        neigh = np.count_nonzero(s_board)
        if (neigh == 3):
            new_board[i, j, k] = 1
    return new_board


def part_1(inp):
    ss = 6
    f = [[1 if x == '#' else 0 for x in c] for c in inp]
    board = _get_init_board(f, ss)
    new_board = np.copy(board)
    for _ in range(ss):
        new_board = _one_turn(new_board)
    return np.count_nonzero(new_board)

############


def _get_init_board_2(first_board, ss):
    lf = len(first_board)
    lff = lf + 2 * ss
    board = np.zeros((lff, lff, lff, lff))
    cen = lff // 2
    fb = np.array([first_board])
    x = cen - lf // 2
    if lf % 2 == 0:
        y = cen + lf // 2
    else:
        y = cen + lf // 2 + 1

    board[cen, cen, x:y, x:y] = fb
    return board


def _one_turn_2(board):
    new_board = np.copy(board)
    ind = np.argwhere(board == 1)
    for i, j, k, l in ind:
        s_board = board[
            max(0, i - 1):i + 2,
            max(0, j - 1):j + 2,
            max(0, k - 1):k + 2,
            max(0, l - 1):l + 2
        ]
        neigh = np.count_nonzero(s_board)
        if neigh not in [3, 4]:
            new_board[i, j, k, l] = 0
    ind_0 = np.argwhere(board == 0)
    for i, j, k, l in ind_0:
        s_board = board[
            max(0, i - 1):i + 2,
            max(0, j - 1):j + 2,
            max(0, k - 1):k + 2,
            max(0, l - 1):l + 2
        ]
        neigh = np.count_nonzero(s_board)
        if (neigh == 3):
            new_board[i, j, k, l] = 1
    return new_board


def part_2(inp):
    ss = 6
    f = [[1 if x == '#' else 0 for x in c] for c in inp]
    board = _get_init_board_2(f, ss)
    new_board = np.copy(board)
    for _ in range(ss):
        new_board = _one_turn_2(new_board)
    return np.count_nonzero(new_board)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
