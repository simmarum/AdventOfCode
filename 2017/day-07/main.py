from collections import Counter


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def parse_inp(inp):
    data = {}
    for line in inp:
        x = line.split()
        name = x[0]
        w = int(x[1].replace('(', '').replace(')', ''))
        childs = []
        if len(x) > 2:
            childs = [c.replace(',', '') for c in x[3:]]
        data[name] = {
            'w': w,
            'childs': childs
        }
    return data


def find_root(data):
    names = set(data.keys())
    all_childs = set()
    for k, v in data.items():
        all_childs = all_childs.union(set(v['childs']))

    return list(names.difference(all_childs))[0]


def part_1(inp):
    data = parse_inp(inp)
    root = find_root(data)
    return root


def find_wrong_balance(data, name, lvl):
    correct_w = None
    tmp_sum = data[name]['w']
    childs_w = []
    for c in data[name]['childs']:
        ss, _correct_w = find_wrong_balance(data, c, lvl + 1)
        if _correct_w:
            return None, _correct_w
        childs_w.append(ss)
        tmp_sum += ss
    x = Counter(childs_w)
    if len(x) > 1:
        wrong_one = x.most_common()[-1][0]
        good_one = x.most_common()[0][0]
        correct_w = wrong_one - good_one
        return None, data[data[name]['childs']
                          [childs_w.index(wrong_one)]]['w'] - correct_w
    return tmp_sum, correct_w


def part_2(inp):
    data = parse_inp(inp)
    root = find_root(data)
    _, correct_w = find_wrong_balance(data, root, 0)
    return correct_w


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
