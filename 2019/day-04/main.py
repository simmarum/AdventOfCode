def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def find_all_numbers(range_start, range_end):
    for number in range(range_start, range_end + 1):
        a1, a2, a3, a4, a5, a6 = [c for c in str(number)]
        is_double = (a1 == a2) or (a2 == a3) or (a3 == a4) or (a4 == a5) or (a5 == a6)  # noqa
        is_never_decrease = (a1 <= a2 <= a3 <= a4 <= a5 <= a6)
        yield is_double and is_never_decrease


def part_1(inp):
    range_start = int(inp[0][0:6])
    range_end = int(inp[0][7:14])
    return sum(find_all_numbers(range_start, range_end))


def find_all_numbers_2(range_start, range_end):
    for number in range(range_start, range_end + 1):
        a1, a2, a3, a4, a5, a6 = [c for c in str(number)]
        is_double = (
            (a1 == a2 != a3) or
            (a1 != a2 == a3 != a4) or
            (a2 != a3 == a4 != a5) or
            (a3 != a4 == a5 != a6) or
            (a4 != a5 == a6)
        )
        is_never_decrease = (a1 <= a2 <= a3 <= a4 <= a5 <= a6)
        yield is_double and is_never_decrease


def part_2(inp):
    range_start = int(inp[0][0:6])
    range_end = int(inp[0][7:14])
    return sum(find_all_numbers_2(range_start, range_end))


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
