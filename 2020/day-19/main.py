import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [line for line in f.read().split("\n\n")]


def _prepare_in(inp):
    dd = {}
    for val in inp.splitlines():
        x = val.split(":")
        dd[int(x[0])] = x[1].strip().replace('"', '')
    return dd


def _resolve_d(dd):
    main_rule = dd[0]
    is_update = True
    while is_update:
        is_update = False
        mr = main_rule.split(" ")
        for i in range(len(mr)):
            if mr[i].isdigit():
                mr[i] = f"( {dd[int(mr[i])]} )"
                is_update = True
        main_rule = ' '.join(mr)

    return f"^({''.join(mr)})$"


def _check_entries(vals, pat):
    ss = 0
    for val in vals.splitlines():
        if re.match(pat, val):
            ss += 1
    return ss


def part_1(inp):
    dd = _prepare_in(inp[0])
    mr = _resolve_d(dd)
    ss = _check_entries(inp[1], mr)
    return ss


def part_2(inp):
    dd = _prepare_in(inp[0])
    # Update phase
    dd[8] = '42 | 42 8'
    # Change to regex way
    dd[8] = '42 +'

    dd[11] = '42 31 | 42 11 31'
    # Hack way - just expand few times that it can handle input data ; )
    for _ in range(2):
        dd[11] = dd[11].replace("11", f"( {dd[11]} )")
    dd[11] = dd[11].replace("11 ", "")
    mr = _resolve_d(dd)
    ss = _check_entries(inp[1], mr)
    return ss


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
