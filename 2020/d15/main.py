from collections import deque


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [line for line in f.read().splitlines()]


def part_1(inp):
    game = list(map(int, inp[0].split(",")[::-1]))
    lgame = len(game)
    for _ in range(lgame, 2020):
        last_num = game[0]
        previous_turn = None
        if last_num in game[1:]:
            previous_turn = game.index(last_num, 1)
            game.insert(0, previous_turn)
        else:
            game.insert(0, 0)
    return game[0]


def part_2(inp):
    nums = list(map(int, inp[0].split(",")))
    game_d = {x: deque([idx+1], maxlen=2) for idx, x in enumerate(nums)}
    lgame = len(game_d)
    last_num = nums[-1]
    for i in range(lgame, 1+30000000):
        if len(game_d[last_num]) == 2:
            new_num = game_d[last_num][1] - game_d[last_num][0]
        else:
            new_num = 0
        if new_num in game_d:
            game_d[new_num].append(i)
        else:
            game_d[new_num] = deque([i], maxlen=2)
        last_num = new_num
    return last_num
    # game = list(map(int, inp[0].split(",")[::-1]))
    # lgame = len(game)
    # for _ in range(lgame, 30000000):
    #     last_num = game[0]
    #     previous_turn = None
    #     if last_num in game[1:]:
    #         previous_turn = game.index(last_num, 1)
    #         game.insert(0, previous_turn)
    #     else:
    #         game.insert(0, 0)
    # return game[0]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
