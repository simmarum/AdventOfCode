from copy import copy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def run_Intcode(int_code, amp_num):
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
            int_code[p1] = INPUTS[amp_num]
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


INPUTS = [0]


def part_1(inp):
    global INPUTS
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 100

    INPUTS = [1]
    output = list(run_Intcode(copy(source_code_orig), 0))
    return output


def part_2(inp):
    global INPUTS
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 150

    INPUTS = [2]
    output = list(run_Intcode(copy(source_code_orig), 0))
    return output


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
