import copy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [
            [c for c in str(line.replace("\n", ""))] for line in f.readlines()]


def _get_pixel(inp, x, y, xx, yy):
    if (x < 0) or (x >= xx) or (y < 0) or (y >= yy):
        return '.'
    else:
        return inp[x][y]


def _get_neighbors(inp, x, y, xx, yy):
    return ''.join(
        [
            _get_pixel(inp, x - 1, y - 1, xx, yy),
            _get_pixel(inp, x - 1, y + 0, xx, yy),
            _get_pixel(inp, x - 1, y + 1, xx, yy),
            _get_pixel(inp, x - 0, y - 1, xx, yy),
            _get_pixel(inp, x - 0, y + 1, xx, yy),
            _get_pixel(inp, x + 1, y - 1, xx, yy),
            _get_pixel(inp, x + 1, y + 0, xx, yy),
            _get_pixel(inp, x + 1, y + 1, xx, yy),
        ]
    )


def part_1(inp):
    board = copy.deepcopy(inp)
    xx = len(board)
    yy = len(board[0])
    for _ in range(0, 100):
        new_board = copy.deepcopy(board)
        for x in range(0, xx):
            for y in range(0, yy):
                n = _get_neighbors(board, x, y, xx, yy)
                ons = n.count('#')
                if (board[x][y] == '#') and (ons != 2) and (ons != 3):
                    new_board[x][y] = '.'
                if (board[x][y] == '.') and (ons == 3):
                    new_board[x][y] = '#'
        board = new_board
    flat_board = ''.join([item for sublist in board for item in sublist])
    return flat_board.count('#')


def _corner_on(inp, xx, yy):
    inp[0][0] = '#'
    inp[xx - 1][0] = '#'
    inp[0][yy - 1] = '#'
    inp[xx - 1][yy - 1] = '#'
    return inp


def _is_corner(x, y, xx, yy):
    if (x == 0) and (y == 0):
        return True
    elif (x == xx - 1) and (y == 0):
        return True
    elif (x == 0) and (y == yy - 1):
        return True
    elif (x == xx - 1) and (y == yy - 1):
        return True
    else:
        return False


def part_2(inp):
    board = copy.deepcopy(inp)
    xx = len(board)
    yy = len(board[0])
    board = _corner_on(board, xx, yy)
    for _ in range(0, 100):
        new_board = copy.deepcopy(board)
        for x in range(0, xx):
            for y in range(0, yy):
                n = _get_neighbors(board, x, y, xx, yy)
                ons = n.count('#')
                if (board[x][y] == '#') and (ons != 2) and (ons != 3):
                    if not _is_corner(x, y, xx, yy):
                        new_board[x][y] = '.'
                if (board[x][y] == '.') and (ons == 3):
                    new_board[x][y] = '#'
        board = new_board
    flat_board = ''.join([item for sublist in board for item in sublist])
    return flat_board.count('#')


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
