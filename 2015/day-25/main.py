import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    code = 20151125
    a = 252533
    b = 33554393
    row = int(re.search('row (\\d+)', inp[0]).group(1))
    column = int(re.search('column (\\d+)', inp[0]).group(1))
    code_number = int((((row + column - 1) / 2) *
                       (row + column)) - row + 1)
    for _ in range(2, code_number + 1):
        code = (code * a) % b

    return code


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
