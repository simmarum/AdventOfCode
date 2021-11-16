import operator
import itertools
import more_itertools
from functools import reduce


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [int(line) for line in f.read().splitlines()]


def part_1(inp):
    inp.sort()
    inp = [0] + inp+[inp[-1]+3]
    x = list(itertools.starmap(operator.sub, zip(inp[1:], inp)))
    return x.count(1) * x.count(3)


def part_2(inp):
    inp.sort()
    inp = [0] + inp+[inp[-1]+3]
    return reduce(lambda a, b: a*b,
                  list(map(lambda el: 7 if el[1] == 4 else pow(2, el[1] - 1),
                           list(filter(lambda el: el[0] == 1,
                                       list(more_itertools.run_length.encode(
                                           list(itertools.starmap(
                                            operator.sub,
                                            zip(inp[1:], inp)
                                            ))
                                       ))
                                       ))
                           ))
                  )


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
