import numpy as np
import heapq


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.readlines()]


dirs = {
    'u': (-1, 0),
    'd': (1, 0),
    'l': (0, -1),
    'r': (0, 1),
}
next_ways = {
    '.u': ('u',),
    '.d': ('d',),
    '.l': ('l',),
    '.r': ('r',),
    '/u': ('r',),
    '/d': ('l',),
    '/l': ('d',),
    '/r': ('u',),
    '\\u': ('l',),
    '\\d': ('r',),
    '\\l': ('u',),
    '\\r': ('d',),
    '-u': ('l', 'r'),
    '-d': ('l', 'r'),
    '-l': ('l',),
    '-r': ('r',),
    '|u': ('u',),
    '|d': ('d',),
    '|l': ('u', 'd'),
    '|r': ('u', 'd'),
}


def part_1(inp):
    layout = np.array([[c for c in line] for line in inp])
    start_node = ((0, -1), 'r')
    visited = set()
    stack = []
    heapq.heappush(stack, start_node)
    step = 0
    while stack:
        step += 1
        if step >= 100000:
            print(
                "Reach safe step number - please increase if you want to calculate more!")
            exit()
        curr_pos, curr_way = heapq.heappop(stack)
        visited.add((curr_pos, curr_way))
        next_pos = (
            curr_pos[0] + dirs[curr_way][0],
            curr_pos[1] + dirs[curr_way][1]
        )
        if not (0 <= next_pos[0] < layout.shape[0]
                and 0 <= next_pos[1] < layout.shape[1]):
            continue
        next_char = layout[next_pos]
        for next_way in next_ways[next_char + curr_way]:
            if not (next_pos, next_way) in visited:
                heapq.heappush(stack, (next_pos, next_way))

    visited_pos = set([p[0] for p in visited])

    return len(visited_pos) - 1


def part_2(inp):
    layout = np.array([[c for c in line] for line in inp])

    start_nodes = []
    for i in range(layout.shape[0]):
        start_nodes.append(((i, -1), 'r'))
        start_nodes.append(((i, layout.shape[1]), 'l'))
    for j in range(layout.shape[1]):
        start_nodes.append(((-1, j), 'd'))
        start_nodes.append(((layout.shape[0], j), 'u'))
    all_node_results = []
    for start_node in start_nodes:
        visited = set()
        stack = []
        heapq.heappush(stack, start_node)
        step = 0
        while stack:
            step += 1
            if step >= 100000:
                print(
                    "Reach safe step number - please increase if you want to calculate more!")
                exit()
            curr_pos, curr_way = heapq.heappop(stack)
            visited.add((curr_pos, curr_way))
            next_pos = (
                curr_pos[0] + dirs[curr_way][0],
                curr_pos[1] + dirs[curr_way][1]
            )
            if not (0 <= next_pos[0] < layout.shape[0]
                    and 0 <= next_pos[1] < layout.shape[1]):
                continue
            next_char = layout[next_pos]
            for next_way in next_ways[next_char + curr_way]:
                if not (next_pos, next_way) in visited:
                    heapq.heappush(stack, (next_pos, next_way))

        visited_pos = set([p[0] for p in visited])
        all_node_results.append(
            (
                len(visited_pos) - 1,
                start_node
            )
        )

    return sorted(all_node_results, reverse=True)[0][0]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
