from copy import deepcopy
from functools import reduce
from operator import xor


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def knot_hash(hash_str):
    lengths = list(map(ord, list(hash_str)))
    data = list(range(256))

    lengths = lengths + [17, 31, 73, 47, 23]
    data_len = len(data)
    skip_size = 0
    idx = 0
    for round in range(1, 64 + 1):
        for ll in lengths:
            new_data = deepcopy(data)
            for i in range(ll):
                new_data[(idx + i) %
                         data_len] = data[(idx + ll - 1 - i) %
                                          data_len]
            data = new_data
            idx += (ll + skip_size)
            skip_size += 1
    main_hash = ''
    for i in range(16):
        one_hash = data[i * 16:(i + 1) * 16]
        single_hash = f'{reduce(xor, one_hash):0>2x}'
        main_hash += single_hash
    return main_hash


def part_1(inp):
    hash_seed = inp[0]
    # hash_seed = 'flqrgnkx'
    used_sq = 0
    for i in range(128):
        hash_str = hash_seed + '-' + str(i)
        main_hash = knot_hash(hash_str)
        main_hash_bin = ''.join([f'{int(x, 16):0>4b}' for x in main_hash])
        main_hash_repr = main_hash_bin.replace('1', '#').replace('0', '.')
        used_sq += main_hash_repr.count('#')
    return used_sq


def dfs(grid, i, j, v):
    dirs = [[0, -1],
            [-1, 0],
            [0, 1],
            [1, 0]]
    rows = len(grid)
    cols = len(grid[0])

    if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '#':
        return
    grid[i][j] = '@'

    v.append((i, j))

    for dir in dirs:
        dfs(grid, i + dir[0], j + dir[1], v)


def part_2(inp):
    hash_seed = inp[0]
    # hash_seed = 'flqrgnkx'
    board = []
    for i in range(128):
        hash_str = hash_seed + '-' + str(i)
        main_hash = knot_hash(hash_str)
        main_hash_bin = ''.join([f'{int(x, 16):0>4b}' for x in main_hash])
        main_hash_repr = main_hash_bin.replace('1', '#').replace('0', '.')
        board.append(list(main_hash_repr))

    rows = len(board)
    cols = len(board[0])
    coordinates = set()
    for i in range(rows):
        for j in range(cols):
            if board[i][j] != '#':
                continue
            v = []
            dfs(board, i, j, v)
            coordinates.add(tuple(v))

    n_board = deepcopy(board)
    for idx, coords in enumerate(coordinates):
        for x, y in coords:
            n_board[x][y] = idx

    return len(coordinates)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
