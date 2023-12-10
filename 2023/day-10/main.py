import numpy as np


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [[c for c in str(line).replace("\n", "")]
                for line in f.readlines()]


def travel_board(board, curr_pos, step_cnt, prev_way, border):
    first_way = ''
    ways = {
        'd': [(1, 0), 'd', '|LJ'],
        'u': [(-1, 0), 'u', '|LJ'],
        'r': [(0, 1), 'r', '|F7'],
        'l': [(0, -1), 'l', '|F7'],
    }
    next_ways = {
        '|': [('u', 'u'), ('d', 'd')],
        '-': [('l', 'l'), ('r', 'r')],
        'L': [('d', 'r'), ('l', 'u')],
        'J': [('d', 'l'), ('r', 'u')],
        'F': [('u', 'r'), ('l', 'd')],
        '7': [('u', 'l'), ('r', 'd')],
    }
    while not ((step_cnt != 0) and (board[curr_pos] == 'S')):
        border.add((int(curr_pos[0]), int(curr_pos[1])))
        if step_cnt == 0:
            for way, name, next in ways.values():
                new_pos = (curr_pos[0] + way[0], curr_pos[1] + way[1])
                try:
                    if board[new_pos][0] in next:
                        curr_pos = new_pos
                        step_cnt += 1
                        prev_way = name
                        first_way = prev_way
                        break
                except IndexError:
                    pass
        else:
            for n_way in next_ways[board[curr_pos][0]]:
                if prev_way == n_way[0]:
                    way = ways[n_way[1]][0]
                    new_pos = (curr_pos[0] + way[0], curr_pos[1] + way[1])
                    try:
                        board[new_pos][0]  # just to check if index is valid
                        curr_pos = new_pos
                        step_cnt += 1
                        prev_way = n_way[1]
                        break
                    except IndexError:
                        pass

    replace_s = {
        'dd': '|',
        'uu': '|',
        'lr': '-',
        'rl': '-',
        'dr': '7',
        'lu': '7',
        'dl': 'F',
        'ru': 'F',
        'ur': 'J',
        'ld': 'J',
        'ul': 'L',
        'rd': 'L',
    }
    return step_cnt, replace_s[first_way + prev_way]


def part_1(inp):
    start = 'S'
    step_cnt = 0
    border = set()
    board = np.array(inp)
    start_idx = np.where(board == start)
    path_len, _ = travel_board(board, start_idx, step_cnt, None, border)

    return (path_len + 1) // 2


def part_2(inp):
    start = 'S'
    step_cnt = 0
    border = set()
    board = np.array(inp)
    start_idx = np.where(board == start)
    _, replace_s = travel_board(board, start_idx, step_cnt, None, border)
    inside_points = 0
    for y, line in enumerate(inp):
        inside = False
        last_char = ''
        for x, c in enumerate(line):
            if (y, x) in border:
                if c == 'S':
                    c = replace_s
                if c in '|S':
                    inside = not inside
                elif c in 'FL':
                    last_char = c
                elif (last_char + c == 'FJ') or (last_char + c == 'L7'):
                    inside = not inside
            else:
                if inside:
                    inside_points += 1
    return inside_points


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
