from queue import Queue, Empty
from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


INPUTS = defaultdict(Queue)


def nic_computer(int_code, inp_reg):

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
            tmp_inp = -1
            try:
                tmp_inp = INPUTS[inp_reg].get_nowait()
            except Empty:
                tmp_inp = -1
            int_code[p1] = tmp_inp
            yield None
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


def run_nic_computer(
        source_code_orig, nic_cnt):
    global INPUTS

    nics = []
    for nic_num in range(nic_cnt):
        INPUTS[nic_num].put(nic_num)
        nics.append(nic_computer(source_code_orig[:], nic_num))
    while True:
        for nic in nics:
            dest_add = next(nic)
            if dest_add is None:
                continue
            x = next(nic)
            y = next(nic)
            # print(f"{dest_add=}, {x=}, {y=}")
            if dest_add == 255:
                return x, y

            INPUTS[dest_add].put(x)
            INPUTS[dest_add].put(y)


def part_1(inp):
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 5000
    nic_cnt = 50
    x, y = run_nic_computer(
        source_code_orig, nic_cnt)
    return y


def run_nic_computer_with_nat(
        source_code_orig, nic_cnt, max_iter):
    global INPUTS

    nics = []
    nat_x = None
    nat_y = None
    nat_y_last_sent = None

    for nic_num in range(nic_cnt):
        INPUTS[nic_num].put(nic_num)
        nics.append(nic_computer(source_code_orig[:], nic_num))
    idle_state_cnt = 0
    for _ in range(max_iter):
        for nic_num, nic in enumerate(nics):
            dest_add = next(nic)
            if dest_add is None:
                continue
            x = next(nic)
            y = next(nic)
            if dest_add == 255:
                nat_x = x
                nat_y = y
            else:
                INPUTS[dest_add].put(x)
                INPUTS[dest_add].put(y)

        if all([q.qsize() == 0 for q in INPUTS.values()]):
            idle_state_cnt += 1
            if idle_state_cnt > 2:
                INPUTS[0].put(nat_x)
                INPUTS[0].put(nat_y)
                if nat_y_last_sent == nat_y:
                    return nat_x, nat_y
                nat_y_last_sent = nat_y
        else:
            idle_state_cnt = 0
    return None, None


def part_2(inp):
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 5000
    nic_cnt = 50
    max_iter = 1000
    x, y = run_nic_computer_with_nat(
        source_code_orig, nic_cnt, max_iter)
    return y


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
