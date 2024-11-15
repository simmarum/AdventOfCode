def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.read().splitlines()]


def part_1(inp):
    all_inst = []
    acc = 0
    for val in inp:
        x = val.split(" ")
        all_inst.append([x[0], int(x[1]), False])
    i = 0
    ll = len(all_inst)
    while True:
        if i >= ll:
            return "Reach end input!"
        if all_inst[i][2] is True:
            break
        if all_inst[i][0] == "nop":
            all_inst[i][2] = True
            i += 1
        elif all_inst[i][0] == "jmp":
            all_inst[i][2] = True
            i += all_inst[i][1]
        elif all_inst[i][0] == "acc":
            all_inst[i][2] = True
            acc += all_inst[i][1]
            i += 1
    return acc


def part_2(inp):

    def resolve(all_inst):
        acc = 0
        i = 0
        ll = len(all_inst)
        while True:
            if i >= ll:
                return True, acc
            if all_inst[i][2] is True:
                return False, acc
            elif all_inst[i][0] == "nop":
                all_inst[i][2] = True
                i += 1
            elif all_inst[i][0] == "jmp":
                all_inst[i][2] = True
                i += all_inst[i][1]
            elif all_inst[i][0] == "acc":
                all_inst[i][2] = True
                acc += all_inst[i][1]
                i += 1

    ll = len(inp)
    ii = 0
    for ii in range(ll):
        all_inst = []
        for val in inp:
            x = val.split(" ")
            all_inst.append([x[0], int(x[1]), False])

        if all_inst[ii][0] == "jmp":
            all_inst[ii][0] = "nop"
        elif all_inst[ii][0] == "nop":
            all_inst[ii][0] = "jmp"
        g, nacc = resolve(all_inst)
        if g:
            return nacc


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
