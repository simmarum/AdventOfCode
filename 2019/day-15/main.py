import heapq
from queue import Queue
from copy import copy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


INPUTS = [0]


def repair_droid(int_code, input_register):

    def _mode_dec_r(int_code, mode, value, relative_base):
        if mode == '0':
            return int_code[value]
        elif mode == '1':
            return value
        elif mode == '2':
            return int_code[value + relative_base]
        else:
            raise RuntimeError(f"Wrong {mode=}")

    def _mode_dec_w(mode, value, relative_base):
        if mode == '0':
            return value
        elif mode == '2':
            return value + relative_base
        else:
            raise RuntimeError(f"Wrong {mode=}")

    relative_base = 0
    ip = 0
    while True:
        opp_code = int_code[ip]
        opp_code_str = f"{opp_code:05d}"
        opp_code = int(opp_code_str[-2:])
        ip_inc = 0
        if opp_code == 1:
            a, b, c = int_code[ip + 1], int_code[ip + 2], int_code[ip + 3]
            ip_inc = 4
            p1 = _mode_dec_r(int_code, opp_code_str[-3], a, relative_base)
            p2 = _mode_dec_r(int_code, opp_code_str[-4], b, relative_base)
            p3 = _mode_dec_w(opp_code_str[-5], c, relative_base)
            int_code[p3] = p1 + p2
        elif opp_code == 2:
            a, b, c = int_code[ip + 1], int_code[ip + 2], int_code[ip + 3]
            ip_inc = 4
            p1 = _mode_dec_r(int_code, opp_code_str[-3], a, relative_base)
            p2 = _mode_dec_r(int_code, opp_code_str[-4], b, relative_base)
            p3 = _mode_dec_w(opp_code_str[-5], c, relative_base)
            int_code[p3] = p1 * p2
        elif opp_code == 3:
            a = int_code[ip + 1]
            ip_inc = 2
            p1 = _mode_dec_w(opp_code_str[-3], a, relative_base)
            int_code[p1] = INPUTS[input_register]
        elif opp_code == 4:
            a = int_code[ip + 1]
            ip_inc = 2
            yield _mode_dec_r(int_code, opp_code_str[-3], a, relative_base)
        elif opp_code == 5:
            a, b = int_code[ip + 1], int_code[ip + 2]
            ip_inc = 3
            p1 = _mode_dec_r(int_code, opp_code_str[-3], a, relative_base)
            p2 = _mode_dec_r(int_code, opp_code_str[-4], b, relative_base)
            if p1 != 0:
                ip = p2
                ip_inc = 0
        elif opp_code == 6:
            a, b = int_code[ip + 1], int_code[ip + 2]
            ip_inc = 3
            p1 = _mode_dec_r(int_code, opp_code_str[-3], a, relative_base)
            p2 = _mode_dec_r(int_code, opp_code_str[-4], b, relative_base)
            if p1 == 0:
                ip = p2
                ip_inc = 0
        elif opp_code == 7:
            a, b, c = int_code[ip + 1], int_code[ip + 2], int_code[ip + 3]
            ip_inc = 4
            p1 = _mode_dec_r(int_code, opp_code_str[-3], a, relative_base)
            p2 = _mode_dec_r(int_code, opp_code_str[-4], b, relative_base)
            p3 = _mode_dec_w(opp_code_str[-5], c, relative_base)
            int_code[p3] = int(p1 < p2)
        elif opp_code == 8:
            a, b, c = int_code[ip + 1], int_code[ip + 2], int_code[ip + 3]
            ip_inc = 4
            p1 = _mode_dec_r(int_code, opp_code_str[-3], a, relative_base)
            p2 = _mode_dec_r(int_code, opp_code_str[-4], b, relative_base)
            p3 = _mode_dec_w(opp_code_str[-5], c, relative_base)
            int_code[p3] = int(p1 == p2)
        elif opp_code == 9:
            a = int_code[ip + 1]
            ip_inc = 2
            p1 = _mode_dec_r(int_code, opp_code_str[-3], a, relative_base)
            relative_base += p1

        elif opp_code == 99:
            ip_inc = 1
            # raise StopIteration()
            break
        else:
            raise RuntimeError(f"Found new {opp_code=}")
        ip += ip_inc


def run_repair_droid(
        source_code_orig, inp_reg, hug_left_wall, max_iter):
    global INPUTS

    repair_droid_instance = repair_droid(
        copy(source_code_orig),
        inp_reg)
    curr_pos = complex(0, 0)
    screen = {curr_pos: 99}
    dirs = {
        1: complex(0, -1),
        4: complex(1, 0),
        2: complex(0, 1),
        3: complex(-1, 0),
    }
    if hug_left_wall:
        dir_order = [1, 4, 2, 3]
    else:
        dir_order = [1, 3, 2, 4]
    curr_dir_id = 0
    INPUTS = [dir_order[curr_dir_id]]
    for _ in range(max_iter):
        try:
            status = next(repair_droid_instance)
            if status == 0:
                screen[curr_pos + dirs[INPUTS[inp_reg]]] = 0
                curr_dir_id = (curr_dir_id + 1) % 4
                INPUTS[inp_reg] = dir_order[curr_dir_id]
            elif status == 1:
                screen[curr_pos + dirs[INPUTS[inp_reg]]] = 1
                curr_pos += dirs[INPUTS[inp_reg]]
                curr_dir_id = (curr_dir_id - 1) % 4
                INPUTS[inp_reg] = dir_order[curr_dir_id]
            elif status == 2:
                screen[curr_pos + dirs[INPUTS[inp_reg]]] = 2
                curr_pos += dirs[dir_order[curr_dir_id]]
                break
        except StopIteration:
            break
    else:
        print(f"Loop all iteration... Please increase {max_iter=}")
        return {}
    return screen


