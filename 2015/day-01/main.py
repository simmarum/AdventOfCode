def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    for val in inp:
        return val.count('(') - val.count(')')


def part_2(inp):
    floor = 0
    for val in inp:
        for idx, c in enumerate(val, start=1):
            if c == '(':
                floor += 1
            if c == ')':
                floor -= 1
            if floor == -1:
                return idx


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
