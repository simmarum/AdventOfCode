
def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [[int(c) for c in str(line.replace("\n", ""))]
                for line in f.readlines()]


def _get_pixel(inp, x, y, xx, yy):
    if (x < 0) or (x >= xx) or (y < 0) or (y >= yy):
        return None
    else:
        return inp[x][y]


def _get_neighbors(inp, x, y, xx, yy):
    return [
        _get_pixel(inp, x - 1, y + 0, xx, yy),
        _get_pixel(inp, x - 0, y - 1, xx, yy),
        _get_pixel(inp, x - 0, y + 1, xx, yy),
        _get_pixel(inp, x + 1, y + 0, xx, yy),
    ]


def part_1(inp):
    xx = len(inp)
    yy = len(inp[0])
    lowest_points = []
    for x in range(0, xx):
        for y in range(0, yy):
            n = _get_neighbors(inp, x, y, xx, yy)
            local_v = inp[x][y]
            lowest = all([True if (num is None) or (
                local_v < num) else False for num in n])
            if lowest:
                lowest_points.append(local_v)
    return sum(res + 1 for res in lowest_points)


def flood(inp, x, y, i):
    if inp[x][y] == 0:
        inp[x][y] = i
        if x > 0:
            flood(inp, x - 1, y, i)
        if x < len(inp) - 1:
            flood(inp, x + 1, y, i)
        if y > 0:
            flood(inp, x, y - 1, i)
        if y < len(inp[x]) - 1:
            flood(inp, x, y + 1, i)


def part_2(inp):
    xx = len(inp)
    yy = len(inp[0])
    basin_sizes = []
    for x in range(0, xx):
        for y in range(0, yy):
            if inp[x][y] < 9:
                inp[x][y] = 0
            else:
                inp[x][y] = -1
    for i in range(1, 1000):
        zero_point = None
        for x in range(0, xx):
            for y in range(0, yy):
                if inp[x][y] == 0:
                    zero_point = [x, y]
                    break
            if zero_point is not None:
                break
        if zero_point is not None:
            flood(inp, zero_point[0], zero_point[1], i)
        res = [int(item) for sublist in inp for item in sublist].count(i)
        if res == 0:
            break
        basin_sizes.append(res)

    basin_sizes = sorted(basin_sizes, reverse=True)[0:3]

    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
