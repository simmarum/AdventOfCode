def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    viruses = set()
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == '#':
                viruses.add((y, x))
    curr_node = (len(inp) // 2, len(inp[0]) // 2)
    curr_dir = (-1, 0)
    add_cnts = 0
    for t in range(10000):
        if curr_node in viruses:
            curr_dir = (curr_dir[1], -curr_dir[0])
            viruses.remove(curr_node)
        else:
            curr_dir = (-curr_dir[1], curr_dir[0])
            viruses.add(curr_node)
            add_cnts += 1
        curr_node = (curr_node[0] + curr_dir[0], curr_node[1] + curr_dir[1])
    return add_cnts


def part_2(inp):
    viruses = {}
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == '#':
                viruses[(y, x)] = 'infected'
    curr_node = (len(inp) // 2, len(inp[0]) // 2)
    curr_dir = (-1, 0)
    add_cnts = 0
    for t in range(10000000):
        if curr_node in viruses:
            if viruses[curr_node] == 'weakened':
                viruses[curr_node] = 'infected'
                add_cnts += 1
            elif viruses[curr_node] == 'infected':
                curr_dir = (curr_dir[1], -curr_dir[0])
                viruses[curr_node] = 'flagged'
            elif viruses[curr_node] == 'flagged':
                curr_dir = (-curr_dir[0], -curr_dir[1])
                del viruses[curr_node]
        else:
            curr_dir = (-curr_dir[1], curr_dir[0])
            viruses[curr_node] = 'weakened'
        curr_node = (curr_node[0] + curr_dir[0], curr_node[1] + curr_dir[1])
    return add_cnts


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
