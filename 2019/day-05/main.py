def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def run_Intcode(int_code, input_value, is_part_2):
    ip = 0
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
            int_code[a] = input_value
        elif opp_code == 4:
            a = int_code[ip + 1:ip + 2][0]
            ip_inc = 2
            yield int_code[a] if opp_code_str[-3] == '0' else a
        elif is_part_2 and opp_code == 5:
            a, b = int_code[ip + 1:ip + 3]
            ip_inc = 3
            p1 = int_code[a] if opp_code_str[-3] == '0' else a
            p2 = int_code[b] if opp_code_str[-4] == '0' else b
            if p1 != 0:
                ip = p2
                ip_inc = 0
        elif is_part_2 and opp_code == 6:
            a, b = int_code[ip + 1:ip + 3]
            ip_inc = 3
            p1 = int_code[a] if opp_code_str[-3] == '0' else a
            p2 = int_code[b] if opp_code_str[-4] == '0' else b
            if p1 == 0:
                ip = p2
                ip_inc = 0
        elif is_part_2 and opp_code == 7:
            a, b, c = int_code[ip + 1:ip + 4]
            ip_inc = 4
            p1 = int_code[a] if opp_code_str[-3] == '0' else a
            p2 = int_code[b] if opp_code_str[-4] == '0' else b
            int_code[c] = int(p1 < p2)
        elif is_part_2 and opp_code == 8:
            a, b, c = int_code[ip + 1:ip + 4]
            ip_inc = 4
            p1 = int_code[a] if opp_code_str[-3] == '0' else a
            p2 = int_code[b] if opp_code_str[-4] == '0' else b
            int_code[c] = int(p1 == p2)

        elif opp_code == 99:
            ip_inc = 1
            break
        else:
            # raise RuntimeError(f"Found new {opp_code=}")
            return None
        ip += ip_inc
    return int_code[0]


def part_1(inp):
    source_code = list(map(int, inp[0].split(','))) + [0, 0, 0]
    return list(run_Intcode(source_code, 1, False))[-1]


def part_2(inp):
    source_code = list(map(int, inp[0].split(','))) + [0, 0, 0]
    return list(run_Intcode(source_code, 5, True))[-1]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
