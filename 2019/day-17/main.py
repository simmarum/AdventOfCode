from queue import Queue


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def infinite_zeros():
    while True:
        yield 0


INPUTS = infinite_zeros()


def ascii_droid(int_code):

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
            int_code[p1] = next(INPUTS)
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


def run_ascii_droid_for_screen(
        source_code_orig, max_iter):
    global INPUTS

    ascii_droid_instance = ascii_droid(source_code_orig[:])
    curr_pos = complex(0, 0)
    screen = {}
    for _ in range(max_iter):
        try:
            status = next(ascii_droid_instance)
            if status == 10:
                curr_pos = complex(0, curr_pos.imag + 1)
            else:
                screen[curr_pos] = status
                curr_pos += complex(1, 0)
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
        ord('#'): '#',
        ord('.'): '.',
        ord('<'): '<',
        ord('>'): '>',
        ord('v'): 'v',
        ord('^'): '^',
    }
    screen_str = ""
    for y in range(min_y, max_y + 1):
        screen_str += "\n"
        for x in range(min_x, max_x + 1):
            screen_str += graphic[screen.get(complex(x, y), -1)]
    print(screen_str)


def find_intersections(screen, wall_values):
    intersections = set()
    for k, v in screen.items():
        if v in wall_values:
            wall_ns = 0
            for n_diff in (complex(0, -1), complex(0, 1),
                           complex(1, 0), complex(-1, 0)):
                wall_ns += screen.get(k + n_diff, -1) in wall_values
            if wall_ns == 4:
                intersections.add(k)
    return intersections


def part_1(inp):
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 5000
    max_iter = 10000
    screen = run_ascii_droid_for_screen(
        source_code_orig, max_iter)
    intersections = find_intersections(screen, wall_values=[ord('#')])
    return sum((int(p.real * p.imag) for p in intersections))


def maze_find_path_goes_straight(maze, curr_point, curr_dir, exit_point,
                                 path, wall_values):
    """Find exit in maze - on intersection go straight (maze as dictionary as complex numbers)

    Args:
        maze (dict): {complex(0,0):0}
        curr_point (complex): start of the maze
        curr_dir (str): direction in maze U/D/L/R
        exit_point (complex): exit of the maze
        path (list): list where path will be store in format of dir,number ([R,8,L,7,...])
        wall_values (list<int>): value of walls values (cannot travel there)

    Returns:
        paths (list<path>)
    """

    wall_values_str = [chr(c) for c in wall_values]
    dirs_maze = {
        ord('^'): 'U',
        ord('v'): 'D',
        ord('<'): 'L',
        ord('>'): 'R',
    }
    dirs = {
        'U': complex(0, -1),
        'D': complex(0, 1),
        'L': complex(-1, 0),
        'R': complex(1, 0),
    }
    dirs_inv = {v: k for k, v in dirs.items()}
    dirs_change = {
        dirs['U']: {
            'L': dirs['L'],
            'R': dirs['R'],
            'S': dirs['U']
        },
        dirs['D']: {
            'L': dirs['R'],
            'R': dirs['L'],
            'S': dirs['D']
        },
        dirs['L']: {
            'L': dirs['D'],
            'R': dirs['U'],
            'S': dirs['L']
        },
        dirs['R']: {
            'L': dirs['U'],
            'R': dirs['D'],
            'S': dirs['R']
        },
    }
    if curr_dir is None:
        curr_dir = dirs_maze[maze[curr_point]]

    q = Queue()
    q.put((curr_point, curr_dir, path))

    while not q.empty():
        c_point, c_dir, c_path = q.get()
        # print(f"{c_point=}, {c_dir=}, {c_path=}, {q.qsize()}")  # noqa
        if c_point == exit_point:
            yield c_path
            continue

        n_point_l = c_point + dirs_change[dirs[c_dir]]['L']
        n_point_s = c_point + dirs_change[dirs[c_dir]]['S']
        n_point_r = c_point + dirs_change[dirs[c_dir]]['R']
        n_l = (n_point_l in maze) and (
            chr(maze[n_point_l]) not in wall_values_str)
        n_s = (n_point_s in maze) and (
            chr(maze[n_point_s]) not in wall_values_str)
        n_r = (n_point_r in maze) and (
            chr(maze[n_point_r]) not in wall_values_str)

        if sum((n_l, n_s, n_r)) == 1:
            if n_l:
                q.put((n_point_l, dirs_inv[dirs_change[dirs[c_dir]]['L']], [*c_path, 'L', 1]))  # noqa
            if n_r:
                q.put((n_point_r, dirs_inv[dirs_change[dirs[c_dir]]['R']], [*c_path, 'R', 1]))  # noqa
        if n_s:
            q.put((n_point_s, dirs_inv[dirs_change[dirs[c_dir]]['S']], [*c_path[:-1], c_path[-1] + 1]))  # noqa


