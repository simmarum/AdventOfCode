def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [line for line in f.read().splitlines()]


def part_1(inp):
    all_ing = set()
    all_alg = set()
    alg_pot = {}
    use_alg_ings = set()
    raw_ings = []
    for val in inp:
        x = val.split("(")
        ings = x[0].strip().split(" ")
        algs = x[1].replace(")", "").replace(",", "").split(" ")[1:]

        raw_ings.append(ings)

        all_ing.update(ings)
        all_alg.update(algs)

        for alg in algs:
            if alg not in alg_pot:
                alg_pot[alg] = set(ings)
            else:
                alg_pot[alg].intersection_update(ings)

    match_alg_ing = {}

    while len(match_alg_ing) != len(all_alg):
        for alg, ings in alg_pot.items():
            ings -= use_alg_ings
            if len(ings) == 1:
                ing = ings.pop()
                match_alg_ing[alg] = ing
                use_alg_ings.add(ing)

    rest_alg_ings = all_ing - use_alg_ings

    ss = 0
    for raw_ing in raw_ings:
        ss += len(rest_alg_ings.intersection(raw_ing))

    return ss, match_alg_ing


def part_2(inp):
    _, match_alg_ing = part_1(inp)

    res = ','.join(
        [
            x[1]
            for x in sorted(
                match_alg_ing.items(),
                key=lambda x: x[0]
            )
        ]
    )

    return res


def main():
    inp = read_file()
    res_1, _ = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
