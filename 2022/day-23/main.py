def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def get_elves(inp):
    elves = set()
    for y, line in enumerate(inp):
        if not line:
            continue
        for x, c in enumerate(line):
            if c == '#':
                elves.add(complex(y, x))
    return elves


def print_elves(elves, msg="No message"):
    print(msg)
    min_y = 1_000_000
    min_x = 1_000_000
    max_y = -1_000_000
    max_x = -1_000_000
    for elf in elves:
        min_y = int(min(min_y, elf.real))
        min_x = int(min(min_x, elf.imag))
        max_y = int(max(max_y, elf.real))
        max_x = int(max(max_x, elf.imag))
    for y in range(min_y, max_y + 1):
        line = []
        for x in range(min_x, max_x + 1):
            if complex(y, x) in elves:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))
    print()
    print(f"{len(elves)=}")
    print()


def spread_elves(elves, rounds):
    checks_idx = -1
    checks = [
        (complex(-1, -1), complex(-1, 0), complex(-1, 1)),
        (complex(1, -1), complex(1, 0), complex(1, 1)),
        (complex(-1, -1), complex(0, -1), complex(1, -1)),
        (complex(-1, 1), complex(0, 1), complex(1, 1)),
    ]
    moves = [
        complex(-1, 0),
        complex(1, 0),
        complex(0, -1),
        complex(0, 1),
    ]

    for round in range(1, rounds + 1):
        checks_idx = (checks_idx + 1) % 4
        new_elves = set()
        tmp_elves = set()
        tmp_elves_rm = set()
        for elf in elves:
            if not any([elf + c in elves for check in checks for c in check]):
                new_elves.add(elf)
            else:
                for i in range(4):
                    tmp_check_idx = (checks_idx + i) % 4
                    if not any(
                            [elf + c in elves for c in checks[tmp_check_idx]]):
                        if elf + moves[tmp_check_idx] in tmp_elves:
                            tmp_elves_rm.add(elf + moves[tmp_check_idx])
                        else:
                            tmp_elves.add(elf + moves[tmp_check_idx])
                        break
                else:
                    new_elves.add(elf)
        if len(elves) == len(new_elves):
            return elves, round
        for elf_rm in tmp_elves_rm:
            for i in range(4):
                if elf_rm + moves[i] in elves:
                    new_elves.add(elf_rm + moves[i])
        tmp_elves.difference_update(tmp_elves_rm)
        elves = new_elves.union(tmp_elves)
        # print_elves(elves, f"== End of Round {round} ==")
    return elves, None


def count_free_space(elves):
    min_y = 1_000_000
    min_x = 1_000_000
    max_y = -1_000_000
    max_x = -1_000_000
    for elf in elves:
        min_y = int(min(min_y, elf.real))
        min_x = int(min(min_x, elf.imag))
        max_y = int(max(max_y, elf.real))
        max_x = int(max(max_x, elf.imag))
    return (max_y - min_y + 1) * (max_x - min_x + 1) - len(elves)


def part_1(inp):
    elves = get_elves(inp)
    # print_elves(elves, "== Initial State ==")
    elves, _ = spread_elves(elves, rounds=10)
    return count_free_space(elves)


def part_2(inp):
    elves = get_elves(inp)
    _, round = spread_elves(elves, rounds=1000)
    return round


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
