from collections import Counter


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return f.read()


def part_1(inp):
    cnt = 0
    for d in inp.split("\n\n"):
        d = d.replace("\n", "")
        cnt += len(set([c for c in d]))

    return cnt


def part_2(inp):
    cnt = 0
    for d in inp.split("\n\n"):
        people = len(d.split("\n"))
        d = d.replace("\n", "")
        ans_counter = Counter(d)
        good_ans = {q: count for q, count in ans_counter.items()
                    if count == people}
        cnt += len(good_ans)
    return cnt


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
