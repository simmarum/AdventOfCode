import networkx as nx


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def create_graph(inp):
    edges = []
    for line in inp:
        if not line:
            continue
        l_node, r_nodes = line.split(":")
        l_node = l_node.strip()
        r_nodes = r_nodes.strip()
        r_nodes = [r_node.strip() for r_node in r_nodes.split(" ")]
        edges.extend([(l_node, r_node) for r_node in r_nodes])
    nodes = list(set([node for edge in edges for node in edge]))
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G


def part_1(inp):
    G = create_graph(inp)

    def recorded_most_valuable_edge(G):
        betweenness = nx.edge_betweenness_centrality(G)
        max_edge = max(betweenness, key=betweenness.get)
        # print(max_edge)
        return max_edge

    comp = nx.community.girvan_newman(
        G, most_valuable_edge=recorded_most_valuable_edge)

    disjoint = tuple(sorted(c) for c in next(comp))
    return len(disjoint[0]) * len(disjoint[1])


def part_2(inp):
    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
