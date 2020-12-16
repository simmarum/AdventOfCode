from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [line for line in f.read().split("\n\n")]


def part_1(inp):
    rules = defaultdict(set)
    for val in inp[0].split("\n"):
        x = val.split(":")
        r = x[1].strip().split("or")
        for rr in r:
            xx = rr.split("-")
            rules[x[0]].update(set(range(int(xx[0]), int(xx[1])+1)))

    all_vals = set()
    for v in rules.values():
        all_vals.update(v)

    s = 0
    for val in inp[2].split("\n")[1:]:
        for n in list(map(int, val.split(","))):
            if n not in all_vals:
                s += n

    return s


def part_2(inp):
    rules = defaultdict(set)
    for val in inp[0].split("\n"):
        x = val.split(":")
        r = x[1].strip().split("or")
        for rr in r:
            xx = rr.split("-")
            rules[x[0]].update(set(range(int(xx[0]), int(xx[1])+1)))

    my_ticket = list(map(int, inp[1].split("\n")[1].split(",")))

    all_vals = set()
    for v in rules.values():
        all_vals.update(v)

    tickets = []
    for val in inp[2].split("\n")[1:]:
        ticket = list(map(int, val.split(",")))
        good = True
        for n in ticket:
            if n not in all_vals:
                good = False
                break
        if good:
            tickets.append(ticket)

    ll = len(rules)
    resolve = defaultdict(set)
    for i in range(ll):
        tmp_class = set([x[i] for x in tickets])
        for k, r in rules.items():
            if tmp_class.issubset(r):
                resolve[k].add(i)

    orders = [[k, v] for k, v in resolve.items()]
    final_order = []
    while len(orders) > 0:
        orders.sort(key=lambda x: len(x[1]))
        if len(orders[0][1]) == 1:
            final_order.append(orders[0])
            for i in range(1, len(orders)):
                orders[i][1] = orders[i][1].difference(orders[0][1])
            orders.remove(orders[0])

    m = 1
    for x in final_order:
        if "departure" in x[0]:
            m *= my_ticket[list(x[1])[0]]
    return m


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
