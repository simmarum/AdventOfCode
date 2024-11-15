from copy import copy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def arcade_cabinet(int_code, input_register):

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


def run_arcade_cabinet(
        source_code_orig, inp_reg, put_quarter, max_iter):
    global INPUTS
    if put_quarter:
        source_code_orig[0] = 2

    arcade_cabinet_instance = arcade_cabinet(
        copy(source_code_orig),
        inp_reg)
    screen = {}
    paddle_pos = None
    ball_pos = None
    max_score = 0
    INPUTS = [0]
    for _ in range(max_iter):
        try:
            x = next(arcade_cabinet_instance)
            y = next(arcade_cabinet_instance)
            tile_id = next(arcade_cabinet_instance)
            if (x, y) == (-1, 0):
                max_score = max(max_score, tile_id)
            else:
                screen[complex(x, y)] = tile_id
            if tile_id == 3:
                paddle_pos = complex(x, y)
            if tile_id == 4:
                ball_pos = complex(x, y)
                if paddle_pos and ball_pos:
                    if paddle_pos.real < ball_pos.real:
                        INPUTS[inp_reg] = 1
                    elif paddle_pos.real > ball_pos.real:
                        INPUTS[inp_reg] = -1
                    else:
                        INPUTS[inp_reg] = 0

        except StopIteration:
            break
    else:
        print(f"Loop all iteration... Please increase {max_iter=}")
        return None, None
    return sum([1 for p in screen.values() if p == 2]), max_score


INPUTS = [0]
POSITIONS = [complex(0, 0)]


def part_1(inp):
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 1000
    inp_reg = 0
    max_iter = 100_000
    block_cnt, _ = run_arcade_cabinet(
        source_code_orig, inp_reg, False, max_iter)
    return block_cnt


def print_screen(screen):
    min_x = min((int(p.real) for p in screen.keys()))
    max_x = max((int(p.real) for p in screen.keys()))
    min_y = min((int(p.imag) for p in screen.keys()))
    max_y = max((int(p.imag) for p in screen.keys()))
    graphic = {
        0: ' ',
        1: '#',
        2: '*',
        3: '-',
        4: 'o'
    }
    screen_str = ""
    for y in range(min_y, max_y + 1):
        screen_str += "\n"
        for x in range(min_x, max_x + 1):
            screen_str += graphic[screen.get(complex(x, y), 0)]
    print(screen_str)


def part_2(inp):
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 1000
    inp_reg = 0
    max_iter = 100_000
    _, max_score = run_arcade_cabinet(
        source_code_orig, inp_reg, True, max_iter)
    return max_score


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
