def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def infinite_zeros():
    while True:
        yield 0


INPUTS = infinite_zeros()


def spring_droid(int_code):

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


def run_spring_droid_part_1(
        source_code_orig):
    global INPUTS
    input_str_array = [
        # spring_droid jumps 4 tiles
        # D need to be ground (D == true)

        # third tile (C) is hole and D is ground - can jump (first tile of next
        # island)
        'NOT C J\n',
        'AND D J\n',
        # next tile (A) is hole - need jump
        'NOT A T\n',
        'OR T J\n',
        'WALK\n'

    ]
    input_str = ''.join(input_str_array)
    INPUTS = (ord(c) for c in input_str)
    spring_droid_instance = spring_droid(source_code_orig[:])

    while True:
        try:
            yield next(spring_droid_instance)
        except StopIteration:
            return None


def part_1(inp):
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 5000
    hull_damage = list(run_spring_droid_part_1(source_code_orig))
    try:
        return ''.join([chr(c) for c in hull_damage])
    except ValueError:
        return hull_damage[-1]


def run_spring_droid_part_2(
        source_code_orig):
    global INPUTS
    input_str_array = [
        # spring_droid jumps 4 tiles
        # D need to be ground (D == true)

        # third tile (C) is hole and D is ground and eighth tile (H) is ground
        # - can double jump
        'NOT C J\n',
        'AND D J\n',
        'AND H J\n',
        # second tile (B) is hole and D is ground - can jump (first tile of
        # next island)
        'NOT B T\n',
        'AND D T\n',
        'OR T J\n',
        # next tile (A) is hole - need jump
        'NOT A T\n',
        'OR T J\n',
        'RUN\n'

    ]
    input_str = ''.join(input_str_array)
    INPUTS = (ord(c) for c in input_str)
    spring_droid_instance = spring_droid(source_code_orig[:])

    while True:
        try:
            yield next(spring_droid_instance)
        except StopIteration:
            return None


def part_2(inp):
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 5000
    hull_damage = list(run_spring_droid_part_2(source_code_orig))
    try:
        return ''.join([chr(c) for c in hull_damage])
    except ValueError:
        return hull_damage[-1]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
