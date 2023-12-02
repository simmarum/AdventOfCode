import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    return sum([
        int(
            re.search(r"\d", x).group(0) +
            re.search(r"\d", x[::-1]).group(0)
        )
        for x in inp])


def part_2(inp):
    lookup = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    l_pattern = '|'.join(sorted(re.escape(k) for k in lookup))
    r_pattern = '|'.join(sorted(re.escape(k[::-1]) for k in lookup))
    return sum([
        int(
            re.search(r"\d", re.sub(l_pattern, lambda m: lookup.get(m.group(0)), x)).group(0) +
            re.search(
                r"\d", re.sub(
                    r_pattern, lambda m: lookup.get(
                        m.group(0)[::-1]), x[::-1])).group(0)
        )
        for x in inp])


def main():
    inp = read_file()
    # res_1 = part_1(inp)
    # print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
