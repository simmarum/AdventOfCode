def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    full_cointans = 0
    for line in inp:
        e1a, e1b, e2a, e2b = list(map(int, line.split(',')[0].split(
            '-'))) + list(map(int, line.split(',')[1].split('-')))
        e1 = set(range(e1a, e1b + 1))
        e2 = set(range(e2a, e2b + 1))
        if e1.issubset(e2) or e2.issubset(e1):
            full_cointans += 1
    return full_cointans


def part_2(inp):
    overlaps = 0
    for line in inp:
        e1a, e1b, e2a, e2b = list(map(int, line.split(',')[0].split(
            '-'))) + list(map(int, line.split(',')[1].split('-')))
        e1 = set(range(e1a, e1b + 1))
        e2 = set(range(e2a, e2b + 1))
        if len(e1.intersection(e2)) > 0:
            overlaps += 1
    return overlaps


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
