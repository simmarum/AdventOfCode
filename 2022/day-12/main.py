import numpy as np
import heapq


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


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
                    if ord(board[neighbor[1]][neighbor[0]]) - \
                            ord(board[current[1]][current[0]]) > 1:
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


def part_1(inp):
    world = np.array([[c for c in line] for line in inp])
    start_node = tuple(list(np.argwhere(world == 'S')[0])[::-1])  # y,x
    end_node = tuple(list(np.argwhere(world == 'E')[0])[::-1])  # y,x
    world[start_node[1]][start_node[0]] = 'a'
    world[end_node[1]][end_node[0]] = 'z'
    path = astar(world, start_node, end_node)
    return len(path) - 1


def part_2(inp):
    world = np.array([[c for c in line] for line in inp])
    start_node = tuple(list(np.argwhere(world == 'S')[0])[::-1])  # y,x
    end_node = tuple(list(np.argwhere(world == 'E')[0])[::-1])  # y,x
    world[start_node[1]][start_node[0]] = 'a'
    world[end_node[1]][end_node[0]] = 'z'
    min_path = 1_000_000_000
    for start_node in [tuple(point[::-1])
                       for point in np.argwhere(world == 'a')]:
        # y,x
        path = astar(world, start_node, end_node)
        if path:
            min_path = min(min_path, len(path) - 1)
    return min_path


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
