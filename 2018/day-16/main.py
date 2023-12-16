from ast import literal_eval
from copy import copy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


codes = {
    0: 'r[{A}] + r[{B}]',  # addr
    1: 'r[{A}] + {B}',  # addi

    2: 'r[{A}] * r[{B}]',  # mulr
    3: 'r[{A}] * {B}',  # muli

    4: 'r[{A}] & r[{B}]',  # banr
    5: 'r[{A}] & {B}',  # bani

    6: 'r[{A}] | r[{B}]',  # borr
    7: 'r[{A}] | {B}',  # bori

    8: 'r[{A}]',  # setr
    9: '{A}',  # seti

    10: 'int({A} > r[{B}])',  # gtir
    11: 'int(r[{A}] > {B})',  # gtri
    12: 'int(r[{A}] > r[{B}])',  # gtrr

    13: 'int({A} == r[{B}])',  # eqir
    14: 'int(r[{A}] == {B})',  # eqri
    15: 'int(r[{A}] == r[{B}])',  # eqrr
}


def part_1(inp):
    before = None
    after = None
    code = None
    three_or_more = 0
    for line in inp:
        if (before is None) and ('Before' in line):
            before = literal_eval(line.replace('Before: ', ''))
        elif (after is None) and ('After' in line):
            after = literal_eval(line.replace('After: ', ''))
        elif (code is None) and ((before is not None)):
            code = list(map(int, line.split(' ')))
        if (code is not None) and (before is not None) and (after is not None):
            tmp_solution = set()
            for k, v in codes.items():
                r = copy(before)
                r[code[3]] = eval(v.format(A=code[1], B=code[2]))
                if r == after:
                    tmp_solution.add(k)
            if len(tmp_solution) >= 3:
                three_or_more += 1
            before = None
            after = None
            code = None

    return three_or_more


def part_2(inp):
    before = None
    after = None
    code = None
    r = [0, 0, 0, 0]
    solution = {k: set(codes.keys()) for k in codes.keys()}
    for line in inp:
        if (before is None) and ('Before' in line):
            before = literal_eval(line.replace('Before: ', ''))
        elif (after is None) and ('After' in line):
            after = literal_eval(line.replace('After: ', ''))
        elif (code is None) and ((before is not None)):
            code = list(map(int, line.split(' ')))
        elif (code is not None) and (before is not None) and (after is not None):
            tmp_solution = set()
            for k, v in codes.items():
                r = copy(before)
                r[code[3]] = eval(v.format(A=code[1], B=code[2]))
                if r == after:
                    tmp_solution.add(k)
                    # print(k, v)
                r = [0, 0, 0, 0]
            solution[code[0]] = solution[code[0]].intersection(tmp_solution)
            if len(solution[code[0]]) == 1:
                for k in codes.keys():
                    if k != code[0]:
                        solution[k] = solution[k].difference(solution[code[0]])
            before = None
            after = None
            code = None

        elif '' != line:
            final_code = list(map(int, line.split(' ')))
            r[final_code[3]] = eval(codes[list(solution[final_code[0]])[0]].format(
                A=final_code[1], B=final_code[2]))
    return r[0]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
