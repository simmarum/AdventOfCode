from ast import literal_eval
import math
from itertools import permutations


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def al(data, new_num):
    if new_num is None:
        return data
    if isinstance(data, int):
        return data + new_num
    return [al(data[0], new_num), data[1]]


def ar(data, new_num):
    if new_num is None:
        return data
    if isinstance(data, int):
        return data + new_num
    return [data[0], ar(data[1], new_num)]


def explode(data, level):
    if isinstance(data, int):
        return False, None, data, None
    if level == 0:
        return True, data[0], 0, data[1]
    exp, left, data[0], right = explode(data[0], level - 1)
    if exp:
        return True, left, [data[0], al(data[1], right)], None
    exp, left, data[1], right = explode(data[1], level - 1)
    if exp:
        return True, None, [ar(data[0], left), data[1]], right
    return False, None, data, None


def split(data):
    if isinstance(data, int):
        if data >= 10:
            return True, [math.floor(data / 2), math.ceil(data / 2)]
        return False, data
    change, data[0] = split(data[0])
    if change:
        return True, [data[0], data[1]]
    change, data[1] = split(data[1])
    return change, [data[0], data[1]]


def magn(data):
    if isinstance(data, int):
        return data
    return 3 * magn(data[0]) + 2 * magn(data[1])


def merge(all_data, new_data):
    data = [all_data, new_data]
    while True:
        change, _, data, _ = explode(data, 4)
        if change:
            continue
        change, data = split(data)
        if not change:
            break
    return data


def part_1(inp):
    first_data = literal_eval(inp[0])
    for other_line in inp[1:]:
        new_data = literal_eval(other_line)
        first_data = merge(first_data, new_data)
    return magn(first_data)


def part_2(inp):
    all_perms = permutations(inp, 2)
    max_res = 0
    for one_perms in all_perms:
        tmp_res = magn(
            merge(literal_eval(one_perms[0]), literal_eval(one_perms[1])))
        max_res = max(max_res, tmp_res)
    return max_res


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
