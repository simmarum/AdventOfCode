import numpy as np


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    city = np.zeros((1000, 1000), int)
    for val in inp:
        tmp = val.replace("turn ", "").split(" ")
        command = tmp[0]
        l, t = [int(x) for x in tmp[1].split(",")]
        r, b = [int(x)+1 for x in tmp[3].split(",")]
        if command == 'on':
            city[l:r, t:b] = np.ones((abs(r-l), abs(b-t)), int)
        if command == 'off':
            city[l:r, t:b] = np.zeros((abs(r-l), abs(b-t)), int)
        if command == 'toggle':
            city[l:r, t:b] = (1-city[l:r, t:b])
    return np.sum(city)


def part_2(inp):
    city = np.zeros((1000, 1000), int)
    for val in inp:
        tmp = val.replace("turn ", "").split(" ")
        command = tmp[0]
        l, t = [int(x) for x in tmp[1].split(",")]
        r, b = [int(x)+1 for x in tmp[3].split(",")]
        if command == 'on':
            city[l:r, t:b] += np.ones((abs(r-l), abs(b-t)), int)
        if command == 'off':
            city[l:r, t:b] -= np.ones((abs(r-l), abs(b-t)), int)
            city[l:r, t:b] = city[l:r, t:b].clip(min=0)
        if command == 'toggle':
            city[l:r, t:b] += np.ones((abs(r-l), abs(b-t)), int)
            city[l:r, t:b] += np.ones((abs(r-l), abs(b-t)), int)
    return np.sum(city)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
