from operator import add, mul


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [line for line in f.read().splitlines()]


def part_1(inp):
    dd = {'N': [1, 0], 'S': [-1, 0],
          'E': [0, 1], 'W': [0, -1]}
    pos = [0, 0]
    pos_dir = 0
    pos_dir_all = 'ESWN'
    for val in inp:
        d, v = val[0], int(val[1:])
        if d == 'R':
            pos_dir = (pos_dir + v//90) % 4
        elif d == 'L':
            pos_dir = (pos_dir + 4 - v//90) % 4
        elif d == 'F':
            pos = list(
                map(add, pos, map(lambda x: x*v, dd[pos_dir_all[pos_dir]])))
        else:
            pos = list(map(add, pos, map(lambda x: x*v, dd[d])))
    return abs(pos[0])+abs(pos[1])


def part_2(inp):
    dd = {'N': [1, 0], 'S': [-1, 0],
          'E': [0, 1], 'W': [0, -1]}
    pos = [0, 0]
    w_pos = [1, 10]
    for val in inp:
        d, v = val[0], int(val[1:])
        if d == 'R':
            for _ in range(v//90):
                w_pos = [-w_pos[1], w_pos[0]]
        elif d == 'L':
            for _ in range(v//90):
                w_pos = [w_pos[1], -w_pos[0]]
        elif d == 'F':
            pos = list(
                map(add, pos, map(lambda x: x*v, w_pos)))
        else:
            w_pos = list(map(add, w_pos, map(lambda x: x*v, dd[d])))
    return abs(pos[0])+abs(pos[1])


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
