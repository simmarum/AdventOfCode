import more_itertools


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [int(line) for line in f.readlines()]


def part_1(inp):
    return sum([1 if j-i > 0 else 0 for i, j in zip(inp[:-1], inp[1:])])


def part_2(inp):
    sliding_wind = [sum(x) for x in more_itertools.triplewise(inp)]
    return sum([1 if j-i > 0 else 0 for i, j in zip(sliding_wind[:-1], sliding_wind[1:])])


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
