def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    days = 80
    fish = list(map(int, inp[0].split(',')))
    for _ in range(days):
        to_add = fish.count(0)
        fish = list(map(lambda x: 7 if x == 0 else x, fish))
        fish.extend([9] * to_add)
        fish = list(map(lambda x: x - 1, fish))
    return len(fish)


def part_2(inp):
    days = 256
    fish = list(map(int, inp[0].split(',')))
    ocean = {}
    for i in range(0, 10):
        ocean[i] = fish.count(i)

    for _ in range(days):
        ocean[9] += ocean[0]
        ocean[7] += ocean[0]
        ocean[0], ocean[1], ocean[2], ocean[3], ocean[4], ocean[5], ocean[6], ocean[7], ocean[8], ocean[9] = \
            ocean[1], ocean[2], ocean[3], ocean[4], ocean[5], ocean[6], ocean[7], ocean[8], ocean[9], 0
    return sum(ocean.values())


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
