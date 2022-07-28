def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [int(c) for c in f.read().splitlines()[0]]


def _print(m, p=False):
    if p:
        print(m)


def part_1(inp):
    cups = inp
    min_lab = min(cups)
    max_lab = max(cups)
    pick_len = 3
    pick_pos = 1
    cur_pos = 0

    for i in range(1, 1 + 100):
        if i > 1:
            cups.append(cups.pop(0))
        _print(f"-- move {i} --")
        cur_c = cups[cur_pos]
        _print(f"cups: ({cur_c}) {cups[1:]}")

        pick_c = cups[pick_pos:pick_pos + pick_len]
        rest_c = cups[cur_pos:cur_pos + 1] + cups[pick_pos + pick_len:]
        _print(f"pick up: {pick_c}")

        dest_c = cur_c - 1
        while dest_c not in rest_c:
            dest_c -= 1
            if dest_c < min_lab:
                dest_c = max_lab
        _print(f"destination: {dest_c}\n")

        dest_idx = rest_c.index(dest_c) + 1
        rest_c[dest_idx:dest_idx] = pick_c
        cups = rest_c

    while cups[0] != 1:
        cups.append(cups.pop(0))
    _print("-- final --")
    _print(f"cups: {cups}")
    res = ''.join(map(str, cups[1:]))
    return res


def part_2(inp):
    cups = inp

    cups_map = list(range(1, 1_000_000 + 2))

    for k, v in zip(cups, cups[1:] + [max(cups) + 1]):
        cups_map[k] = v
    cups_map[1_000_000] = cups[0]
    cups_map[0] = -1
    cur_cup = cups[0]
    for i in range(1, 1 + 10_000_000):
        _print(f"-- move {i} --")
        p1 = cups_map[cur_cup]
        p2 = cups_map[p1]
        p3 = cups_map[p2]
        dest_c = (cur_cup - 2) % 1_000_000 + 1
        while dest_c in [p1, p2, p3]:
            dest_c = (dest_c - 2) % 1_000_000 + 1

        # # current cup need to point where 3 picked cup pointed
        # cups_map[cur_cup] = cups_map[p3]
        # # destination cup need to point 1 picked cup
        # cups_map[dest_c] = p1
        # # 3 picked cup need to point where destination cup pointed
        # cups_map[p3] = cups_map[dest_c]

        cups_map[cur_cup], cups_map[dest_c], cups_map[p3] = \
            cups_map[p3], p1, cups_map[dest_c]

        cur_cup = cups_map[cur_cup]

    c1 = cups_map[1]
    c2 = cups_map[c1]
    res = c1 * c2
    return res


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
