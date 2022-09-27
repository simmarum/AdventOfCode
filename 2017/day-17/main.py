def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    step = int(inp[0])
    # step = 3
    spinlock = [0]
    idx = 0
    for i in range(1, 1 + 2017):
        idx = ((idx + step) % i) + 1
        spinlock.insert(idx, i)
    return spinlock[idx + 1]


def part_2(inp):
    step = int(inp[0])
    idx = 0
    last_one = 0
    for i in range(1, 1 + 50_000_000):
        idx = ((idx + step) % i) + 1
        if idx == 1:
            last_one = i
    return last_one


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
