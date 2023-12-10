import re
from itertools import combinations


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    y_line = 2000000
    y_line_spots = set()
    y_line_placed = set()
    for line in inp:
        sx, sy, bx, by = list(map(int, re.sub(r"[^0-9 \-]", "", line).split()))
        if by == y_line:
            y_line_placed.add(bx)
        if sy == y_line:
            y_line_placed.add(sx)

        d = abs(sx - bx) + abs(sy - by)
        if (sy - d) <= y_line <= (sy + d):
            d_left = d - abs(sy - y_line)
            y_line_spots = y_line_spots.union(
                set(range(sx - d_left, sx + d_left + 1)))

    y_line_spots.difference_update(y_line_placed)
    return len(y_line_spots)


def part_2(inp):
    max_coord = 4000000
    distances = {}
    for line in inp:
        sx, sy, bx, by = list(map(int, re.sub(r"[^0-9 \-]", "", line).split()))
        d = abs(sx - bx) + abs(sy - by)
        distances[(sx, sy)] = d
    pairs = []
    for (k1, v1), (k2, v2) in combinations(distances.items(), 2):
        if (abs(k1[0] - k2[0]) + abs(k1[1] - k2[1])) == v1 + v2 + 2:
            pairs.append((k1, k2))
    for (s1, s2), (s3, s4) in combinations(pairs, 2):
        s1, s2 = sorted([s1, s2])
        s3, s4 = sorted([s3, s4])
        diagonals = []
        for sa, sb in zip([s1, s3], [s2, s4]):
            da = distances[sa] + 1
            db = distances[sb] + 1
            end = (sa[0] + da, sa[1])
            start = (sb[0] - db, sb[1])
            diagonals.append([start, end])
        l1 = diagonals[0]
        l2 = diagonals[1]
        dx = (l1[0][0] - l1[1][0], l2[0][0] - l2[1][0])
        dy = (l1[0][1] - l1[1][1], l2[0][1] - l2[1][1])
        # pochodna
        dd = dx[0] * dy[1] - dx[1] * dy[0]
        if dd != 0:
            d = (l1[0][0] * l1[1][1] - l1[0][1] * l1[1][0],
                 l2[0][0] * l2[1][1] - l2[0][1] * l2[1][0])
            x = int(round((d[0] * dx[1] - d[1] * dx[0]) / dd))
            y = int(round((d[0] * dy[1] - d[1] * dy[0]) / dd))
            return x * max_coord + y


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    # res_2 = solve_b(inp)
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
