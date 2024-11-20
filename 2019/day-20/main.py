from collections import defaultdict
import networkx as nx


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.readlines()]


def get_maze(inp):
    maze = {}
    for y, row in enumerate(inp):
        for x, elem in enumerate(row):
            maze[complex(x, y)] = elem.replace(' ', '#')
    return maze


def create_graph(maze):
    neighbors = [complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0)]
    g = nx.Graph()
    portals = defaultdict(list)
    start_pos = None
    end_pos = None
    for curr_pos, curr_val in maze.items():
        if curr_val.isupper():
            curr_pos_neighbors = [curr_pos + n_diff for n_diff in neighbors if maze.get(curr_pos + n_diff, '#') != '#']  # noqa
            if len(curr_pos_neighbors) == 2:
                if maze.get(curr_pos_neighbors[0]).isupper():
                    char_pos, tile_pos = curr_pos_neighbors
                else:
                    tile_pos, char_pos = curr_pos_neighbors
                portal_name = curr_val + \
                    maze[char_pos] if curr_val < maze[char_pos] else maze[char_pos] + curr_val
                portals[portal_name].append(tile_pos)
                if portal_name == 'AA':
                    start_pos = tile_pos
                elif portal_name == 'ZZ':
                    end_pos = tile_pos
        elif curr_val == '.':
            [g.add_edge(curr_pos, curr_pos + n_diff) for n_diff in neighbors if maze.get(curr_pos + n_diff, '#') == '.']  # noqa
    [g.add_edge(portal_teleports[0], portal_teleports[1]) for portal_teleports in portals.values() if len(portal_teleports) == 2]  # noqa
    return g, start_pos, end_pos


def part_1(inp):
    maze = get_maze(inp)
    g, start_pos, end_pos = create_graph(maze)
    return nx.shortest_path_length(g, start_pos, end_pos)


def create_graph_with_lvls(maze, max_lvl):
    neighbors = [complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0)]
    max_real = max([k.real for k in maze.keys()])
    max_imag = max([k.imag for k in maze.keys()])
    g = nx.Graph()
    portals = defaultdict(list)
    start_pos = None
    end_pos = None
    for curr_pos, curr_val in maze.items():
        if curr_val.isupper():
            curr_pos_neighbors = [curr_pos + n_diff for n_diff in neighbors if maze.get(curr_pos + n_diff, '#') != '#']  # noqa
            if len(curr_pos_neighbors) == 2:
                if maze.get(curr_pos_neighbors[0]).isupper():
                    char_pos, tile_pos = curr_pos_neighbors
                else:
                    tile_pos, char_pos = curr_pos_neighbors
                portal_name = curr_val + \
                    maze[char_pos] if curr_val < maze[char_pos] else maze[char_pos] + curr_val
                portals[portal_name].append(tile_pos)
                if portal_name == 'AA':
                    start_pos = tile_pos
                elif portal_name == 'ZZ':
                    end_pos = tile_pos
        elif curr_val == '.':
            for lvl in range(max_lvl):
                g.add_node((curr_pos, lvl))
                [g.add_edge((curr_pos, lvl), (curr_pos + n_diff, lvl)) for n_diff in neighbors if maze.get(curr_pos + n_diff, '#') == '.']  # noqa
    for portal_teleports in portals.values():
        if len(portal_teleports) == 2:
            if portal_teleports[0].real in (2, max_real - 2):
                teleport_out_pos, teleport_in_pos = portal_teleports
            elif portal_teleports[0].imag in (2, max_imag - 2):
                teleport_out_pos, teleport_in_pos = portal_teleports
            else:
                teleport_in_pos, teleport_out_pos = portal_teleports
            for lvl in range(max_lvl - 1):
                g.add_edge((teleport_in_pos, lvl), (teleport_out_pos, lvl + 1))
                g.add_edge((teleport_out_pos, lvl + 1), (teleport_in_pos, lvl))
    return g, start_pos, end_pos


def part_2(inp):
    maze = get_maze(inp)
    g, start_pos, end_pos = create_graph_with_lvls(maze, max_lvl=26)
    return nx.shortest_path_length(g, (start_pos, 0), (end_pos, 0))


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
