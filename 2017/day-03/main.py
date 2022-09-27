def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def find_x_y_in_spiral(step):
    layer = 1
    leg = 0
    x = 0
    y = 0
    if step > 1:
        for _ in range(2, step + 1):
            if leg == 0:
                x += 1
                if x == layer:
                    leg += 1
            elif leg == 1:
                y += 1
                if y == layer:
                    leg += 1
            elif leg == 2:
                x -= 1
                if -x == layer:
                    leg += 1
            elif leg == 3:
                y -= 1
                if -y == layer:
                    leg = 0
                    layer += 1
    return x, y


def part_1(inp):
    x, y = find_x_y_in_spiral(int(inp[0]))
    return abs(x) + abs(y)


def find_in_spiral_sum_lt(max_step, number):
    all_nums = {}
    layer = 1
    leg = 0
    x = 0
    y = 0
    all_nums[(0, 0)] = 1
    for _ in range(2, max_step + 1):
        if leg == 0:
            x += 1
            if x == layer:
                leg += 1
        elif leg == 1:
            y += 1
            if y == layer:
                leg += 1
        elif leg == 2:
            x -= 1
            if -x == layer:
                leg += 1
        elif leg == 3:
            y -= 1
            if -y == layer:
                leg = 0
                layer += 1
        ss = 0
        for dx, dy in [(1, 0), (1, 1), (0, 1), (-1, 1),
                       (-1, 0), (-1, -1), (0, -1), (1, -1)]:
            ss += all_nums.get((x + dx, y + dy), 0)
        all_nums[(x, y)] = ss
        if ss > number:
            return ss
    return None


def part_2(inp):
    return find_in_spiral_sum_lt(100, int(inp[0]))


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
