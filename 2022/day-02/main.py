def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    # A/X Rock 1
    # B/Y Paper 2
    # C/Z Scissors 3

    # W/D/L 0/3/6
    all_combinations = {
        'A X': 3 + 1,
        'A Y': 6 + 2,
        'A Z': 0 + 3,

        'B X': 0 + 1,
        'B Y': 3 + 2,
        'B Z': 6 + 3,

        'C X': 6 + 1,
        'C Y': 0 + 2,
        'C Z': 3 + 3,
    }

    return sum([all_combinations[line] for line in inp])


def part_2(inp):
    # A Rock 1
    # B Paper 2
    # C Scissors 3

    # X Lose
    # Y Draw
    # Z Win

    # W/D/L 0/3/6
    all_combinations = {
        'A X': 0 + 3,
        'A Y': 3 + 1,
        'A Z': 6 + 2,

        'B X': 0 + 1,
        'B Y': 3 + 2,
        'B Z': 6 + 3,

        'C X': 0 + 2,
        'C Y': 3 + 3,
        'C Z': 6 + 1,
    }

    return sum([all_combinations[line] for line in inp])


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
