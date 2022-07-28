import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.read().splitlines()]


class P1_int(int):
    def __add__(self, other):
        return P1_int(int(self) + int(other))

    def __sub__(self, other):
        return P1_int(int(self) * int(other))


class P2_int(int):
    def __add__(self, other):
        return P2_int(int(self) * int(other))

    def __mul__(self, other):
        return P2_int(int(self) + int(other))


def part_1(inp):
    ss = 0
    for val in inp:
        tt = val.replace('*', '-')
        tt = re.sub(r"(\d+)", r"P1_int(\1)", tt)
        ss += eval(tt)
    return ss


def part_2(inp):
    ss = 0
    for val in inp:
        tt = val.replace('*', '?').replace('+', '*').replace('?', '+')
        tt = re.sub(r"(\d+)", r"P2_int(\1)", tt)
        ss += eval(tt)
    return ss


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
