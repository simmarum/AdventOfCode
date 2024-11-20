from math import atan2, degrees


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def infinite_zeros():
    while True:
        yield 0


INPUTS = infinite_zeros()


def deploy_drone(int_code):

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


def run_deploy_drone_for_screen(
        source_code_orig, screen_size, beam_degree_min, beam_degree_max):
    global INPUTS
    positions = []
    for y in range(screen_size):
        for x in range(screen_size):
            if (x, y) == (0, 0):
                positions.append((x, y))
            elif beam_degree_min <= degrees(atan2(x, y)) <= beam_degree_max:
                positions.append((x, y))

    def gen_x_y(positions):
        for x, y in positions:
            yield x
            yield y
    INPUTS = gen_x_y(positions)

    screen = {}
    for x, y in positions:
        try:
            deploy_drone_instance = deploy_drone(source_code_orig[:])
            status = next(deploy_drone_instance)
            screen[complex(x, y)] = status
        except StopIteration:
            break
    return screen


def run_deploy_drone_for_fitting_square(
        source_code_orig, start_x, start_y, square_size):
    global INPUTS
    x = start_x
    y = start_y
    while True:
        try:
            INPUTS = (p for p in (x, y))
            deploy_drone_instance = deploy_drone(source_code_orig[:])
            status = next(deploy_drone_instance)
            if status == 1:
                new_x = x - (square_size - 1)
                new_y = y + (square_size - 1)
                if new_x > 0 and new_y > 0:
                    INPUTS = (p for p in (new_x, new_y))
                    deploy_drone_instance = deploy_drone(source_code_orig[:])
                    status = next(deploy_drone_instance)
                    if status == 1:
                        return min(x, new_x), min(y, new_y)
                x += 1
            if status == 0:
                y += 1

        except StopIteration:
            break
    return 0, 0


def print_screen(screen):
    min_x = min((int(p.real) for p in screen.keys()))
    max_x = max((int(p.real) for p in screen.keys()))
    min_y = min((int(p.imag) for p in screen.keys()))
    max_y = max((int(p.imag) for p in screen.keys()))
    graphic = {
        -1: '?',
        0: '.',
        1: '#',
    }
    screen_str = ""
    for y in range(min_y, max_y + 1):
        screen_str += "\n"
        for x in range(min_x, max_x + 1):
            screen_str += graphic[screen.get(complex(x, y), -1)]
    print(screen_str)


def part_1(inp):
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 5000
    screen_size = 50
    screen = run_deploy_drone_for_screen(
        source_code_orig, screen_size, 25, 38)
    return sum(screen.values())


def part_2(inp):
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 5000
    square_size = 100
    screen_size = 15
    screen = run_deploy_drone_for_screen(
        source_code_orig, screen_size, 25, 38)
    max_y = screen_size - 1
    max_x = max(
        (int(
            k.real) for k, v in screen.items() if int(
            k.imag) == max_y and v == 1))
    min_x = min(
        (int(
            k.real) for k, v in screen.items() if int(
            k.imag) == max_y and v == 1))
    base_ratio = 100
    while max_x - min_x < square_size * 0.75:
        new_min_x = int(base_ratio * (min_x / max_y))
        new_max_x = int(base_ratio * (max_x / max_y))
        new_max_y = int((max_y * new_max_x) / max_x)
        min_x = new_min_x
        max_x = new_max_x
        max_y = new_max_y
        base_ratio += 10
    x, y = run_deploy_drone_for_fitting_square(
        source_code_orig, max_x, max_y, square_size)

    return x * 10_000 + y


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
