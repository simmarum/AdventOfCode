def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def sieve(max_n):
    sieve_arr = [[] for _ in range(max_n + 1)]
    for i in range(1, max_n):
        for j in range(i, max_n, i):
            sieve_arr[j].append(i)
    return sieve_arr


def part_1(inp):
    presents_target = int(inp[0])
    good_house = 0
    max_n = 1_000_000
    sieve_arr = sieve(max_n)
    for i in range(1, max_n + 1):
        presents = sum(sieve_arr[i]) * 10
        # print(f'House {i} got {presents} presents.')
        if presents >= presents_target:
            # print(f'House {i} got {presents} presents.')
            # print("Found first house with good amount of presents!")
            good_house = i
            break
    return good_house


def sieve_2(max_n):
    sieve_arr = [[] for _ in range(max_n + 1)]
    for i in range(1, max_n):
        for j in range(i, max_n, i):
            if i * 50 > j:
                sieve_arr[j].append(i)
    return sieve_arr


def part_2(inp):
    presents_target = int(inp[0])
    good_house = 0
    max_n = 1_000_000
    sieve_arr = sieve_2(max_n)
    for i in range(1, max_n + 1):
        presents = sum(sieve_arr[i]) * 11
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
