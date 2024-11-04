from collections import defaultdict, deque


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def read_stars(inp):
    return [tuple(map(int, line.split(","))) for line in inp]


def find_constellations(stars):
    constellations = defaultdict(set)
    for s1i, s1 in enumerate(stars):
        for s2i, s2 in enumerate(stars):
            if (abs(s1[0] - s2[0]) + abs(s1[1] - s2[1]) +
                    abs(s1[2] - s2[2]) + abs(s1[3] - s2[3])) <= 3:
                constellations[s1i].add(s2i)

    seen = set()
    constellations_num = 0
    for si in range(len(stars)):
        if si not in seen:
            constellations_num += 1
            queue = deque()
            queue.append(si)
            while queue:
                si_seen = queue.popleft()
                if si_seen not in seen:
                    seen.add(si_seen)
                    [queue.append(cs) for cs in constellations[si_seen]]

    return constellations_num


def part_1(inp):
    stars = read_stars(inp)
    constellations_num = find_constellations(stars)
    return constellations_num


def part_2(inp):
    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
