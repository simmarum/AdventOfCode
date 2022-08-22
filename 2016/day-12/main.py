def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def simulate(registers, inp):
    i = 0
    step = 0
    while i < len(inp):
        step += 1
        if step == 100_000_000:
            return None
        instr = inp[i]
        if 'cpy' in instr:
            _, f, t = instr.split()
            if f not in 'abcd':
                registers[t] = int(f)
            else:
                registers[t] = registers[f]
            i += 1
        if 'inc' in instr:
            _, r = instr.split()
            registers[r] = registers[r] + 1
            i += 1
        if 'dec' in instr:
            _, r = instr.split()
            registers[r] = registers[r] - 1
            i += 1
        if 'jnz' in instr:
            _, r, s = instr.split()
            tmp_val = None
            if r not in 'abcd':
                tmp_val = int(r)
            else:
                tmp_val = registers[r]
            if tmp_val != 0:
                i = i + int(s)
            else:
                i += 1
    return registers['a']


def part_1(inp):
    registers = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
    }
    return simulate(registers, inp)


def part_2(inp):
    registers = {
        'a': 0,
        'b': 0,
        'c': 1,
        'd': 0,
    }
    return simulate(registers, inp)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
