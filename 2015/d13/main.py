from itertools import permutations


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line.replace("\n", "").replace(".", "")) for line in f.readlines()]


def part_1(inp):
    sit = {}
    people = set()
    for val in inp:
        p1, _, op, m, _, _, _, _, _, _, p2 = val.split(" ")
        if op == "lose":
            m = -int(m)
        else:
            m = int(m)
        sit[f"{p1}_{p2}"] = m
        people.add(p1)
        people.add(p2)
    people = list(people)
    people_len = len(people)
    max_s = float('-inf')
    for one_per in permutations(people, people_len):
        s = 0
        for i in range(people_len):
            s += sit[f"{one_per[i]}_{one_per[(i+1) % people_len]}"]
            s += sit[f"{one_per[(i+1) % people_len]}_{one_per[i]}"]
        max_s = max(max_s, s)
    return max_s


def part_2(inp):
    sit = {}
    people = set()
    for val in inp:
        p1, _, op, m, _, _, _, _, _, _, p2 = val.split(" ")
        if op == "lose":
            m = -int(m)
        else:
            m = int(m)
        sit[f"{p1}_{p2}"] = m
        people.add(p1)
        people.add(p2)
    people = list(people)
    for person in people:
        sit[f"<myself>_{person}"] = 0
        sit[f"{person}_<myself>"] = 0
    people.append("<myself>")
    people_len = len(people)
    max_s = float('-inf')
    for one_per in permutations(people, people_len):
        s = 0
        for i in range(people_len):
            s += sit[f"{one_per[i]}_{one_per[(i+1) % people_len]}"]
            s += sit[f"{one_per[(i+1) % people_len]}_{one_per[i]}"]
        max_s = max(max_s, s)
    return max_s


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
