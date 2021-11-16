def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    x = 0
    y = 0
    houses = {'0_0'}
    cnt = 0
    for val in inp:
        for c in val:
            if c == '^':
                x += 1
            elif c == 'v':
                x -= 1
            elif c == '>':
                y += 1
            elif c == '<':
                y -= 1
            houses.add(f"{x}_{y}")
        cnt = len(houses)
    return cnt


def part_2(inp):
    x = 0
    y = 0
    x_r = 0
    y_r = 0
    houses = {'0_0'}
    cnt = 0
    for val in inp:
        for c in val[::2]:
            if c == '^':
                x += 1
            elif c == 'v':
                x -= 1
            elif c == '>':
                y += 1
            elif c == '<':
                y -= 1
            houses.add(f"{x}_{y}")
        for c in val[1::2]:
            if c == '^':
                x_r += 1
            elif c == 'v':
                x_r -= 1
            elif c == '>':
                y_r += 1
            elif c == '<':
                y_r -= 1
            houses.add(f"{x_r}_{y_r}")
        cnt = len(houses)
    return cnt


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
