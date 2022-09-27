def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    valids = 0
    for line in inp:
        x = line.split()
        if len(x) == len(set(x)):
            valids += 1
    return valids


def part_2(inp):
    valids = 0
    for line in inp:
        x = line.split()
        x = [''.join(sorted(c)) for c in x]
        if len(x) == len(set(x)):
            valids += 1
    return valids


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
