from collections import deque
import networkx as nx
from copy import deepcopy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [[c for c in str(line).replace('\n', '')] for line in f.readlines()]


class Unit:
    def __init__(self, unit_type, x, y, d):
        self.unit_type = unit_type
        self.x = x
        self.y = y
        self.is_alive = True
        self.hp = 200
        self.attack_damage = d

    def pos(self):
        return (self.x, self.y)

    def attack(self, damage):
        if self.is_alive:
            self.hp -= damage
            if self.hp <= 0:
                self.is_alive = False


def find_closest(graph, excluded_nodes, start, targets):
    if start not in graph:
        return [], None

    seen = set()
    q = deque([(start, 0)])
    found_dist = None
    closest = []
    while q:
        cell, dist = q.popleft()
        if found_dist is not None and dist > found_dist:
            return closest, found_dist
        if cell in seen or cell in excluded_nodes:
            continue
        seen.add(cell)
        if cell in targets:
            found_dist = dist
            closest.append(cell)
        for n in graph.neighbors(cell):
            if n not in seen:
                q.append((n, dist + 1))
    return closest, found_dist


def neighbours(x, y):
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]


def reading_order(pos):
    return pos[1], pos[0]


def solve(inp, d, no_elves_die):
    data = deepcopy(inp)
    units = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            t = data[y][x]
            if t in "GE":
                units.append(Unit(t, x, y, 3 if t == "G" else d))
                data[y][x] = "."

    G = nx.Graph()
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == ".":
                for (x2, y2) in neighbours(x, y):
                    if 0 <= x2 < len(data[0]) and 0 <= y2 < len(data) and data[y2][x2] == ".":
                        G.add_edge((x, y), (x2, y2))

    round = 0
    while True:
        order = sorted(units, key=lambda c: reading_order(c.pos()))

        for idx, c in enumerate(order):
            if not c.is_alive:
                continue
            enemies = [e for e in units if e.unit_type !=
                       c.unit_type and e.is_alive]
            enemy_positions = [e.pos() for e in enemies]
            nearby_cells = neighbours(*c.pos())
            enemy_positions_in_range = [
                p for p in nearby_cells if p in enemy_positions]
            if not enemy_positions_in_range:
                surrounding = []
                for e in enemies:
                    surrounding.extend(neighbours(*e.pos()))
                surrounding = [s for s in surrounding if s in G]
                excluded_nodes = [e.pos()
                                  for e in units if e.is_alive and e != c]
                closest_targets, dist = find_closest(
                    G, excluded_nodes, c.pos(), surrounding)

                if closest_targets:
                    choice = min(closest_targets, key=reading_order)
                    for s in sorted(nearby_cells, key=reading_order):
                        _, d = find_closest(G, excluded_nodes, s, [choice])
                        if d == dist - 1:
                            c.x, c.y = s
                            break

                enemy_positions_in_range = [
                    p for p in neighbours(*c.pos()) if p in enemy_positions]

            if enemy_positions_in_range:
                enemies = [e for e in enemies if e.pos()
                           in enemy_positions_in_range]

                lowest_health = min(enemies, key=lambda e: (
                    e.hp, reading_order(e.pos())))
                lowest_health.attack(c.attack_damage)

                if no_elves_die and lowest_health.unit_type == "E" and not lowest_health.is_alive:
                    return False, 0

                alive = set(e.unit_type for e in units if e.is_alive)
                if len(alive) == 1:
                    if idx == len(order) - 1:
                        round += 1
                    return True, round * sum(e.hp for e in units if e.is_alive)
        round += 1


def part_1(inp):
    _, score = solve(inp, 3, False)
    return score


def part_2(inp):
    i = 3
    while True:
        no_elves_died, score = solve(inp, i, True)
        if no_elves_died:
            return score
        i += 1


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
