from collections import defaultdict
import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def simulate_bots(inp, part_2):
    bots = defaultdict(list)
    outputs = defaultdict(list)
    search_min = 17
    search_max = 61

    instructions_move = {}
    for line in inp:
        m = re.search('value (\\d+) goes to bot (\\d+)', line)
        if m:
            bots[int(m.group(2))].append(int(m.group(1)))
        m = re.search(
            'bot (\\d+) gives low to (bot|output) (\\d+) and high to (bot|output) (\\d+)',
            line)
        if m:
            instructions_move[int(m.group(1))] = (
                m.group(2), int(m.group(3)), m.group(4), int(m.group(5)))

    search_bot = None
    while bots:
        for bot_num, bot_chips in dict(bots).items():
            if len(bot_chips) == 2:
                min_c, max_c = sorted(bot_chips)
                del bots[bot_num]
                if (min_c == search_min) and (max_c == search_max):
                    search_bot = bot_num
                if instructions_move[bot_num][0] == 'bot':
                    bots[instructions_move[bot_num][1]].append(min_c)
                if instructions_move[bot_num][0] == 'output':
                    outputs[instructions_move[bot_num][1]].append(min_c)

                if instructions_move[bot_num][2] == 'bot':
                    bots[instructions_move[bot_num][3]].append(max_c)
                if instructions_move[bot_num][2] == 'output':
                    outputs[instructions_move[bot_num][3]].append(max_c)

    if not part_2:
        return search_bot
    else:
        return outputs[0][0] * outputs[1][0] * outputs[2][0]


def part_1(inp):
    return simulate_bots(inp, False)


def part_2(inp):
    return simulate_bots(inp, True)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
