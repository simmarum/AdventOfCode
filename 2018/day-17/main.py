def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def read_inp(inp):
    data = set()
    y_min, y_max = 1_000_000_000_000, 0
    for line in inp:
        s = sorted(line.split(', '))
        x = s[0].replace('x=', '')
        y = s[1].replace('y=', '')
        if '..' in x:
            x1, x2 = map(int, x.split('..'))
        else:
            x1, x2 = int(x), int(x)
        if '..' in y:
            y1, y2 = map(int, y.split('..'))
        else:
            y1, y2 = int(y), int(y)
        data.add((x1, x2, y1, y2))
        y_min = min(y_min, y1, y2)
        y_max = max(y_max, y1, y2)
    return data, y_min, y_max


def part_1(inp):
    data, y_min, y_max = read_inp(inp)
    print(data, y_min, y_max)
    return None


def part_2(inp):
    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
