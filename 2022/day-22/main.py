import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def parse_inp(inp):
    tiles = {}
    instructions = []
    for y, line in enumerate(inp):
        if not line:
            continue
        if line[0].isdigit():
            instructions = re.split(r'(L|R)', line)
        for x, v in enumerate(line):
            if v != ' ':
                tiles[(y, x)] = v
    return tiles, instructions


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


def add_pos(a, b):
    return tuple(sum(x) for x in zip(a, b))


def print_tiles(tiles, path):
    l = {
        (0, 1): '>',
        (0, -1): '<',
        (1, 0): 'v',
        (-1, 0): '^',
    }
    tt = [[' ']*(1+max([t[1] for t in tiles.keys()]))
          for _ in range(1+max([t[0] for t in tiles.keys()]))]
    for k, v in tiles.items():
        tt[k[0]][k[1]] = v
    for k, v in path:
        tt[k[0]][k[1]] = l[v]
    [print(''.join(t)) for t in tt]


def part_1(inp):
    tiles, instructions = parse_inp(inp)
    if len(instructions) % 2 == 1:
        instructions.append(None)
    curr_pos = min([t for t in tiles if t[0] == 0])
    curr_dir = (0, 1)
    path = [(curr_pos, curr_dir)]
    it = iter(instructions)
    for cnt, next_dir in zip(it, it):
        for step in range(int(cnt)):
            next_pos = add_pos(curr_pos, curr_dir)
            if next_pos not in tiles:
                if curr_dir == (0, 1):
                    next_pos = min(
                        [t for t in tiles if t[0] == curr_pos[0]])
                if curr_dir == (0, -1):
                    next_pos = max(
                        [t for t in tiles if t[0] == curr_pos[0]])
                if curr_dir == (1, 0):
                    next_pos = min(
                        [t for t in tiles if t[1] == curr_pos[1]])
                if curr_dir == (-1, 0):
                    next_pos = max(
                        [t for t in tiles if t[1] == curr_pos[1]])
            if tiles[next_pos] == '#':
                if next_dir:
                    curr_dir = lookup[curr_dir][next_dir]
                else:
                    path.append((curr_pos, curr_dir))

                break
            else:
                path.append((curr_pos, curr_dir))
                curr_pos = next_pos
        else:
            if next_dir:
                curr_dir = lookup[curr_dir][next_dir]
            else:
                path.append((curr_pos, curr_dir))

    # print_tiles(tiles, path)
    col = curr_pos[1] + 1
    row = curr_pos[0] + 1
    facing_l = {
        (0, 1): 0,
        (0, -1): 2,
        (1, 0): 1,
        (-1, 0): 3,
    }
    facing = facing_l[curr_dir]
    return 1000*row + 4*col + facing


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
