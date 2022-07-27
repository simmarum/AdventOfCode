import itertools


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def _get_shop():
    return {
        'Weapons': {
            'Dagger': {'cost': 8, 'damage': 4, 'armor': 0},
            'Shortsword': {'cost': 10, 'damage': 5, 'armor': 0},
            'Warhammer': {'cost': 25, 'damage': 6, 'armor': 0},
            'Longsword': {'cost': 40, 'damage': 7, 'armor': 0},
            'Greataxe': {'cost': 74, 'damage': 8, 'armor': 0},
        },
        'Armor': {
            '_': {'cost': 0, 'damage': 0, 'armor': 0},
            'Leather': {'cost': 13, 'damage': 0, 'armor': 1},
            'Chainmail': {'cost': 31, 'damage': 0, 'armor': 2},
            'Splintmail': {'cost': 53, 'damage': 0, 'armor': 3},
            'Bandedmail': {'cost': 75, 'damage': 0, 'armor': 4},
            'Platemail': {'cost': 102, 'damage': 0, 'armor': 5},
        },
        'Rings': {
            '_': {'cost': 0, 'damage': 0, 'armor': 0},
            'Defense_+1': {'cost': 20, 'damage': 0, 'armor': 1},
            'Damage_+1': {'cost': 25, 'damage': 1, 'armor': 0},
            'Defense_+2': {'cost': 40, 'damage': 0, 'armor': 2},
            'Damage_+2': {'cost': 50, 'damage': 2, 'armor': 0},
            'Defense_+3': {'cost': 80, 'damage': 0, 'armor': 3},
            'Damage_+3': {'cost': 100, 'damage': 3, 'armor': 0},
        },
    }


def _prepare_all_stats(shop, asc=True):
    all_possibilities = list(itertools.product(*[
        shop['Weapons'].keys(),
        shop['Armor'].keys(),
        shop['Rings'].keys(),
        shop['Rings'].keys(),
        shop['Rings'].keys(),
    ]))
    good_possibilities = []
    for one_pos in all_possibilities:
        rings = list(one_pos[2:5])
        try:
            while True:
                rings.remove('_')
        except ValueError:
            pass
        l_rings = len(rings)
        l_rings_set = len(set(rings))
        if l_rings == l_rings_set:
            good_possibilities.append(
                [
                    shop['Weapons'][one_pos[0]]['cost'] +
                    shop['Armor'][one_pos[1]]['cost'] +
                    shop['Rings'][one_pos[2]]['cost'] +
                    shop['Rings'][one_pos[3]]['cost'] +
                    shop['Rings'][one_pos[4]]['cost']
                ] + list(one_pos))
    if asc:
        good_possibilities = sorted(good_possibilities, key=lambda x: x[0])
    else:
        good_possibilities = sorted(
            good_possibilities, key=lambda x: x[0], reverse=True)
    return good_possibilities


def part_1(inp):
    e_hit_points = int(inp[0].split(' ')[2])
    e_damage = int(inp[1].split(' ')[1])
    e_armor = int(inp[2].split(' ')[1])
    shop = _get_shop()
    stats = _prepare_all_stats(shop)
    win_stat = None
    for i, stat in enumerate(stats):
        h_hit_points = 100
        h_damage = (
            shop['Weapons'][stat[1]]['damage'] +
            shop['Armor'][stat[2]]['damage'] +
            shop['Rings'][stat[3]]['damage'] +
            shop['Rings'][stat[4]]['damage'] +
            shop['Rings'][stat[5]]['damage']
        )
        h_armor = (
            shop['Weapons'][stat[1]]['armor'] +
            shop['Armor'][stat[2]]['armor'] +
            shop['Rings'][stat[3]]['armor'] +
            shop['Rings'][stat[4]]['armor'] +
            shop['Rings'][stat[5]]['armor']
        )
        h_to_e_damage = max(1, h_damage - e_armor)
        e_to_h_damage = max(1, e_damage - h_armor)

        turns_to_enemy_dead = int(e_hit_points / h_to_e_damage) + \
            1 if e_hit_points % h_to_e_damage != 0 else int(
                e_hit_points / h_to_e_damage)
        turns_to_hero_dead = int(h_hit_points / e_to_h_damage) + \
            1 if h_hit_points % e_to_h_damage != 0 else int(
                h_hit_points / e_to_h_damage)
        # print(f"Round: {i}")
        # print(f"Stat: {stat}")
        # print(f"\tEnemy: {e_hit_points}, {e_damage}, {e_armor}")
        # print(f"\tHero: {h_hit_points}, {h_damage}, {h_armor}")
        # print(f"\tBattle: h_to_e_damage: {h_to_e_damage}")
        # print(f"\tBattle: e_to_h_damage: {e_to_h_damage}")
        # print(f"\tBattle: turns_to_enemy_dead: {turns_to_enemy_dead}")
        # print(f"\tBattle: turns_to_hero_dead: {turns_to_hero_dead}")
        # print()
        if turns_to_hero_dead >= turns_to_enemy_dead:
            win_stat = stat
            break

    return win_stat[0]


def part_2(inp):
    e_hit_points = int(inp[0].split(' ')[2])
    e_damage = int(inp[1].split(' ')[1])
    e_armor = int(inp[2].split(' ')[1])
    shop = _get_shop()
    stats = _prepare_all_stats(shop, asc=False)
    lose_stat = None
    for i, stat in enumerate(stats):
        h_hit_points = 100
        h_damage = (
            shop['Weapons'][stat[1]]['damage'] +
            shop['Armor'][stat[2]]['damage'] +
            shop['Rings'][stat[3]]['damage'] +
            shop['Rings'][stat[4]]['damage'] +
            shop['Rings'][stat[5]]['damage']
        )
        h_armor = (
            shop['Weapons'][stat[1]]['armor'] +
            shop['Armor'][stat[2]]['armor'] +
            shop['Rings'][stat[3]]['armor'] +
            shop['Rings'][stat[4]]['armor'] +
            shop['Rings'][stat[5]]['armor']
        )
        h_to_e_damage = max(1, h_damage - e_armor)
        e_to_h_damage = max(1, e_damage - h_armor)

        turns_to_enemy_dead = int(e_hit_points / h_to_e_damage) + \
            1 if e_hit_points % h_to_e_damage != 0 else int(
                e_hit_points / h_to_e_damage)
        turns_to_hero_dead = int(h_hit_points / e_to_h_damage) + \
            1 if h_hit_points % e_to_h_damage != 0 else int(
                h_hit_points / e_to_h_damage)
        # print(f"Round: {i}")
        # print(f"Stat: {stat}")
        # print(f"\tEnemy: {e_hit_points}, {e_damage}, {e_armor}")
        # print(f"\tHero: {h_hit_points}, {h_damage}, {h_armor}")
        # print(f"\tBattle: h_to_e_damage: {h_to_e_damage}")
        # print(f"\tBattle: e_to_h_damage: {e_to_h_damage}")
        # print(f"\tBattle: turns_to_enemy_dead: {turns_to_enemy_dead}")
        # print(f"\tBattle: turns_to_hero_dead: {turns_to_hero_dead}")
        # print()
        if turns_to_hero_dead < turns_to_enemy_dead:
            lose_stat = stat
            break

    return lose_stat[0]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
