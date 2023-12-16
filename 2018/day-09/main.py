from blist import blist


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    inp_split = inp[0].split()

    # players_cnt = 30
    players_cnt = int(inp_split[0])
    # last_marble = 5807
    last_marble = int(inp_split[6])

    players = blist([0] * players_cnt)
    marbles = blist([0])
    curr_idx = 0
    for i in range(1, last_marble + 1):
        if i % 23 == 0:
            curr_idx = ((curr_idx - 7) + len(marbles)) % len(marbles)
            players[i % players_cnt] += (i + marbles.pop(curr_idx + 1))
        else:
            curr_idx = (curr_idx + 2) % len(marbles)
            marbles.insert(curr_idx + 1, i)

    return max(players)


def part_2(inp):
    inp_split = inp[0].split()

    players_cnt = int(inp_split[0])
    last_marble = int(inp_split[6]) * 100

    players = blist([0] * players_cnt)
    marbles = blist([0])
    curr_idx = 0
    for i in range(1, last_marble + 1):
        if i % 23 == 0:
            curr_idx = ((curr_idx - 7) + len(marbles)) % len(marbles)
            players[i % players_cnt] += (i + marbles.pop(curr_idx + 1))
        else:
            curr_idx = (curr_idx + 2) % len(marbles)
            marbles.insert(curr_idx + 1, i)

    return max(players)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
