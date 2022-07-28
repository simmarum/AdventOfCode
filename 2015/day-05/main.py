from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    cnt = 0
    vowels = 'aeiou'
    for val in inp:
        if ('ab' in val) or ('cd' in val) or ('pq' in val) or ('xy' in val):
            continue
        if len([each for each in val if each in vowels]) < 3:
            continue
        if sum([c == val[idx + 1] for idx, c in enumerate(val[:-1])]) < 1:
            continue
        cnt += 1
    return cnt


def part_2(inp):
    cnt = 0
    for val in inp:
        check_1 = False
        tmp_pairs = defaultdict(set)
        for idx, c in enumerate(val[:-1]):
            tmp_key = f"{c}{val[idx+1]}"
            tmp_pairs[tmp_key].add(idx)
            tmp_pairs[tmp_key].add(idx + 1)
        for k, v in tmp_pairs.items():
            if len(v) >= 4:
                check_1 = True

        check_2 = sum([c == val[idx + 2]
                      for idx, c in enumerate(val[:-2])]) > 0
        if check_1 and check_2:
            cnt += 1

    return cnt


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
