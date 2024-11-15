from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def get_val(regs, k):
    try:
        return int(k)
    except ValueError:
        return regs[k]


def part_1(inp):
    mul_cnt = 0
    regs = defaultdict(int)
    idx = 0
    step = 0
    while idx < len(inp):
        step += 1
        if step > 100_000:
            return None
        line_spl = inp[idx].split()
        # print(line_spl, regs)
        if line_spl[0] == 'set':
            regs[line_spl[1]] = get_val(regs, line_spl[2])
            idx += 1
        elif line_spl[0] == 'sub':
            regs[line_spl[1]] -= get_val(regs, line_spl[2])
            idx += 1
        elif line_spl[0] == 'mul':
            regs[line_spl[1]] *= get_val(regs, line_spl[2])
            idx += 1
            mul_cnt += 1
        elif line_spl[0] == 'jnz':
            if get_val(regs, line_spl[1]) != 0:
                idx += get_val(regs, line_spl[2])
            else:
                idx += 1
    return mul_cnt


def part_2(inp):
    h = 0
    b = 99
    c = b
    b = b * 100
    b = b + 100000
    c = b + 17000

    while True:  # Line 32 jnz 1 -23
        f = 1
        d = 2
        # e = 2

        while True:  # Line 24
            if b % d == 0:
                f = 0
            d = d + 1
            if d != b:
                continue
            if f == 0:
                h = h + 1
            if b == c:
                return h
            b = b + 17
            break


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
