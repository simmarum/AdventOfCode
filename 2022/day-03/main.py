import string


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    prior_sum = 0
    for line in inp:
        line_a = line[:len(line) // 2]
        line_b = line[len(line) // 2:]
        common_char = set(line_a).intersection(line_b).pop()
        if common_char in string.ascii_lowercase:
            char_prior = ord(common_char) - ord('a') + 1
        else:
            char_prior = ord(common_char) - ord('A') + 1 + 26
        prior_sum += char_prior
    return prior_sum


def part_2(inp):
    prior_sum = 0
    inp_iter = iter(inp)
    for line_a, line_b, line_c in zip(inp_iter, inp_iter, inp_iter):
        common_char = set(line_a).intersection(
            line_b).intersection(line_c).pop()
        if common_char in string.ascii_lowercase:
            char_prior = ord(common_char) - ord('a') + 1
        else:
            char_prior = ord(common_char) - ord('A') + 1 + 26
        prior_sum += char_prior
    return prior_sum


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
