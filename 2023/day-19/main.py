import operator
import functools
import re
from copy import deepcopy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return f.read().split("\n\n")


def get_rules(inp):
    rules = {}
    for line in re.split(r'\n', inp[0]):
        rule_name, rule_body = line.split("{")
        rule_body_list = rule_body[0:-1].split(",")
        rules[rule_name] = rule_body_list
    return rules


def get_parts(inp):
    parts = []
    for part in re.split(r'\n', inp[1]):
        if not part:
            continue
        values = {}
        for item in part[1:-1].split(','):
            name, value = item.split('=')
            values[name] = int(value)
        parts.append(values)
    return parts


def check_part(rules, part, name):
    if name == 'A':
        return True
    if name == 'R':
        return False
    for rule in rules[name]:
        if ':' in rule:
            cond, target = rule.split(':')
            if '>' in cond:
                name, value = cond.split('>')
                if part[name] > int(value):
                    return check_part(rules, part, target)
            elif '<' in cond:
                name, value = cond.split('<')
                if part[name] < int(value):
                    return check_part(rules, part, target)
            else:
                assert 0, rule
        else:
            return check_part(rules, part, rule)
    assert 0, name


def split_range_less(r, value):
    if r.start > value:
        return range(0), r
    if r.stop > value:
        return range(r.start, value), range(value, r.stop)
    return r, range(0)


def split_range_more(r, value):
    if r.stop < value:
        return range(0), r
    if r.start <= value:
        return range(value + 1, r.stop), range(r.start, value + 1)
    return r, range(0)


def parts_possibilities(rules, part, name):
    part_size = functools.reduce(
        operator.mul, list(map(len, part.values())), 1)
    if part_size == 0:
        return 0
    if name == 'A':
        return part_size
    if name == 'R':
        return 0
    result = 0
    for rule in rules[name]:
        if ':' in rule:
            cond, target = rule.split(':')
            if '>' in cond:
                name, value = cond.split('>')
                r_true, r_false = split_range_more(part[name], int(value))
                part_a = deepcopy(part)
                part_a[name] = r_true
                part[name] = r_false
                result += parts_possibilities(rules, part_a, target)
            elif '<' in cond:
                name, value = cond.split('<')
                r_true, r_false = split_range_less(part[name], int(value))
                part_a = deepcopy(part)
                part_a[name] = r_true
                part[name] = r_false
                result += parts_possibilities(rules, part_a, target)
            else:
                assert 0, rule
        else:
            result += parts_possibilities(rules, part, rule)
    return result


def part_1(inp):
    rules = get_rules(inp)
    parts = get_parts(inp)
    total = 0
    for part in parts:
        if check_part(rules, part, 'in'):
            total += sum(part.values())
    return total


def part_2(inp):
    rules = get_rules(inp)
    part = {
        'x': range(1, 4001),
        'm': range(1, 4001),
        'a': range(1, 4001),
        's': range(1, 4001),
    }

    return parts_possibilities(rules, part, 'in')


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
