from collections import deque
from copy import deepcopy
import re
from itertools import combinations, chain


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def print_board(b):
    columns = ['F', *sorted(b.keys())]
    print(f"Board after move: {b['@']}")
    for i in range(4, 0, -1):
        tmp_print = []
        for col in columns:
            if col == '@':
                continue
            if col == 'F':
                tmp_print.append(f'F{i}')
            else:
                if b[col] == i:
                    tmp_print.append(col)
                else:
                    tmp_print.append('.')
        print(''.join(['{0:3}'.format(str(x)) for x in tmp_print]))


def check_floor(b, f):
    generators = set()
    microchips = set()
    for name, floor in b.items():
        if floor == f:
            if 'G' in name:
                generators.add(name[0])
            if 'M' in name:
                microchips.add(name[0])
    if (len(generators) == 0) or (len(microchips) == 0):
        return True
    if len(microchips.difference(generators)) == 0:
        return True
    return False


def is_final_floor(b):
    all_final_floor = True
    for name, floor in b.items():
        if name in ['#', '@']:
            continue
        if floor != 4:
            all_final_floor = False
            break
    return all_final_floor


def available_moves(b):
    tmp_moves = []
    elevator_floor = b['#']
    for name, floor in b.items():
        if name == '#':
            continue
        if floor == elevator_floor:
            tmp_moves.append(name)
    all_moves = chain(combinations(tmp_moves, 2), combinations(tmp_moves, 1))
    for move in all_moves:
        for direction in [-1, 1]:
            next_floor = elevator_floor + direction
            if 1 <= next_floor <= 4:
                nb = deepcopy(b)
                for m in move:
                    nb[m] = next_floor
                nb['#'] = next_floor
                if check_floor(
                        nb, elevator_floor) and check_floor(
                        nb, next_floor):
                    nb['@'] += 1
                    yield nb


def num_elem_per_floor(b):
    # 4 floors
    floors = [[0, 0], [0, 0], [0, 0], [0, 0]]
    for name, floor in b.items():
        if 'G' in name:
            floors[floor - 1][0] += 1
        if 'M' in name:
            floors[floor - 1][1] += 1
    return (b['#'], tuple(tuple(f) for f in floors))


def solve_board(b):
    already_seen = set()
    q = deque([b])

    while q:
        board = q.popleft()
        if is_final_floor(board):
            return board['@']

        for next_b in available_moves(board):
            k = num_elem_per_floor(next_b)
            if k not in already_seen:
                already_seen.add(k)
                q.append(next_b)


def read_board(inp, part_2):
    last_letter_used = 'O'
    lookup_table = {}
    floors_lookup = {
        'first': 1,
        'second': 2,
        'third': 3,
        'fourth': 4,
    }
    board = {
        '@': 0,
        '#': 1,
    }
    for line in inp:
        floor = line.split()[1]
        if (part_2) and (floors_lookup[floor] == 1):
            line = line + 'elerium generator '
            line = line + 'elerium-compatible microchip '
            line = line + 'dilithium generator '
            line = line + 'dilithium-compatible microchip'
        generators = re.findall(r'\w+(?= generator)', line)
        for name in generators:
            if name not in lookup_table:
                lookup_table[name] = last_letter_used
                last_letter_used = chr(ord(last_letter_used) + 1)
            board[lookup_table[name] + 'G'] = floors_lookup[floor]
        microchips = re.findall(r'\w+(?=-compatible microchip)', line)
        for name in microchips:
            if name not in lookup_table:
                lookup_table[name] = last_letter_used
                last_letter_used = chr(ord(last_letter_used) + 1)
            board[lookup_table[name] + 'M'] = floors_lookup[floor]
    return board


def part_1(inp):
    board = read_board(inp, False)
    moves = solve_board(board)
    return moves


def part_2(inp):
    board = read_board(inp, True)
    moves = solve_board(board)
    return moves


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
