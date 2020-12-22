def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [line for line in f.read().split("\n\n")]


def part_1(inp):
    d1 = list(map(int, inp[0].split("\n")[1:]))
    d2 = list(map(int, inp[1].split("\n")[1:]))
    while d1 and d2:
        c1 = d1.pop(0)
        c2 = d2.pop(0)
        if c1 > c2:
            d1.extend([c1, c2])
        else:
            d2.extend([c2, c1])
    win_deck = d1 if d1 else d2

    ss = 0
    for i, e in enumerate(reversed(win_deck), 1):
        ss += i*e
    return ss


def _print(m, p=False):
    if p:
        print(m)


def _recurse_game(d1, d2, game_idx):
    _print(f"=== Game {game_idx}===\n")
    ri = 0
    decks_config = {1: set(), 2: set()}
    while d1 and d2:
        ri += 1
        _print(f"-- Round {ri} (Game {game_idx})")
        _print(f"P1 deck: {d1}")
        _print(f"P2 deck: {d2}")
        d1s = ','.join(map(str, d1))
        d2s = ','.join(map(str, d2))
        if d1s in decks_config[1] and d2s in decks_config[2]:
            _print("P1 and P2 have the same decks again")
            d1 = [-1]
            d2 = []
            break
        decks_config[1].add(d1s)
        decks_config[2].add(d2s)
        c1 = d1.pop(0)
        c2 = d2.pop(0)
        _print(f"P1 card: {c1}")
        _print(f"P2 card: {c2}")
        if len(d1) >= c1 and len(d2) >= c2:
            _print(f"Go to sub-game: {game_idx+1}")
            rd1, rd2 = _recurse_game(d1[:c1], d2[:c2], game_idx+1)
            _print(f"Return from sub-game: {game_idx+1}")
            if rd1:
                d1.extend([c1, c2])
                _print(f"P1 wins round {ri} of game {game_idx}\n")
            else:
                d2.extend([c2, c1])
                _print(f"P2 wins round {ri} of game {game_idx}\n")
        else:
            if c1 > c2:
                _print(f"P1 wins round {ri} of game {game_idx}\n")
                d1.extend([c1, c2])
            else:
                d2.extend([c2, c1])
                _print(f"P2 wins round {ri} of game {game_idx}\n")
    if d1:
        _print(f"P1 wins game {game_idx}\n")
    else:
        _print(f"P2 wins game {game_idx}\n")
    return d1, d2


def part_2(inp):
    d1 = list(map(int, inp[0].split("\n")[1:]))
    d2 = list(map(int, inp[1].split("\n")[1:]))

    d1, d2 = _recurse_game(d1, d2, 1)
    win_deck = d1 if d1 else d2
    _print(f"Win deck: {win_deck}")
    ss = 0
    for i, e in enumerate(reversed(win_deck), 1):
        ss += i*e
    return ss


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
