from collections import defaultdict
import pprint


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.read().splitlines()]


def part_1(inp):
    dd = defaultdict(set)
    for val in inp:
        tmp_a = val.split(",")
        tmp_b = tmp_a[0].split("contain")
        outer = tmp_b[0].replace("bags", "").replace(
            "bag", "").strip().replace(" ", "_")
        for inner in (tmp_b[1:] + tmp_a[1:]):
            _, c1, c2, _ = (inner.strip().split(" ") + [None])[:4]
            dd[outer].add(f"{c1}_{c2}")

    while True:
        is_update = False
        for k, v in dd.items():
            tmp_new_d = v.copy()
            for ki in v:
                if ki in dd:
                    old_tmp_new_d = tmp_new_d.copy()
                    tmp_new_d.update(dd[ki])
                    if old_tmp_new_d != tmp_new_d:
                        is_update = True
            dd[k].update(tmp_new_d)
        if is_update:
            continue
        else:
            break
    cnt = 0
    for k, v in dd.items():
        if "shiny_gold" in v:
            cnt += 1
    return cnt


def part_2(inp):
    dd = defaultdict(set)
    for val in inp:
        tmp_a = val.split(",")
        tmp_b = tmp_a[0].split("contain")
        outer = tmp_b[0].replace("bags", "").replace(
            "bag", "").strip().replace(" ", "_")
        for inner in (tmp_b[1:] + tmp_a[1:]):
            n, c1, c2, _ = (inner.strip().split(" ") + [None])[:4]
            dd[outer].add((n, f"{c1}_{c2}"))

    def resolve(k, plate):
        cnt = 0
        for s in plate[k]:
            if s[1] == "other_bags.":
                cnt += 0
            else:
                cnt += int(s[0]) + int(s[0]) * resolve(s[1], plate)
        return cnt
    res = resolve('shiny_gold', dd)
    return res


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
