from curses.ascii import isdigit
from itertools import permutations
import numpy as np
import heapq


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def read_board(inp):
    board = []
    nums = {}
    for line in inp:
        board.append([c for c in line])
    for y in range(len(board)):
        for x in range(len(board[y])):
            if isdigit(board[y][x]):
                nums[board[y][x]] = (x, y)

    board = np.array(board)
    return board, nums


def get_two_points(nums):
    two_points = {}
    for k1, v1 in nums.items():
        for k2, v2 in nums.items():
            if k1 == k2:
                continue
            if k1 + '_' + k2 in two_points:
                continue
            if k2 + '_' + k1 in two_points:
                continue
            two_points[k1 + '_' + k2] = [v1, v2, None]
    return two_points


def astar_heuristic(a, b, with_diagonal=False):
    if with_diagonal:
        return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
    else:
        return abs(b[0] - a[0]) + abs((b[1] - a[1]))


def astar(board, start, goal, with_diagonal=False, wall_char='#'):
    if with_diagonal:
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0),
                     (1, 1), (1, -1), (-1, 1), (-1, -1)]
    else:
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: astar_heuristic(start, goal, with_diagonal)}
    oheap = []
    heapq.heappush(oheap, (fscore[start], start))
    while oheap:
        current = heapq.heappop(oheap)[1]
        if current == goal:
            route = []
            while current in came_from:
                route.append(current)
                current = came_from[current]
            route = route + [start]
            route = route[::-1]
            return route

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + \
                astar_heuristic(current, neighbor, with_diagonal)
            if 0 <= neighbor[1] < board.shape[0]:
                if 0 <= neighbor[0] < board.shape[1]:
                    if board[neighbor[1]][neighbor[0]] == wall_char:
                        continue
                else:
                    continue
            else:
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(
                    neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [
                    i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + \
                    astar_heuristic(neighbor, goal, with_diagonal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))
    return False


def get_all_paths(board, two_points):
    for name, points in two_points.items():
        path = astar(board, points[0], points[1])
        two_points[name][2] = len(path) - 1
    return two_points


def find_shortest_path(nums, two_points, return_to_start=False):
    all_nums = nums.keys()
    min_len = 1_000_000_000
    for one_perm in permutations(all_nums, len(all_nums)):
        if one_perm[0] != '0':
            continue
        if return_to_start:
            one_perm = list(one_perm) + ['0']

        tmp_points = [one_perm[i - 1] + '_' + one_perm[i]
                      for i in range(1, len(one_perm))]
        tmp_len = []
        for name in tmp_points:
            if name in two_points:
                tmp_len.append(two_points[name][2])
            else:
                tmp_len.append(two_points[name[2] + name[1] + name[0]][2])
        tmp_len = sum(tmp_len)
        min_len = min(min_len, tmp_len)
    return min_len


def part_1(inp):
    board, nums = read_board(inp)
    two_points = get_two_points(nums)
    two_points = get_all_paths(board, two_points)
    min_len = find_shortest_path(nums, two_points)
    return min_len


def part_2(inp):
    board, nums = read_board(inp)
    two_points = get_two_points(nums)
    two_points = get_all_paths(board, two_points)
    min_len = find_shortest_path(nums, two_points, return_to_start=True)
    return min_len


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
