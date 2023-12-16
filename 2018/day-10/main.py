import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def print_message(data):
    x_min = min(p[0] for p in data)
    x_max = max(p[0] for p in data)
    y_min = min(p[1] for p in data)
    y_max = max(p[1] for p in data)
    if y_max - y_min > 30:
        return
    if x_max - x_min > 100:
        return
    board = []
    for _ in range((y_max - y_min + 1)):
        row = []
        for _ in range((x_max - x_min + 1)):
            row.append('.')
        board.append(row)
    for p in data:
        board[p[1] - y_min][p[0] - x_min] = '#'
    [print(''.join(row)) for row in board]


def part_1(inp):
    data = []
    for line in inp:
        m = re.match("position=<(.*),(.*)> velocity=<(.*),(.*)>", line)
        if m:
            data.append((int(m.group(1)), int(m.group(2)),
                         int(m.group(3)), int(m.group(4))))
    area_shrink = True
    for second in range(10606):
        area_before = (max(p[0] for p in data) - min(p[0] for p in data)) * \
            (max(p[1] for p in data) - min(p[1] for p in data))
        new_data = [(p[0] + p[2], p[1] + p[3], p[2], p[3]) for p in data]
        area_after = (max(p[0] for p in new_data) - min(p[0] for p in new_data)) * \
            (max(p[1] for p in new_data) - min(p[1] for p in new_data))
        area_shrink = area_after < area_before
        if area_shrink is False:
            print(f"{second} seconds elapsed")
            print_message(data)
            return second
        data = new_data
    return None


def part_2(inp):
    return "Look at the output of part_1"


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
