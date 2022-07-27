import math


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def _divisors(n):
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield int(i)
            if i * i != n:
                yield int(n / i)


def part_1(inp):
    presents_target = int(inp[0])
    good_house = 0
    for i in range(1_000_000):
        presents = sum(_divisors(i)) * 10
        # print(f'House {i} got {presents} presents.')
        if presents >= presents_target:
            # print(f'House {i} got {presents} presents.')
            # print("Found first house with good amount of presents!")
            good_house = i
            break
    return good_house


def _divisors_2(n):
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            if i * 50 > n:
                yield int(i)
            if i * i != n:
                if int(n / i) * 50 > n:
                    yield int(n / i)


def part_2(inp):
    presents_target = int(inp[0])
    good_house = 0
    for i in range(1_000_000):
        presents = sum(_divisors_2(i)) * 11
        # print(f'House {i} got {presents} presents.')
        if presents >= presents_target:
            # print(f'House {i} got {presents} presents.')
            # print("Found first house with good amount of presents!")
            good_house = i
            break
    return good_house


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
