import numpy as np
np.set_printoptions(linewidth=200)


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def send_sand(sand_source, space, max_x, max_y):
    if sand_source[1] > max_y:
        print(sand_source)
        return False
    for dir in [(0, 1), (-1, 1), (1, 1)]:
        new_pos = (sand_source[0]+dir[0], sand_source[1]+dir[1])
        if space[new_pos[1], new_pos[0]] == '.':
            return send_sand(new_pos, space, max_x, max_y)
    else:
        if space[sand_source[1], sand_source[0]] == '+':
            return False
        space[sand_source[1], sand_source[0]] = 'o'
        return True
    return None


def part_1(inp):
    data = [[tuple(map(int, p.split(',')))
             for p in line.split('->')] for line in inp]
    walls = set()
    for wall in data:
        for p1, p2 in zip(wall, wall[1:]):
            if p1[0] == p2[0]:
                x = p1[0]
                for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
                    walls.add((x, y))
            if p1[1] == p2[1]:
                y = p1[1]
                for x in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
                    walls.add((x, y))
    max_x = max([p[0] for p in walls])
    max_y = max([p[1] for p in walls])
    margin = 5

    space = np.full(shape=(max_y+margin, max_x+margin), fill_value='.')
    for pw in walls:
        space[pw[1], pw[0]] = '#'

    sand_source = (500, 0)
    space[sand_source[1], sand_source[0]] = '+'

    for i in range(1000):
        sand_placed = send_sand(sand_source, space, max_x, max_y)
        if sand_placed is False:
            break
    return i


def part_2(inp):
    data = [[tuple(map(int, p.split(',')))
             for p in line.split('->')] for line in inp]
    walls = set()
    for wall in data:
        for p1, p2 in zip(wall, wall[1:]):
            if p1[0] == p2[0]:
                x = p1[0]
                for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
                    walls.add((x, y))
            if p1[1] == p2[1]:
                y = p1[1]
                for x in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
                    walls.add((x, y))
    max_x = max([p[0] for p in walls])
    max_y = max([p[1] for p in walls])
    margin = 1000
    infinite_floor_margin = 2
    for x in range(0, max_x+margin):
        walls.add((x, max_y+infinite_floor_margin))
    max_y = max([p[1] for p in walls])

    space = np.full(shape=(max_y+margin, max_x+margin), fill_value='.')
    for pw in walls:
        space[pw[1], pw[0]] = '#'

    sand_source = (500, 0)
    space[sand_source[1], sand_source[0]] = '+'

    for i in range(100_000):
        sand_placed = send_sand(sand_source, space, max_x,
                                max_y)
        if sand_placed is False:
            break
    return i+1


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
