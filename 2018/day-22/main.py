import networkx as nx
from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def read_input(inp):
    depth = int(inp[0].split()[1])
    target_x, target_y = inp[1].split()[1].split(',')
    target = complex(int(target_x), int(target_y))
    return target, depth


def create_map(start, target, map_size, depth):
    geo_map = {}
    ero_map = {}
    type_map = {}
    for x in range(0, int(map_size.real + 1)):
        for y in range(0, int(map_size.imag + 1)):
            cur_pos = complex(x, y)
            if cur_pos in [start, target]:
                geo_map[cur_pos] = 0
            elif x == 0:
                geo_map[cur_pos] = y * 48271
            elif y == 0:
                geo_map[cur_pos] = x * 16807
            else:
                geo_map[cur_pos] = ero_map[cur_pos -
                                           complex(1, 0)] * ero_map[cur_pos - complex(0, 1)]

            ero_map[cur_pos] = (geo_map[cur_pos] + depth) % 20183
            type_map[cur_pos] = ero_map[cur_pos] % 3

    return type_map


def part_1(inp):
    target, depth = read_input(inp)
    start = complex(0, 0)

    # target = complex(10, 10)
    # depth = 510

    map_size = target + complex(0, 0)
    type_map = create_map(start, target, map_size, depth)

    return sum(type_map.values())


def dijkstra(type_map, start, map_size, target):
    # rocky = 0
    # wet = 1
    # narrow 2
    # torch = 0
    # climbing gear = 1
    # neither  2
    valid_tools = {
        0: [0, 1],
        1: [1, 2],
        2: [2, 0]
    }
    valid_regions = defaultdict(list)
    for k, v in valid_tools.items():
        for v_name in v:
            valid_regions[v_name].append(k)

    graph = nx.Graph()
    for x in range(0, int(map_size.real + 1)):
        for y in range(0, int(map_size.imag + 1)):
            cur_pos = complex(x, y)
            tools = valid_tools[type_map[cur_pos]]
            graph.add_edge(
                (cur_pos, tools[0]), (cur_pos, tools[1]), weight=7)
            for move in (complex(0, 1), complex(0, -1),
                         complex(1, 0), complex(-1, 0)):
                new_pos = cur_pos + move
                if 0 <= new_pos.real <= map_size.real and 0 <= new_pos.imag <= map_size.imag:
                    new_tools = valid_tools[type_map[new_pos]]
                    for tool in set(tools).intersection(set(new_tools)):
                        graph.add_edge(
                            (cur_pos, tool), (new_pos, tool), weight=1)

    return nx.dijkstra_path_length(graph, (start, 0), (target, 0))


def part_2(inp):
    target, depth = read_input(inp)
    start = complex(0, 0)

    # target = complex(10, 10)
    # depth = 510

    map_size = target + complex(50, 50)

    type_map = create_map(start, target, map_size, depth)
    return dijkstra(type_map, start, map_size, target)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
