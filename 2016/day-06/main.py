from collections import Counter


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [list(str(line).replace('\n', '')) for line in f.readlines()]


def part_1(inp):
    trasnpose_data = [list(i) for i in zip(*inp)]
    message = ''.join([Counter(sublist).most_common(1)[0][0]
                       for sublist in trasnpose_data])
    return message


def part_2(inp):
    trasnpose_data = [list(i) for i in zip(*inp)]
    message = ''.join([Counter(sublist).most_common()[-1][0]
                       for sublist in trasnpose_data])
    return message


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
