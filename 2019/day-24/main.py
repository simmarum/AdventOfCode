def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def read_scan(inp):
    eris = {}
    for y, line in enumerate(inp):
        for x, elem in enumerate(line):
            eris[complex(x, y)] = elem
    return eris


def print_eris(eris, minute):
    min_x = min((int(p.real) for p in eris.keys()))
    max_x = max((int(p.real) for p in eris.keys()))
    min_y = min((int(p.imag) for p in eris.keys()))
    max_y = max((int(p.imag) for p in eris.keys()))
    lookup = {
        0: "Initial state:",
        1: "After {minute} minute:",
    }
    eris_str = lookup.get(
        minute,
        f"After {minute} minutes:").format(
        minute=minute)
    for y in range(min_y, max_y + 1):
        eris_str += "\n"
        for x in range(min_x, max_x + 1):
            eris_str += eris.get(complex(x, y), '.')
    print(eris_str)


def simulate_live(eris, max_minutes):
    eris_history = [eris]
    neighbors = [complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0)]
    for minute in range(1, max_minutes + 1):
        new_eris = {}
        for pos, val in eris.items():
            n_bugs = [eris.get(pos + n_diff, '.')
                      for n_diff in neighbors].count('#')
            if (val == '#'):
                new_val = '.'
                if n_bugs in (1,):
                    new_val = '#'
            else:
                new_val = '.'
                if n_bugs in (1, 2):
                    new_val = '#'
            new_eris[pos] = new_val
        if new_eris in eris_history:
            # print_eris(new_eris, minute)
            return new_eris

        eris = new_eris
        eris_history.append(eris)
        # print_eris(eris, minute)
    return eris


def part_1(inp):
    size = 5
    eris = read_scan(inp)
    # print_eris(eris, 0)
    max_minutes = 2000
    eris = simulate_live(eris, max_minutes)
    biodiversity_rating = sum([2**int((k.imag * size) + (k.real + 0))
                               for k, v in eris.items() if v == '#'])
    return biodiversity_rating


def read_scan_int(inp, size):
    eris = {}
    for y, line in enumerate(inp):
        for x, elem in enumerate(line, 1):
            eris[(0, y * size + x)] = elem
    del eris[(0, 13)]
    return eris


def simulate_live_with_depth(eris, max_minutes, size):
    neighbors = {

        #      |     |         |     |
        #   1  |  2  |    3    |  4  |  5
        #      |     |         |     |
        # -----+-----+---------+-----+-----
        #      |     |         |     |
        #   6  |  7  |    8    |  9  |  10
        #      |     |         |     |
        # -----+-----+---------+-----+-----
        #      |     |A|B|C|D|E|     |
        #      |     |-+-+-+-+-|     |
        #      |     |F|G|H|I|J|     |
        #      |     |-+-+-+-+-|     |
        #  11  | 12  |K|L|?|N|O|  14 |  15
        #      |     |-+-+-+-+-|     |
        #      |     |P|Q|R|S|T|     |
        #      |     |-+-+-+-+-|     |
        #      |     |U|V|W|X|Y|     |
        # -----+-----+---------+-----+-----
        #      |     |         |     |
        #  16  | 17  |    18   |  19 |  20
        #      |     |         |     |
        # -----+-----+---------+-----+-----
        #      |     |         |     |
        #  21  | 22  |    23   |  24 |  25
        #      |     |         |     |

        # pos: [(+-lvl, neighbor_pos),...]
        # R D L U
        # first row
        1: [(0, 2), (0, 6), (-1, 12), (-1, 8)],
        2: [(0, 3), (0, 7), (0, 1), (-1, 8)],
        3: [(0, 4), (0, 8), (0, 2), (-1, 8)],
        4: [(0, 5), (0, 9), (0, 3), (-1, 8)],
        5: [(-1, 14), (0, 10), (0, 4), (-1, 8)],
        # second row
        6: [(0, 7), (0, 11), (-1, 12), (0, 1)],
        7: [(0, 8), (0, 12), (0, 6), (0, 2)],
        8: [(0, 9), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (0, 7), (0, 3)],
        9: [(0, 10), (0, 14), (0, 8), (0, 4)],
        10: [(-1, 14), (0, 15), (0, 9), (0, 5)],
        # third row
        11: [(0, 12), (0, 16), (-1, 12), (0, 6)],
        12: [(1, 1), (1, 6), (1, 11), (1, 16), (1, 21), (0, 17), (0, 11), (0, 7)],
        # 13 inner lvl
        14: [(0, 15), (0, 19), (1, 5), (1, 10), (1, 15), (1, 20), (1, 25), (0, 9)],
        15: [(-1, 14), (0, 20), (0, 14), (0, 10)],
        # fourth row
        16: [(0, 17), (0, 21), (-1, 12), (0, 11)],
        17: [(0, 18), (0, 22), (0, 16), (0, 12)],
        18: [(0, 19), (0, 23), (0, 17), (1, 21), (1, 22), (1, 23), (1, 24), (1, 25)],
        19: [(0, 20), (0, 24), (0, 18), (0, 14)],
        20: [(-1, 14), (0, 25), (0, 19), (0, 15)],
        # fifth row
        21: [(0, 22), (-1, 18), (-1, 12), (0, 16)],
        22: [(0, 23), (-1, 18), (0, 21), (0, 17)],
        23: [(0, 24), (-1, 18), (0, 22), (0, 18)],
        24: [(0, 25), (-1, 18), (0, 23), (0, 19)],
        25: [(-1, 14), (-1, 18), (0, 24), (0, 20)],
    }
    positions = list(eris.keys())
    for lvl in range(1, max_minutes // 2 + 1):
        for (curr_lvl, curr_pos) in positions:
            eris[(lvl, curr_pos)] = 0
            eris[(-lvl, curr_pos)] = 0

    for minute in range(1, max_minutes + 1):
        new_eris = {}
        for (curr_lvl, curr_pos), curr_val in eris.items():
            n_bugs = [eris.get((curr_lvl + lvl_diff, n_pos), '.')
                      for lvl_diff, n_pos in neighbors[curr_pos]].count('#')
            if (curr_val == '#'):
                new_val = '.'
                if n_bugs in (1,):
                    new_val = '#'
            else:
                new_val = '.'
                if n_bugs in (1, 2):
                    new_val = '#'
            new_eris[(curr_lvl, curr_pos)] = new_val

        eris = new_eris
        # print_eris(eris, minute)
    # print(sorted(eris.items()))
    return eris


def part_2(inp):
    size = 5
    max_minutes = 200
    eris = read_scan_int(inp, size)
    eris = simulate_live_with_depth(eris, max_minutes, size)
    # print(eris)
    return list(eris.values()).count('#')


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
