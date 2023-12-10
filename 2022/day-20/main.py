from collections import deque


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [int(line) for line in f.readlines()]


def part_1(inp):
    zero_val = (inp.index(0), 0)
    buffer = deque(enumerate(inp))
    original_appears = buffer.copy()
    for i in original_appears:
        idx = buffer.index(i)
        buffer.rotate(-idx)
        _, v = buffer.popleft()
        buffer.rotate(-v)
        buffer.appendleft(i)
    zero_idx = buffer.index(zero_val)
    res = sum(buffer[(zero_idx + magic_n) % len(buffer)][1]
              for magic_n in [1000, 2000, 3000])
    return res


def part_2(inp):
    inp = [x * 811589153 for x in inp]
    zero_val = (inp.index(0), 0)
    buffer = deque(enumerate(inp))
    original_appears = buffer.copy()
    for _ in range(10):
        for i in original_appears:
            idx = buffer.index(i)
            buffer.rotate(-idx)
            _, v = buffer.popleft()
            buffer.rotate(-v)
            buffer.appendleft(i)
    zero_idx = buffer.index(zero_val)
    res = sum(buffer[(zero_idx + magic_n) % len(buffer)][1]
              for magic_n in [1000, 2000, 3000])
    return res


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
