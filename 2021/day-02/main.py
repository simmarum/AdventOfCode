def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    horizontal = 0
    depth = 0
    for one_line in inp:
        where, how_much = one_line.split(" ")
        if where == 'down':
            depth += int(how_much)
        if where == 'up':
            depth -= int(how_much)
        if where == 'forward':
            horizontal += int(how_much)

    return depth * horizontal


def part_2(inp):
    horizontal = 0
    depth = 0
    aim = 0
    for one_line in inp:
        where, how_much = one_line.split(" ")
        if where == 'down':
            aim += int(how_much)
        if where == 'up':
            aim -= int(how_much)
        if where == 'forward':
            horizontal += int(how_much)
            depth += (int(how_much) * aim)

    return depth * horizontal


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
