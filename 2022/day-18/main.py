import numpy as np
from scipy import ndimage


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    points = [tuple(map(int, line.split(','))) for line in inp]
    return sum([(6 - sum([abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) +
                          abs(p1[2] - p2[2]) == 1 for p2 in points])) for p1 in points])


def part_2(inp):
    points = set([tuple(map(int, line.split(','))) for line in inp])
    lazy_sum_of_surface = sum([
        (6 - sum([
            abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) +
            abs(p1[2] - p2[2]) == 1 for p2 in points
        ])
        ) for p1 in points
    ])
    max_dim = max((max(p) for p in points)) + 1
    world = np.zeros((max_dim, max_dim, max_dim), dtype='bool')
    for p in points:
        world[p] = True
    world2 = ndimage.binary_fill_holes(world)
    world3 = np.logical_xor(world, world2)
    points_trapped = list(map(tuple, np.argwhere(world3)))

    points = set([tuple(map(int, line.split(','))) for line in inp])
    lazy_sum_of_surface_points_trapped = sum([
        (6 - sum([
            abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) +
            abs(p1[2] - p2[2]) == 1 for p2 in points_trapped
        ])
        ) for p1 in points_trapped
    ])
    return lazy_sum_of_surface - lazy_sum_of_surface_points_trapped


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
