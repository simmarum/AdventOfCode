from copy import deepcopy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [int(line) for line in f.readlines()]


def part_1(inp):
    jumps = deepcopy(inp)
    step = 0
    instr = 0
    instr_len = len(jumps) - 1
    while True:
        step += 1
        new_instr = instr + jumps[instr]
        jumps[instr] += 1
        instr = new_instr
        if new_instr > instr_len:
            break
    return step


def part_2(inp):
    jumps = deepcopy(inp)
    step = 0
    instr = 0
    instr_len = len(jumps) - 1
    while True:
        step += 1
        new_instr = instr + jumps[instr]
        if jumps[instr] >= 3:
            jumps[instr] -= 1
        else:
            jumps[instr] += 1
        instr = new_instr
        if new_instr > instr_len:
            break
    return step


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
