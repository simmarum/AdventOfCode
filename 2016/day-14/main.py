from calendar import c
from hashlib import md5
import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def get_hash(s, stretch_times):
    hash = md5((s).encode()).hexdigest().lower()
    if stretch_times > 0:
        for _ in range(stretch_times):
            hash = md5((hash).encode()).hexdigest().lower()
    return hash


def get_keys(salt, stretch_times, num_keys, num_gen_hash):
    all_hashes = [(i, get_hash((salt + str(i)), stretch_times))
                  for i in range(num_gen_hash)]
    all_hashes = [
        (h[0],
         h[1],
            re.search(
            r'([a-z0-9])\1{2}',
            h[1],
            flags=re.I)) for h in all_hashes]
    all_hashes = [
        (h[0],
         h[1],
            h[2][0]) if h[2] is not None else (
            h[0],
            h[1],
            None) for h in all_hashes]
    all_hashes = [
        (h[0],
         h[1],
            h[2],
            re.search(
            r'([a-z0-9])\1{4}',
            h[1],
            flags=re.I)) for h in all_hashes]
    all_hashes = [
        (h[0],
         h[1],
            h[2],
            h[3][0]) if h[3] is not None else (
            h[0],
            h[1],
            h[2],
            None) for h in all_hashes]

    good_hashes = []
    for i in range(len(all_hashes)):
        h3 = all_hashes[i]
        if h3[2] is None:
            continue
        tmp_val = h3[2] + h3[2][0] + h3[2][0]
        for h5 in all_hashes[i + 1:i + 1001]:
            if h5[3] is None:
                continue
            if h5[3] == tmp_val:
                good_hashes.append((h3, h5))
                break
        if len(good_hashes) == num_keys:
            break

    if len(good_hashes) < num_keys:
        for i, gh in enumerate(good_hashes):
            print(i, gh)
        raise RuntimeError("Do not find all keys!")

    return good_hashes[-1][0][0]


def part_1(inp):
    salt = inp[0]
    return get_keys(salt, 0, 64, 40_000)


def part_2(inp):
    salt = inp[0]
    return get_keys(salt, 2016, 64, 40_000)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
