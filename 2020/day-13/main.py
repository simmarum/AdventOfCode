from operator import mul
from functools import reduce


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [line for line in f.read().splitlines()]


def part_1(inp):
    n = int(inp[0])
    sched = list(map(int, list(set(inp[1].split(',')).difference(set(['x'])))))
    d = float('inf')
    act_s = 0
    for s in sched:
        y = s - (n % s)
        if y <= d:
            act_s = s
            d = y
    return act_s * d


def nwd(a, b):
    return nwd(b, a % b) if b else a


def nww(a, b):
    return a * b // nwd(a, b)


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def _check_nww(s):
    x = reduce(nww, [v[1] for v in s])
    y = reduce(mul, [v[1] for v in s])
    if x == y:
        return y
    else:
        raise RuntimeError("Numbers are not relatively first!")


def part_2(inp):
    # Chinese remainder theorem
    sched = [(int(v) - i, int(v))
             for i, v in enumerate(inp[1].split(',')) if v != 'x']
    n = _check_nww(sched)
    sched = [(v[0], v[1], n // v[1], mul_inv(n // v[1], v[1])) for v in sched]
    ss = 0
    sm = 1
    for v in sched:
        ss += v[0] * v[3] * v[2]
        sm *= v[1]
    res = ss % sm
    return res


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
