def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [line for line in f.read().splitlines()]


def part_1(inp):
    mask = ''
    mem = {}
    for val in inp:
        sval = val.split(" ")
        if "mask" in val:
            mask = sval[2]
        else:
            sval[2] = int(
                ''.join(
                    [x if mask[idx] == 'X' else mask[idx]
                     for idx, x in enumerate(
                         bin(int(sval[2]))[2:].zfill(36))
                     ]),
                2)
            mem[sval[0].split("[")[1].  split("]")[0]] = sval[2]
    return sum(mem.values())


def part_2(inp):
    mask = ''
    mem = {}
    for val in inp:
        sval = val.split(" ")
        if "mask" in val:
            mask = sval[2]
        else:
            old_add = int(sval[0].split("[")[1].split("]")[0])
            bin_str = bin(old_add)[2:].zfill(36)
            new_bin_str = [c for c in bin_str]
            for idx, _ in enumerate(bin_str):
                if mask[idx] == '1':
                    new_bin_str[idx] = '1'
                elif mask[idx] == 'X':
                    new_bin_str[idx] = 'X'
            new_add = []
            indices = [i for i, x in enumerate(new_bin_str) if x == "X"]
            cnt_x = len(indices)
            if cnt_x == 0:
                new_add.append(new_bin_str)
            else:
                for i in range(2**cnt_x):
                    nbs = new_bin_str
                    si = bin(i)[2:].zfill(cnt_x)
                    for idx, idx_s in enumerate(indices):
                        nbs[idx_s] = si[idx]
                    new_add.append(int(''.join(nbs), 2))
            for ad in new_add:
                mem[ad] = int(sval[2])
    return sum(mem.values())


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
