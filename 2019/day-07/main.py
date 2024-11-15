from copy import copy
from itertools import permutations


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def run_Intcode(int_code, phase, amp_num):
    ip = 0
    is_phase_read = False
    while True:
        opp_code = int_code[ip]
        opp_code_str = f"{opp_code:09d}"
        opp_code = int(opp_code_str[-2:])
        ip_inc = 0
        if opp_code == 1:
            a, b, c = int_code[ip + 1:ip + 4]
            ip_inc = 4
            p1 = int_code[a] if opp_code_str[-3] == '0' else a
            p2 = int_code[b] if opp_code_str[-4] == '0' else b
            int_code[c] = p1 + p2
        elif opp_code == 2:
            a, b, c = int_code[ip + 1:ip + 4]
            ip_inc = 4
            p1 = int_code[a] if opp_code_str[-3] == '0' else a
            p2 = int_code[b] if opp_code_str[-4] == '0' else b
            int_code[c] = p1 * p2
        elif opp_code == 3:
            a = int_code[ip + 1:ip + 2][0]
            ip_inc = 2
            if not is_phase_read:
                int_code[a] = phase
                is_phase_read = True
            else:
                int_code[a] = INPUTS[amp_num]
        elif opp_code == 4:
            a = int_code[ip + 1:ip + 2][0]
            ip_inc = 2
            yield int_code[a] if opp_code_str[-3] == '0' else a
        elif opp_code == 5:
            a, b = int_code[ip + 1:ip + 3]
            ip_inc = 3
            p1 = int_code[a] if opp_code_str[-3] == '0' else a
            p2 = int_code[b] if opp_code_str[-4] == '0' else b
            if p1 != 0:
                ip = p2
                ip_inc = 0
        elif opp_code == 6:
            a, b = int_code[ip + 1:ip + 3]
            ip_inc = 3
            p1 = int_code[a] if opp_code_str[-3] == '0' else a
            p2 = int_code[b] if opp_code_str[-4] == '0' else b
            if p1 == 0:
                ip = p2
                ip_inc = 0
        elif opp_code == 7:
            a, b, c = int_code[ip + 1:ip + 4]
            ip_inc = 4
            p1 = int_code[a] if opp_code_str[-3] == '0' else a
            p2 = int_code[b] if opp_code_str[-4] == '0' else b
            int_code[c] = int(p1 < p2)
        elif opp_code == 8:
            a, b, c = int_code[ip + 1:ip + 4]
            ip_inc = 4
            p1 = int_code[a] if opp_code_str[-3] == '0' else a
            p2 = int_code[b] if opp_code_str[-4] == '0' else b
            int_code[c] = int(p1 == p2)

        elif opp_code == 99:
            ip_inc = 1
            raise StopIteration()
        else:
            raise RuntimeError(f"Found new {opp_code=}")
        ip += ip_inc


INPUTS = [0, 0, 0, 0, 0]


def part_1(inp):
    global INPUTS
    source_code_orig = list(map(int, inp[0].split(','))) + [0, 0, 0]
    max_output = 0
    phases_ids = [0, 1, 2, 3, 4]
    for phases in permutations(phases_ids):
        INPUTS = [0, 0, 0, 0, 0]
        amps = [run_Intcode(copy(source_code_orig), phase, amp_num)
                for amp_num, phase in enumerate(phases)]
        output = 0
        curr_amp = 0
        try:
            while True:
                output = next(amps[curr_amp])
                curr_amp = (curr_amp + 1) % 5
                INPUTS[curr_amp] = output
        except RuntimeError:
            max_output = max(max_output, output)

    return max_output


def part_2(inp):
    global INPUTS
    source_code_orig = list(map(int, inp[0].split(','))) + [0, 0, 0]
    max_output = 0
    phases_ids = [5, 6, 7, 8, 9]
    for phases in permutations(phases_ids):
        INPUTS = [0, 0, 0, 0, 0]
        amps = [run_Intcode(copy(source_code_orig), phase, amp_num)
                for amp_num, phase in enumerate(phases)]
        output = 0
        curr_amp = 0
        try:
            while True:
                output = next(amps[curr_amp])
                curr_amp = (curr_amp + 1) % 5
                INPUTS[curr_amp] = output
        except RuntimeError:
            max_output = max(max_output, output)

    return max_output


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
