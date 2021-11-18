import itertools


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [int(line.replace("\n", "")) for line in f.readlines()]


def part_1(inp):
    inp = sorted(inp, reverse=True)
    all_combs_sum = 0
    for i in range(0, len(inp)):
        all_combs = [x for x in itertools.combinations(
            inp, i) if sum(x) == 150]
        all_combs_sum += len(all_combs)

    return all_combs_sum


def part_2(inp):
    inp = sorted(inp, reverse=True)
    for i in range(0, len(inp)):
        all_combs = [x for x in itertools.combinations(
            inp, i) if sum(x) == 150]
        if all_combs:
            break
    return len(all_combs)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
