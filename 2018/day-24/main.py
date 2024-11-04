import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


G_IMM = 'Immune System'
G_INF = 'Infection'
DO_PRINT = False
DO_PRINT_2 = False


def my_print(msg=''):
    if DO_PRINT:
        print(msg)


def my_print_2(msg=''):
    if DO_PRINT_2:
        print(msg)


def read_input(inp, boost):
    groups = []
    inp = ''.join(inp).replace("\n ", " ").split('\n')
    for line in inp:
        if 'Immune System' in line:
            g_curr = G_IMM
            idx = 1
        elif 'Infection' in line:
            g_curr = G_INF
            idx = 1
        elif line.strip() == '':
            continue
        else:
            m = re.search(r'(\d+) units each with (\d+) hit points', line)
            units = m.group(1) if m else 0
            hp = m.group(2) if m else 0
            m = re.search(r'weak to ([a-z, ]+)', line)
            weak = {s.strip() for s in m.group(1).split(',')} if m else {}
            m = re.search(r'immune to ([a-z, ]+)', line)
            immune = {s.strip() for s in m.group(1).split(',')} if m else {}
            m = re.search(r'attack that does (\d+) (\w+)', line)
            att = m.group(1) if m else 0
            att_type = m.group(2) if m else ''
            m = re.search(r'initiative (\d+)', line)
            init = m.group(1) if m else 0

            groups.append(
                {
                    'side': g_curr,
                    'id': idx,
                    'units': int(units),
                    'hp': int(hp),
                    'weak': weak,
                    'immune': immune,
                    'att': int(att) + boost if g_curr == G_IMM else int(att),
                    'att_type': att_type,
                    'init': int(init),
                    'power': int(units) * (int(att) + boost if g_curr == G_IMM else int(att))
                }
            )
            idx += 1
    return groups


def check_win(groups):
    if groups is None:
        return None
    return len(set([g['side'] for g in groups])) == 2


def print_war_units(groups):
    if not DO_PRINT:
        return
    group_name_to_print = None
    for g in sorted(groups, key=lambda x: (x['side'], x['id'])):
        if g['side'] != group_name_to_print:
            group_name_to_print = g['side']
            my_print(f"{group_name_to_print}:")
        my_print(f"Group {g['id']} contains {g['units']} units")
    my_print()


def select_targets(groups):
    groups = sorted(
        groups,
        key=lambda x: (
            x['power'],
            x['init']),
        reverse=True)
    choosen_targets = set()
    for g in groups:
        g['next_attack'] = (0, 0, 0, 0, '0')
        for g_def in groups:
            if (g_def['id'], g_def['side']) in choosen_targets:
                continue
            if g['side'] == g_def['side']:
                continue
            att_mul = 1
            if g['att_type'] in g_def['weak']:
                att_mul = 2
            if g['att_type'] in g_def['immune']:
                continue
            damage = g['power'] * att_mul
            g['next_attack'] = max(
                g['next_attack'],
                (damage,
                 g_def['power'],
                    g_def['init'],
                    g_def['id'],
                    g_def['side']))
            my_print(f"{g['side']} group {g['id']} would deal defending group {
                g_def['id']} {damage} damage ({g_def['power']=}, {g_def['init']=})")
        if g['next_attack'] != (0, 0, 0, 0, '0'):
            choosen_targets.add((g['next_attack'][3], g['next_attack'][4]))
        else:
            g['next_attack'] = None
    my_print()
    return groups


def attack(groups):
    groups = sorted(groups, key=lambda x: x['init'], reverse=True)
    total_units_killed = 0
    for g in groups:
        if g['units'] <= 0:
            continue
        if not g['next_attack']:
            continue
        _, _, _, g_def_id, g_def_side = g['next_attack']
        g_def = list(
            filter(
                lambda x: (
                    x['id'] == g_def_id) and (
                    x['side'] == g_def_side), groups))[0]
        att_mul = 1
        if g['att_type'] in g_def['weak']:
            att_mul = 2
        if g['att_type'] in g_def['immune']:
            att_mul = 0
        damage = g['power'] * att_mul
        units_killed = min(damage // g_def['hp'], g_def['units'])
        total_units_killed += units_killed
        g_def['units'] = g_def['units'] - units_killed
        g_def['power'] = g_def['units'] * g_def['att']
        my_print(f"{g['side']} group {g['id']} attacks defending group {
            g_def_id}, killing {units_killed} units ({damage=} {g_def['hp']=} {att_mul=})")
    if total_units_killed == 0:
        my_print_2("No units were killed this round - endless battle - skipped")
        return None

    groups = [g for g in groups if g['units'] > 0]
    my_print()
    return groups


def simulate_war(groups):
    it = 0
    while check_win(groups):
        it += 1
        print_war_units(groups)
        groups = select_targets(groups)
        groups = attack(groups)
    if groups is None:
        return None, None
    return sum([g['units'] for g in groups]), groups[0]['side']


def part_1(inp):
    boost = 0
    groups = read_input(inp, boost)
    winner_units, winner_side = simulate_war(groups)
    return winner_units


def part_2(inp):
    boost_min = 0
    boost_max = 2000
    max_iter = 50
    lowest_winner_G_IMM = 1_000_000_000_000_000
    boost_check = set()
    for it in range(1, max_iter + 1):
        boost = boost_min + ((boost_max - boost_min) // 2)
        if boost in boost_check:
            return lowest_winner_G_IMM
        groups = read_input(inp, boost)
        winner_units, winner_side = simulate_war(groups)
        if winner_side == G_IMM:
            my_print_2(
                f"{winner_side} wins again with {winner_units} left... ({boost=})")
            lowest_winner_G_IMM = min(lowest_winner_G_IMM, winner_units)
            if boost_min == boost_max:
                return winner_units
            boost_max = boost - 1

        elif winner_side == G_INF:
            my_print_2(
                f"{winner_side} wins again with {winner_units} left... ({boost=})")
            boost_min = boost + 1
        else:
            boost_min = boost + 1

        boost_check.add(boost)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
