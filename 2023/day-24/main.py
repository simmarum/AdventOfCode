import re
from itertools import combinations
import sympy as sym


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    hailstones = sorted([list(map(int, re.findall(r'-?\d+', line)))
                         for line in inp])
    hailstones_pairs = combinations(hailstones, 2)
    area_min = 200000000000000
    area_max = 400000000000000
    collisions = 0
    for hpa, hpb in hailstones_pairs:
        apx, apy, apz, avx, avy, avz = hpa
        bpx, bpy, bpz, bvx, bvy, bvz = hpb
        ma = avy / avx
        mb = bvy / bvx
        if ma == mb:
            continue
        ca = apy - (ma * apx)
        cb = bpy - (mb * bpx)
        x = (cb - ca) / (ma - mb)
        y = ma * x + ca

        t1 = (x - apx) / avx
        t2 = (x - bpx) / bvx
        if t1 < 0 or t2 < 0:
            continue
        if (area_min <= x <= area_max) and (area_min <= y <= area_max):
            collisions += 1

    return collisions


def part_2(inp):
    hailstones = sorted([list(map(int, re.findall(r'-?\d+', line)))
                         for line in inp])
    hA, hB, hC = hailstones[0:3]
    apx, apy, apz, avx, avy, avz = hA
    bpx, bpy, bpz, bvx, bvy, bvz = hB
    cpx, cpy, cpz, cvx, cvy, cvz = hC

    spx, spy, spz, svx, svy, svz, t1, t2, t3 = sym.symbols(
        'spx,spy,spz,svx,svy,svz,t1,t2,t3')

    spx, spy, spz, svx, svy, svz, t1, t2, t3 = sym.solve(
        [
            sym.Eq(spx + svx * t1, apx + avx * t1),
            sym.Eq(spy + svy * t1, apy + avy * t1),
            sym.Eq(spz + svz * t1, apz + avz * t1),
            sym.Eq(spx + svx * t2, bpx + bvx * t2),
            sym.Eq(spy + svy * t2, bpy + bvy * t2),
            sym.Eq(spz + svz * t2, bpz + bvz * t2),
            sym.Eq(spx + svx * t3, cpx + cvx * t3),
            sym.Eq(spy + svy * t3, cpy + cvy * t3),
            sym.Eq(spz + svz * t3, cpz + cvz * t3),
        ],
        (spx, spy, spz, svx, svy, svz, t1, t2, t3)
    )[0]

    return spx + spy + spz


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
