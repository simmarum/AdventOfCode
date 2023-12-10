from functools import reduce
import operator
from copy import deepcopy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    magic_sum = 0
    for line in inp:
        last_values = []
        line = list(map(int, line.split(" ")))
        res = deepcopy(line)
        last_values.append(res[-1])
        while len(set(res)) > 1:
            res = list(map(operator.sub, res[1:], res[:-1]))
            last_values.append(res[-1])

        magic_sum += sum(last_values)
    return magic_sum


def part_2(inp):
    magic_sum = 0
    for line in inp:
        first_values = []
        line = list(map(int, line.split(" ")))
        res = deepcopy(line)
        first_values.append(res[0])
        while len(set(res)) > 1:
            res = list(map(operator.sub, res[1:], res[:-1]))
            first_values.append(res[0])
        first_values.append(0)
        magic_sum += reduce(lambda a, b: b - a, first_values[::-1])
    return magic_sum


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
