import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    red_max_pos = 12
    green_max_pos = 13
    blue_max_pos = 14
    all_data = {}
    good_games = []
    for line in inp:
        game_id = int(re.search(r"Game (\d+)", line).group(1))
        all_data[game_id] = []
        for one_turn in line.split(":")[1].split(";"):
            # print(one_turn)
            m = re.search(r"(\d+) red", one_turn)
            if m:
                red = int(m.group(1))
            else:
                red = 0
            m = re.search(r"(\d+) green", one_turn)
            if m:
                green = int(m.group(1))
            else:
                green = 0
            m = re.search(r"(\d+) blue", one_turn)
            if m:
                blue = int(m.group(1))
            else:
                blue = 0
            all_data[game_id].append([red, green, blue])
        red_max = max([x[0] for x in all_data[game_id]])
        green_max = max([x[1] for x in all_data[game_id]])
        blue_max = max([x[2] for x in all_data[game_id]])
        game_is_possible = True
        game_is_possible = game_is_possible and (red_max <= red_max_pos)
        game_is_possible = game_is_possible and (green_max <= green_max_pos)
        game_is_possible = game_is_possible and (blue_max <= blue_max_pos)
        if game_is_possible:
            good_games.append(game_id)
    return sum(good_games)


def part_2(inp):
    all_data = {}
    good_games_multiply = []
    for line in inp:
        game_id = int(re.search(r"Game (\d+)", line).group(1))
        all_data[game_id] = []
        for one_turn in line.split(":")[1].split(";"):
            # print(one_turn)
            m = re.search(r"(\d+) red", one_turn)
            if m:
                red = int(m.group(1))
            else:
                red = 0
            m = re.search(r"(\d+) green", one_turn)
            if m:
                green = int(m.group(1))
            else:
                green = 0
            m = re.search(r"(\d+) blue", one_turn)
            if m:
                blue = int(m.group(1))
            else:
                blue = 0
            all_data[game_id].append([red, green, blue])
        red_max = max([x[0] for x in all_data[game_id]])
        green_max = max([x[1] for x in all_data[game_id]])
        blue_max = max([x[2] for x in all_data[game_id]])
        good_games_multiply.append(red_max * green_max * blue_max)
    return sum(good_games_multiply)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
