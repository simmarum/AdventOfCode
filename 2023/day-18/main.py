def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).split() for line in f.readlines()]


dirs = {
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0),
    'U': (0, -1),
    '0': (1, 0),
    '1': (0, 1),
    '2': (-1, 0),
    '3': (0, -1)
}


def find_area(steps):
    pos = 0
    ans = 1
    for (x, y), n in steps:
        pos += x * n
        ans += y * n * pos + n / 2

    return int(ans)


def part_1(inp):
    steps = [(dirs[d], int(s)) for d, s, _ in inp]
    return find_area(steps)


def part_2(inp):
    steps = [(dirs[c[-2]], int(c[2:-2], 16)) for _, _, c in inp]
    return find_area(steps)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
