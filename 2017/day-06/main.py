from copy import deepcopy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    banks = list(map(int, inp[0].split()))
    # banks = [0, 2, 7, 0]
    step = 0
    all_redistribution = set(tuple(banks))
    banks_len = len(banks)

    while True:
        step += 1
        max_bank = max(banks)
        idx_max_bank = banks.index(max_bank)
        split_whole = max_bank // banks_len
        split_one = max_bank - (banks_len * split_whole)
        banks[idx_max_bank] = 0
        banks = [x + split_whole for x in banks]
        for i in range(1, split_one + 1):
            banks[(idx_max_bank + i) % banks_len] += 1
        if tuple(banks) in all_redistribution:
            return step
        else:
            all_redistribution.add(tuple(banks))

    return banks


def part_2(inp):
    banks = list(map(int, inp[0].split()))
    # banks = [0, 2, 7, 0]
    step = 0
    all_redistribution = {tuple(banks): 0}
    banks_len = len(banks)

    while True:
        step += 1
        max_bank = max(banks)
        idx_max_bank = banks.index(max_bank)
        split_whole = max_bank // banks_len
        split_one = max_bank - (banks_len * split_whole)
        banks[idx_max_bank] = 0
        banks = [x + split_whole for x in banks]
        for i in range(1, split_one + 1):
            banks[(idx_max_bank + i) % banks_len] += 1
        if tuple(banks) in all_redistribution:
            return step - all_redistribution[tuple(banks)]
        else:
            all_redistribution[tuple(banks)] = step

    return banks


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
