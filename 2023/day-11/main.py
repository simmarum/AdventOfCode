import numpy as np
from itertools import combinations


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.readlines()]


def part_1(inp):
    # fill empty space
    rows = []
    cols = []
    space = np.array([[c for c in line] for line in inp])
    for i in reversed(range(space.shape[0])):
        if np.all(space[i] == space[i][0]):
            rows.append(i)
    space = space.T
    for i in reversed(range(space.shape[0])):
        if np.all(space[i] == space[i][0]):
            cols.append(i)
    space = space.T

    # get all galaxies
    galaxies = np.argwhere(space == '#').tolist()
    galaxies_comb = list(combinations(galaxies, 2))
    path_sum = 0
    space_expand_ratio = 2
    for a, b in galaxies_comb:
        # path = astar(space, tuple(two_galaxies[0]), tuple(two_galaxies[1]))
        col_min = min(b[1], a[1])
        col_max = max(b[1], a[1])
        col_expand = sum([col_min < c < col_max for c in cols])
        col_max += (col_expand * (space_expand_ratio - 1))
        row_min = min(b[0], a[0])
        row_max = max(b[0], a[0])
        row_expand = sum([row_min < r < row_max for r in rows])
        row_max += (row_expand * (space_expand_ratio - 1))
        path_sum += abs(row_min - row_max) + abs(col_min - col_max)
    return path_sum


def part_2(inp):
    # fill empty space
    rows = []
    cols = []
    space = np.array([[c for c in line] for line in inp])
    for i in reversed(range(space.shape[0])):
        if np.all(space[i] == space[i][0]):
            rows.append(i)
    space = space.T
    for i in reversed(range(space.shape[0])):
        if np.all(space[i] == space[i][0]):
            cols.append(i)
    space = space.T

    # get all galaxies
    galaxies = np.argwhere(space == '#').tolist()
    galaxies_comb = list(combinations(galaxies, 2))
    path_sum = 0
    space_expand_ratio = 1000000
    for a, b in galaxies_comb:
        # path = astar(space, tuple(two_galaxies[0]), tuple(two_galaxies[1]))
        col_min = min(b[1], a[1])
        col_max = max(b[1], a[1])
        col_expand = sum([col_min < c < col_max for c in cols])
        col_max += (col_expand * (space_expand_ratio - 1))
        row_min = min(b[0], a[0])
        row_max = max(b[0], a[0])
        row_expand = sum([row_min < r < row_max for r in rows])
        row_max += (row_expand * (space_expand_ratio - 1))
        path_sum += abs(row_min - row_max) + abs(col_min - col_max)
    return path_sum


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
