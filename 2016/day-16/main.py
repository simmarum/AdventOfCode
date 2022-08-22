import more_itertools


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def disk_overwrite(start, size):
    while len(start) < size:
        b = start[::-1]
        b = b.translate(str.maketrans({'0': '1', '1': '0'}))
        start = start + '0' + b
    return start[:size]


def calc_checksum(str_over):
    checksum = str_over
    while len(checksum) % 2 == 0:
        checksum = ''.join(
            ['1' if x[0] == x[1] else '0' for x in more_itertools.chunked(checksum, 2)])
    return checksum


def part_1(inp):
    start = inp[0]
    str_over = disk_overwrite(start, 272)
    return calc_checksum(str_over)


def part_2(inp):
    start = inp[0]
    str_over = disk_overwrite(start, 35651584)
    return calc_checksum(str_over)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
