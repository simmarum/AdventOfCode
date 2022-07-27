def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    new_molecules = set()
    possibilities = []
    for line in inp:
        if '=>' in line:
            possibilities.append(line.strip().split(' => '))
        elif len(line) > 2:
            molecule = line.strip()
    len_mol = len(molecule)
    for one_pos in possibilities:
        for i in range(len_mol):
            if molecule.startswith(one_pos[0], i):
                new_molecules.add(
                    molecule[:i] + molecule[i:].replace(one_pos[0], one_pos[1], 1))
    return len(new_molecules)


def part_2(inp):
    from random import shuffle
    possibilities = []
    for line in inp:
        if '=>' in line:
            possibilities.append(line.strip().split(' => '))
        elif len(line) > 2:
            molecule = line.strip()
    final_molecule = 'e'
    target = molecule
    steps = 0

    while target != final_molecule:
        tmp = target
        for posx, posy in possibilities:
            if posy not in target:
                continue
            target = target.replace(posy, posx, 1)
            steps += 1
        if tmp == target:
            target = molecule
            steps = 0
            shuffle(possibilities)

    return steps


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
