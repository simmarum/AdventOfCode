
def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def find_path_to_root(g, node):
    if g.get(node) in g:
        n, p = find_path_to_root(g, g[node])
        p.append(node)
        return 1 + n, p
    else:
        return 1, []


def part_1(inp):
    g = {line.split(")")[1]: line.split(")")[0] for line in inp}
    return sum((find_path_to_root(g, g_name)[0] for g_name in g))


def part_2(inp):
    g = {line.split(")")[1]: line.split(")")[0] for line in inp}
    _, p_you = find_path_to_root(g, "YOU")
    _, p_san = find_path_to_root(g, "SAN")
    p_you_len = len(p_you)
    p_san_len = len(p_san)
    idx_match = 0
    for i in range(p_you_len + 1):
        if p_you[i] != p_san[i]:
            idx_match = i
            break
    return (p_san_len - 1 - idx_match) + (p_you_len - 1 - idx_match)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
