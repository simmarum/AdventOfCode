
def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    keypad = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    )
    position = [1, 1]
    mn_x = 0
    mx_x = len(keypad[0]) - 1
    mn_y = 0
    mx_y = len(keypad) - 1
    code = ''
    for line in inp:
        for c in line:
            if c == 'U':
                position = [max(mn_x, position[0] - 1), position[1]]
            if c == 'D':
                position = [min(mx_x, position[0] + 1), position[1]]
            if c == 'L':
                position = [position[0], max(mn_y, position[1] - 1)]
            if c == 'R':
                position = [position[0], min(mx_y, position[1] + 1)]
        code += str(keypad[position[0]][position[1]])
    return int(code)


def part_2(inp):
    keypad = (
        ('x', 'x', 'x', 'x', 'x', 'x', 'x'),
        ('x', 'x', 'x', '1', 'x', 'x', 'x'),
        ('x', 'x', '2', '3', '4', 'x', 'x'),
        ('x', '5', '6', '7', '8', '9', 'x'),
        ('x', 'x', 'A', 'B', 'C', 'x', 'x'),
        ('x', 'x', 'x', 'D', 'x', 'x', 'x'),
        ('x', 'x', 'x', 'x', 'x', 'x', 'x'),
    )
    position = [3, 1]
    code = ''
    for line in inp:
        for c in line:
            move = [0, 0]
            if c == 'U':
                move = [-1, 0]
            if c == 'D':
                move = [1, 0]
            if c == 'L':
                move = [0, -1]
            if c == 'R':
                move = [0, 1]
            if keypad[position[0] + move[0]][position[1] + move[1]] != 'x':
                position = [position[0] + move[0], position[1] + move[1]]
        code += str(keypad[position[0]][position[1]])
    return code


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
