from itertools import islice, takewhile
from more_itertools import locate


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def parse_inp(inp):
    pots = inp[0].replace('initial state: ', '')
    rules = {}
    for line in inp[2:]:
        r = line.split(' => ')
        rules[r[0]] = r[1]
    return pots, rules


def part_1(inp):
    pots, rules = parse_inp(inp)
    left_add = 0
    # print("0", ('.'*(5-left_add))+pots)
    for gen in range(1, 21):
        start_dot_cnt = sum(1 for _ in takewhile(lambda c: c == '.', pots))
        tmp_left_add = max(0, (5-start_dot_cnt))
        pots = ('.'*tmp_left_add)+pots
        left_add += tmp_left_add

        end_dot_cnt = sum(1 for _ in takewhile(
            lambda c: c == '.', reversed(pots)))
        tmp_left_add = max(0, (5-end_dot_cnt))
        pots = pots+('.'*tmp_left_add)

        pots = ''.join([rules.get(''.join(x), '.') for x in zip(
            islice(pots, 0, None, 1),
            islice(pots, 1, None, 1),
            islice(pots, 2, None, 1),
            islice(pots, 3, None, 1),
            islice(pots, 4, None, 1),
        )])
        left_add -= 2
        # print(gen, left_add, ('.'*(5-left_add))+pots)
    indices = sum([i-left_add for i in locate(pots, lambda x: x == '#')])
    return indices


def part_2(inp):
    pots, rules = parse_inp(inp)
    left_add = 0
    magic_sums = []
    magic_diffs = []
    # Do only first 3k gens to check for some pattern - cheese way ; )
    for gen in range(1, 3000+1):
        start_dot_cnt = sum(1 for _ in takewhile(lambda c: c == '.', pots))
        tmp_left_add = max(0, (5-start_dot_cnt))
        pots = ('.'*tmp_left_add)+pots
        left_add += tmp_left_add

        end_dot_cnt = sum(1 for _ in takewhile(
            lambda c: c == '.', reversed(pots)))
        tmp_left_add = max(0, (5-end_dot_cnt))
        pots = pots+('.'*tmp_left_add)

        pots = ''.join([rules.get(''.join(x), '.') for x in zip(
            islice(pots, 0, None, 1),
            islice(pots, 1, None, 1),
            islice(pots, 2, None, 1),
            islice(pots, 3, None, 1),
            islice(pots, 4, None, 1),
        )])
        left_add -= 2
        magic_sums.append(
            sum([i-left_add for i in locate(pots, lambda x: x == '#')]))
        if gen > 1:
            magic_diffs.append(magic_sums[-1]-magic_sums[-2])
        if gen > 10:
            # I assume that at least 10 gens need to generate the same diff
            #   it is at least last 10 gens add the same amount of plants
            if len(set(magic_diffs[-10:])) == 1:
                print(gen, magic_diffs[-1], magic_sums[-1])
                return magic_sums[-1]+((50000000000-gen)*magic_diffs[-1])


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
