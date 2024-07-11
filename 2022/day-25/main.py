def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.readlines() if line]


def snafu_sum(inp):
    snafu_decoder = {
        '2': 2,
        '1': 1,
        '0': 0,
        '-': -1,
        '=': -2
    }
    snafu_encoder = {v: k for k, v in snafu_decoder.items()}
    snafu_max_digit = 32
    snafu_sum = [0] * snafu_max_digit
    for snafu in inp:
        for i, c in enumerate(snafu[::-1]):
            snafu_sum[snafu_max_digit - 1 - i] += snafu_decoder[c]

    for i in range(len(snafu_sum) - 1, -1, -1):
        a = snafu_sum[i] // 5
        b = snafu_sum[i] % 5
        if b > 2:
            b = b - 5
            a += 1
        snafu_sum[i] = b
        snafu_sum[i - 1] += a

    return ''.join([snafu_encoder[c] for c in snafu_sum]).lstrip('0')


def part_1(inp):
    return snafu_sum(inp)


def part_2(inp):
    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
