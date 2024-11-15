from queue import Queue
import heapq


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def get_maze_as_dict(inp, split_to_4_vault=False):
    maze = {}
    for y, row in enumerate(inp):
        for x, elem in enumerate(row):
            maze[complex(x, y)] = elem
    if split_to_4_vault:
        vault = [k for k, v in maze.items() if v == '@'][0]
        maze[vault + complex(-1, -1)] = '@1'
        maze[vault + complex(-1, 0)] = '#'
        maze[vault + complex(-1, 1)] = '@2'
        maze[vault + complex(0, -1)] = '#'
        maze[vault + complex(0, 0)] = '#'
        maze[vault + complex(0, 1)] = '#'
        maze[vault + complex(1, -1)] = '@3'
        maze[vault + complex(1, 0)] = '#'
        maze[vault + complex(1, 1)] = '@4'
    keys = {v: k for k, v in maze.items() if v.islower() or v.startswith('@')}
    return maze, keys


def print_maze(maze):
    min_x = min((int(p.real) for p in maze.keys()))
    max_x = max((int(p.real) for p in maze.keys()))
    min_y = min((int(p.imag) for p in maze.keys()))
    max_y = max((int(p.imag) for p in maze.keys()))
    maze_str = ""
    for y in range(min_y, max_y + 1):
        maze_str += "\n"
        for x in range(min_x, max_x + 1):
            maze_str += maze.get(complex(x, y), -1)
    print(maze_str)


def search_for_key_access_list(maze, start_point):
    neighbors_diff = [complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0)]  # noqa
    q = Queue()
    q.put((start_point, 0, ()))
    visited = set()
    key_mapping = dict()
    while not q.empty():
        c_point, c_dist, c_doors = q.get()
        if c_point in visited:
            continue
        visited.add(c_point)

        if maze[c_point].islower() and start_point != c_point:
            key_mapping[maze[c_point]] = (c_dist, frozenset(c_doors))
        for n_diff in neighbors_diff:
            n_point = c_point + n_diff
            if maze[n_point] != '#':
                new_doors = c_doors
                if maze[n_point].isupper():
                    new_doors = c_doors + (maze[n_point].lower(),)
                q.put((n_point, c_dist + 1, new_doors))
    return key_mapping


def find_best_route(start_tuple, key_key_mapping, keys):
    distances = dict()
    keys_len = len(keys) - len(start_tuple)
    q = [(0, (start_tuple, frozenset()))]
    heapq.heapify(q)
    while q:
        c_dist, c_node = heapq.heappop(q)
        if c_node in distances:
            continue
        distances[c_node] = c_dist

        c_node_node, c_node_keys = c_node

        if len(c_node_keys) == keys_len:
            return c_dist

        for i in range(len(c_node_node)):
            for k, (k_dist, k_doors) in key_key_mapping[c_node_node[i]].items():  # noqa
                if (k_doors.issubset(c_node_keys)) and (
                        k not in c_node_keys):
                    heapq.heappush(
                        q,
                        (
                            c_dist + k_dist,
                            (
                                c_node_node[:i] + (k,) + c_node_node[i + 1:],
                                c_node_keys.union(frozenset(k))
                            )
                        )
                    )


def part_1(inp):
    maze, keys = get_maze_as_dict(inp)
    key_key_mapping = {
        k_name: search_for_key_access_list(
            maze, k_point) for k_name, k_point in keys.items()}
    min_dist = find_best_route(('@',), key_key_mapping, keys)
    return min_dist


def part_2(inp):
    maze, keys = get_maze_as_dict(inp, split_to_4_vault=True)
    key_key_mapping = {
        k_name: search_for_key_access_list(
            maze, k_point) for k_name, k_point in keys.items()}
    min_dist = find_best_route(('@1', '@2', '@3', '@4'), key_key_mapping, keys)
    return min_dist


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
