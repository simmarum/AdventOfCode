import copy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [[int(c) for c in str(line).replace('\n', '')]
                for line in f.readlines()]


def in_list(inp, item):
    for i, _ in enumerate(inp):
        for j, _ in enumerate(inp[i]):
            if inp[i][j] > item:
                return i, j
    return None


def _inc(inp):
    for i, _ in enumerate(inp):
        for j, _ in enumerate(inp[i]):
            inp[i][j] += 1


def _flash(inp, x, y, xx, yy, flash_history):
    adj_list = [
        (-1, -1), (-1, 0), (-1, +1),
        (0, -1), (0, +1),
        (+1, -1), (+1, 0), (+1, +1),
    ]
    for i, j in adj_list:
        nx = x + i
        ny = y + j
        if (nx < 0) or (nx >= xx) or (ny < 0) or (ny >= yy):
            pass
        else:
            inp[nx][ny] += 1
    flash_history.add((x, y))
    for (x, y) in flash_history:
        inp[x][y] = 0
    return flash_history


def part_1(inp):
    board = copy.deepcopy(inp)
    xx = len(board)
    yy = len(board[0])
    sum_flash = 0
    for i in range(100):
        _inc(board)
        flash_history = set()
        pixel_9 = in_list(board, 9)
        while pixel_9 is not None:
            flash_history = _flash(
                board, pixel_9[0], pixel_9[1], xx, yy, flash_history)
            pixel_9 = in_list(board, 9)
        sum_flash += len(flash_history)
    return sum_flash


def part_2(inp):
    board = copy.deepcopy(inp)
    xx = len(board)
    yy = len(board[0])
    all_flash_num = xx * yy
    all_flash_step = None
    for i in range(300):
        _inc(board)
        flash_history = set()
        pixel_9 = in_list(board, 9)
        while pixel_9 is not None:
            flash_history = _flash(
                board, pixel_9[0], pixel_9[1], xx, yy, flash_history)
            pixel_9 = in_list(board, 9)
        if len(flash_history) == all_flash_num:
            all_flash_step = i + 1
            break
    return all_flash_step


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
