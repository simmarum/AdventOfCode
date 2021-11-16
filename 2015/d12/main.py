import json


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return f.read()


def _sum_json(json_x):
    s = 0
    new_json = None
    if type(json_x) == list:
        new_json = json_x
    elif type(json_x) == dict:
        new_json = json_x.values()
    for el in new_json:
        if type(el) == int:
            s += el
        elif type(el) == list:
            s += _sum_json(el)
        elif type(el) == dict:
            s += _sum_json(el)
    return s


def part_1(inp):
    x = json.loads(inp)
    return _sum_json(x)


def _sum_json_2(json_x):
    s = 0
    new_json = None
    if type(json_x) == list:
        new_json = json_x
    elif type(json_x) == dict:
        new_json = json_x.values()
        if "red" in new_json:
            return 0
    for el in new_json:
        if type(el) == int:
            s += el
        elif type(el) == list:
            s += _sum_json_2(el)
        elif type(el) == dict:
            s += _sum_json_2(el)
    return s


def part_2(inp):
    x = json.loads(inp)
    return _sum_json_2(x)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
