# pip install bases.py
from bases import Bases
from collections import defaultdict
bases = Bases()


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line.replace("\n", "")) for line in f.readlines()]


def next_pass(p):
    new_p = bases.toBase26(bases.fromBase26(p)+1).rjust(8, 'a')
    op = None
    if "i" in new_p:
        op = "i"
        op_new = "j"
    if "l" in new_p:
        op = "l"
        op_new = "m"
    if "o" in new_p:
        op = "o"
        op_new = "p"

    if op != None:
        ii = new_p.index(op)
        new_p = (new_p[:ii] + op_new).ljust(8, 'a')

    return new_p


def part_1(inp):
    val = inp[0]

    while True:
        val = next_pass(val)
        check_1 = False
        for idx, c in enumerate(val[:-2]):
            c1 = c
            c2 = val[idx+1]
            c3 = val[idx+2]
            if (chr(ord(c) + 1) == c2) and (chr(ord(c2) + 1) == c3):
                check_1 = True
                break
        check_2 = False
        if ("i" not in val) and ("l" not in val) and ("l" not in val):
            check_2 = True
        check_3 = False
        check_3_cnt = 0
        val_len = len(val)
        idx = 0
        while True:
            if idx+1 >= val_len:
                break
            if val[idx] == val[idx+1]:
                check_3_cnt += 1
                idx += 2
            else:
                idx += 1
            if check_3_cnt >= 2:
                check_3 = True
                break
        if check_1 and check_2 and check_3:
            return val


def part_2(inp):
    return part_1(inp)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2([res_1])
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
