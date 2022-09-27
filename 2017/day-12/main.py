from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def parse_input(inp):
    data = defaultdict(list)
    for line in inp:
        x = line.split()
        data[x[0]] += [c.replace(',', '') for c in x[2:]]
    return data


def get_successors(data, node):
    node_visited = set()
    node_to_visit = set(data[node])
    while node_to_visit:
        successor_node = node_to_visit.pop()
        node_visited.add(successor_node)
        node_to_visit = node_to_visit.union(set(data[successor_node]))
        node_to_visit = node_to_visit.difference(node_visited)
    return node_visited


def part_1(inp):
    data = parse_input(inp)
    start_node = '0'
    return len(get_successors(data, start_node))


def part_2(inp):
    data = parse_input(inp)
    avaiable_nodes = set(data.keys())
    separate_groups = 0
    while avaiable_nodes:
        start_node = avaiable_nodes.pop()
        successors = get_successors(data, start_node)
        avaiable_nodes = avaiable_nodes.difference(successors)
        separate_groups += 1
    return separate_groups


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
