from itertools import combinations
from copy import deepcopy
from math import lcm


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def read_moons(inp):
    return [[int(p) for p in line[1:-1].replace("x=", "").replace("y=", "")
             .replace("z=", "").split(",")] for line in inp]


def print_situation(t, moons, vels):
    print(f"After {t} steps:")
    for moon, vel in zip(moons, vels):
        print(f"pos=<x={moon[0]: >3}, y={moon[1]: >3}, z={moon[2]: >3}>, vel=<x={vel[0]: >3}, y={vel[1]: >3}, z={vel[2]: >3}>")  # noqa
    print()


def simulate(moons, vels, max_time):
    # print_situation(0, moons, vels)
    moons_len = len(moons)
    total_energy = 0
    for t in range(1, max_time + 1):
        for m_id_pairs in combinations(range(moons_len), 2):
            for p_id in range(3):
                if moons[m_id_pairs[0]
                         ][p_id] < moons[m_id_pairs[1]][p_id]:
                    vels[m_id_pairs[0]][p_id] += 1
                    vels[m_id_pairs[1]][p_id] -= 1
                elif moons[m_id_pairs[0]][p_id] > moons[m_id_pairs[1]][p_id]:
                    vels[m_id_pairs[0]][p_id] -= 1
                    vels[m_id_pairs[1]][p_id] += 1

        for moon_id in range(moons_len):
            for p_id in range(3):
                moons[moon_id][p_id] += vels[moon_id][p_id]
        total_energy = sum([sum([abs(mp) for mp in m]) *
                            sum([abs(vp) for vp in v]) for m, v in zip(moons, vels)])
        # print_situation(t, moons, vels)
    return total_energy


def part_1(inp):
    moons = read_moons(inp)
    vels = [[0, 0, 0] for _ in range(len(moons))]
    return simulate(moons, vels, max_time=1000)


def simulate_periods(moons, vels, max_time):
    periods = [0, 0, 0]
    moons_len = len(moons)
    initial_moons = deepcopy(moons)
    m_id_paris_all = list(combinations(range(moons_len), 2))
    for p_id in range(3):
        for t in range(1, max_time + 1):
            for m_id_pairs in m_id_paris_all:
                if moons[m_id_pairs[0]][p_id] < moons[m_id_pairs[1]][p_id]:
                    vels[m_id_pairs[0]][p_id] += 1
                    vels[m_id_pairs[1]][p_id] -= 1
                elif moons[m_id_pairs[0]][p_id] > moons[m_id_pairs[1]][p_id]:
                    vels[m_id_pairs[0]][p_id] -= 1
                    vels[m_id_pairs[1]][p_id] += 1

            moons[0][p_id] += vels[0][p_id]
            moons[1][p_id] += vels[1][p_id]
            moons[2][p_id] += vels[2][p_id]
            moons[3][p_id] += vels[3][p_id]

            found_period = (
                moons[0][p_id] == initial_moons[0][p_id] and
                moons[1][p_id] == initial_moons[1][p_id] and
                moons[2][p_id] == initial_moons[2][p_id] and
                moons[3][p_id] == initial_moons[3][p_id]
            )
            if found_period:
                periods[p_id] = t + 1
                break
        else:
            print(f"Reach max time for {p_id=}, please increase {max_time=}")
    return periods


def part_2(inp):
    moons = read_moons(inp)
    vels = [[0, 0, 0] for _ in range(len(moons))]
    periods = simulate_periods(moons, vels, max_time=1000_000)
    return lcm(*periods)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
