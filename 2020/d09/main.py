from itertools import combinations


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [int(line) for line in f.read().splitlines()]


def part_1(inp):
    pre_n = 25
    inp_len = len(inp)
    for i in range(pre_n, inp_len):
        if inp[i] not in [sum(x) for x in combinations(inp[i-pre_n:i], 2)]:
            return inp[i]
    return None


def part_2(inp, prev_num):
    i, j = 0, 0
    while True:
        t_s = sum(inp[i:j])
        if t_s == prev_num:
            return min(inp[i:j]) + max(inp[i:j])
        elif t_s < prev_num:
            j += 1
        else:
            i += 1
    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp, res_1)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
