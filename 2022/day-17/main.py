import numpy as np


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


blocks = {
    0: {
        's': [(0, 0), (1, 0), (2, 0), (3, 0)],
        'w': 4,
        'h': 1
    },
    1: {
        's': [(1, 0), (0, -1), (1, -1), (2, -1), (1, -2)],
        'w': 3,
        'h': 3
    },
    2: {
        's': [(0, -2), (1, -2), (2, 0), (2, -1), (2, -2)],
        'w': 3,
        'h': 3
    },
    3: {
        's': [(0, 0), (0, -1), (0, -2), (0, -3)],
        'w': 1,
        'h': 4
    },
    4: {
        's': [(0, 0), (0, -1), (1, 0), (1, -1)],
        'w': 2,
        'h': 2
    },
}


def print_b(board, board_w, board_h_min=0, board_h_max=10):
    print('+'+'-'*board_w+'+')
    for y in range(board_h_max, board_h_min-1, -1):
        row = ''
        for x in range(0, board_w):
            if (x, y) in board:
                row += '#'
            else:
                row += '.'
        print('|'+row+'|')
    print('+'+'-'*board_w+'+')


def check_block_location(block_place, board_w):
    return all([((0 <= p[0] < board_w) * (0 <= p[1])) for p in block_place])


def part_1(inp):
    commands = inp[0]
    board_w = 7
    board_h_for_print = 30
    board = set()
    start_w = 2
    start_h_diff = 3
    step = 0
    curr_command = -1
    all_comands = len(commands)
    curr_block = -1
    curr_block_cnt = 0
    curr_block_pos = (None, None)
    curr_block_place = None
    block = None
    all_blocks = len(blocks)
    is_block_active = False
    is_block_to_move = True
    max_block_h = -1
    while True:
        step += 1
        # print(step, curr_block_cnt, max_block_h)
        if not is_block_active:
            is_block_active = True
            is_block_to_move = True
            curr_block_cnt += 1
            if curr_block_cnt == 2023:
                return max_block_h + 1
            curr_block = (curr_block + 1) % all_blocks
            block = blocks[curr_block]
            curr_block_pos = (start_w, max_block_h + block['h'] + start_h_diff)
            curr_block_place = set([(shape[0]+curr_block_pos[0], shape[1] +
                                     curr_block_pos[1]) for shape in block['s']])
            if check_block_location(curr_block_place, board_w):
                if not curr_block_place.intersection(board):
                    board = board.union(curr_block_place)
                else:
                    raise ValueError("Block is placed wrong!")
        if is_block_to_move:
            is_block_to_move = False
            curr_command = (curr_command + 1) % all_comands
            cmd = commands[curr_command]
            if cmd == '<':
                move_pos = (-1, 0)
            else:
                move_pos = (1, 0)
            new_place = set([(x[0]+move_pos[0], x[1]+move_pos[1])
                             for x in curr_block_place])

            if check_block_location(new_place, board_w) and not new_place.intersection(board.difference(curr_block_place)):
                board = board.difference(curr_block_place).union(new_place)
                curr_block_place = new_place
            else:
                pass

            # falling
            fall_pos = (0, -1)
            new_place = set([(x[0]+fall_pos[0], x[1]+fall_pos[1])
                             for x in curr_block_place])
            if check_block_location(new_place, board_w) and not new_place.intersection(board.difference(curr_block_place)):
                board = board.difference(curr_block_place).union(new_place)
                curr_block_place = new_place
                is_block_to_move = True
            else:
                is_block_active = False
                max_block_h = max([max_block_h]+[p[1]
                                                 for p in curr_block_place])

    return None


def part_2(inp):
    commands = inp[0]
    board_w = 7
    board_h_for_print = 30
    board = set()
    start_w = 2
    start_h_diff = 3
    step = 0
    curr_command = -1
    all_comands = len(commands)
    curr_block = -1
    curr_block_cnt = 0
    curr_block_pos = (None, None)
    curr_block_place = None
    block = None
    all_blocks = len(blocks)
    is_block_active = False
    is_block_to_move = True
    max_block_h = -1
    cache = {}
    while True:
        step += 1
        if not is_block_active:
            is_block_active = True
            is_block_to_move = True
            # detect cycle
            if (curr_block, curr_command) in cache:
                c_curr_block_cnt, c_max_block_h = cache[(
                    curr_block, curr_command)]
                m = (1_000_000_000_000 -
                     curr_block_cnt) % (c_curr_block_cnt-curr_block_cnt)
                if not m:
                    return max_block_h+1 + (c_max_block_h-(max_block_h+1)) * ((1_000_000_000_000-curr_block_cnt) // (c_curr_block_cnt-curr_block_cnt))
            else:
                cache[(curr_block, curr_command)
                      ] = curr_block_cnt, max_block_h+1
            curr_block_cnt += 1
            curr_block = (curr_block + 1) % all_blocks
            block = blocks[curr_block]
            curr_block_pos = (start_w, max_block_h + block['h'] + start_h_diff)
            curr_block_place = set([(shape[0]+curr_block_pos[0], shape[1] +
                                     curr_block_pos[1]) for shape in block['s']])
            if check_block_location(curr_block_place, board_w):
                if not curr_block_place.intersection(board):
                    board = board.union(curr_block_place)
                else:
                    raise ValueError("Block is placed wrong!")
        if is_block_to_move:
            is_block_to_move = False
            curr_command = (curr_command + 1) % all_comands
            cmd = commands[curr_command]
            if cmd == '<':
                move_pos = (-1, 0)
            else:
                move_pos = (1, 0)
            new_place = set([(x[0]+move_pos[0], x[1]+move_pos[1])
                             for x in curr_block_place])

            if check_block_location(new_place, board_w) and not new_place.intersection(board.difference(curr_block_place)):
                board = board.difference(curr_block_place).union(new_place)
                curr_block_place = new_place
            else:
                pass

            # falling
            fall_pos = (0, -1)
            new_place = set([(x[0]+fall_pos[0], x[1]+fall_pos[1])
                             for x in curr_block_place])
            if check_block_location(new_place, board_w) and not new_place.intersection(board.difference(curr_block_place)):
                board = board.difference(curr_block_place).union(new_place)
                curr_block_place = new_place
                is_block_to_move = True
            else:
                is_block_active = False
                max_block_h = max([max_block_h]+[p[1]
                                                 for p in curr_block_place])


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
