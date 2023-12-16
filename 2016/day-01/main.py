def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    instructions = inp[0].replace(' ', '').split(',')
    point = [0, 0]
    direction = [0, 1]
    for instr in instructions:
        instr_dir = instr[0]
        instr_len = int(instr[1:])
        if instr_dir == 'R':
            direction = [direction[1], -direction[0]]
        if instr_dir == 'L':
            direction = [-direction[1], direction[0]]
        point = [point[0] + (instr_len * direction[0]),
                 point[1] + (instr_len * direction[1])]
    return abs(point[0]) + abs(point[1])


def part_2(inp):
    instructions = inp[0].replace(' ', '').split(',')
    point = [0, 0]
    direction = [0, 1]
    visited = set()
    visited_twice = False
    for instr in instructions:
        instr_dir = instr[0]
        instr_len = int(instr[1:])
        if instr_dir == 'R':
            direction = [direction[1], -direction[0]]
        if instr_dir == 'L':
            direction = [-direction[1], direction[0]]
        for _ in range(instr_len):
            point = [point[0] + (direction[0]),
                     point[1] + (direction[1])]
            if tuple(point) in visited:
                visited_twice = True
                break
            else:
                visited.add(tuple(point))
        if visited_twice:
            break
    return abs(point[0]) + abs(point[1])


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
