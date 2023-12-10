from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    curr_path = []
    dirs = defaultdict(int)
    for line in inp:
        if '$ cd ..' in line:
            curr_path.pop()
        elif '$ cd /' in line:
            curr_path = ['.']
        elif '$ cd ' in line:
            curr_path.append(line.replace('$ cd ', '').strip())
        elif line[0].isdigit():
            size, _ = line.split()
            for i in range(len(curr_path)):
                dirs['/'.join(curr_path[:i + 1])] += int(size)
    return sum([v for _, v in dirs.items() if v < 100_000])


def part_2(inp):
    curr_path = []
    dirs = defaultdict(int)
    for line in inp:
        if '$ cd ..' in line:
            curr_path.pop()
        elif '$ cd /' in line:
            curr_path = ['.']
        elif '$ cd ' in line:
            curr_path.append(line.replace('$ cd ', '').strip())
        elif line[0].isdigit():
            size, _ = line.split()
            for i in range(len(curr_path)):
                dirs['/'.join(curr_path[:i + 1])] += int(size)
    return min([v for _, v in dirs.items() if dirs['.'] - v < 40_000_000])


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