def find_start_exit_points(screen, wall_values, robot_values):
    start_point = None
    exit_point = None
    for k, v in screen.items():
        if v in wall_values:
            wall_ns = 0
            for n_diff in (complex(0, -1), complex(0, 1),
                           complex(1, 0), complex(-1, 0)):
                wall_ns += screen.get(k + n_diff, -
                                      1) in wall_values + robot_values
            if wall_ns == 1:
                exit_point = k
        elif v in robot_values:
            start_point = k
    return start_point, exit_point


def find_routines_from_path(path):
    path_str = ''.join([str(c) for c in path])
    for a_len in range(1, 5):
        ari = 0
        arj = a_len * 2
        a_routine = path[ari:arj]
        a_routine_str = ''.join([str(c) for c in a_routine])
        for b_len in range(1, 5):
            bri = arj
            brj = arj + b_len * 2
            b_routine = path[bri:brj]
            b_routine_str = ''.join([str(c) for c in b_routine])
            for c_len in range(1, 5):
                cri = brj
                crj = brj + c_len * 2
                while True:
                    c_routine = path[cri:crj]
                    c_routine_str = ''.join([str(c) for c in c_routine])
                    if c_routine == a_routine:
                        cri += len(a_routine)
                        crj += len(a_routine)
                    elif c_routine == b_routine:
                        cri += len(b_routine)
                        crj += len(b_routine)
                    else:
                        break
                path_str_routines = path_str.replace(
                    a_routine_str,
                    'A').replace(
                    b_routine_str,
                    'B').replace(
                    c_routine_str,
                    'C')
                if len(set(path_str_routines)) <= 3:
                    return path_str_routines, a_routine, b_routine, c_routine
    return "", [], [], []


def translate_routines_for_ascii_droid(
        routines, routine_a, routine_b, routine_c):
    routines = ','.join(list(routines))
    routine_a = ','.join([str(c) for c in routine_a])
    routine_b = ','.join([str(c) for c in routine_b])
    routine_c = ','.join([str(c) for c in routine_c])
    routines_len = len(routines)
    routine_a_len = len(routine_a)
    routine_b_len = len(routine_b)
    routine_c_len = len(routine_c)
    if max((routines_len, routine_a_len, routine_b_len, routine_c_len)) > 20:
        RuntimeError("Some routine is more than 20 characters...")
    routines = [ord(c) for c in routines] + [ord('\n')]
    routine_a = [ord(c) for c in routine_a] + [ord('\n')]
    routine_b = [ord(c) for c in routine_b] + [ord('\n')]
    routine_c = [ord(c) for c in routine_c] + [ord('\n')]
    return routines, routine_a, routine_b, routine_c


def run_ascii_droid_for_dust(
        source_code_orig, max_iter):
    global INPUTS
    source_code_orig[0] = 2
    ascii_droid_instance = ascii_droid(source_code_orig[:])
    dust_collected_or_trash = None
    for _ in range(max_iter):
        try:
            dust_collected_or_trash = next(ascii_droid_instance)
        except StopIteration:
            return dust_collected_or_trash
    else:
        print(f"Loop all iteration... Please increase {max_iter=}")
        return 0


def part_2(inp):
    global INPUTS
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 5000
    max_iter = 10000
    screen = run_ascii_droid_for_screen(
        source_code_orig, max_iter)

    start_point, exit_point = find_start_exit_points(
        screen, [ord('#')], [ord('<'), ord('^'), ord('v'), ord('>')])
    paths = list(maze_find_path_goes_straight(
        maze=screen,
        curr_point=start_point,
        curr_dir=None,
        exit_point=exit_point,
        path=[],
        wall_values=[ord('.')]))
    if len(paths) > 1:
        RuntimeError("Found more than one path... something is wrong(?)")
    path = paths[0]
    routines, routine_a, routine_b, routine_c = find_routines_from_path(path)
    routines, routine_a, routine_b, routine_c = translate_routines_for_ascii_droid(routines, routine_a, routine_b, routine_c)  # noqa

    not_to_video_feed = [ord('n'), ord('\n')]
    droid_inputs = routines + routine_a + routine_b + routine_c + not_to_video_feed
    INPUTS = (x for x in droid_inputs)

    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 5000
    max_iter = 10000
    dust_collected = run_ascii_droid_for_dust(
        source_code_orig, max_iter)
    return dust_collected


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
