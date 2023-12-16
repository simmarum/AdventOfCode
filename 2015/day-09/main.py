from itertools import permutations


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line.replace("\n", "")) for line in f.readlines()]


def part_1(inp):
    dist = {}
    cities = set()
    for val in inp:
        m1, _, m2, _, d = val.split(" ")
        cities.add(m1)
        cities.add(m2)
        dist[f"{m1}_{m2}"] = int(d)
        dist[f"{m2}_{m1}"] = int(d)
    cities = list(cities)
    min_dst = float('inf')
    for cmb in permutations(cities, len(cities)):
        d = 0
        for idx, k in enumerate(cmb[:-1]):
            d += dist[f"{k}_{cmb[idx+1]}"]
        min_dst = min(min_dst, d)
    return min_dst


def part_2(inp):
    dist = {}
    cities = set()
    for val in inp:
        m1, _, m2, _, d = val.split(" ")
        cities.add(m1)
        cities.add(m2)
        dist[f"{m1}_{m2}"] = int(d)
        dist[f"{m2}_{m1}"] = int(d)
    cities = list(cities)
    max_dst = float('-inf')
    for cmb in permutations(cities, len(cities)):
        d = 0
        for idx, k in enumerate(cmb[:-1]):
            d += dist[f"{k}_{cmb[idx+1]}"]
        max_dst = max(max_dst, d)
    return max_dst


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
