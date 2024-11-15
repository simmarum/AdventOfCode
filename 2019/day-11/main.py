from copy import copy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def hull_painting_robot(int_code, input_register, canvas):

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
            INPUTS[input_register] = canvas.get(POSITIONS[input_register], 0)
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


def run_hull_painting_robot(
        source_code_orig, inp_reg, canvas, curr_point, max_iter):
    global INPUTS
    global POSITIONS
    dirs = {
        'U': complex(0, -1),
        'D': complex(0, 1),
        'L': complex(-1, 0),
        'R': complex(1, 0)
    }
    dirs_change = {
        # 0 left 90
        # 1 right 90
        dirs['U']: {
            0: dirs['L'],
            1: dirs['R'],
        },
        dirs['D']: {
            0: dirs['R'],
            1: dirs['L'],
        },
        dirs['L']: {
            0: dirs['D'],
            1: dirs['U'],
        },
        dirs['R']: {
            0: dirs['U'],
            1: dirs['D'],
        },
    }
    curr_dir = dirs['U']
    POSITIONS = [curr_point]
    hull_painting_robot_instance = hull_painting_robot(
        copy(source_code_orig),
        inp_reg,
        canvas)
    for _ in range(max_iter):
        try:
            paint_to_color = next(hull_painting_robot_instance)
            turn = next(hull_painting_robot_instance)
            canvas[curr_point] = paint_to_color
            curr_dir = dirs_change[curr_dir][turn]
            curr_point = curr_point + curr_dir
            POSITIONS[inp_reg] = curr_point
        except StopIteration:
            break
    else:
        return print(f"Loop all iteration... Please increase {max_iter=}")
    return len(canvas)


INPUTS = [0]
POSITIONS = [complex(0, 0)]


def part_1(inp):
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 1000
    curr_point = complex(0, 0)
    canvas = {curr_point: 0}
    inp_reg = 0
    max_iter = 100_000
    return run_hull_painting_robot(
        source_code_orig, inp_reg, canvas, curr_point, max_iter)


def print_canvas(canvas):
    min_x = min((int(p.real) for p in canvas.keys()))
    max_x = max((int(p.real) for p in canvas.keys()))
    min_y = min((int(p.imag) for p in canvas.keys()))
    max_y = max((int(p.imag) for p in canvas.keys()))
    canvas_str = ""
    for y in range(min_y, max_y + 1):
        canvas_str += "\n"
        for x in range(min_x, max_x + 1):
            if canvas.get(complex(x, y), 0) == 0:
                canvas_str += " "
            else:
                canvas_str += "#"
    print(canvas_str)


def part_2(inp):
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 1000
    curr_point = complex(0, 0)
    canvas = {curr_point: 1}
    inp_reg = 0
    max_iter = 100_000
    run_hull_painting_robot(
        source_code_orig, inp_reg, canvas, curr_point, max_iter)
    print_canvas(canvas)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
