from functools import reduce
from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.readlines()]


def part_1(inp):
    return sum(reduce(
        lambda x, y: (
            (x + ord(y)) * 17) %
        256, word + "", 0) for word in inp[0].split(","))


def part_2(inp):
    hashmap = defaultdict(lambda: defaultdict(int))
    for word in inp[0].split(","):
        label = word[:-1] if '-' in word else word[:-2]
        label_hash = reduce(
            lambda x, y: (
                (x + ord(y)) * 17) %
            256, label + "", 0)
        is_equal = '=' in word
        if is_equal:
            focus = int(word[-1])
            hashmap[label_hash][label] = focus
        else:
            if label in hashmap[label_hash]:
                del hashmap[label_hash][label]
    focus_power = 0
    for b, v in hashmap.items():
        focus_power += sum([(int(b) + 1) * idx *
                            e for idx, e in enumerate(list(v.values()), 1)])
    return focus_power


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
