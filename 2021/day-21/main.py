from functools import lru_cache


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    dice = 0
    roll_cnt = 0
    board = list(range(1, 11))
    end_points = 1000
    players_pos = dict()
    players_points = dict()
    for line in inp:
        x = line.split()
        players_pos[int(x[1])] = board.index(int(x[4]))
        players_points[int(x[1])] = 0
    for round in range(1, 1000):
        for player in players_pos.keys():
            rollout = []
            for _ in range(3):
                dice = (dice+1) % 100
                roll_cnt += 1
                rollout.append(dice)
            players_pos[player] = (players_pos[player] + sum(rollout)) % 10
            players_points[player] += board[players_pos[player]]
            # print(
            #     f"Player {player} rolls {rollout} and moves to space {board[players_pos[player]]} for a total points of {players_points[player]}.")
            if players_points[player] >= end_points:
                xx = list(players_points.keys())
                xx.remove(player)
                otherplayer = xx[0]
                otherplayer_points = players_points[otherplayer]
                return otherplayer_points * roll_cnt

    return None


@lru_cache(maxsize=None)
def play(players_pos, players_points, roll_cnt, board, end_points):
    if players_points[0] >= end_points:
        return 1, 0
    elif players_points[1] >= end_points:
        return 0, 1

    p1_wins = 0
    p2_wins = 0
    for dice in range(1, 1+3):
        player_id = (roll_cnt % 6) // 3
        new_pos = (players_pos[player_id] + dice) % 10
        if roll_cnt % 3 == 2:
            new_points = players_points[player_id] + board[new_pos]
        else:
            new_points = players_points[player_id]
        if player_id == 0:
            tmp_pos = (new_pos, players_pos[1])
            tmp_points = (new_points, players_points[1])
        else:
            tmp_pos = (players_pos[0], new_pos)
            tmp_points = (players_points[0], new_points)

        p1_win, p2_win = play(tmp_pos, tmp_points,
                              roll_cnt + 1, board, end_points)

        p1_wins += p1_win
        p2_wins += p2_win
    return p1_wins, p2_wins


def part_2(inp):
    roll_cnt = 0
    board = tuple(range(1, 11))
    end_points = 21
    players_pos = [0, 0]
    players_points = [0, 0]
    for i, line in enumerate(inp):
        x = line.split()
        players_pos[i] = board.index(int(x[4]))
        players_points[i] = 0

    p1_wins, p2_wins = play(
        tuple(players_pos), tuple(players_points), roll_cnt, board, end_points)
    return max((p1_wins, p2_wins))


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
