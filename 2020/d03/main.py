from functools import reduce


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.readlines()]


def part_1(inp):
    trees = 0
    x = 0
    x_max = len(inp[0])
    for val in inp[1:]:
        x += 3
        x %= x_max
        if (val[x] == '#'):
            trees += 1

    return trees


def part_2(inp):
    xy_add = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    all_trees = []
    for x_add, y_add in xy_add:
        trees = 0
        x = 0
        y = 0
        x_max = len(inp[0])
        for y in range(y_add, len(inp), y_add):
            x += x_add
            x %= x_max
            if (inp[y][x] == '#'):
                trees += 1
        all_trees.append(trees)

    return reduce((lambda x, y: x * y), all_trees)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
