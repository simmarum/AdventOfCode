def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.read().splitlines()]


def part_1(inp):
    max_id = 0
    for s in inp:
        s = s.replace('B', '1').replace(
            'F', '0').replace('L', '0').replace('R', '1')
        row = s[0:7]
        col = s[7:11]
        row = int(row, base=2)
        col = int(col, base=2)
        max_id = max(max_id, row*8+col)

    return max_id


def part_2(inp):
    found_ids = set()
    for s in inp:
        s = s.replace('B', '1').replace(
            'F', '0').replace('L', '0').replace('R', '1')
        s_id = int(s[0:7], base=2) * 8 + int(s[7:11], base=2)
        found_ids.add(s_id)

    my_ids = list(
        set(range(min(found_ids)-1, max(found_ids)+1)).difference(found_ids))
    my_ids.sort()
    return my_ids


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
