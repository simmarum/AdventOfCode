def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def create_tiles(start, num):
    for _ in range(num - 1):
        s = '.' + start[-1] + '.'
        start.append(''.join(['^' if s[i - 1:i + 2] in ['^..', '^^.',
                     '.^^', '..^'] else '.' for i in range(1, len(s) - 1)]))
    return start


def part_1(inp):
    start = inp[0]
    # start = '.^^.^.^^^^'
    num = 40
    start = create_tiles([start], num)
    one_row_start = ''.join(start)
    return one_row_start.count('.')


def part_2(inp):
    start = inp[0]
    num = 400_000
    start = create_tiles([start], num)
    one_row_start = ''.join(start)
    return one_row_start.count('.')


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
