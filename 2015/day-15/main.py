import math


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.readlines()]


def part_1(inp):
    ings = []
    for one_line in inp:
        split_line = one_line.split(" ")
        ings.append([
            int(split_line[2][:-1]),
            int(split_line[4][:-1]),
            int(split_line[6][:-1]),
            int(split_line[8][:-1])
        ])
    ings_inv = list(map(list, zip(*ings)))
    max_sum = 100
    all_combs = []
    for a in range(0, max_sum + 1):
        for b in range(0, max_sum + 1 - a):
            for c in range(0, max_sum + 1 - a - b):
                for d in range(0, max_sum + 1 - a - b - c):
                    if a + b + c + d == max_sum:
                        all_combs.append((a, b, c, d))
    res = max([math.prod([max(0, sum([a * b for a, b in zip(one_comb, one_ing_inv)]))
                          for one_ing_inv in ings_inv]) for one_comb in all_combs])
    return res


def part_2(inp):
    ings = []
    for one_line in inp:
        split_line = one_line.split(" ")
        ings.append([
            int(split_line[2][:-1]),
            int(split_line[4][:-1]),
            int(split_line[6][:-1]),
            int(split_line[8][:-1]),
            int(split_line[10])
        ])
    ings_inv = list(map(list, zip(*ings)))
    max_cal = 500
    max_sum = 100
    all_combs = []
    for a in range(0, max_sum + 1):
        for b in range(0, max_sum + 1 - a):
            for c in range(0, max_sum + 1 - a - b):
                for d in range(0, max_sum + 1 - a - b - c):
                    if a + b + c + d == max_sum:
                        all_combs.append((a, b, c, d))
    res = max([math.prod([max(0, sum([a * b for a, b in zip(one_comb, one_ing_inv)]))
                          for one_ing_inv in ings_inv[:-1]]) for one_comb in all_combs
               if sum([a * b for a, b in zip(one_comb, ings_inv[-1])]) == max_cal])
    return res


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
