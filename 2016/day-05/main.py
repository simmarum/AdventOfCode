import hashlib


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    key = inp[0]
    password = ''
    for i in range(10_000_000):
        h = hashlib.md5((key + str(i)).encode()).hexdigest()
        if h[0:5] == '00000':
            password += h[5]
            # print(password, i)
            if len(password) == 8:
                break

    if len(password) != 8:
        raise RuntimeError("Password is too short - increase range in loop")
    return password


def part_2(inp):
    key = inp[0]
    password = '________'
    for i in range(30_000_000):
        h = hashlib.md5((key + str(i)).encode()).hexdigest()
        if h[0:5] == '00000':
            if h[5] in '01234567':
                if password[int(h[5])] == '_':
                    password = password[:int(h[5])] + \
                        h[6] + password[int(h[5]) + 1:]
            # print(password, i, h[5], h[6])
            if '_' not in password:
                break

    if '_' in password:
        raise RuntimeError("Password is not complete - increase range in loop")
    return password


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
