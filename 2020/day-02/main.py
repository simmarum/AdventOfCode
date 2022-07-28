def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def prepare_input(one_line):
    x = one_line.replace("\n", "").split(" ")
    c_min, c_max = x[0].split("-")
    c_char = x[1][:-1]
    c_pass = x[2]
    return int(c_min), int(c_max), c_char, c_pass


def part_1(inp):
    valid_cnt = 0
    for val in inp:
        c_min, c_max, c_char, c_pass = prepare_input(val)
        c_cnt = c_pass.count(c_char)
        if ((c_min <= c_cnt) and (c_cnt <= c_max)):
            valid_cnt += 1

    return valid_cnt


def part_2(inp):
    valid_cnt = 0
    for val in inp:
        c_min, c_max, c_char, c_pass = prepare_input(val)
        if ((c_pass[c_min - 1] == c_char) != (c_pass[c_max - 1] == c_char)):
            valid_cnt += 1

    return valid_cnt


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
