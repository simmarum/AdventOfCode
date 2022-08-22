from collections import deque


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def elf_left(magic_num):
    output = []
    while magic_num > 1:
        if magic_num % 2 == 0:
            output.append(0)
        else:
            output.append(1)
        magic_num = magic_num // 2
    res = 1
    for i, v in enumerate(output, 1):
        if v == 1:
            res = res + (2**i)
    return res


def elf_across(magic_num):
    left = deque()
    right = deque()
    for i in range(1, magic_num + 1):
        if i < (magic_num // 2) + 1:
            left.append(i)
        else:
            right.appendleft(i)
    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        # rotate
        right.appendleft(left.popleft())
        left.append(right.pop())
    return left[0] or right[0]


def part_1(inp):
    magic_num = int(inp[0])
    return elf_left(magic_num)


def part_2(inp):
    magic_num = int(inp[0])
    return elf_across(magic_num)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
