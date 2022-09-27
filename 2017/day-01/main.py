def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def solve(number, step):
    number_len = len(number)
    magic_sum = 0
    for i in range(number_len):
        if number[i] == number[(i + step) % number_len]:
            magic_sum += int(number[i])
    return magic_sum


def part_1(inp):
    return solve(inp[0], 1)


def part_2(inp):
    return solve(inp[0], len(inp[0]) // 2)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
