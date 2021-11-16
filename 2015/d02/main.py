from collections import Counter


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    all_paper = 0
    for val in inp:
        l, w, h = [int(x) for x in val.split("x")]
        a = l*w
        b = l*h
        c = w*h
        trash = min(a, b, c)
        present = 2*a + 2*b + 2*c + trash
        all_paper += present
    return all_paper


def part_2(inp):
    all_ribbon = 0
    for val in inp:
        l, w, h = [int(x) for x in val.split("x")]
        a = min(l, w, h)
        b = min(list((Counter([l, w, h]) - Counter([a])).elements()))
        all_ribbon += ((a+a+b+b) + (l*w*h))
    return all_ribbon


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
