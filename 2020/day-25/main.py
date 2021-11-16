import itertools


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [int(line) for line in f.read().splitlines()]


def part_1(inp):
    c = inp[0]
    d = inp[1]
    sub_num = 7
    m = 20201227
    for i in itertools.count():
        if pow(sub_num, i, m) == d:
            return pow(c, i, m)
    return None


def part_2(inp):
    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
