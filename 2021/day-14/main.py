from more_itertools import pairwise
from collections import Counter
from collections import defaultdict
import copy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    data = [x for x in inp if ('->' not in x) and ('' != x)][0]
    rules = [x.replace(' ', '').split('->')
             for x in inp if '->' in x]
    rules = {v[0]: f'{v[0][0]}{v[1]}' for v in rules}
    for _ in range(10):
        data = ''.join([rules.get(''.join(c), c)
                        for c in pairwise(data)]) + data[-1]
    c = Counter(data)
    max_c = c[max(c, key=c.get)]
    min_c = c[min(c, key=c.get)]
    return max_c - min_c


def part_2(inp):
    data = [x for x in inp if ('->' not in x) and ('' != x)][0]
    rules = [x.replace(' ', '').split('->')
             for x in inp if '->' in x]
    rules = {v[0]: [f'{v[0][0]}{v[1]}', f'{v[1]}{v[0][1]}'] for v in rules}
    freq = defaultdict(int)
    for c in pairwise(data):
        freq[''.join(c)] += 1
    for _ in range(40):
        nfreq = copy.deepcopy(freq)
        for k, v in freq.items():
            new_v = rules.get(k, None)
            if new_v:
                nfreq[k] -= v
                nfreq[new_v[0]] += v
                nfreq[new_v[1]] += v
        freq = copy.deepcopy(nfreq)
    data_c = defaultdict(int)
    for k, v in freq.items():
        data_c[k[0]] += v
        data_c[k[1]] += v

    data_c[data[0]] += 1
    data_c[data[-1]] += 1
    c = Counter(data_c)
    c = {k: v // 2 for k, v in data_c.items()}
    max_c = c[max(c, key=c.get)]
    min_c = c[min(c, key=c.get)]
    return max_c - min_c


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
