from collections import deque

DIRECTIONS = {
    '>': ((1, 0),),
    '<': ((-1, 0),),
    '^': ((0, -1),),
    'v': ((0, 1),),
    '.': ((1, 0), (-1, 0), (0, 1), (0, -1)),
}


def get_neighbors(position, trail_map, slopes=True):
    width = len(trail_map[0])
    height = len(trail_map)
    x, y = position
    for dx, dy in DIRECTIONS[trail_map[y][x] if slopes else '.']:
        new_x, new_y = x + dx, y + dy
        if (0 <= new_x < width) and (0 <= new_y < height) and (
                trail_map[new_y][new_x] != '#'):
            yield new_x, new_y


def get_graph(trail_map, start_vertex, slopes=True):
    vertices = [start_vertex]
    visited = set()
    graph = {}
    while vertices:
        vertex = vertices.pop()
        if vertex in visited:
            continue
        graph[vertex] = []
        for next_step in get_neighbors(vertex, trail_map, slopes):
            length = 1
            prev = vertex
            position = next_step
            dead_end = False
            while True:
                neighbors = list(get_neighbors(position, trail_map, slopes))
                if neighbors == [
                        prev] and trail_map[position[1]][position[0]] in '<>^v':
                    dead_end = True
                    break
                if len(neighbors) != 2:
                    break
                for neighbor in neighbors:
                    if neighbor != prev:
                        length += 1
                        prev = position
                        position = neighbor
                        break
            if dead_end:
                continue
            graph[vertex].append((position, length))
            vertices.append(position)
        visited.add(vertex)
    return graph


def iter_hike_lengths(graph, goal):
    start = (1, 0)
    stack = deque([(start, 0, {start})])
    while stack:
        last, length, visited = stack.popleft()
        if last == goal:
            yield length
            continue
        for new, edge_length in graph[last]:
            if new not in visited:
                stack.appendleft((new, length + edge_length, visited | {new}))


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    start_vertex = (1, 0)
    end_vertex = (len(inp[0]) - 2, len(inp) - 1)
    graph = get_graph(inp, start_vertex, True)
    return max(iter_hike_lengths(graph, end_vertex))


def part_2(inp):
    start_vertex = (1, 0)
    end_vertex = (len(inp[0]) - 2, len(inp) - 1)
    graph = get_graph(inp, start_vertex, False)
    return max(iter_hike_lengths(graph, end_vertex))
    return


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
