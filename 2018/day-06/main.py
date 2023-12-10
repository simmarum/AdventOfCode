import numpy as np
from scipy.spatial import distance


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    points = [tuple(map(int, line.split(','))) for line in inp]
    marg = 0
    max_x = 0
    max_y = 0
    for p1 in points:
        for p2 in points:
            max_x = max(max_x, p1[0])
            max_x = max(max_x, p2[0])
            max_y = max(max_y, p1[1])
            max_y = max(max_y, p2[1])
            marg = max(marg, abs(
                p2[0] - p1[0]) + abs(p2[1] - p1[1]))
    board = [[-1] * (max_x + (marg * 2))
             for _ in range((max_y + (marg * 2)))]

    for y in range(len(board)):
        for x in range(len(board[y])):
            neareast_points = sorted(
                [(abs(p[0] + marg - x) + abs(p[1] + marg - y), i) for i, p in enumerate(points)])[0:2]
            if neareast_points[0][0] < neareast_points[1][0]:
                if neareast_points[0][1] == 0:
                    # board[y][x] = chr(neareast_points[0][1]+ord('A'))
                    board[y][x] = neareast_points[0][1]
                else:
                    # board[y][x] = chr(neareast_points[0][1]+ord('a'))
                    board[y][x] = neareast_points[0][1]

    avail_points = set(range(len(points)))
    points_on_edge = set(board[0])\
        .union(set(board[-1]))\
        .union(set([row[0] for row in board]))\
        .union(set(row[-1] for row in board))
    avail_points.difference_update(points_on_edge)

    max_area = 0
    flat_board = [item for sublist in board for item in sublist]
    for point in avail_points:
        max_area = max(max_area, flat_board.count(point))
    return max_area


def part_2():
    # need to use numpy and scipy - my solution from part 1 was too slow :(
    points = np.loadtxt(
        f"{__file__.rstrip('main.py')}input.txt", delimiter=',')

    xmin, _ = points.min(axis=0) - 1
    xmax, _ = points.max(axis=0) + 2

    xgrid, ygrid = np.meshgrid(np.arange(xmin, xmax), np.arange(xmin, xmax))
    targets = np.dstack([xgrid, ygrid]).reshape(-1, 2)

    cityblock = distance.cdist(points, targets, metric='cityblock')

    origin_distances = cityblock.sum(axis=0)
    region = np.where(origin_distances < 10000, 1, 0)

    return region.sum()


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2()
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
