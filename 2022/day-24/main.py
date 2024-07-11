def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.readlines() if line]


def get_world(inp):
    dirs = {
        'v': complex(1, 0),
        '^': complex(-1, 0),
        '>': complex(0, 1),
        '<': complex(0, -1),
        '@': complex(0, 0)  # stay in place
    }
    wall = set()
    blizzard = set()
    # shift all by minus 1 for easier use of modulo
    for y, line in enumerate(inp, -1):
        for x, c in enumerate(line, -1):
            if c == '#':
                wall.add(complex(y, x))
            if c in 'v^><':
                blizzard.add((complex(y, x), dirs[c]))
    max_y = int(max(w.real for w in wall))
    max_x = int(max(w.imag for w in wall))
    # instead of custom start/end where player can be add more walls around
    wall.update({complex(-2, x) for x in range(-1, -1 + 3 + 1)})
    wall.update({complex(max_y + 1, x)
                for x in range(max_x - 3, max_x - 3 + 4 + 1)})
    start_pos = complex(-1, 0)
    end_pos = complex(max_y, max_x - 1)
    return wall, blizzard, max_y, max_x, start_pos, end_pos, dirs


def travel_blizzard(wall, blizzard, max_y, max_x,
                    start_pos, destination, dirs):
    stack = set([start_pos])
    step = 0
    while destination:
        step += 1
        current_blizzard = {
            complex(
                (bp.real + step * bd.real) % max_y,
                (bp.imag + step * bd.imag) % max_x
            ) for bp, bd in blizzard
        }
        new_stack = {complex(p.real + d.real, p.imag + d.imag)
                     for d in list(dirs.values()) for p in stack}
        stack = new_stack.difference(current_blizzard, wall)
        if destination[0] in stack:
            yield step
            stack = set([destination.pop(0)])


def part_1(inp):
    wall, blizzard, max_y, max_x, start_pos, end_pos, dirs = get_world(inp)
    return list(travel_blizzard(wall, blizzard, max_y, max_x,
                                start_pos, [end_pos], dirs))[0]


def part_2(inp):
    wall, blizzard, max_y, max_x, start_pos, end_pos, dirs = get_world(inp)
    return list(travel_blizzard(wall, blizzard, max_y, max_x,
                                start_pos, [end_pos, start_pos, end_pos], dirs))[2]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
