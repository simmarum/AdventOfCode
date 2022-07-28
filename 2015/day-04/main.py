import hashlib


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    val = inp[0]
    idx = 1
    while True:
        h = hashlib.md5((val + str(idx)).encode("utf-8")).hexdigest()[0:5]
        if (h[0] == '0') and (h == len(h) * h[0]):
            return idx
        idx += 1


def part_2(inp):
    val = inp[0]
    idx = 1
    while True:
        h = hashlib.md5((val + str(idx)).encode("utf-8")).hexdigest()[0:6]
        if (h[0] == '0') and (h == len(h) * h[0]):
            return idx
        idx += 1


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
