from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    points = 0
    for line in inp:
        numbers = line.split(":")[1]
        win_nums = set([int(x.strip())
                        for x in numbers.split("|")[0].strip().split(" ")
                        if x.strip() != ""])
        your_nums = set([int(x.strip())
                         for x in numbers.split("|")[1].strip().split(" ")
                         if x.strip() != ""])
        win_cnt = len(your_nums.intersection(win_nums))
        points += 2 ** (win_cnt - 1) if (win_cnt - 1) >= 0 else 0
    return points


def part_2(inp):
    cards_copies = defaultdict(int)
    for line in inp:
        card_id = int(line.split(":")[0].replace("Card ", "").strip()) - 1
        cards_copies[card_id] += 1
        numbers = line.split(":")[1]
        win_nums = set([int(x.strip())
                        for x in numbers.split("|")[0].strip().split(" ")
                        if x.strip() != ""])
        your_nums = set([int(x.strip())
                         for x in numbers.split("|")[1].strip().split(" ")
                         if x.strip() != ""])
        win_cnt = len(your_nums.intersection(win_nums))
        for i in range(1, win_cnt + 1):
            cards_copies[card_id + i] += cards_copies[card_id]

    return sum(cards_copies.values())


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
