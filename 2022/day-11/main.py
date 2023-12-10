from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def parse_inp(inp):
    monkeys = defaultdict(dict)
    magic_modulo = 1
    for line in inp:
        if 'Monkey' in line:
            monkey = int(line.split()[1][:-1])
        if 'Starting' in line:
            monkeys[monkey]['items'] = list(
                map(int, line.split(':')[1].split(',')))
            monkeys[monkey]['cnt'] = 0
        if 'Operation' in line:
            monkeys[monkey]['op'] = line.split('=')[1]
        if 'Test: divisible' in line:
            monkeys[monkey]['test'] = int(line.split()[3])
            magic_modulo *= monkeys[monkey]['test']
        if 'If true' in line:
            monkeys[monkey][True] = int(line.split()[5])
        if 'If false' in line:
            monkeys[monkey][False] = int(line.split()[5])
    return monkeys, magic_modulo


def part_1(inp):
    monkeys, _ = parse_inp(inp)
    rounds = 20
    for ri in range(rounds):
        for k in monkeys.keys():
            for ii in range(len(monkeys[k]['items'])):
                monkeys[k]['cnt'] += 1
                tmp_item = monkeys[k]['items'].pop(0)
                tmp_item = eval(monkeys[k]['op'].replace('old', str(tmp_item)))
                tmp_item = tmp_item // 3
                monkeys[monkeys[k][tmp_item % monkeys[k]['test'] == 0]
                        ]['items'].append(tmp_item)
    most_active_monkeys = list(
        sorted([(v['cnt']) for k, v in monkeys.items()], reverse=True))[:2]
    return most_active_monkeys[0] * most_active_monkeys[1]


def part_2(inp):
    monkeys, magic_modulo = parse_inp(inp)
    rounds = 10_000
    for ri in range(rounds):
        for k in monkeys.keys():
            for ii in range(len(monkeys[k]['items'])):
                monkeys[k]['cnt'] += 1
                tmp_item = eval(monkeys[k]['op'].replace(
                    'old', str(monkeys[k]['items'].pop(0)))) % magic_modulo
                monkeys[monkeys[k][tmp_item % monkeys[k]['test'] == 0]
                        ]['items'].append(tmp_item)
    most_active_monkeys = list(
        sorted([(v['cnt']) for k, v in monkeys.items()], reverse=True))[:2]
    return most_active_monkeys[0] * most_active_monkeys[1]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
