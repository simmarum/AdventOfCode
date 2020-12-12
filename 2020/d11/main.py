import numpy as np


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [[str(c) for c in line] for line in f.read().splitlines()]


def _magic_change(arr):
    new_arr = arr.copy()
    for (x, y), value in np.ndenumerate(arr):
        if value == '.':
            continue
        s_arr = arr[max(0, x-1):x+2, max(0, y-1):y+2]
        unique, counts = np.unique(s_arr, return_counts=True)
        sub_data = dict(zip(unique, counts))
        if (value == 'L') and (sub_data.get('#') is None):
            new_arr[x, y] = '#'
        if (value == '#') and (sub_data.get('#') >= 5):  # count itself
            new_arr[x, y] = 'L'
    return new_arr


def part_1(inp):
    length = max(map(len, inp))
    board = np.array([xi+[None]*(length-len(xi)) for xi in inp])
    calc_board = board
    while True:
        new_board = _magic_change(calc_board)
        if np.array_equal(calc_board, new_board):
            unique, counts = np.unique(new_board, return_counts=True)
            sub_data = dict(zip(unique, counts))
            return sub_data.get("#")
        calc_board = new_board
    return None


def _magic_change_2(arr):
    new_arr = arr.copy()
    m, n = arr.shape
    dd = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for (x, y), value in np.ndenumerate(arr):
        if value == '.':
            continue
        cnt_occup = 0
        for i, j in dd:
            xi = x+i
            yj = y+j
            while (0 <= xi < m) and (0 <= yj < n):
                if arr[xi][yj] == '#':
                    cnt_occup += 1
                    break
                elif arr[xi][yj] == 'L':
                    break
                xi += i
                yj += j

        if (value == 'L') and (cnt_occup == 0):
            new_arr[x, y] = '#'
        if (value == '#') and (cnt_occup >= 5):  # do not count itself
            new_arr[x, y] = 'L'
    return new_arr


def part_2(inp):
    length = max(map(len, inp))
    board = np.array([xi+[None]*(length-len(xi)) for xi in inp])
    calc_board = board
    while True:
        new_board = _magic_change_2(calc_board)
        if np.array_equal(calc_board, new_board):
            unique, counts = np.unique(new_board, return_counts=True)
            sub_data = dict(zip(unique, counts))
            return sub_data.get("#")
        calc_board = new_board
    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
