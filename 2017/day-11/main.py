def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def axial_distance(ax, ay, bx, by):
    return int((abs(ay - by)
                + abs(ay + ax - by - bx)
                + abs(ax - bx)) // 2)


def find_dinstance_on_grid(ax, ay, bx, by):
    return axial_distance(ax, ay, bx, by)


def walk_on_grid(inp, is_part_2):
    #   \ n  /     #     \ 0,-1 /
    # nw +--+ ne   # -1,0 +----+ 1,-1
    #   /    \     #     /      \
    # -+      +-   #  --+  0,0   +--
    #   \    /     #     \      /
    # sw +--+ se   # -1,1 +----+ 1,0
    #   / s  \     #     / 0,1  \
    direction_lookup = {
        'nw': (-1, 0),
        'n': (0, -1),
        'ne': (1, -1),
        'se': (1, 0),
        's': (0, 1),
        'sw': (-1, 1),
    }
    _max_dist = 0
    for line in inp:
        sx, sy = 0, 0
        x, y = 0, 0
        for direction in line.split(','):
            x, y = x + direction_lookup[direction][0], y + \
                direction_lookup[direction][1]
            dist = find_dinstance_on_grid(sx, sy, x, y)
            _max_dist = max(_max_dist, dist)
    if is_part_2 is False:
        return dist
    else:
        return _max_dist


def part_1(inp):
    return walk_on_grid(inp, False)


def part_2(inp):
    return walk_on_grid(inp, True)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
