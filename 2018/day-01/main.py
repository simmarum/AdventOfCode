def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [int(line) for line in f.readlines()]


def part_1(inp):
    return sum(inp)


def part_2(inp):
    cur_freq = 0
    saw_freq = set([cur_freq])
    i = 0
    len_inp = len(inp)
    while True:
        cur_freq += inp[i % len_inp]
        i += 1
        if cur_freq in saw_freq:
            return cur_freq
        else:
            saw_freq.add(cur_freq)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
