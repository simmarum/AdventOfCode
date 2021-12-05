from itertools import chain


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    data = []
    for x in inp:
        one_line = x.replace('-', '').replace('>', ',').split(',')
        data_part = [int(xx.strip()) for xx in one_line]
        data.append(data_part)
    size = 1 + max(filter(lambda x: isinstance(
        x, (int)), chain.from_iterable(data)))
    board = [0] * (size*size)
    for one_geo in data:
        x1 = one_geo[0]
        y1 = one_geo[1]
        x2 = one_geo[2]
        y2 = one_geo[3]

        if (x1 == x2) and (y1 != y2):
            if y1 > y2:
                y1, y2 = y2, y1
            for tmp_y in range(y1, y2 + 1):
                board[x1*size+tmp_y] += 1
        elif (x1 != x2) and (y1 == y2):
            if x1 > x2:
                x1, x2 = x2, x1
            for tmp_x in range(x1, x2 + 1):
                board[tmp_x * size + y1] += 1

    return sum([1 for x in board if x >= 2])


def part_2(inp):
    data = []
    for x in inp:
        one_line = x.replace('-', '').replace('>', ',').split(',')
        data_part = [int(xx.strip()) for xx in one_line]
        data.append(data_part)
    size = 1 + max(filter(lambda x: isinstance(
        x, (int)), chain.from_iterable(data)))
    board = [0] * (size*size)
    for one_geo in data:
        x1 = one_geo[0]
        y1 = one_geo[1]
        x2 = one_geo[2]
        y2 = one_geo[3]

        if x1 <= x2:
            xs = list(range(x1, x2 + 1))
        else:
            xs = list(reversed(range(x2, x1 + 1)))

        if y1 <= y2:
            ys = list(range(y1, y2 + 1))
        else:
            ys = list(reversed(range(y2, y1 + 1)))

        if len(xs) == 1:
            xs = xs * len(ys)
        if len(ys) == 1:
            ys = ys * len(xs)

        for i in range(len(xs)):
            board[xs[i]*size+ys[i]] += 1

    return sum([1 for x in board if x >= 2])


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
