import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def read_data(inp):
    grid = {}
    empty = None
    for line in inp:
        m = re.match(
            '/dev/grid/node-x(\\d+)-y(\\d+) +(\\d+)T +(\\d+)T +(\\d+)T +(\\d+)%',
            line)
        if m:
            grid[(int(m.group(1)), int(m.group(2)))] = {
                'size': int(m.group(3)),
                'used': int(m.group(4)),
                'avail': int(m.group(5)),
                'use': int(m.group(6)),
            }
            if int(m.group(4)) == 0:
                empty = (int(m.group(1)), int(m.group(2)))
    max_x = max([x[0] for x in grid.keys()])
    max_y = max([x[1] for x in grid.keys()])
    return grid, empty, max_x, max_y


def part_1(inp):
    viable_pairs = 0
    grid, _, _, _ = read_data(inp)
    for k1, v1 in grid.items():
        for k2, v2 in grid.items():
            if k1 == k2:
                continue
            if (v1['used'] > 0) and (v1['used'] <= v2['avail']):
                viable_pairs += 1
    return viable_pairs


def solve(start, end, grid, max_x, max_y, obst=None):
    for value in grid.values():
        value['distance'] = 1_000_000
        value['previous'] = None

    queue = [start]
    grid[start]['distance'] = 0
    while len(queue) > 0:
        n = queue.pop(0)
        for dirx, diry in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = n[0] + dirx
            ny = n[1] + diry

            if (0 <= nx <= max_x) and (0 <= ny <= max_y) and (
                    grid[(nx, ny)]['used'] < 100) and ((nx, ny) != obst):
                if grid[(nx, ny)]['distance'] > grid[n]['distance'] + 1:
                    grid[(nx, ny)]['distance'] = grid[n]['distance'] + 1
                    grid[(nx, ny)]['previous'] = n
                    queue.append((nx, ny))
                if (nx, ny) == end:
                    path = [(nx, ny)]
                    while grid[path[-1]]['previous'] is not None:
                        path.append(grid[path[-1]]['previous'])
                    return path[-2::-1]


def part_2(inp):
    grid, empty, max_x, max_y = read_data(inp)
    end = (max_x, 0)
    start = (0, 0)
    shortest_path = solve(end, start, grid, max_x, max_y)
    cnt = 0
    while start != end:
        path = solve(empty, shortest_path.pop(0), grid, max_x, max_y, obst=end)
        cnt += (len(path) + 1)
        empty = end
        end = path[-1]

    return cnt


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
