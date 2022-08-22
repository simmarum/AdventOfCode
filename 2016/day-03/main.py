import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    good_triangle = 0
    for line in inp:
        m = re.search(' *(\\d+) *(\\d+) *(\\d+)', line)
        a = int(m.group(1))
        b = int(m.group(2))
        c = int(m.group(3))

        if (a + b > c) and (a + c > b) and (b + c > a):
            good_triangle += 1
    return good_triangle


def part_2(inp):
    good_triangle = 0
    a_nums = []
    b_nums = []
    c_nums = []
    for line in inp:
        m = re.search(' *(\\d+) *(\\d+) *(\\d+)', line)
        a = int(m.group(1))
        b = int(m.group(2))
        c = int(m.group(3))
        a_nums.append(a)
        b_nums.append(b)
        c_nums.append(c)
    all_nums = a_nums + b_nums + c_nums
    all_nums = iter(all_nums)
    for a, b, c in zip(all_nums, all_nums, all_nums):
        if (a + b > c) and (a + c > b) and (b + c > a):
            good_triangle += 1
    return good_triangle


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
