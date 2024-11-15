from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def read_input(inp):
    reactions = {}
    for line in inp:
        chemicals, result = line.split("=>")
        result_cnt, result_name = [
            int(x) if x.isdigit() else x for x in result.strip().split(" ")]
        chemicals_array = chemicals.split(",")
        chemicals_array = [
            [int(x) if x.isdigit() else x for x in c.strip().split(" ")] for c in chemicals_array]
        reactions[result_name] = {
            'cnt': result_cnt,
            'chemicals': chemicals_array
        }
    return reactions


def get_min_ore_for_fuel(inventory, reactions):
    was_something_created = True
    while was_something_created:
        was_something_created = False
        for item_name, item_cnt in inventory.items():
            if item_name == 'ORE':
                continue
            if item_cnt < 0:
                was_something_created = True
                reaction = reactions[item_name]
                reaction_output_cnt = reaction['cnt']
                reaction_chemicals = reaction['chemicals']
                for chemical_cnt, chemical_name in reaction_chemicals:
                    inventory[chemical_name] -= chemical_cnt
                inventory[item_name] += reaction_output_cnt
    return inventory


def part_1(inp):
    reactions = read_input(inp)
    inventory = defaultdict(int)
    inventory = {k: 0 for k in reactions.keys()}
    inventory['FUEL'] = -1
    inventory['ORE'] = 0
    inventory = get_min_ore_for_fuel(inventory, reactions)
    return -inventory['ORE']


def get_ore_for_fuel_fast(reactions, fuel_cnt):
    required = {'FUEL': fuel_cnt}
    storage = defaultdict(int)
    while True:
        try:
            next_chem = next(chem for chem in required if chem != 'ORE')
        except StopIteration:
            break
        reaction = reactions[next_chem]
        reaction_cnt = reaction['cnt']
        reaction_chemicals = reaction['chemicals']

        next_chem_cnt, next_chem_left = divmod(
            required[next_chem], reaction_cnt)
        if next_chem_left > 0:
            storage[next_chem] = reaction_cnt - next_chem_left
            next_chem_cnt += 1
        del required[next_chem]

        for chem_cnt, chem_name in reaction_chemicals:
            required[chem_name] = required.get(chem_name, 0) + (next_chem_cnt *
                                                                chem_cnt) - storage[chem_name]
            del storage[chem_name]

    return required['ORE']


def part_2(inp):
    reactions = read_input(inp)
    storage_ore = 1_000_000_000_000
    req_ore = get_ore_for_fuel_fast(reactions, 1)
    fuel_min, fuel_max = storage_ore // req_ore, int(
        storage_ore // req_ore * 10)
    while fuel_max - fuel_min >= 2:
        fuel_half = fuel_min + (fuel_max - fuel_min) // 2
        req_ore = get_ore_for_fuel_fast(reactions, fuel_half)
        if req_ore > storage_ore:
            fuel_max = fuel_half
        else:
            fuel_min = fuel_half
    return fuel_min


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
