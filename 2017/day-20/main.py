import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    max_time = 1000
    data = []
    for i, line in enumerate(inp):
        m = re.match("p=<(.*)>, v=<(.*)>, a=<(.*)>", line)
        p = list(map(int, m.group(1).split(',')))
        v = list(map(int, m.group(2).split(',')))
        a = list(map(int, m.group(3).split(',')))
        data.append([p, v, a, i, sum(map(abs, p))])

    for t in range(1, max_time + 1):
        for i in range(len(data)):
            data[i][1] = [
                data[i][1][0] + data[i][2][0],
                data[i][1][1] + data[i][2][1],
                data[i][1][2] + data[i][2][2],
            ]
            data[i][0] = [
                data[i][0][0] + data[i][1][0],
                data[i][0][1] + data[i][1][1],
                data[i][0][2] + data[i][1][2],
            ]
            data[i][4] = sum(map(abs, data[i][0]))
    return sorted(data, key=lambda x: x[4])[0][3]


def part_2(inp):
    max_time = 1000
    data = []
    for i, line in enumerate(inp):
        m = re.match("p=<(.*)>, v=<(.*)>, a=<(.*)>", line)
        p = list(map(int, m.group(1).split(',')))
        v = list(map(int, m.group(2).split(',')))
        a = list(map(int, m.group(3).split(',')))
        data.append([p, v, a])

    for t in range(1, max_time + 1):
        for i in range(len(data)):
            data[i][1] = [
                data[i][1][0] + data[i][2][0],
                data[i][1][1] + data[i][2][1],
                data[i][1][2] + data[i][2][2],
            ]
            data[i][0] = [
                data[i][0][0] + data[i][1][0],
                data[i][0][1] + data[i][1][1],
                data[i][0][2] + data[i][1][2],
            ]
        data_pos = [d[0] for d in data]
        data_pos = [d for d in data_pos if data_pos.count(d) == 1]
        data = [d for d in data if d[0] in data_pos]
    return len(data)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
