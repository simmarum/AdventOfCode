import numpy as np


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [list(str(line).replace('\n', '')) for line in f.readlines()]


def print_sea(sea, i=None):
    print(f"State after step: {i}")
    for x in sea:
        print(''.join(x))


def solve(sea):
    sea = np.array(sea, dtype=str)
    step = 0
    # print_sea(sea, step)
    max_x = sea.shape[1]
    max_y = sea.shape[0]
    can_move = True
    while can_move is True:
        can_move = False
        step += 1
        # east
        to_move = []
        it = np.nditer(sea, flags=['multi_index'])
        while not it.finished:
            # print(it[0], it.multi_index)
            if it[0] == '>':
                if sea[it.multi_index[0]][(
                        it.multi_index[1] + 1) % max_x] == '.':
                    to_move.append([
                        (it.multi_index[0], it.multi_index[1]),
                        (it.multi_index[0], (it.multi_index[1] + 1) % max_x)
                    ])
            it.iternext()
        for move in to_move:
            can_move = True
            sea[move[0][0]][move[0][1]] = '.'
            sea[move[1][0]][move[1][1]] = '>'

        # south
        to_move = []
        it = np.nditer(sea, flags=['multi_index'], order='F')
        while not it.finished:
            if it[0] == 'v':
                if sea[(it.multi_index[0] + 1) %
                        max_y][it.multi_index[1]] == '.':
                    to_move.append([
                        (it.multi_index[0], it.multi_index[1]),
                        ((it.multi_index[0] + 1) % max_y, it.multi_index[1])
                    ])
            it.iternext()
        for move in to_move:
            can_move = True
            sea[move[0][0]][move[0][1]] = '.'
            sea[move[1][0]][move[1][1]] = 'v'

        # print_sea(sea, step)
    return step


def part_1(inp):
    return solve(inp)


def part_2(inp):
    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
