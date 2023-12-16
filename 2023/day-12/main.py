from functools import cache


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


@cache
def resolve_springs(springs, rules):
    springs = springs.lstrip(".")
    if springs == '':  # end of entry
        if rules == ():  # no more blocks
            return 1
        else:
            return 0
    if rules == ():  # no more blocks
        if '#' in springs:  # there is bad spring
            return 0
        else:
            return 1
    if springs[0] == '#':  # we proceed bad string
        # no more space or there is good spring one on the path
        if (len(springs) < rules[0]) or (
                '.' in springs[:rules[0]]):
            return 0
        elif len(springs) == rules[0]:  # last possible combination
            if len(rules) == 1:
                return 1
            else:
                return 0
        elif springs[rules[0]] == '#':  # next spring is bad spring
            return 0
        else:  # good combination so remove one block/rule and repeat
            return resolve_springs(
                springs[rules[0] + 1:],
                rules[1:]
            )
    # we spot '?' replace with '#' or '.' (remove because we do not care about
    # dots)
    return resolve_springs(
        '#' + springs[1:], rules) + resolve_springs(springs[1:], rules)


def part_1(inp):
    sum_entries = 0
    for line in inp:
        line = line.strip().split(" ")
        springs = line[0]
        rules = tuple([int(c) for c in line[1].split(",")])
        sum_entries += resolve_springs(springs, rules)
    return sum_entries


def part_2(inp):
    sum_entries = 0
    for line in inp:
        line = line.strip().split(" ")
        springs = line[0]
        rules = tuple([int(c) for c in line[1].split(",")])
        springs = '?'.join([springs] * 5)
        rules = rules * 5
        sum_entries += resolve_springs(springs, rules)
    return sum_entries


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
