import sys

sys.setrecursionlimit(2_773)


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def read_inp(inp):
    walls = set()
    y_min, y_max = 1_000_000_000_000, 0
    x_min, x_max = 1_000_000_000_000, 0
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

        x1, x2 = list(sorted([x1, x2]))
        y1, y2 = list(sorted([y1, y2]))
        for px in range(x1, x2 + 1):
            for py in range(y1, y2 + 1):
                walls.add(complex(px, py))
        y_min = min(y_min, y1, y2)
        y_max = max(y_max, y1, y2)
        x_min = min(x_min, x1, x2)
        x_max = max(x_max, x1, x2)
    return walls, y_min, y_max, x_min, x_max


def print_world(walls, y_min, y_max, x_min, x_max, water, water_stopped):
    print()
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if complex(x, y) in walls:
                print('#', end='')
            elif complex(x, y) in water_stopped:
                print('~', end='')
            elif complex(x, y) in water:
                print('|', end='')
            else:
                print('.', end='')
        print()
    print()


def fall_one_grain(start_point, move, walls, water,
                   water_stopped, y_min, y_max):
    water.add(start_point)
    next_point_down = start_point + complex(0, 1)
    next_point_left = start_point + complex(-1, 0)
    next_point_right = start_point + complex(1, 0)

    if next_point_down not in walls:
        if (next_point_down not in water) and (next_point_down.imag <= y_max):
            fall_one_grain(
                next_point_down,
                complex(0, 1),
                walls,
                water,
                water_stopped,
                y_min,
                y_max)
        if next_point_down not in water_stopped:
            return False
    is_left_blocked = (
        (next_point_left in walls)
        or (
            (next_point_left not in water)
            and (fall_one_grain(next_point_left, complex(-1, 0), walls, water, water_stopped, y_min, y_max))
        )
    )
    is_right_blocked = (
        (next_point_right in walls)
        or (
            (next_point_right not in water)
            and (fall_one_grain(next_point_right, complex(1, 0), walls, water, water_stopped, y_min, y_max))
        )
    )

    if (move == complex(0, 1)) and is_left_blocked and is_right_blocked:
        water_stopped.add(start_point)

        while next_point_left in water:
            water_stopped.add(next_point_left)
            next_point_left += complex(-1, 0)
        while next_point_right in water:
            water_stopped.add(next_point_right)
            next_point_right += complex(1, 0)

    return (
        (
            (move == complex(-1, 0))
            and (is_left_blocked or next_point_left in walls)
        )
        or (
            (move == complex(1, 0))
            and (is_right_blocked or next_point_right in walls)
        )
    )


def part_1(inp):
    walls, y_min, y_max, x_min, x_max = read_inp(inp)
    water = set()
    water_stopped = set()
    # print_world(walls, y_min, y_max, x_min, x_max, water, water_stopped)
    fall_one_grain(
        start_point=complex(500, 0),
        move=complex(0, 1),
        walls=walls,
        water=water,
        water_stopped=water_stopped,
        y_min=y_min,
        y_max=y_max
    )
    # print_world(walls, y_min, y_max, x_min, x_max, water, water_stopped)
    all_water = water.union(water_stopped)
    all_water_in_range = [p for p in all_water if y_min <= p.imag <= y_max]
    return len(all_water_in_range)


def part_2(inp):
    walls, y_min, y_max, x_min, x_max = read_inp(inp)
    water = set()
    water_stopped = set()
    # print_world(walls, y_min, y_max, x_min, x_max, water, water_stopped)
    fall_one_grain(
        start_point=complex(500, 0),
        move=complex(0, 1),
        walls=walls,
        water=water,
        water_stopped=water_stopped,
        y_min=y_min,
        y_max=y_max
    )
    # print_world(walls, y_min, y_max, x_min, x_max, water, water_stopped)
    all_water_in_range = [p for p in water_stopped if y_min <= p.imag <= y_max]
    return len(all_water_in_range)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
