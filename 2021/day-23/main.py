import heapq
from dataclasses import dataclass
import heapq


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


@dataclass(frozen=True)
class State:
    energy: int
    rooms: tuple
    hallway: tuple = (None,) * 11

    def __lt__(self, other):
        return self.energy < other.energy

    @property
    def fingerprint(self):
        return (self.hallway, self.rooms)

    @property
    def is_done(self):
        return all(h is None for h in self.hallway) and all(
            all([a == i for a in room]) for i, room in enumerate(self.rooms)
        )


def insert(tpl, i, new):
    return tpl[:i] + (new,) + tpl[i + 1:]


def solve(rooms):
    exits = (2, 4, 6, 8)
    room_size = len(rooms[0])
    todo = [State(0, rooms)]
    visited = set()
    while todo:
        state = heapq.heappop(todo)
        if state.is_done:
            return state.energy
        if state.fingerprint in visited:
            continue
        visited.add(state.fingerprint)
        for ri, room in enumerate(state.rooms):
            if room and not all(a == ri for a in room):
                a = room[-1]
                for to, d in ((-1, -1), (11, 1)):
                    for hi in range(exits[ri] + d, to, d):
                        if hi in exits:
                            continue
                        if state.hallway[hi] is not None:
                            break
                        new = State(
                            state.energy
                            + (room_size - len(room) + 1 + abs(exits[ri] - hi))
                            * (10 ** a),
                            insert(state.rooms, ri, room[:-1]),
                            insert(state.hallway, hi, a),
                        )
                        if new.fingerprint not in visited:
                            heapq.heappush(todo, new)
        for i, a in enumerate(state.hallway):
            if a is None:
                continue
            if i < exits[a] and any(
                u is not None for u in state.hallway[i + 1: exits[a]]
            ):
                continue
            if i > exits[a] and any(
                u is not None for u in state.hallway[exits[a] + 1: i]
            ):
                continue
            if any(u != a for u in state.rooms[a]):
                continue
            new = State(
                state.energy
                + (room_size - len(state.rooms[a]) +
                   abs(exits[a] - i)) * (10 ** a),
                insert(state.rooms, a, (state.rooms[a] + (a,))),
                insert(state.hallway, i, None),
            )
            if new.fingerprint not in visited:
                heapq.heappush(todo, new)


def part_1(inp):
    board = dict()
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            if c in ('#', ' ', '\n', '.'):
                continue
            board[(x, y)] = c
    board = list(
        dict(sorted(board.items(), key=lambda item: item[0])).values())
    rooms = tuple([
        (ord(board[1]) - ord('A'), ord(board[0]) - ord('A')),
        (ord(board[3]) - ord('A'), ord(board[2]) - ord('A')),
        (ord(board[5]) - ord('A'), ord(board[4]) - ord('A')),
        (ord(board[7]) - ord('A'), ord(board[6]) - ord('A'))
    ])
    return solve(rooms)


def part_2(inp):
    board = dict()
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            if c in ('#', ' ', '\n', '.'):
                continue
            board[(x, y)] = c
    board = list(
        dict(sorted(board.items(), key=lambda item: item[0])).values())
    rooms = tuple([
        (ord(board[1]) - ord('A'), 3, 3, ord(board[0]) - ord('A')),
        (ord(board[3]) - ord('A'), 1, 2, ord(board[2]) - ord('A')),
        (ord(board[5]) - ord('A'), 0, 1, ord(board[4]) - ord('A')),
        (ord(board[7]) - ord('A'), 2, 0, ord(board[6]) - ord('A'))
    ])
    return solve(rooms)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
