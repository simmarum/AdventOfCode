import string
import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    polymer = inp[0]
    regex_patter = "|".join(
        [f"{char}{char.upper()}|{char.upper()}{char}" for char in string.ascii_lowercase])
    polymer_len = len(polymer)
    while True:
        polymer = re.sub(regex_patter, "", polymer, count=0, flags=0)
        if len(polymer) == polymer_len:
            return polymer_len
        else:
            polymer_len = len(polymer)
    return None


def part_2(inp):
    polymer = inp[0]
    regex_patter = "|".join(
        [f"{char}{char.upper()}|{char.upper()}{char}" for char in string.ascii_lowercase])
    min_polymer_len = len(polymer)
    for char in string.ascii_lowercase:
        remove_pattern = f"{char}|{char.upper()}"
        tmp_polymer = re.sub(remove_pattern, "", polymer, count=0, flags=0)
        polymer_len = len(tmp_polymer)
        while True:
            tmp_polymer = re.sub(
                regex_patter, "", tmp_polymer, count=0, flags=0)
            if len(tmp_polymer) == polymer_len:
                min_polymer_len = min(polymer_len, min_polymer_len)
                break
            else:
                polymer_len = len(tmp_polymer)
    return min_polymer_len


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
