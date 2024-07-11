import re
import numpy as np


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def parse_inp(inp):
    instructions = []
    world = []
    start_tile = None
    for y, line in enumerate(inp):
        world_line = []
        if not line:
            continue
        if line[0].isdigit():
            instructions = re.split(r'(L|R)', line)
            continue
        for x, v in enumerate(line):
            if v != ' ':
                if start_tile is None:
                    start_tile = (y, x)
            world_line.append(v)
        world.append(world_line)
    max_line_len = max(len(line) for line in world)
    world = [line + [' '] * (max_line_len - len(line)) for line in world]
    tiles = np.array(world)
    return tiles, instructions, start_tile


dirs = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}
lookup = {
    # R
    (0, 1): {
        'R': (1, 0),
        'L': (-1, 0)
    },
    # L
    (0, -1): {
        'R': (-1, 0),
        'L': (1, 0)
    },
    # U
    (-1, 0): {
        'R': (0, 1),
        'L': (0, -1)
    },
    # D
    (1, 0): {
        'R': (0, -1),
        'L': (0, 1)
    },
}


def get_portal_type_1(dx):
    # Used in example on site
    p = {}
    # 14 portals out of the map
    #     1
    # 2 3 4
    #     5 6
    for di in range(dx):
        # 3->1 U->R (1->3 L->D)
        ay, ax = 1 * dx + 0 * di + 0, 1 * dx + 1 * di + 0
        by, bx = 0 * dx + 1 * di + 0, 2 * dx + 0 * di + 0
        p[((ay, ax), dirs['U'])] = ((by, bx), dirs['R'])
        p[((by, bx), dirs['L'])] = ((ay, ax), dirs['D'])
        # 1->2 U->D (2->1 U->D)
        ay, ax = 0 * dx + 0 * di + 0, 2 * dx + 1 * di + 0
        by, bx = 1 * dx + 0 * di + 0, 1 * dx - 1 * di - 1
        p[((ay, ax), dirs['U'])] = ((by, bx), dirs['D'])
        p[((by, bx), dirs['U'])] = ((ay, ax), dirs['D'])
        # 1->6 R->L (6->1 R->L)
        ay, ax = 1 * dx - 1 * di - 1, 3 * dx + 0 * di - 1
        by, bx = 2 * dx + 1 * di + 0, 4 * dx + 0 * di - 1
        p[((ay, ax), dirs['R'])] = ((by, bx), dirs['L'])
        p[((by, bx), dirs['R'])] = ((ay, ax), dirs['L'])
        # 4->6 R->D (6->4 U->L)
        ay, ax = 2 * dx - 1 * di - 1, 3 * dx + 0 * di - 1
        by, bx = 2 * dx + 0 * di + 0, 3 * dx + 1 * di + 0
        p[((ay, ax), dirs['R'])] = ((by, bx), dirs['D'])
        p[((by, bx), dirs['U'])] = ((ay, ax), dirs['L'])
        # 3->5 D->R (5->3 L->U)
        ay, ax = 2 * dx + 0 * di - 1, 2 * dx - 1 * di - 1
        by, bx = 2 * dx + 1 * di + 0, 2 * dx + 0 * di + 0
        p[((ay, ax), dirs['D'])] = ((by, bx), dirs['R'])
        p[((by, bx), dirs['L'])] = ((ay, ax), dirs['U'])
        # 2->5 D->U (5->2 D->U)
        ay, ax = 2 * dx + 0 * di - 1, 1 * dx - 1 * di - 1
        by, bx = 3 * dx + 0 * di - 1, 2 * dx + 1 * di + 0
        p[((ay, ax), dirs['D'])] = ((by, bx), dirs['U'])
        p[((by, bx), dirs['D'])] = ((ay, ax), dirs['U'])
        # 2->6 L->U (6->2 D->R)
        ay, ax = 1 * dx + 1 * di + 0, 0 * dx + 0 * di + 0
        by, bx = 3 * dx + 0 * di - 1, 4 * dx - 1 * di - 1
        p[((ay, ax), dirs['L'])] = ((by, bx), dirs['U'])
        p[((by, bx), dirs['D'])] = ((ay, ax), dirs['R'])
    return p


