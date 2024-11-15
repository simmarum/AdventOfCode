def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def part_1(inp):
    wires_points = set()
    min_distance = 2**32
    for line_idx, line in enumerate(inp):
        curr_point = complex(0, 0)
        for move in line.split(','):
            move_dir, move_cnt = move[0], int(move[1:])
            if move_dir == 'U':
                diff = complex(0, 1)
            elif move_dir == 'D':
                diff = complex(0, -1)
            elif move_dir == 'R':
                diff = complex(1, 0)
            elif move_dir == 'L':
                diff = complex(-1)
            for _ in range(1, move_cnt + 1):
                curr_point = curr_point + diff
                if (line_idx == 1) and (curr_point in wires_points):
                    min_distance = min(
                        min_distance,
                        int(abs(curr_point.real) + abs(curr_point.imag))
                    )
                else:
                    wires_points.add(curr_point)
    return min_distance


def part_2(inp):
    wires = [{complex(0, 0): 0}, {complex(0, 0): 0}]
    min_distance = 2**32
    for line_idx, line in enumerate(inp):
        curr_point = complex(0, 0)
        curr_len = 0
        for move in line.split(','):
            move_dir, move_cnt = move[0], int(move[1:])
            if move_dir == 'U':
                diff = complex(0, 1)
            elif move_dir == 'D':
                diff = complex(0, -1)
            elif move_dir == 'R':
                diff = complex(1, 0)
            elif move_dir == 'L':
                diff = complex(-1)
            for _ in range(1, move_cnt + 1):
                curr_point = curr_point + diff
                curr_len += 1
                wires[line_idx][curr_point] = curr_len
                if (line_idx == 1) and (curr_point in wires[0]):
                    min_distance = min(
                        min_distance,
                        wires[0][curr_point] + wires[1][curr_point]
                    )
    return min_distance


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
