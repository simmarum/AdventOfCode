def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    data = list(map(int, inp[0].split(',')))
    max_depth = max(data)
    results = []
    for depth in range(max_depth):
        res = sum([abs(x - depth) for x in data])
        results.append((depth, res))

    results = sorted(results, key=lambda x: x[1])
    return results[0][1]


def part_2(inp):
    data = list(map(int, inp[0].split(',')))
    max_depth = max(data)
    results = []
    for depth in range(max_depth):
        res = sum([int(((1 + abs(x - depth)) / 2) * abs(x - depth))
                   for x in data])
        results.append((depth, res))
    results = sorted(results, key=lambda x: x[1])
    return results[0][1]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
