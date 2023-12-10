from functools import cache


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def parse_inp(inp):
    blueprints = []
    for line in inp:
        id, a, b, c, d, e, f = [
            int(x.replace(':', '')) for x in line.split() if x.replace(':', '').isdigit()]
        blueprints.append((id, a, b, c, d, e, f, max(a, b, c, e)))
    return tuple(blueprints)


# speed up - may not work for every input
part_1_magic_time = 2
part_2_magic_time = 10


@cache
def max_geos(state):
    # state
    # 0 blueprint id
    # 1 ore_r cost ore
    # 2 cla_r cost ore
    # 3 obs_r cost ore
    # 4 obs_r cost cla
    # 5 geo_r cost ore
    # 6 geo_r cost obs
    # 7 max cost ore
    # 8 ore robots
    # 9 clay robots
    # 10 obsidian robots
    # 11 geode robots
    # 12 ore
    # 13 clay
    # 14 obsidian
    # 15 time left
    if state[15] == 0:
        return 0

    if state[16] == 1 and state[15] < part_1_magic_time:
        if state[11] < 1:
            return 0
    if state[16] == 2 and state[15] < part_2_magic_time:
        if state[11] < 1:
            return 0

    if (state[12] >= state[5]) and (state[14] >= state[6]):
        return state[11] + max_geos(
            (
                *state[0:8],
                state[8],
                state[9],
                state[10],
                state[11] + 1,
                state[12] + state[8] - state[5],
                state[13] + state[9],
                state[14] + state[10] - state[6],
                state[15] - 1,
                state[16]
            )
        )
    possible_obs = state[14]
    for i in range(0, state[15] - 2):
        possible_obs += state[10] + i
    if possible_obs < state[6]:
        return state[11] * state[15]

    new_states = []
    # no robot
    new_states.append(
        max_geos(
                (
                    *state[0:8],
                    state[8],
                    state[9],
                    state[10],
                    state[11],
                    state[12] + state[8],
                    state[13] + state[9],
                    state[14] + state[10],
                    state[15] - 1,
                    state[16]
                )
        )
    )
    # ore robot
    if (state[12] >= state[1]) and (state[8] < state[7]):
        new_states.append(
            max_geos(
                    (
                        *state[0:8],
                        state[8] + 1,
                        state[9],
                        state[10],
                        state[11],
                        state[12] + state[8] - state[1],
                        state[13] + state[9],
                        state[14] + state[10],
                        state[15] - 1,
                        state[16]
                    )
            )
        )
    # clay robot
    if (state[12] >= state[2]) and (state[9] < state[4]):
        new_states.append(
            max_geos(
                    (
                        *state[0:8],
                        state[8],
                        state[9] + 1,
                        state[10],
                        state[11],
                        state[12] + state[8] - state[2],
                        state[13] + state[9],
                        state[14] + state[10],
                        state[15] - 1,
                        state[16]
                    )
            )
        )
    # obs robot
    if (state[12] >= state[3]) and (
            state[13] >= state[4]) and (state[10] < state[6]):
        new_states.append(
            max_geos(
                    (
                        *state[0:8],
                        state[8],
                        state[9],
                        state[10] + 1,
                        state[11],
                        state[12] + state[8] - state[3],
                        state[13] + state[9] - state[4],
                        state[14] + state[10],
                        state[15] - 1,
                        state[16]
                    )
            )
        )
    return state[11] + max(new_states)


def part_1(inp):
    blueprints = parse_inp(inp)
    total = 0
    for blueprint in blueprints:
        b_res = max_geos(
            (
                *(blueprint),
                *(1, 0, 0, 0, 0, 0, 0, 24),
                1
            )
        )
        total += blueprint[0] * b_res
    return total


def part_2(inp):
    blueprints = parse_inp(inp)
    total = 1
    for blueprint in blueprints[0:3]:
        b_res = max_geos(
            (
                *(blueprint),
                *(1, 0, 0, 0, 0, 0, 0, 32),
                2
            )
        )
        total *= b_res
    return total


def main():
    inp = read_file()
    # res_1 = part_1(inp)
    # print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
