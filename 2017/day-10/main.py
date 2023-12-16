from copy import deepcopy
from functools import reduce
from operator import xor


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    lengths = list(map(int, inp[0].split(',')))
    data = list(range(256))
    # lengths = [3, 4, 1, 5]
    # data = list(range(5))
    data_len = len(data)
    skip_size = 0
    idx = 0

    for ll in lengths:
        new_data = deepcopy(data)
        for i in range(ll):
            new_data[(idx + i) %
                     data_len] = data[(idx + ll - 1 - i) %
                                      data_len]
        data = new_data
        idx += (ll + skip_size)
        skip_size += 1

    return data[0] * data[1]


def part_2(inp):
    if len(inp) == 0:
        lengths = []
    else:
        lengths = list(map(ord, list(inp[0])))
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
        single_hash = hex(reduce(xor, one_hash))[2:4]
        main_hash += single_hash
    return main_hash


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
