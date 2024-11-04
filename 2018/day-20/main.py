from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def get_all_distances(inp):
    dirs = {
        'N': complex(0, -1),
        'S': complex(0, 1),
        'E': complex(1, 0),
        'W': complex(-1, 0),
    }
    curr_position = complex(0, 0)
    prev_position = curr_position
    world = defaultdict(set)
    world_dist = {
        curr_position: 0
    }
    crossroads = []
    for c in inp[0]:
        if c == '^':
            pass
        elif c == '$':
            pass
        elif c == '(':
            crossroads.append(curr_position)
        elif c == ')':
            curr_position = crossroads.pop()
        elif c == '|':
            curr_position = crossroads[-1]
        else:
            curr_position += dirs[c]
            world[curr_position].add(prev_position)
            if curr_position not in world_dist:
                world_dist[curr_position] = world_dist[prev_position] + 1
            else:
                world_dist[curr_position] = min(
                    world_dist[curr_position],
                    world_dist[prev_position] + 1
                )
        prev_position = curr_position
    return world_dist


def part_1(inp):
    world_dist = get_all_distances(inp)
    return max(world_dist.values())


def part_2(inp):
    world_dist = get_all_distances(inp)
    return sum([1 for dist in world_dist.values() if dist >= 1000])


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
