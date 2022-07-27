import itertools
import math


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [int(line) for line in f.readlines()]


def split_presents(inp, how_many_groups):
    presents = inp
    if len(presents) != len(set(presents)):
        raise RuntimeError("Non unique presents weigth!")

    p_sum = sum(presents)
    w_group = p_sum // how_many_groups
    first_groups = []
    fg = []
    for i in range(1, len(presents)):
        first_groups = [combo for combo in itertools.combinations(
            presents, i) if sum(combo) == w_group]
        if first_groups != []:
            break
    first_groups = sorted(first_groups, key=lambda g: math.prod(g))
    return math.prod(first_groups[0])


def part_1(inp):
    return split_presents(inp, 3)


def part_2(inp):
    return split_presents(inp, 4)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
