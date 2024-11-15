from copy import copy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def run_Intcode(intcode):
    ip = 0
    while True:
        oppcode, a, b, c = intcode[ip:ip + 4]
        if oppcode == 1:
            intcode[c] = intcode[a] + intcode[b]
        elif oppcode == 2:
            intcode[c] = intcode[a] * intcode[b]
        elif oppcode == 99:
            break
        else:
            # raise RuntimeError(f"Found new {oppcode=}")
            return None
        ip += 4
    return intcode[0]


def part_1(inp):
    source_code = list(map(int, inp[0].split(','))) + [0, 0, 0]
    source_code[1] = 12
    source_code[2] = 2
    return run_Intcode(source_code)


def part_2(inp):
    source_code = list(map(int, inp[0].split(','))) + [0, 0, 0]
    for noun in range(0, 100):
        for verb in range(0, 100):
            source_code_copy = copy(source_code)
            source_code_copy[1] = noun
            source_code_copy[2] = verb
            if run_Intcode(source_code_copy) == 19690720:
                return 100 * noun + verb
    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
