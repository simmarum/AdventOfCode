import re
import numpy as np


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def read_data(inp):
    discs = {}
    for line in inp:
        m = re.match(
            r'Disc #(\d) has (\d+) positions; at time=(\d+), it is at position (\d+)',
            line)
        discs[int(m.group(1))] = {
            'positions': int(m.group(2)),
            'time': int(m.group(3)),
            'pos': int(m.group(4))
        }
    return discs


def solve_discs(discs):
    time_to_correct_place = []
    time_intervals = []
    for k, v in discs.items():
        time_to_correct_place.append(
            (v['positions'] - v['pos'] - k) % v['positions'])
        time_intervals.append(v['positions'])
    while len(set(time_to_correct_place)) > 1:
        tmp_val = max(time_to_correct_place)
        for i in range(len(time_to_correct_place)):
            # print("!", i, time_to_correct_place)
            if time_to_correct_place[i] == tmp_val:
                # print("@", i, time_to_correct_place)
                continue
            if time_to_correct_place[i] < tmp_val:
                if (tmp_val -
                        time_to_correct_place[i]) % time_intervals[i] == 0:
                    coef = int(
                        (tmp_val - time_to_correct_place[i]) // time_intervals[i])
                else:
                    coef = int(
                        ((tmp_val - time_to_correct_place[i]) // time_intervals[i]) + 1)
                time_to_correct_place[i] = time_to_correct_place[i] + \
                    ((coef) * time_intervals[i])

    return time_to_correct_place[0]


def part_1(inp):
    discs = read_data(inp)
    return solve_discs(discs)


def part_2(inp):
    discs = read_data(inp)
    discs[max(discs) + 1] = {
        'positions': 11,
        'time': 0,
        'pos': 0
    }
    return solve_discs(discs)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
