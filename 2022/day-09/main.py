import numpy as np


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    head = [0, 0]
    tail = [0, 0]
    tail_pos = set()
    dir_map = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0),
    }
    all_good_diff = [
        [0, 0],
        [0, -1], [0, 1],
        [-1, 0], [1, 0],
        [1, -1], [1, 1],
        [-1, 1], [1, 1],
    ]
    for line in inp:
        direction, cnt = line.split()
        for i in range(int(cnt)):
            head[0] += dir_map[direction][0]
            head[1] += dir_map[direction][1]
            if [head[0] - tail[0], head[1] - tail[1]] not in all_good_diff:
                dx = head[0] - tail[0]
                dy = head[1] - tail[1]
                if dx == 2:
                    tail[0] += 1
                    tail[1] += dy
                if dx == -2:
                    tail[0] += -1
                    tail[1] += dy
                if dy == 2:
                    tail[0] += dx
                    tail[1] += 1
                if dy == -2:
                    tail[0] += dx
                    tail[1] += -1
            tail_pos.add(tuple(tail))

    return len(tail_pos)


def part_2(inp):
    snake = [[0, 0] for _ in range(10)]
    tail_pos = set()
    dir_map = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0),
    }
    all_good_diff = [
        [0, 0],
        [0, -1], [0, 1],
        [-1, 0], [1, 0],
        [1, -1], [1, 1],
        [-1, 1], [-1, -1],
    ]
    magic_map = {
        2: 1,
        1: 1,
        0: 0,
        -1: -1,
        -2: -1
    }
    for line in inp:
        direction, cnt = line.split()
        for i in range(int(cnt)):
            snake[0][0] += dir_map[direction][0]
            snake[0][1] += dir_map[direction][1]
            for j in range(1, len(snake)):
                dx = snake[j - 1][0] - snake[j][0]
                dy = snake[j - 1][1] - snake[j][1]
                if [dx, dy] not in all_good_diff:
                    snake[j][0] += magic_map[dx]
                    snake[j][1] += magic_map[dy]
                tail_pos.add(tuple(snake[-1]))
            # print(tail_pos)

    return len(tail_pos)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
