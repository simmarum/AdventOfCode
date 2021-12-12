from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '').split('-')
                for line in f.readlines()]


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set([p for p in path if not p.isupper()]):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def part_1(inp):
    g = defaultdict(set)
    for x in inp:
        g[x[0]].add(x[1])
        g[x[1]].add(x[0])
    all_path = list(dfs_paths(g, 'start', 'end'))
    all_path = sorted(all_path)
    return len(all_path)


def dfs_paths_cnt(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        tmp_path = []
        was_two_small = False
        for p in path:
            if (p == 'start') or (p == 'end'):
                tmp_path.append(p)
            elif (p.isupper()):
                continue
            else:
                if path.count(p) >= 2:
                    was_two_small = True
                    tmp_path.append(p)
        if was_two_small:
            tmp_path += [p for p in path if not p.isupper()]
        for next in graph[vertex] - set(tmp_path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def part_2(inp):
    g = defaultdict(set)
    for x in inp:
        g[x[0]].add(x[1])
        g[x[1]].add(x[0])
    all_path = list(dfs_paths_cnt(g, 'start', 'end'))
    all_path = sorted(all_path)
    return len(all_path)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