def get_portal_type_2(dx):
    # Used in my input
    p = {}
    # 14 portals out of the map
    #   1 2
    #   3
    # 4 5
    # 6
    for di in range(dx):
        # 3->4 L->D (4->3 U->R)
        ay, ax = 1 * dx + 1 * di + 0, 1 * dx + 0 * di + 0
        by, bx = 2 * dx + 0 * di + 0, 0 * dx + 1 * di + 0
        p[((ay, ax), dirs['L'])] = ((by, bx), dirs['D'])
        p[((by, bx), dirs['U'])] = ((ay, ax), dirs['R'])
        # 1->4 L->R (4->1 L->R)
        ay, ax = 0 * dx + 1 * di + 0, 1 * dx + 0 * di + 0
        by, bx = 3 * dx - 1 * di - 1, 0 * dx + 0 * di + 0
        p[((ay, ax), dirs['L'])] = ((by, bx), dirs['R'])
        p[((by, bx), dirs['L'])] = ((ay, ax), dirs['R'])
        # 1->6 U->R (6->1 L->D)
        ay, ax = 0 * dx + 0 * di + 0, 1 * dx + 1 * di + 0
        by, bx = 3 * dx + 1 * di + 0, 0 * dx + 0 * di + 0
        p[((ay, ax), dirs['U'])] = ((by, bx), dirs['R'])
        p[((by, bx), dirs['L'])] = ((ay, ax), dirs['D'])
        # 6->2 D->D (2->6 U->U)
        ay, ax = 4 * dx + 0 * di - 1, 0 * dx + 1 * di + 0
        by, bx = 0 * dx + 0 * di + 0, 2 * dx + 1 * di + 0
        p[((ay, ax), dirs['D'])] = ((by, bx), dirs['D'])
        p[((by, bx), dirs['U'])] = ((ay, ax), dirs['U'])
        # 6->5 R->U (5->6 D->L)
        ay, ax = 3 * dx + 1 * di + 0, 1 * dx + 0 * di - 1
        by, bx = 3 * dx + 0 * di - 1, 1 * dx + 1 * di + 0
        p[((ay, ax), dirs['R'])] = ((by, bx), dirs['U'])
        p[((by, bx), dirs['D'])] = ((ay, ax), dirs['L'])
        # 2->5 R->L (5->2 R->L)
        ay, ax = 0 * dx + 1 * di + 0, 3 * dx + 0 * di - 1
        by, bx = 3 * dx - 1 * di - 1, 2 * dx + 0 * di - 1
        p[((ay, ax), dirs['R'])] = ((by, bx), dirs['L'])
        p[((by, bx), dirs['R'])] = ((ay, ax), dirs['L'])
        # 2->3 D->L (3->2 R->U)
        ay, ax = 1 * dx + 0 * di - 1, 2 * dx + 1 * di + 0
        by, bx = 1 * dx + 1 * di + 0, 2 * dx + 0 * di - 1
        p[((ay, ax), dirs['D'])] = ((by, bx), dirs['L'])
        p[((by, bx), dirs['R'])] = ((ay, ax), dirs['U'])
    return p


def travel_map(inp, part):
    tiles, instructions, start_tile = parse_inp(inp)
    if start_tile is None:
        raise RuntimeError(f"{start_tile=} cannot be None")
    curr_pos = start_tile
    curr_dir = (0, 1)
    max_y = tiles.shape[0]
    max_x = tiles.shape[1]
    p = {}
    dx = None
    if part == 2:
        for (wy, wx) in ((3, 4), (4, 3)):
            dy = max_y // wy
            dx = max_x // wx
            if dy == dx:
                break
        else:
            raise RuntimeError(
                f"Something wrong with dimensions: {
                    max_y=} {
                    max_x=}")
        p = get_portal_type_2(dx)

    prev_dir = None
    for instr in instructions:
        if instr in 'LR':
            curr_dir = lookup[curr_dir][instr]
        else:
            for step in range(int(instr)):
                prev_dir = None
                next_pos, next_dir = p.get((curr_pos, curr_dir), (None, None))
                # print(f"{instr=} {curr_pos=} {
                #       curr_dir=} {next_pos=} {next_dir=}")
                if next_pos is None:
                    next_pos, next_dir = (
                        (
                            (curr_pos[0] + curr_dir[0] + max_y) % max_y,
                            (curr_pos[1] + curr_dir[1] + max_x) % max_x
                        ),
                        curr_dir
                    )
                else:
                    prev_dir = curr_dir
                if tiles[next_pos] == ' ':
                    while tiles[next_pos] == ' ':
                        next_pos, next_dir = (
                            (
                                (next_pos[0] + next_dir[0] + max_y) % max_y,
                                (next_pos[1] + next_dir[1] + max_x) % max_x
                            ),
                            next_dir
                        )
                if tiles[next_pos] == '.':
                    curr_pos = next_pos
                    curr_dir = next_dir
                    continue
                if tiles[next_pos] == '#':
                    # curr_dir = next_dir
                    break

    col = curr_pos[1] + 1
    row = curr_pos[0] + 1
    curr_dir_points = {
        (0, 1): 0,
        (0, -1): 2,
        (1, 0): 1,
        (-1, 0): 3,
    }
    final_dir = curr_dir
    if prev_dir:
        final_dir = prev_dir
    return 1000 * row + 4 * col + curr_dir_points[final_dir]


def part_1(inp):
    return travel_map(inp, part=1)


def part_2(inp):
    return travel_map(inp, part=2)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
