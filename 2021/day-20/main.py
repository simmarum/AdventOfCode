from operator import itemgetter
import copy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def _print_board(bb):
    x_min = min([x[0] for x in bb]) - 1
    x_max = max([x[0] for x in bb]) + 1
    y_min = min([x[1] for x in bb]) - 1
    y_max = max([x[1] for x in bb]) + 1
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            if (x, y) in bb:
                print('#', end='')
            else:
                print('.', end='')
        print()


def part_1(inp):
    lookup = [c for c in inp[0]]
    data = [x for x in inp[2:]]
    board = set()
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == '#':
                board.add((j, i))

    new_edge = False
    for step in range(1, 2+1):
        x_min = min([x[0] for x in board])
        x_max = max([x[0] for x in board])
        y_min = min([x[1] for x in board])
        y_max = max([x[1] for x in board])
        board_new = set()
        for x in range(x_min-1, x_max+2):
            for y in range(y_min-1, y_max+2):
                index = 0
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        xx, yy = x+dx, y+dy
                        index <<= 1
                        index |= ((xx, yy) in board) or (
                            new_edge and not (
                                x_min <= xx <= x_max and y_min <= yy <= y_max)
                        )
                if lookup[index] == '#':
                    board_new.add((x, y))
        board = copy.deepcopy(board_new)
        new_edge = lookup[-new_edge] == '#'
        # _print_board(board)
    return len(board)


def part_2(inp):
    lookup = [c for c in inp[0]]
    data = [x for x in inp[2:]]
    board = set()
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == '#':
                board.add((j, i))

    new_edge = False
    for step in range(1, 50+1):
        x_min = min([x[0] for x in board])
        x_max = max([x[0] for x in board])
        y_min = min([x[1] for x in board])
        y_max = max([x[1] for x in board])
        board_new = set()
        for x in range(x_min-1, x_max+2):
            for y in range(y_min-1, y_max+2):
                index = 0
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        xx, yy = x+dx, y+dy
                        index <<= 1
                        index |= ((xx, yy) in board) or (
                            new_edge and not (
                                x_min <= xx <= x_max and y_min <= yy <= y_max)
                        )
                if lookup[index] == '#':
                    board_new.add((x, y))
        board = copy.deepcopy(board_new)
        new_edge = lookup[-new_edge] == '#'
        # _print_board(board)
    return len(board)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
