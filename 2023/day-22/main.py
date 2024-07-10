from collections import defaultdict
from copy import deepcopy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.readlines()]


def get_bricks(inp):
    bricks = []
    for line in inp:
        if not line:
            continue
        a, b = line.split("~")
        a = list(map(int, a.split(",")))
        b = list(map(int, b.split(",")))
        a, b = min(a, b), max(a, b)
        bricks.append([a, b])
    return list(sorted(bricks, key=lambda x: (x[0][2], x[0][1], x[0][0])))


def fall_down(bricks):
    min_z_per_xy = defaultdict(int)
    for i in range(len(bricks)):
        b = bricks[i]
        max_z_ava = 0
        for x in range(b[0][0], b[1][0] + 1):
            for y in range(b[0][1], b[1][1] + 1):
                max_z_ava = max(max_z_ava, min_z_per_xy[(x, y)])
        b_h = bricks[i][1][2] - bricks[i][0][2]
        bricks[i][0][2] = max_z_ava + 1
        bricks[i][1][2] = bricks[i][0][2] + b_h
        for x in range(b[0][0], b[1][0] + 1):
            for y in range(b[0][1], b[1][1] + 1):
                min_z_per_xy[(x, y)] = bricks[i][1][2]

    bricks_fill = {}
    for i, b in enumerate(bricks):
        for x in range(b[0][0], b[1][0] + 1):
            for y in range(b[0][1], b[1][1] + 1):
                for z in range(b[0][2], b[1][2] + 1):
                    bricks_fill[(x, y, z)] = i
    bricks_ud = {}
    for i, b in enumerate(bricks):
        b_u = set()
        b_d = set()
        for x in range(b[0][0], b[1][0] + 1):
            for y in range(b[0][1], b[1][1] + 1):
                tmp = bricks_fill.get((x, y, b[1][2] + 1), None)
                if tmp is not None:
                    b_u.add(tmp)
                tmp = bricks_fill.get((x, y, b[0][2] - 1), None)
                if tmp is not None:
                    b_d.add(tmp)
        bricks_ud[i] = {
            'u': b_u,
            'd': b_d
        }
    can_be_removed = 0
    for b, v in bricks_ud.items():
        if len(v['u']) == 0:
            can_be_removed += 1
        elif len(v['u']) >= 1:
            if all([(len(bricks_ud[up_b]['d']) > 1) for up_b in list(v['u'])]):
                can_be_removed += 1
    return can_be_removed


def fall_down_with_skip(bricks):
    min_z_per_xy = defaultdict(int)
    for i in range(len(bricks)):
        b = bricks[i]
        max_z_ava = 0
        for x in range(b[0][0], b[1][0] + 1):
            for y in range(b[0][1], b[1][1] + 1):
                max_z_ava = max(max_z_ava, min_z_per_xy[(x, y)])
        b_h = bricks[i][1][2] - bricks[i][0][2]
        bricks[i][0][2] = max_z_ava + 1
        bricks[i][1][2] = bricks[i][0][2] + b_h
        for x in range(b[0][0], b[1][0] + 1):
            for y in range(b[0][1], b[1][1] + 1):
                min_z_per_xy[(x, y)] = bricks[i][1][2]

    falls_sum = 0
    for bi in range(len(bricks)):
        bricks_skip = deepcopy(bricks)
        del (bricks_skip[bi])
        min_z_per_xy = defaultdict(int)
        falls = 0
        for i in range(len(bricks_skip)):
            b = bricks_skip[i]
            max_z_ava = 0
            for x in range(b[0][0], b[1][0] + 1):
                for y in range(b[0][1], b[1][1] + 1):
                    max_z_ava = max(max_z_ava, min_z_per_xy[(x, y)])
            b_h = bricks_skip[i][1][2] - bricks_skip[i][0][2]
            if bricks_skip[i][0][2] > max_z_ava + 1:
                falls += 1
            bricks_skip[i][0][2] = max_z_ava + 1
            bricks_skip[i][1][2] = bricks_skip[i][0][2] + b_h
            for x in range(b[0][0], b[1][0] + 1):
                for y in range(b[0][1], b[1][1] + 1):
                    min_z_per_xy[(x, y)] = bricks_skip[i][1][2]
        falls_sum += falls

    return falls_sum


def part_1(inp):
    bricks = get_bricks(inp)
    return fall_down(bricks)


def part_2(inp):
    bricks = get_bricks(inp)
    return fall_down_with_skip(bricks)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
