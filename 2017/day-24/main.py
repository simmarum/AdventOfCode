from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def parse_components(inp):
    components = defaultdict(set)
    for l in inp:
        a, b = [int(x) for x in l.split('/')]
        components[a].add(b)
        components[b].add(a)
    return components


def poss_bridges(bridge, components):
    bridge = bridge or [(0, 0)]
    cur = bridge[-1][1]
    for b in components[cur]:
        if not ((cur, b) in bridge or (b, cur) in bridge):
            new = bridge + [(cur, b)]
            yield new
            yield from poss_bridges(new, components)


def solve(inp):
    components = parse_components(inp)
    mx = []
    for bridge in poss_bridges(None, components):
        mx.append((len(bridge), sum(a + b for a, b in bridge)))
    return mx


def part_1(inp):
    solution = solve(inp)
    return sorted(solution, key=lambda x: x[1])[-1][1]


def part_2(inp):
    solution = solve(inp)
    return sorted(solution)[-1][1]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
