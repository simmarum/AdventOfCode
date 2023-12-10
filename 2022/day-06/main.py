def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    line = inp[0]
    for i in range(4, len(line)):
        if len(set(line[i - 4:i])) == 4:
            return i


def part_2(inp):
    line = inp[0]
    for i in range(14, len(line)):
        if len(set(line[i - 14:i])) == 14:
            return i


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
