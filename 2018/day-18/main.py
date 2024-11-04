import numpy as np


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.readlines()]


def print_world(world, iteration):
    print(f"{iteration=}")
    for row in world:
        print("".join([str(c) for c in row]))
    print()


def create_world(inp):
    lookup = {
        '.': 0,
        '|': 1,
        '#': 2
    }
    world = np.array([[lookup[cc] for cc in c] for c in inp], dtype=np.int8)
    world = np.pad(world, 1, constant_values=0)
    return world


def get_neighbors(world, cell):
    r = [0, 0, 0]
    py = cell[0]
    px = cell[1]
    r[world[py + -1, px + -1]] += 1
    r[world[py + -1, px + 0]] += 1
    r[world[py + -1, px + 1]] += 1
    r[world[py + 0, px + -1]] += 1
    r[world[py + 0, px + 1]] += 1
    r[world[py + 1, px + -1]] += 1
    r[world[py + 1, px + 0]] += 1
    r[world[py + 1, px + 1]] += 1
    return r


def run_game(world, iterations=3):
    rules = {
        0: lambda x: 1 if x[1] >= 3 else 0,
        1: lambda x: 2 if x[2] >= 3 else 1,
        2: lambda x: 2 if (x[2] >= 1 and x[1] >= 1) else 0
    }
    unique_worlds = list()
    curr_world = np.copy(world)
    new_world = np.copy(world)

    curr_world_str = curr_world.tobytes()
    unique_worlds.append(curr_world_str)
    # print_world(curr_world, 0)
    for iteration in range(1, iterations + 1):
        for iy, ix in np.ndindex(
                (curr_world.shape[0] - 1, curr_world.shape[1] - 1)):
            if iy == 0 or ix == 0:
                continue
            neighbors = get_neighbors(curr_world, (iy, ix))
            new_world[iy, ix] = rules[curr_world[iy, ix]](neighbors)

        curr_world = np.copy(new_world)
        curr_world_str = curr_world.tobytes()

        try:
            unique_world_idx = unique_worlds.index(curr_world_str)
            return np.frombuffer(unique_worlds[(
                (iterations - iteration) % (len(unique_worlds) - unique_world_idx)) + unique_world_idx], dtype=np.int8)
        except ValueError:
            unique_worlds.append(curr_world_str)

        # print_world(curr_world, iteration)
    return curr_world


def part_1(inp):
    world = create_world(inp)
    curr_world = run_game(world, 10)
    unique, counts = np.unique(curr_world, return_counts=True)
    magic_counter = dict(zip(unique, counts))
    return magic_counter[1] * magic_counter[2]


def part_2(inp):
    world = create_world(inp)
    curr_world = run_game(world, 1000000000)
    unique, counts = np.unique(curr_world, return_counts=True)
    magic_counter = dict(zip(unique, counts))
    return magic_counter[1] * magic_counter[2]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
