from itertools import combinations


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    magic_sum = 0
    for line in inp:
        x = list(map(int, line.split()))
        magic_sum += (max(x) - min(x))
    return magic_sum


def part_2(inp):
    magic_sum = 0
    for line in inp:
        x = list(map(int, line.split()))
        x = sorted(x, reverse=True)
        all_pairs = (combinations(x, 2))
        for pair in all_pairs:
            if pair[0] % pair[1] == 0:
                magic_sum += (pair[0] // pair[1])
                break
    return magic_sum


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
