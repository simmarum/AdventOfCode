import numpy as np


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.readlines()]


def get_positions(inp):
    rocks = set()
    start_pos = None
    x_max = 0
    y_max = 0
    for x, line in enumerate(inp):
        x_max = max(x_max, x)
        for y, c in enumerate(line):
            y_max = max(y_max, y)
            if c == '#':
                rocks.add((x, y))
            elif c == 'S':
                start_pos = (x, y)
    return start_pos, rocks, (x_max, y_max)


def go_everywhere(start_pos, rocks, min_tile,
                  max_tile, steps, return_steps=[]):
    ret_steps = []
    positions = set([start_pos])
    for step in range(1, steps + 1):
        positions = {(pos[0] + dx, pos[1] + dy)
                     for pos in positions
                     for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))}
        positions.difference_update(rocks)
        if step in return_steps:
            ret_steps.append(len(positions))
    if ret_steps:
        return ret_steps
    else:
        return len(positions)


def part_1(inp):
    start_pos, rocks, max_tile = get_positions(inp)
    return go_everywhere(start_pos, rocks, (0, 0), max_tile, 64)


def part_2(inp):
    # 26501365 = 202300 * 131 + 65 where 131 is the dimension of the grid
    start_pos, rocks, max_tile = get_positions(inp)
    inp_extended = []
    # 5 because it needs to be big enough to calculate a,b,c
    ext_n = 5
    for _ in range(ext_n):
        for line in inp:
            inp_extended.append(ext_n * line.replace("S", "."))
    start_pos = (
        (max_tile[0] + 1) * (ext_n // 2) + start_pos[0],
        (max_tile[1] + 1) * (ext_n // 2) + start_pos[1]
    )
    _, rocks, max_tile = get_positions(inp_extended)
    a, b, c = go_everywhere(start_pos, rocks, (0, 0), max_tile,
                            65 + 131 + 131, [65, 65 + 131, 65 + 131 + 131])
    vandermonde = np.matrix([[0, 0, 1], [1, 1, 1], [4, 2, 1]])
    b = np.array([a, b, c])
    x = np.linalg.solve(vandermonde, b).astype(np.int64)
    n = 202300
    return x[0] * n * n + x[1] * n + x[2]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
