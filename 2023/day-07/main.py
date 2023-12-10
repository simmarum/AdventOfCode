from collections import Counter


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    games = [
        [
            line.split(" ")[0],  # hand
            int(line.split(" ")[1]),  # bid
            None,  # hand_type
        ]
        for line in inp]
    order = [c for c in '23456789TJQKA']
    hand_type_lookup = {
        '11111': '2',
        '2111': '3',
        '221': '4',
        '311': '5',
        '32': '6',
        '41': '7',
        '5': '8'
    }
    for game in games:
        hand_cnt = ''.join([str(x[1]) for x in Counter(game[0]).most_common()])
        game[2] = hand_type_lookup[hand_cnt] + game[0]
    games = sorted(
        games,
        key=lambda x: [
            order.index(c) for c in x[2]],
        reverse=False)
    return sum([x[1] * (idx + 1) for idx, x in enumerate(games)])


def part_2(inp):
    games = [
        [
            line.split(" ")[0],  # hand
            int(line.split(" ")[1]),  # bid
            None,  # hand_type
        ]
        for line in inp]
    order = [c for c in 'J23456789TQKA']
    hand_type_lookup = {
        '0_11111': '2',
        '0_2111': '3',
        '0_221': '4',
        '0_311': '5',
        '0_32': '6',
        '0_41': '7',
        '0_5': '8',

        '1_1111': '3',
        '1_211': '5',
        '1_22': '6',
        '1_31': '7',
        '1_4': '8',

        '2_111': '5',
        '2_21': '7',
        '2_3': '8',

        '3_11': '7',
        '3_2': '8',

        '4_1': '8',

        '5_0': '8',
    }
    for game in games:
        game_no_j = game[0].replace("J", "")
        num_of_j = len(game[0]) - len(game_no_j)
        if num_of_j == 5:
            hand_cnt = '5_0'
        else:
            hand_cnt = str(
                num_of_j) + "_" + ''.join([str(x[1]) for x in Counter(game_no_j).most_common()])
        game[2] = hand_type_lookup[hand_cnt] + game[0]
    games = sorted(
        games,
        key=lambda x: [
            order.index(c) for c in x[2]],
        reverse=False)
    return sum([x[1] * (idx + 1) for idx, x in enumerate(games)])


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
