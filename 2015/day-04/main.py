import _md5
from multiprocessing import Pool
from math import ceil


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def f_1(val, idx_min, idx_max):
    for idx in range(idx_min, idx_max + 1):
        if '00000' == _md5.md5((val + str(idx)).encode("utf-8")).hexdigest()[0:5]:  # noqa
            return idx
    return None


def part_1(inp):
    val = inp[0]
    pool_size = 6
    max_size = 1_000_000
    chunk_size = int(ceil(max_size / pool_size))
    args = []
    for pool_num in range(pool_size):
        args.append(
            (val, chunk_size * pool_num, min(chunk_size * (pool_num + 1), max_size))
        )
    with Pool(pool_size) as p:
        res = p.starmap(f_1, args)
        return [r for r in res if r is not None][0]


def f_2(val, idx_min, idx_max):
    for idx in range(idx_min, idx_max + 1):
        if '000000' == _md5.md5((val + str(idx)).encode("utf-8")).hexdigest()[0:6]:  # noqa
            return idx
    return None


def part_2(inp):
    val = inp[0]
    pool_size = 6
    max_size = 10_000_000
    chunk_size = int(ceil(max_size / pool_size))
    args = []
    for pool_num in range(pool_size):
        args.append(
            (val, chunk_size * pool_num, min(chunk_size * (pool_num + 1), max_size))
        )
    with Pool(pool_size) as p:
        res = p.starmap(f_2, args)
        return [r for r in res if r is not None][0]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
