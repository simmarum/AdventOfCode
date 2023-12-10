from functools import reduce


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.readlines()]


def part_1(inp):
    rules = inp[0]
    map = {
        x.split("=")[0].strip(): (
            x.split("=")[1].split(",")[0].replace("(", "").strip(),
            x.split("=")[1].split(",")[1].replace(")", "").strip()
        ) for x in inp[2:]
    }
    current_place = 'AAA'
    step = 0
    while current_place != 'ZZZ':
        step += 1
        if rules[(step - 1) % len(rules)] == 'R':
            current_place = map[current_place][1]
        if rules[(step - 1) % len(rules)] == 'L':
            current_place = map[current_place][0]
    return step


def nwd(a, b): return nwd(b, a % b) if b else a
def nww(a, b): return a * b // nwd(a, b)


def part_2(inp):
    rules = inp[0]
    map = {
        x.split("=")[0].strip(): (
            x.split("=")[1].split(",")[0].replace("(", "").strip(),
            x.split("=")[1].split(",")[1].replace(")", "").strip()
        ) for x in inp[2:]
    }
    current_places = [x for x in map.keys() if x[-1] == 'A']
    steps = [0 for _ in current_places]
    for idx, _ in enumerate(current_places):
        while current_places[idx][-1] != 'Z':
            steps[idx] += 1
            if rules[(steps[idx] - 1) % len(rules)] == 'R':
                current_places[idx] = map[current_places[idx]][1]
            if rules[(steps[idx] - 1) % len(rules)] == 'L':
                current_places[idx] = map[current_places[idx]][0]

    return reduce(nww, steps)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
