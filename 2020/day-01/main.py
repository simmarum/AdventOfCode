import itertools
from functools import reduce


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [int(line) for line in f.readlines()]


def part_1(inp):
    for val in inp:
        second_val = 2020-val
        if second_val in inp:
            return second_val * val


def part_2(inp):
    for comb in itertools.combinations(inp, 3):
        if sum(comb) == 2020:
            return reduce((lambda x, y: x * y), comb)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
