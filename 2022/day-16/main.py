from itertools import product


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def parse_inp(inp):
    nodes = {}
    for line in inp:
        tmp_split = line.split()
        node = tmp_split[1]
        rate = int(tmp_split[4].split('=')[1][:-1])
        children = [c.replace(',', '') for c in tmp_split[9:]]
        nodes[node] = (rate, children)
    return nodes


def part_1(inp):
    nodes = parse_inp(inp)
    max_step = 30
    states = [('AA', tuple(), 0)]
    best = {}
    for t in range(1, max_step + 1):
        new_states = []
        for node, opened, pressure in states:
            key = (node, opened)
            if (key in best) and (pressure <= best[key]):
                continue
            best[key] = pressure
            rate, children = nodes[node]
            if (node not in opened) and (rate > 0):
                new_states.append(
                    (
                        node,
                        tuple(sorted(set(opened + (node,)))),
                        pressure + (rate * (max_step - t))
                    )
                )
            for child in children:
                new_states.append((child, opened, pressure))
        states = new_states
    return max([p for _, _, p in states])


def part_2(inp):
    nodes = parse_inp(inp)
    nodes_id = {k: 2**idx for idx, k in enumerate(list(sorted(nodes.keys())))}
    max_step = 26
    states = [('AA', 'AA', 0, 0)]
    best = {}
    best_max = 0
    for t in range(1, max_step + 1):
        new_states = set()
        # print(t, len(states))
        for node1, node2, opened, pressure in states:
            node1, node2 = sorted([node1, node2])
            key = (node1, node2, opened)
            if (key in best) and (pressure <= best[key]):
                continue
            # speed up - may not work for all inputs
            best_max = max(best_max, pressure)
            if best and pressure < 0.75 * best_max:
                continue

            best[key] = pressure
            rate1, children1 = nodes[node1]
            rate2, children2 = nodes[node2]
            if (nodes_id[node1] & opened == 0) and (rate1 > 0) and (
                    nodes_id[node2] & opened == 0) and (rate2 > 0) and (node1 != node2):
                new_states.add(
                    (
                        node1,
                        node2,
                        opened | nodes_id[node1] | nodes_id[node2],
                        pressure + (rate1 * (max_step - t)) +
                        (rate2 * (max_step - t))
                    )
                )
            else:
                tmp_opened = opened
                if (nodes_id[node1] & tmp_opened == 0) and (rate1 > 0):
                    tmp_opened = tmp_opened | nodes_id[node1]
                    for c2 in children2:
                        new_states.add(
                            (
                                *sorted([node1, c2]),
                                tmp_opened,
                                pressure + (rate1 * (max_step - t))
                            )
                        )

                if (nodes_id[node2] & tmp_opened == 0) and (rate2 > 0):
                    tmp_opened = tmp_opened | nodes_id[node2]
                    for c1 in children1:
                        new_states.add(
                            (
                                *sorted([c1, node2]),
                                tmp_opened,
                                pressure + (rate2 * (max_step - t))
                            )
                        )

            for child1, child2 in product(children1, children2):
                new_states.add(
                    (
                        *sorted([child1, child2]),
                        opened,
                        pressure
                    )
                )
        states = new_states
    return max(best.values())


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
