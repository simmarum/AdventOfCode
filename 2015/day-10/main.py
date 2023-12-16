def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line.replace("\n", "")) for line in f.readlines()]


def part_1(inp, iterations):
    val = inp[0]

    def resolve(val):
        act_cnt = 0
        act_c = val[0]
        out_str = ""
        last_idx = len(val) - 1
        for idx, c in enumerate(val):
            if c == act_c:
                act_cnt += 1
            else:
                out_str += f"{act_cnt}{act_c}"
                act_c = c
                act_cnt = 1
            if idx == last_idx:
                out_str += f"{act_cnt}{act_c}"
        return out_str
    res = val
    for _ in range(iterations):
        res = resolve(res)
    return len(res)


def part_2(inp, iterations):
    return part_1(inp, iterations)


def main():
    inp = read_file()
    res_1 = part_1(inp, 40)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp, 50)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
