import re
from copy import deepcopy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [line for line in f.read().splitlines()]


def _print(m, p=True):
    if p:
        print(m)


map_size = 200
map_guide = {
    'e': (0, 1),
    'se': (1, 0),
    'sw': (1, -1),
    'w': (0, -1),
    'nw': (-1, 0),
    'ne': (-1, 1)
}


def part_1(inp):
    p = re.compile(r"(e|se|sw|w|nw|ne)")
    cc = map_size//2
    hex_map = [[False]*map_size for _ in range(map_size)]
    for val in inp:
        directions = re.findall(p, val)
        sx = cc
        sy = cc
        for one_dir in directions:
            tmp_move = map_guide[one_dir]
            sx += tmp_move[0]
            sy += tmp_move[1]
        hex_map[sx][sy] = not hex_map[sx][sy]
    res = sum([row.count(True) for row in hex_map])
    return res, hex_map


def _flip_floor(hex_map):
    new_hex_map = deepcopy(hex_map)
    for ix, x in enumerate(hex_map):
        for iy, y in enumerate(x):
            trues = 0
            for one_dir in map_guide.values():
                tx = min(max(0, ix+one_dir[0]), map_size-1)
                ty = min(max(0, iy+one_dir[1]), map_size-1)
                tmp_tile = hex_map[tx][ty]
                if tmp_tile:
                    trues += 1
            if (y) and ((trues == 0) or (trues > 2)):
                new_hex_map[ix][iy] = False
            elif (not y) and (trues == 2):
                new_hex_map[ix][iy] = True
    return new_hex_map


def part_2(inp, hex_map):
    flip_hex_map = deepcopy(hex_map)
    for day in range(1, 1+100):
        flip_hex_map = _flip_floor(flip_hex_map)
        res = sum([row.count(True) for row in flip_hex_map])
        _print(f"\tDay {day}: {res}")
    return res


def main():
    inp = read_file()
    res_1, hex_map = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp, hex_map)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
