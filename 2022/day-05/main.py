from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    stack = defaultdict(list)
    col_w = 4
    stack_lines = []
    for line in inp:
        if line == '':
            for stack_line in stack_lines[:-1]:
                for i, item in enumerate(stack_line):
                    if item != '':
                        stack[stack_lines[-1][i]].append(item)
        elif 'move' not in line:
            stack_item = [line[i:i + col_w].replace(' ', '').replace(
                '[', '').replace(']', '') for i in range(0, len(line), col_w)]
            stack_lines.append(stack_item)
        else:
            _, n, _, a, _, b = line.split()
            for _ in range(int(n)):
                stack[b].insert(0, stack[a].pop(0))
    return ''.join([stack[k][0] for k in sorted(stack.keys())])


def part_2(inp):
    stack = defaultdict(list)
    col_w = 4
    stack_lines = []
    for line in inp:
        if line == '':
            for stack_line in stack_lines[:-1]:
                for i, item in enumerate(stack_line):
                    if item != '':
                        stack[stack_lines[-1][i]].append(item)
        elif 'move' not in line:
            stack_item = [line[i:i + col_w].replace(' ', '').replace(
                '[', '').replace(']', '') for i in range(0, len(line), col_w)]
            stack_lines.append(stack_item)
        else:
            _, n, _, a, _, b = line.split()
            for ni in range(int(n)):
                stack[b].insert(ni, stack[a].pop(0))
    return ''.join([stack[k][0] for k in sorted(stack.keys())])


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
