def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    _, _, _, _, num_a = inp[0].split()
    _, _, _, _, num_b = inp[1].split()
    # num_a, num_b = 65, 8921
    num_a, num_b = int(num_a), int(num_b)
    magic_num = 2147483647
    gen_a = 16807
    gen_b = 48271

    total = 0
    for _ in range(40_000_000):
        num_a = (num_a * gen_a) % magic_num
        num_b = (num_b * gen_b) % magic_num
        # 65536 = 2**16
        if (num_a ^ num_b) % 65536 == 0:
            total += 1
    return total


def part_2(inp):
    _, _, _, _, num_a = inp[0].split()
    _, _, _, _, num_b = inp[1].split()
    # num_a, num_b = 65, 8921
    num_a, num_b = int(num_a), int(num_b)
    magic_num = 2147483647
    gen_a = 16807
    gen_b = 48271

    total = 0
    for _ in range(5_000_000):
        while True:
            num_a = (num_a * gen_a) % magic_num
            if num_a % 4 == 0:
                break
        while True:
            num_b = (num_b * gen_b) % magic_num
            if num_b % 8 == 0:
                break
        # 65536 = 2**16
        if (num_a ^ num_b) % 65536 == 0:
            total += 1
    return total


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
