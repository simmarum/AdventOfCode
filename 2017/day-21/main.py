import numpy as np


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def solve(inp, iterations):
    patterns = {}
    for line in inp:
        line_splitted = line.split(' => ')
        patterns[line_splitted[0].replace(
            '/', '')] = line_splitted[1].replace('/', '')

    board = np.array([['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']])
    for t in range(iterations):
        board_len = len(board)
        splits = []
        if board_len % 3 == 0:
            splits = list(range(0, board_len + 1, 3))
        if board_len % 2 == 0:
            splits = list(range(0, board_len + 1, 2))
        big_board_chunks = []
        for s1x, s1y in zip(splits[:-1], splits[1:]):
            big_board_chunks_row = []
            for s2x, s2y in zip(splits[:-1], splits[1:]):
                small_board = board[s1x:s1y, s2x:s2y]
                new_small_board = None
                for i in range(4):
                    small_board = np.rot90(small_board)
                    for j in range(2):
                        small_board = np.fliplr(small_board)
                        for k in range(2):
                            small_board = np.flipud(small_board)
                            small_board_str = ''.join(small_board.flatten())
                            if small_board_str in patterns:
                                new_small_board = patterns[small_board_str]
                                reshape_size = 4
                                if len(new_small_board) == 9:
                                    reshape_size = 3
                                new_small_board = np.array(
                                    list(new_small_board)).reshape(
                                    (reshape_size, reshape_size))
                            if new_small_board is not None:
                                break
                        if new_small_board is not None:
                            break
                    if new_small_board is not None:
                        break
                big_board_chunks_row.append(new_small_board)
            big_board_chunks.append(big_board_chunks_row)
        big_board = np.block(big_board_chunks)
        board = big_board

    return (''.join(board.flatten())).count('#')


def part_1(inp):
    return solve(inp, 5)


def part_2(inp):
    return solve(inp, 18)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
