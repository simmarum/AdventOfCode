def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    data = {int(line.split()[0].replace(':', '')): int(line.split()[1]) for line in inp}
    magic_sum = 0
    for k, v in data.items():
        if (k % ((v - 1) * 2)) == 0:
            magic_sum += k * v
    return magic_sum


def part_2(inp):
    data = {int(line.split()[0].replace(':', '')): int(line.split()[1]) for line in inp}
    for i in range(10_000_000):
        if not any([((k + i) % ((v - 1) * 2)) == 0 for k, v in data.items()]):
            return i
    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
