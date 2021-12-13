import copy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def _print_board(board, readable=False):
    print()
    for p in board:
        if readable:
            print(''.join(p).replace('.', ' ').replace('#', '■'))
        else:
            print(''.join(p))


def _merge_board(b1, b2):
    for i in range(len(b1)):
        for j in range(len(b1[i])):
            b1[i][j] = min(b1[i][j], b2[i][j])
    return b1


def part_1(inp):
    data = [[int(xx) for xx in x.split(',')]
            for x in inp if ('fold' not in x) and ('' != x)]
    rules = [x.replace('fold along ', '').split('=')
             for x in inp if 'fold' in x]
    max_x = 1 + max([item[0] for item in data])
    max_y = 1 + max([item[1] for item in data])
    board = [['.' for _ in range(max_x)] for _ in range(max_y)]
    for point in data:
        board[point[1]][point[0]] = '#'

    for rule in rules:
        split_line = int(rule[1])
        margin = 1 if len(board) % 2 == 1 else 0
        if rule[0] == 'y':
            upper_board = board[:split_line]
            bottom_board = board[split_line + margin:]
            bottom_board.reverse()
            upper_board = _merge_board(upper_board, bottom_board)
            board = copy.deepcopy(upper_board)
        elif rule[0] == 'x':
            left_board = [line[:split_line] for line in board]
            right_board = [line[split_line + margin:] for line in board]
            right_board = [list(reversed(line)) for line in right_board]
            left_board = _merge_board(left_board, right_board)
            board = copy.deepcopy(left_board)
        break
    return [item for sublist in board for item in sublist].count('#')


def part_2(inp):
    data = [[int(xx) for xx in x.split(',')]
            for x in inp if ('fold' not in x) and ('' != x)]
    rules = [x.replace('fold along ', '').split('=')
             for x in inp if 'fold' in x]
    max_x = 1 + max([item[0] for item in data])
    max_y = 1 + max([item[1] for item in data])
    board = [['.' for _ in range(max_x)] for _ in range(max_y)]
    for point in data:
        board[point[1]][point[0]] = '#'

    for rule in rules:
        split_line = int(rule[1])
        margin = 1 if len(board) % 2 == 1 else 0
        if rule[0] == 'y':
            upper_board = board[:split_line]
            bottom_board = board[split_line + margin:]
            bottom_board.reverse()
            upper_board = _merge_board(upper_board, bottom_board)
            board = copy.deepcopy(upper_board)
        elif rule[0] == 'x':
            left_board = [line[:split_line] for line in board]
            right_board = [line[split_line + margin:] for line in board]
            right_board = [list(reversed(line)) for line in right_board]
            left_board = _merge_board(left_board, right_board)
            board = copy.deepcopy(left_board)
    _print_board(board, True)
    return [item for sublist in board for item in sublist].count('#')


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
