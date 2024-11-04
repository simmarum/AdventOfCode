import re
import z3


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def parse_input(inp):
    nanobots = {}
    for line in inp:
        x, y, z, r = map(int, re.findall(r'-?\d+', line))
        nanobots[(x, y, z)] = r
    return nanobots


def get_manhattan(a, b):
    return sum(abs(val1 - val2) for val1, val2 in zip(a, b))


def part_1(inp):
    nanobots = parse_input(inp)
    strongest_nanobot = max(nanobots, key=lambda key: nanobots[key])
    nanobots_in_range = list(filter(lambda nanobot: get_manhattan(
        strongest_nanobot, nanobot) <= nanobots[strongest_nanobot], nanobots))
    return len(nanobots_in_range)


def solve_using_z3(nanobots):
    # https://ericpony.github.io/z3py-tutorial/guide-examples.htm
    def get_manhattan_z3(a, b):
        return (
            z3.If((a[0] - b[0]) >= 0, a[0] - b[0], -(a[0] - b[0]))
            + z3.If((a[1] - b[1]) >= 0, a[1] - b[1], -(a[1] - b[1]))
            + z3.If((a[2] - b[2]) >= 0, a[2] - b[2], -(a[2] - b[2]))
        )
    solver = z3.Optimize()
    z3.set_option(html_mode=False)
    z3.set_option(parallel=False)

    best_x = z3.Int('best_x')
    best_y = z3.Int('best_y')
    best_z = z3.Int('best_z')
    distance = z3.Int('distance')

    inside = []
    nano_idx = 0
    for nano_pos, nano_radius in nanobots.items():
        nano_idx += 1
        tmp_nanobot = z3.Int(f'nanobot_{nano_idx:4d}')
        tmp_nanobot_inside = z3.If(
            get_manhattan_z3(
                (best_x, best_y, best_z), (nano_pos)) <= nano_radius, 1, 0)
        solver.add(tmp_nanobot == tmp_nanobot_inside)
        inside.append(tmp_nanobot)

    solver.add(distance == get_manhattan_z3(
        (best_x, best_y, best_z), (0, 0, 0)))

    solver.maximize(z3.Sum(*inside))
    solver.minimize(distance)
    solver.check()

    m = solver.model()
    return m.eval(distance)


def part_2(inp):
    nanobots = parse_input(inp)

    return solve_using_z3(nanobots)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
