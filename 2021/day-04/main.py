def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    nums = inp[0].split(',')
    nums = [int(x) for x in nums]
    xlen = int((len(inp) - 1) / 6)
    boards = []
    for board_num in range(xlen):
        board = [x.split()
                 for x in inp[board_num * 6 + 2: board_num * 6 + 2 + 5]]
        board = [int(item) for sublist in board for item in sublist]
        board_map = [False for x in board]
        boards.append([board, board_map])
        bingo = False
    for num in nums:
        for board, board_map in boards:
            try:
                idx = board.index(num)
                board_map[idx] = True
                if all(board_map[0:5]):
                    bingo = True
                    break
                if all(board_map[5:10]):
                    bingo = True
                    break
                if all(board_map[10:15]):
                    bingo = True
                    break
                if all(board_map[15:20]):
                    bingo = True
                    break
                if all(board_map[20:25]):
                    bingo = True
                    break
                if all(board_map[0::5]):
                    bingo = True
                    break
                if all(board_map[1::5]):
                    bingo = True
                    break
                if all(board_map[2::5]):
                    bingo = True
                    break
                if all(board_map[3::5]):
                    bingo = True
                    break
                if all(board_map[4::5]):
                    bingo = True
                    break
            except ValueError:
                pass
        if bingo:
            b = sum([bx for bi, bx in enumerate(
                board) if board_map[bi] is False])
            res = num * b
            break
    return res


def part_2(inp):
    nums = inp[0].split(',')
    nums = [int(x) for x in nums]
    xlen = int((len(inp) - 1) / 6)
    boards = []
    for board_num in range(xlen):
        board = [x.split()
                 for x in inp[board_num * 6 + 2: board_num * 6 + 2 + 5]]
        board = [int(item) for sublist in board for item in sublist]
        board_map = [False for x in board]
        boards.append([board, board_map, False])

    for num in nums:
        for j, data in enumerate(boards):
            bingo = False
            board = data[0]
            board_map = data[1]
            finish_board = data[2]
            if finish_board:
                continue
            try:
                idx = board.index(num)
                board_map[idx] = True
                if all(board_map[0:5]):
                    bingo = True
                if all(board_map[5:10]):
                    bingo = True
                if all(board_map[10:15]):
                    bingo = True
                if all(board_map[15:20]):
                    bingo = True
                if all(board_map[20:25]):
                    bingo = True
                if all(board_map[0::5]):
                    bingo = True
                if all(board_map[1::5]):
                    bingo = True
                if all(board_map[2::5]):
                    bingo = True
                if all(board_map[3::5]):
                    bingo = True
                if all(board_map[4::5]):
                    bingo = True
            except ValueError:
                pass
            if bingo:
                boards[j][2] = True
                b = sum([bx for bi, bx in enumerate(
                    board) if board_map[bi] is False])
                res = num * b
    return res


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
