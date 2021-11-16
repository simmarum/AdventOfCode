import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line.replace("\n", "")) for line in f.readlines()]


def part_1(inp):
    sum_all = 0
    sum_char = 0
    p = re.compile(r"\\x([0-9a-zA-Z]){2}")
    for val in inp:
        sum_all += len(val)
        val = val[1:-1].replace(r"\\", r"?").replace(
            r"\"", r"?").replace(" ", "")
        val = re.sub(p, "?", val)
        sum_char += len(val)
    return sum_all - sum_char


def part_2(inp):
    sum_all = 0
    sum_enc = 0
    for val in inp:
        sum_all += len(val)
        val = ''.join([c.replace("\\", "\\\\").replace(r'"', r'\"')
                       for c in val])
        val = f'"{val}"'
        sum_enc += len(val)
    return sum_enc - sum_all


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
