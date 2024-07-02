import heapq


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [[int(c) for c in line if c != "\n"] for line in f.readlines()]


def minimal_heat(board, start, end, least, most):
    queue = [(0, *start, 0, 0)]
    seen = set()
    while queue:
        heat, x, y, px, py = heapq.heappop(queue)
        if (x, y) == end:
            return heat
        if (x, y, px, py) in seen:
            continue
        seen.add((x, y, px, py))
        # calculate turns only
        for dx, dy in {(1, 0), (0, 1), (-1, 0), (0, -1)} - \
                {(px, py), (-px, -py)}:
            a, b, h = x, y, heat
            for i in range(1, most + 1):
                a, b = a + dx, b + dy
                if (a, b) in board:
                    h += board[a, b]
                    if i >= least:
                        heapq.heappush(queue, (h, a, b, dx, dy))


def part_1(inp):
    board = {}
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            board[(y, x)] = c
    return minimal_heat(board, (0, 0), max(board), 1, 3)


def part_2(inp):
    board = {}
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            board[(y, x)] = c
    return minimal_heat(board, (0, 0), max(board), 4, 10)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
