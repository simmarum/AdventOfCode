def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    gift = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]  # from task
    map = {
        'children': 0,
        'cats': 1,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 4,
        'vizslas': 5,
        'goldfish': 6,
        'trees': 7,
        'cars': 8,
        'perfumes': 9,
    }
    all_data = []
    for one_line in inp:
        split_line = one_line.split(":")
        tmp_sue = [None] * 10
        for one_comp in ''.join(split_line[1:]).split(","):
            one_comp = one_comp.strip().split(" ")
            tmp_sue[map[one_comp[0]]] = int(one_comp[1])
        all_data.append(tmp_sue)

    pos_sue = []
    for ind_sue, one_sue in enumerate(all_data):
        for i, v in enumerate(one_sue):
            if (v is not None) and (v != gift[i]):
                break
        else:
            pos_sue.append(ind_sue)

    if len(pos_sue) == 1:
        return pos_sue[0] + 1
    else:
        return None


def part_2(inp):
    gift = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]  # from task
    map = {
        'children': 0,
        'cats': 1,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 4,
        'vizslas': 5,
        'goldfish': 6,
        'trees': 7,
        'cars': 8,
        'perfumes': 9,
    }
    all_data = []
    for one_line in inp:
        split_line = one_line.split(":")
        tmp_sue = [None] * 10
        for one_comp in ''.join(split_line[1:]).split(","):
            one_comp = one_comp.strip().split(" ")
            tmp_sue[map[one_comp[0]]] = int(one_comp[1])
        all_data.append(tmp_sue)

    pos_sue = []
    for ind_sue, one_sue in enumerate(all_data):
        for i, v in enumerate(one_sue):
            if (i == 1) or (i == 7):
                if (v is not None) and (v <= gift[i]):
                    break
            elif (i == 3) or (i == 6):
                if (v is not None) and (v >= gift[i]):
                    break
            else:
                if (v is not None) and (v != gift[i]):
                    break
        else:
            pos_sue.append(ind_sue)

    if len(pos_sue) == 1:
        return pos_sue[0] + 1
    else:
        return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
