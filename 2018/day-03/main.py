import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def read_data(inp):
    data = {}
    max_x, max_y, max_w, max_h = 0, 0, 0, 0
    for line in inp:
        m = re.match("#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)", line)
        data[m.group(1)] = {
            'x': int(m.group(2)),
            'y': int(m.group(3)),
            'w': int(m.group(4)),
            'h': int(m.group(5)),
            'x2': int(m.group(2)) + int(m.group(4)),
            'y2': int(m.group(2)) + int(m.group(5)),
        }
        max_x = max(max_x, int(m.group(2)))
        max_y = max(max_y, int(m.group(3)))
        max_w = max(max_w, int(m.group(4)))
        max_h = max(max_h, int(m.group(5)))
    board = []
    for _ in range(max_y + max_h + 10):
        board.append([0] * (max_x + max_w + 10))

    return data, board


def part_1(inp):
    data, board = read_data(inp)
    for _, v in data.items():
        for i in range(v['w']):
            for j in range(v['h']):
                board[v['y'] + j][v['x'] + i] += 1
    cnt_more_than_one = 0
    flat_board = [item for sublist in board for item in sublist]
    for elem in flat_board:
        if elem > 1:
            cnt_more_than_one += 1
    return cnt_more_than_one


def part_2(inp):
    data, board = read_data(inp)
    for k, v in data.items():
        for i in range(v['w']):
            for j in range(v['h']):
                board[v['y'] + j][v['x'] + i] += 1
    for k, v in data.items():
        is_block_alone = True
        for i in range(v['w']):
            for j in range(v['h']):
                if board[v['y'] + j][v['x'] + i] > 1:
                    is_block_alone = False
                    break
            if is_block_alone is False:
                break
        if is_block_alone is True:
            return k
    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
