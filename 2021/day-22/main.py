from itertools import product
from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    board = set()
    for idx, line in enumerate(inp):
        split_line = line.split()
        action = split_line[0]
        where = [int(x) for x in [
            split_line[1].split(',')[0].split('=')[1].split('..')[0],
            split_line[1].split(',')[0].split('=')[1].split('..')[1],
            split_line[1].split(',')[1].split('=')[1].split('..')[0],
            split_line[1].split(',')[1].split('=')[1].split('..')[1],
            split_line[1].split(',')[2].split('=')[1].split('..')[0],
            split_line[1].split(',')[2].split('=')[1].split('..')[1],
        ]]
        if not all([(-50 <= w <= 50) for w in where]):
            continue

        # print(idx, action, where)
        if action == 'on':
            board = board.union(set(product(
                range(where[0], where[1] + 1),
                range(where[2], where[3] + 1),
                range(where[4], where[5] + 1),
            )))
        else:
            board = board.difference(set(product(
                range(where[0], where[1] + 1),
                range(where[2], where[3] + 1),
                range(where[4], where[5] + 1),
            )))

    return len(board)


def part_2(inp):
    board = defaultdict(int)
    for idx, line in enumerate(inp):
        split_line = line.split()
        action = split_line[0]
        where = tuple([int(x) for x in [
            split_line[1].split(',')[0].split('=')[1].split('..')[0],
            split_line[1].split(',')[0].split('=')[1].split('..')[1],
            split_line[1].split(',')[1].split('=')[1].split('..')[0],
            split_line[1].split(',')[1].split('=')[1].split('..')[1],
            split_line[1].split(',')[2].split('=')[1].split('..')[0],
            split_line[1].split(',')[2].split('=')[1].split('..')[1],
        ]])
        # print(idx, action, where)
        new_where = defaultdict(int)
        for where_one, cnt in board.items():
            tmp_where = tuple([
                max(where[0], where_one[0]),
                min(where[1], where_one[1]),
                max(where[2], where_one[2]),
                min(where[3], where_one[3]),
                max(where[4], where_one[4]),
                min(where[5], where_one[5])
            ])
            if ((tmp_where[0] <= tmp_where[1]) and
                (tmp_where[2] <= tmp_where[3]) and
                    (tmp_where[4] <= tmp_where[5])):
                new_where[tmp_where] -= cnt

        for k in new_where.keys():
            board[k] += new_where[k]

        if action == 'on':
            board[where] += 1
    return sum(
        (
            (where[1] - where[0] + 1) *
            (where[3] - where[2] + 1) *
            (where[5] - where[4] + 1)
        ) * cnt
        for where, cnt in board.items()
    )


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
