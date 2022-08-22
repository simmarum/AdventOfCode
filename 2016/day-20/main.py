from dataclasses import dataclass


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def find_all_ips(data):
    max_ip = -1
    allowed_ips = 0
    first_ip = None
    for i in range(len(data) - 1):
        if (i == 0):
            if (data[i][0] > 0):
                return data[i][0] - 1
            else:
                max_ip = data[i][1]

        if (data[i + 1][0] - 1) <= max_ip:
            max_ip = max(max_ip, data[i + 1][1])
        else:
            if first_ip is None:
                first_ip = max_ip + 1
            allowed_ips += (data[i + 1][0] - (max_ip + 1))
            max_ip = data[i + 1][1]

    return first_ip, allowed_ips


def part_1(inp):
    data = sorted([[int(e) for e in c.split('-')] for c in inp])
    first_ip, _ = find_all_ips(data)
    return first_ip


def part_2(inp):
    data = sorted([[int(e) for e in c.split('-')] for c in inp])
    _, allowed_ips = find_all_ips(data)
    return allowed_ips


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
