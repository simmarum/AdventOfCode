import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def decode(line):
    instr = None
    a = None
    b = None
    m = re.search('(rect) (\\d+)x(\\d+)', line)
    if m:
        instr = m.group(1)
        a = int(m.group(2))
        b = int(m.group(3))
    m = re.search('rotate (row) y=(\\d+) by (\\d+)', line)
    if m:
        instr = m.group(1)
        a = int(m.group(2))
        b = int(m.group(3))
    m = re.search('rotate (column) x=(\\d+) by (\\d+)', line)
    if m:
        instr = m.group(1)
        a = int(m.group(2))
        b = int(m.group(3))
    return instr, a, b


def create_display(x, y):
    return [[' ' for i in range(x)] for j in range(y)]


def print_display(d):
    print()
    for row in d:
        print(''.join(row))


def make_rect(d, a, b):
    for bi in range(b):
        for ai in range(a):
            d[bi][ai] = '#'
    return d


def shift_row(d, a, b):
    shift_map = list(range(len(d[0])))
    x = shift_map.pop()
    shift_map.insert(0, x)
    for _ in range(b):
        d = [[row[i] for i in shift_map] if ri ==
             a else row for ri, row in enumerate(d)]
    return d


def shift_column(d, a, b):
    d = [list(i) for i in zip(*d)]
    shift_map = list(range(len(d[0])))
    x = shift_map.pop()
    shift_map.insert(0, x)
    for _ in range(b):
        d = [[row[i] for i in shift_map] if ri ==
             a else row for ri, row in enumerate(d)]
    d = [list(i) for i in zip(*d)]
    return d


def cnt_lit(d):
    d_str = ''.join([''.join(row) for row in d])
    return d_str.count('#')


def part_1(inp):
    display = create_display(50, 6)
    for line in inp:
        instr, a, b = decode(line)
        if instr == 'rect':
            display = make_rect(display, a, b)
        if instr == 'row':
            display = shift_row(display, a, b)
        if instr == 'column':
            display = shift_column(display, a, b)

    return cnt_lit(display)


def part_2(inp):
    display = create_display(50, 6)
    for line in inp:
        instr, a, b = decode(line)
        if instr == 'rect':
            display = make_rect(display, a, b)
        if instr == 'row':
            display = shift_row(display, a, b)
        if instr == 'column':
            display = shift_column(display, a, b)
    print_display(display)
    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
