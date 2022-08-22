def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def cheesy():
    # Manually resolve program to avoid endless loop :(

    # cpy a d
    # cpy 4 c
    # cpy 643 b
    # inc d
    # dec b
    # jnz b -2
    # dec c
    # jnz c -5
    # ^^^^^^^^^^^^ d = a + (4 * 643)

    # cpy d a
    # jnz 0 0
    # cpy a b
    # cpy 0 a
    # cpy 2 c
    # jnz b 2
    # jnz 1 6
    # dec b
    # dec c
    # jnz c -4
    # inc a
    # jnz 1 -7
    # cpy 2 b
    # jnz c 2
    # jnz 1 4
    # dec b
    # dec c
    # jnz 1 -4
    # jnz 0 0
    # out b
    # jnz a -19
    # jnz 1 -21
    # ^^^^^^^^^^^^ this code prints 0 or 1 as binary representation of 'd'

    for a in range(500):
        d = a + (4 * 643)
        tmp_str = "{0:b}".format(d)
        if tmp_str == '101010101010':
            return a
    return None


def part_1(inp):
    return cheesy()


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
