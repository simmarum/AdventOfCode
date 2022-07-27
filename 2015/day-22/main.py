from copy import deepcopy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


all_spells = [
    {
        'name': 'magic_missile',
        'cost': 53,
        'damage': 4,
        'heal': 0,
        'armor': 0,
        'mana': 0,
        'turns': 0,
    },
    {
        'name': 'drain',
        'cost': 73,
        'damage': 2,
        'heal': 2,
        'armor': 0,
        'mana': 0,
        'turns': 0,
    },
    {
        'name': 'shield',
        'cost': 113,
        'damage': 0,
        'heal': 0,
        'armor': 7,
        'mana': 0,
        'turns': 6,
    },
    {
        'name': 'poison',
        'cost': 173,
        'damage': 3,
        'heal': 0,
        'armor': 0,
        'mana': 0,
        'turns': 6,
    },
    {
        'name': 'recharge',
        'cost': 229,
        'damage': 0,
        'heal': 0,
        'armor': 0,
        'mana': 101,
        'turns': 5,
    },
]

all_mana_min = 1_000_000


def simulate(e_hit_points, e_damage,
             h_hit_points, h_mana, h_active_spells,
             h_turn, all_mana, is_part_2):
    h_armor = 0

    if is_part_2 and h_turn:
        h_hit_points -= 1
        if h_hit_points <= 0:
            return False

    new_h_active_spells = []
    for h_spell in h_active_spells:
        if h_spell['turns'] >= 0:
            e_hit_points -= h_spell['damage']
            h_hit_points += h_spell['heal']
            h_armor += h_spell['armor']
            h_mana += h_spell['mana']
        if h_spell['turns'] > 1:
            new_h_active_spells.append({
                'name': h_spell['name'],
                'cost': h_spell['cost'],
                'damage': h_spell['damage'],
                'heal': h_spell['heal'],
                'armor': h_spell['armor'],
                'mana': h_spell['mana'],
                'turns': h_spell['turns'] - 1,
            })
    if e_hit_points <= 0:
        global all_mana_min
        if all_mana < all_mana_min:
            all_mana_min = all_mana
        return True

    if all_mana >= all_mana_min:
        return False

    if h_turn is True:
        for spell in all_spells:
            is_spell_active = False
            for active_spell in new_h_active_spells:
                if active_spell['name'] == spell['name']:
                    is_spell_active = True
                    break
            if (not is_spell_active) and (spell['cost'] <= h_mana):
                next_turn_active_spells = deepcopy(new_h_active_spells)
                next_turn_active_spells.append(spell)
                simulate(
                    e_hit_points=e_hit_points,
                    e_damage=e_damage,
                    h_hit_points=h_hit_points,
                    h_mana=h_mana - spell['cost'],
                    h_active_spells=next_turn_active_spells,
                    h_turn=False,
                    all_mana=all_mana + spell['cost'],
                    is_part_2=is_part_2
                )
    else:
        # enemy turn
        h_hit_points -= max(1, (e_damage - h_armor))
        if h_hit_points > 0:
            simulate(
                e_hit_points=e_hit_points,
                e_damage=e_damage,
                h_hit_points=h_hit_points,
                h_mana=h_mana,
                h_active_spells=new_h_active_spells,
                h_turn=True,
                all_mana=all_mana,
                is_part_2=is_part_2
            )

    pass


def part_1(inp):
    global all_mana_min
    all_mana_min = 1_000_00
    e_hit_points = int(inp[0].split(' ')[2])
    e_damage = int(inp[1].split(' ')[1])

    h_hit_points = 50
    h_mana = 500

    simulate(
        e_hit_points=e_hit_points,
        e_damage=e_damage,
        h_hit_points=h_hit_points,
        h_mana=h_mana,
        h_active_spells=[],
        h_turn=True,
        all_mana=0,
        is_part_2=False
    )
    part_1_res = all_mana_min
    return part_1_res


def part_2(inp):
    global all_mana_min
    all_mana_min = 1_000_00
    e_hit_points = int(inp[0].split(' ')[2])
    e_damage = int(inp[1].split(' ')[1])

    h_hit_points = 50
    h_mana = 500

    simulate(
        e_hit_points=e_hit_points,
        e_damage=e_damage,
        h_hit_points=h_hit_points,
        h_mana=h_mana,
        h_active_spells=[],
        h_turn=True,
        all_mana=0,
        is_part_2=True
    )
    part_2_res = all_mana_min
    return part_2_res


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