def print_screen(screen):
    min_x = min((int(p.real) for p in screen.keys()))
    max_x = max((int(p.real) for p in screen.keys()))
    min_y = min((int(p.imag) for p in screen.keys()))
    max_y = max((int(p.imag) for p in screen.keys()))
    graphic = {
        -1: ' ',
        0: '#',
        1: '.',
        2: 'E',
        99: 'S'
    }
    screen_str = ""
    for y in range(min_y, max_y + 1):
        screen_str += "\n"
        for x in range(min_x, max_x + 1):
            screen_str += graphic[screen.get(complex(x, y), -1)]
    print(screen_str)


def astar_dict(maze, start_value, goal_value, with_diagonal, wall_values):
    """Find shortest path in maze (maze as dictionary as complex numbers)

    Args:
        maze (dict): {complex(0,0):0}
        start_value (int): value of start point
        goal_value (int): value of start point
        with_diagonal (bool, optional): If True use Euclidean else Manhattan. Defaults to False.
        wall_values (list<int>): value of walls values (cannot travel there)

    Returns:
        list<complex>: Path from start to goal.
    """
    if with_diagonal:
        neighbors_diff = [complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0),
                          complex(1, 1), complex(1, -1), complex(-1, 1), complex(-1, -1)]

        def f_func(a, b): return ((b.real - a.real)
                                  ** 2 + (b.imag - a.imag) ** 2)**0.5
    else:
        neighbors_diff = [complex(0, 1), complex(
            0, -1), complex(1, 0), complex(-1, 0)]

        def f_func(a, b): return abs(b.real - a.real) + abs((b.imag - a.imag))

    start = [k for k, v in maze.items() if v == start_value][0]
    goal = [k for k, v in maze.items() if v == goal_value][0]

    close_set = set()
    came_from = {}
    g_score = {start: 0}
    f_score = {start: f_func(start, goal)}
    queue_heap = []
    heapq.heappush(queue_heap, (f_score[start], (start.real, start.imag)))
    while queue_heap:
        current = complex(*heapq.heappop(queue_heap)[1])
        if current == goal:
            route = []
            while current in came_from:
                route.append(current)
                current = came_from[current]
            route = route + [start]
            route = route[::-1]
            return route

        close_set.add(current)
        for n_diff in neighbors_diff:
            neighbor = current + n_diff
            tent_g_score = g_score[current] + f_func(current, neighbor)
            if neighbor not in maze:
                continue
            elif maze[neighbor] in wall_values:
                continue
            elif (neighbor in close_set) and (
                    tent_g_score >= g_score.get(neighbor, 0)):
                continue

            if tent_g_score < g_score.get(neighbor, 0) or neighbor not in [
                    qh[1] for qh in queue_heap]:
                came_from[neighbor] = current
                g_score[neighbor] = tent_g_score
                f_score[neighbor] = tent_g_score + f_func(neighbor, goal)
                heapq.heappush(
                    queue_heap, (f_score[neighbor], (neighbor.real, neighbor.imag)))
    return []


def get_full_screen(source_code_orig, inp_reg, max_iter):
    screen = run_repair_droid(
        source_code_orig, inp_reg, True, max_iter)
    screen_right = run_repair_droid(
        source_code_orig, inp_reg, False, max_iter)
    screen.update(screen_right)
    return screen


def part_1(inp):
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 1000
    inp_reg = 0
    max_iter = 10000
    screen = get_full_screen(source_code_orig, inp_reg, max_iter)
    shortest_path = astar_dict(
        maze=screen,
        start_value=99,
        goal_value=2,
        with_diagonal=False,
        wall_values=[0]
    )
    return len(shortest_path) - 1


def bfs_dict_max_depth(maze, start_value,
                       with_diagonal, wall_values):
    """Find maximum depth in maze (maze as dictionary as complex numbers)

    Args:
        maze (dict): {complex(0,0):0}
        start_value (int): value of start point
        with_diagonal (bool, optional): If True use Euclidean else Manhattan. Defaults to False.
        wall_values (list<int>): value of walls values (cannot travel there)

    Returns:
        int: Maximum depth.
    """
    if with_diagonal:
        neighbors_diff = [complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0),  # noqa
                          complex(1, 1), complex(1, -1), complex(-1, 1), complex(-1, -1)]  # noqa
    else:
        neighbors_diff = [complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0)]  # noqa

    start = [k for k, v in maze.items() if v == start_value][0]

    queue = Queue()
    queue.put((start, 0))
    visited = {}

    while not queue.empty():
        current, depth = queue.get()
        visited[current] = depth

        for n_diff in neighbors_diff:
            neighbor = current + n_diff
            if neighbor not in maze:
                continue
            elif maze[neighbor] in wall_values:
                continue
            elif neighbor in visited:
                continue
            queue.put((neighbor, depth + 1))
    return max(visited.values())


def part_2(inp):
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 1000
    inp_reg = 0
    max_iter = 10000
    screen = get_full_screen(source_code_orig, inp_reg, max_iter)
    max_depth = bfs_dict_max_depth(
        maze=screen,
        start_value=2,
        with_diagonal=False,
        wall_values=[0]
    )
    return max_depth


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
