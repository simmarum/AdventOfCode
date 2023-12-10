from collections import Counter


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    two_count = 0
    three_count = 0
    for box_id in inp:
        c = Counter(box_id)
        if 2 in list(c.values()):
            two_count += 1
        if 3 in list(c.values()):
            three_count += 1
    return two_count * three_count


def part_2(inp):
    for a in range(len(inp)):
        for b in range(a, len(inp)):
            diff_char = 0
            diff_position = -1
            for i in range(len(inp[a])):
                if inp[a][i] != inp[b][i]:
                    diff_char += 1
                    diff_position = i
            if diff_char == 1:
                return inp[a][:diff_position] + inp[a][diff_position + 1:]
    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
