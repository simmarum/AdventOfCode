def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def run_program(a, b, inp):
    registers = {
        'a': a,
        'b': b,
    }
    instr_line = 0
    step = 0
    while instr_line < len(inp):
        step += 1
        instr_split = inp[instr_line].split(' ')
        instr_name = instr_split[0] if 0 < len(instr_split) else None
        instr_reg = instr_split[1].replace(
            ',', '') if 1 < len(instr_split) else None
        instr_off = int(instr_split[2]) if 2 < len(instr_split) else None

        if instr_name == 'hlf':
            registers[instr_reg] = registers[instr_reg] // 2
            instr_line += 1
        elif instr_name == 'tpl':
            registers[instr_reg] = registers[instr_reg] * 3
            instr_line += 1
        elif instr_name == 'inc':
            registers[instr_reg] = registers[instr_reg] + 1
            instr_line += 1
        elif instr_name == 'jmp':
            instr_line += int(instr_reg)
        elif instr_name == 'jie':
            if registers[instr_reg] % 2 == 0:
                instr_line += instr_off
            else:
                instr_line += 1
        elif instr_name == 'jio':
            if registers[instr_reg] == 1:
                instr_line += instr_off
            else:
                instr_line += 1
        else:
            raise RuntimeError(f"Wrong instruction '{instr_split}'!")
    return registers


def part_1(inp):
    registers = run_program(0, 0, inp)
    return registers['b']


def part_2(inp):
    registers = run_program(1, 0, inp)
    return registers['b']


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
