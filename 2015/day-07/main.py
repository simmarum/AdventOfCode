def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def load_board(inp):
    wait_room = {}
    for val in inp:
        tmp_in, out = val.replace("\n", "").split(" -> ")
        wait_room[out] = tmp_in
    return wait_room


def part_1(inp, wait_room):
    def resolve(k, room):
        if k.isdigit():
            eq = k
        else:
            eq = str(room[k])
        if eq.isdigit():
            room[k] = int(eq)
        else:
            i1, op, i2 = (eq.split(" ") + [None, None, None])[:3]
            if "AND" in eq:
                room[k] = resolve(i1, room) & resolve(i2, room)
            elif "OR" in eq:
                room[k] = resolve(i1, room) | resolve(i2, room)
            elif "LSHIFT" in eq:
                room[k] = resolve(i1, room) << int(i2)
                if room[k] < 0:
                    room[k] = 65535 + room[k]
            elif "RSHIFT" in eq:
                room[k] = resolve(i1, room) >> int(i2)
                if room[k] > 65535:
                    room[k] = room[k] - 65535
            elif "NOT" in eq:
                room[k] = 65535 - resolve(op, room)
            else:
                room[k] = resolve(i1, room)
        return room[k]
    return resolve('a', wait_room)


def part_2(inp, wait_room):
    res_1 = part_1(inp, wait_room)
    wait_room = load_board(inp)
    wait_room['b'] = res_1
    return part_1(inp, wait_room)


def main():
    inp = read_file()
    wait_room = load_board(inp)
    res_1 = part_1(inp, wait_room)
    print(f"res_1: {res_1}")
    wait_room = load_board(inp)
    res_2 = part_2(inp, wait_room)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
