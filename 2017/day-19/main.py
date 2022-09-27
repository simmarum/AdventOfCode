def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def get_board(inp):
    board = []
    for line in inp:
        board.append(list(line))
    return board


def print_board(board):
    print()
    for row in board:
        print(''.join(row))
    print()


def solve_board(board, is_part_2):
    path = []
    curr_point = (0, board[0].index('|'))
    dir = (1, 0)
    board_len_0 = len(board)
    board_len_1 = len(board[0])
    step = 0
    while step < 50_000:
        step += 1
        for angle in range(3):
            if angle == 1:
                dir = (-dir[1], dir[0])
            elif angle == 2:
                dir = (-dir[0], -dir[1])
            new_point = (curr_point[0] + dir[0], curr_point[1] + dir[1])
            if ((new_point[0] < board_len_0) and (new_point[1] < board_len_1) and (
                    new_point[0] >= 0) and (new_point[1] >= 0)) and board[new_point[0]][new_point[1]] != ' ':
                path.append(board[new_point[0]][new_point[1]])
                curr_point = new_point
                break
        else:
            break
    if is_part_2 is False:
        letters = ''.join([c for c in path if c not in ['-', '|', '+']])
        return letters
    else:
        return len(path) + 1


def part_1(inp):
    board = get_board(inp)
    return solve_board(board, False)


def part_2(inp):
    board = get_board(inp)
    return solve_board(board, True)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
