import math
import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def cheesy(registers, inp):
    magic_x = None
    magic_y = None
    for instr in inp[::-1]:
        m = re.match('jnz (\\d+) d', instr)
        if m:
            magic_y = int(m.group(1))
        m = re.match('cpy (\\d+) c', instr)
        if m:
            magic_x = int(m.group(1))
            break
    return math.factorial(registers['a']) + (magic_x * magic_y)


def part_1(inp):
    registers = {
        'a': 7,
        'b': 0,
        'c': 0,
        'd': 0,
    }
    return cheesy(registers, inp)


def part_2(inp):
    registers = {
        'a': 12,
        'b': 0,
        'c': 0,
        'd': 0,
    }
    return cheesy(registers, inp)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
