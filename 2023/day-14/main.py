import numpy as np


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.readlines()]


def part_1(inp):
    disc_t = [''.join(e[::-1])
              for e in list(map(list, zip(*inp)))]
    magic_sum = 0
    for line in disc_t:
        curr_roll = 0
        for idx, el in enumerate(line, start=1):
            if el == '.':
                continue
            elif el == '#':
                magic_sum += sum(range(idx - curr_roll, idx))
                curr_roll = 0
            elif el == 'O':
                curr_roll += 1
        idx = len(line) + 1
        magic_sum += sum(range(idx - curr_roll, idx))
    return magic_sum


def part_2(inp):
    def next_phase(disc):
        new_disc = []
        for ii, line in enumerate(np.rot90(disc, 3)):
            new_line = []
            curr_roll = 0
            last_rock = -1
            for idx, el in enumerate(line, start=0):
                if el == '.':
                    continue
                elif el == '#':
                    new_line.extend(
                        ['.'] * (idx - 1 - last_rock - curr_roll) +
                        ['O'] * (curr_roll) +
                        ['#']
                    )
                    curr_roll = 0
                    last_rock = idx
                elif el == 'O':
                    curr_roll += 1
            idx = len(line)
            new_line.extend(
                ['.'] * (idx - 1 - last_rock - curr_roll) +
                ['O'] * (curr_roll)
            )
            new_disc.append(new_line)
        return np.array(new_disc)

    disc = np.array([[c for c in line] for line in inp])
    disc_shape = disc.shape
    cycles = 1000000000
    all_solutions = list()
    for cycle in range(0, 1000):
        for _ in range(4):
            disc = next_phase(disc)
        f_disc = ''.join(disc.flatten().tolist())
        if f_disc in all_solutions:
            loop_start = all_solutions.index(f_disc)
            last_cycle = (
                (cycles - loop_start) %
                (cycle - loop_start)) + loop_start - 1
            last_disc = all_solutions[last_cycle]
            last_disc = np.array([c for c in last_disc]).reshape(disc_shape)
            rows_reversed = np.where(last_disc == 'O')[0]
            rows = [disc_shape[0] - r for r in rows_reversed]
            return sum(rows)
        all_solutions.append(f_disc)

    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
