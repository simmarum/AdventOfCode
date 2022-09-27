from collections import defaultdict
import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def compute(inp, is_part_2):
    regs = defaultdict(int)
    _max_val = 0
    for line in inp:
        m = re.match("(\\w+) (\\w+) (-?\\w+) if (-?\\w+) (.+) (-?\\w+)", line)
        if m:
            reg_name, reg_op, reg_val, if_reg, if_op, if_val = m.groups()
            reg_val = int(reg_val)
            if_val = int(if_val)
            is_if = False
            if if_op == '>':
                if regs[if_reg] > if_val:
                    is_if = True
            if if_op == '<':
                if regs[if_reg] < if_val:
                    is_if = True
            if if_op == '>=':
                if regs[if_reg] >= if_val:
                    is_if = True
            if if_op == '<=':
                if regs[if_reg] <= if_val:
                    is_if = True
            if if_op == '==':
                if regs[if_reg] == if_val:
                    is_if = True
            if if_op == '!=':
                if regs[if_reg] != if_val:
                    is_if = True
            if is_if:
                if reg_op == 'inc':
                    regs[reg_name] += reg_val
                if reg_op == 'dec':
                    regs[reg_name] -= reg_val

        _max_val = max(_max_val, max(regs.values()))
    if is_part_2 is False:
        return max(regs.values())
    else:
        return _max_val


def part_1(inp):
    return compute(inp, is_part_2=False)


def part_2(inp):
    return compute(inp, is_part_2=True)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
